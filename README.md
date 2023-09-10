# league-sns
Script that attempts to change your league of legends summonername to another one the second it becomes available (windows only, tested with python 3.11.3).

Instructions:
1. Install the requirements.txt: `pip install -r requirements.txt`
2. Use a website like [nameslol.com](https://www.nameslol.com/name-checker) to find out the time the desired name becomes available and convert it to unixtime (e.g. with [unixtimestamp](https://www.unixtimestamp.com/)).
3. Update the `name` and `available_at` variables at the beginning of `snipe.py` with your values.
4. Log into the league of legends client with your account, an hour* (at the earliest!) before the name becomes available.
5. Execute `python snipe.py`

\* The access token that's taken from the client at the time of starting the script is valid for one hour and doesn't get validated & refreshed by the script 

Note that the script will use 13900 BE for the name change by default, if you wish to use RP instead, you will have to modify the `changeName` function
