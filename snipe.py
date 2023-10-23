import base64
import sched
import time

import psutil
import requests
requests.packages.urllib3.disable_warnings()



# NOTE: This script only works on windows and requires you to be logged into your client.
name = 'the name'
available_at = 1694820000



# Get client variables
for p in psutil.process_iter():
        if p.name() == 'LeagueClientUx.exe':
                args = p.cmdline()
                for a in args:
                        if '--remoting-auth-token=' in a:
                            auth_token = a.split('--remoting-auth-token=', 1)[1]
                        if '--app-port' in a:
                            app_port = a.split('--app-port=', 1)[1]
                break

lcu_api = f'https://127.0.0.1:{app_port}'
lcu_session_token = base64.b64encode((f'riot:{auth_token}').encode('ascii')).decode('ascii')
lcu_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Basic {lcu_session_token}'
}



# Get store variables
res = requests.get(f'{lcu_api}/lol-store/v1/getStoreUrl', headers=lcu_headers, verify=False)
store_url = res.json()
res = requests.get(f'{lcu_api}/lol-rso-auth/v1/authorization/access-token', headers=lcu_headers, verify=False)
bearer_token = res.json()['token']



# Get accountId
store_headers = {
	'User-Agent': 'RiotClient/18.0.0 (lol-store)',
	'Accept': 'application/json',
	'Authorization': f'Bearer {bearer_token}'
}
session = requests.Session()
session.headers = store_headers
res = session.get(f'{store_url}/storefront/v3/history/purchase?language=en_US')
account_id = res.json()['player']['accountId']



# Method that gets executed on at time of free'ing
def changeName(name, account_id, store_url, session):
        payload = {
                'summonerName': name,
                'accountId': account_id,
                'items': [{
                        'inventoryType': 'SUMMONER_CUSTOMIZATION',
                        'itemId': 1,
                        'ipCost': 13900,
                        'rpCost': None,
                        'quantity': 1
                }]
        }
        status = 0
        while status != 200:
                then = time.time()
                res = session.post(f'{store_url}/storefront/v3/summonerNameChange/purchase?language=en_US', json=payload)
                print('request time: ' + str(then))
                print('request duration: ' + str(res.elapsed))
                status = res.status_code
                print(status)
                print(res.json())
                if status == 429:
                        # Hit rate limit, at this point we can give up
                        exit()
                else:
                        time.sleep(1.2)



# Schedule name change
session.headers['Content-Type'] = 'application/json'
scheduler = sched.scheduler(time.time, time.sleep)
# Wait a little extra to give the backend some time for cleanup
to_wait = available_at - time.time() + .1
e = scheduler.enter(to_wait, 1, changeName, (name, account_id, store_url, session))
scheduler.run()
