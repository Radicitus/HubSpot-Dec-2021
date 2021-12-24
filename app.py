import requests
import json


def pretty_json(j):
    # Create human readable strong from json obj
    pj = json.dumps(j, sort_keys=True, indent=4)
    print(pj)


def create_session_set(user_id, sessions):
    # Determine the groups of sessions

    # Determine the duration of a session group

    # Determine the pages searched in the session group

    # Determine the start time by ordering timestamp
    return


# BEGIN MAIN PROGRAM
# Request data from API
raw_response = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=4345b1d67362a424348e1cd8e827')
# pretty_json(raw_response.json())

# Organize visits by visitorId
grouped_visits = {}
response = json.dumps(raw_response.json())

for v in response:
    continue