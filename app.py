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
    return []


# BEGIN MAIN PROGRAM
# Request data from API
raw_response = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=4345b1d67362a424348e1cd8e827')
# pretty_json(raw_response.json())

# Group visits by visitorId
grouped_visits = {}
response = raw_response.json()['events']

for v in response:
    # v: {url, visitorId, timestamp}
    id = v['visitorId']
    if id in grouped_visits:
        grouped_visits[id].append([v['url'], v['timestamp']])
    else:
        grouped_visits[id] = [[v['url'], v['timestamp']]]

# Sort visits by timestamp
grouped_visits = {k: v for k, v in sorted(grouped_visits.items(), key=lambda item: item[1])}

# Pass grouped visits to helper function and store return values
sessions_by_user = {}
for user, visits in grouped_visits:
    sessions_by_user[user] = create_session_set(user, visits)


print(sessions_by_user)