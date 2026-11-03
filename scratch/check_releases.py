import urllib.request
import json

url = 'https://api.github.com/repos/muhzahjr07/spillburg_profiles/releases'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
releases = json.loads(urllib.request.urlopen(req).read())

print(f"Total Releases: {len(releases)}")
for r in releases:
    print(f"\nRelease Name: {r.get('name')}")
    print(f"Tag: {r.get('tag_name')}")
    print(f"Published: {r.get('published_at')}")
    print("Downloadable Release Assets:")
    for a in r.get('assets', []):
        size_mb = round(a['size'] / (1024 * 1024), 2)
        print(f"  - {a['name']} ({size_mb} MB) -> {a['browser_download_url']}")

