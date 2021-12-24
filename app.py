import requests
import json


def pretty_json(j):
    # Create human readable strong from json obj
    pj = json.dumps(j, sort_keys=True, indent=4)
    print(pj)


def create_session_set(user_id, user_visits):
    sessions = []
    session_pages = []
    session_duration = 0
    session_start = user_visits[0][1]
    # Determine the groups of sessions
    i = 0
    while i < len(user_visits) - 1:
        time_diff = user_visits[i + 1][1] - user_visits[i][1]
        v1 = user_visits[i]
        v2 = user_visits[i + 1]
        if time_diff <= 600000:
            session_pages.append(user_visits[i][0])
            session_pages.append(user_visits[i + 1][0])
            session_duration += time_diff
            i += 1
        else:
            if not session_duration:
                sessions.append(
                    {
                        "duration": session_duration,
                        "pages": user_visits[i][0],
                        "startTime": session_start
                    }
                )
            else:
                sessions.append(
                    {
                        "duration": session_duration,
                        "pages": sorted(session_pages),
                        "startTime": session_start
                    }
                )
            i += 1
            session_pages = []
            session_duration = 0
            session_start = user_visits[i][1]

    return sessions

    # Determine the duration of a session group
    # Determine the pages searched in the session group
    # Determine the start time by ordering timestamp


# BEGIN MAIN PROGRAM
# Request data from API
raw_response = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=4345b1d67362a424348e1cd8e827')

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
for user, visits in grouped_visits.items():
    sessions_by_user[user] = create_session_set(user, visits)

# Jsonify sessions_by_user and send by http call
final_json_payload = {}
final_json_payload['sessionsByUser'] = sessions_by_user
data = json.dumps(final_json_payload)
print(json.dumps(final_json_payload, indent=4))

post_response = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=4345b1d67362a424348e1cd8e827', data)
print(post_response.status_code, post_response.reason, post_response.content)