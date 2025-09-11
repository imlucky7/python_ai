import requests
#import json
import sys

def main():
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # weezer
    #print(json.dumps(response.json(), indent=2))
    res = response.json()
    for result in res['results']:
        print(f"track name is {result['trackName']}")

if __name__ == "__main__":
    main()