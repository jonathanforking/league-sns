# league-sns
Changes your league of legends summonername the second it becomes available (windows only).

Instructions:
    0. Use python 3 (tested with 3.11.3) and install the requirements.txt ```pip install -r requirements.txt```
    1. Use a website like [names.lol](https://www.nameslol.com/name-checker) to find out the time the desired name becomes available, and convert it to unixtime (e.g. with [unixtimestamp](https://www.unixtimestamp.com/))
    2. Update the *name* and *available_at* variables at the beginning of `snipe.py` with your values
    3. Log into your league of legends client with the account whose name you wish to change
    4. Execute ```python snipe.py``` an hour (at the earliest!) before the name becomes available

Note that the script will use be for the name change by default, if you wish to use rp instead, you will have to modify the ```changeName``` function