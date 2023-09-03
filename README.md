# league-sns
Attempts to change your league of legends summonername to another one the second it becomes available (windows only, tested with python 3.11.3).

Instructions:
1. Install the requirements.txt: `pip install -r requirements.txt`
2. Use a website like [names.lol](https://www.nameslol.com/name-checker) to find out the time the desired name becomes available and convert it to unixtime (e.g. with [unixtimestamp](https://www.unixtimestamp.com/)).
3. Update the `name` and `available_at` variables at the beginning of `snipe.py` with your values.
4. Log into your league of legends client with the account whose name you wish to change.
5. Execute `python snipe.py` an hour* (at the earliest!) before the name becomes available.

\* The bearer token that's taken from the client at the time of starting the script is only valid for one hour

Note that the script will use BE for the name change by default, if you wish to use RP instead, you will have to modify the `changeName` function