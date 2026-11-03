import urllib.request
import json

url = 'https://api.github.com/repos/muhzahjr07/spillburg_profiles/actions/runs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
runs = json.loads(urllib.request.urlopen(req).read())['workflow_runs']

for r in runs:
    if 'Pages' in r['name']:
        run_id = r['id']
        jobs_url = f"https://api.github.com/repos/muhzahjr07/spillburg_profiles/actions/runs/{run_id}/jobs"
        jobs_req = urllib.request.Request(jobs_url, headers={'User-Agent': 'Mozilla/5.0'})
        jobs = json.loads(urllib.request.urlopen(jobs_req).read())['jobs']
        for j in jobs:
            print(f"Run {run_id} Job {j['name']}: {j['conclusion']}")
            for s in j.get('steps', []):
                print(f"  Step: {s['name']} -> {s['conclusion']}")
        break

