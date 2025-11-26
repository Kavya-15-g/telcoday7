import requests

class APIResponseError(Exception):
    pass

def fetch_data(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        try:
            return r.json()
        except:
            raise APIResponseError("Not valid JSON")
    except requests.exceptions.Timeout:
        raise APIResponseError("Timeout")
    except requests.exceptions.ConnectionError:
        raise APIResponseError("Bad URL / Unreachable")
    except requests.exceptions.HTTPError as e:
        raise APIResponseError(f"HTTP Error: {e}")

def test(url):
    try:
        print(f"\nTesting: {url}")
        print(fetch_data(url))
    except APIResponseError as e:
        print("Error:", e)

# Test URLs
test("https://jsonplaceholder.typicode.com/comments/1")            # Good
test("https://invalid-url-12345.com")                           # Bad URL
test("https://example.com")                                     # Non-JSON
test("https://jsonplaceholder.typicode.com/invalid-endpoint")   # 404