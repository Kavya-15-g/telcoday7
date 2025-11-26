import requests

def fetch_api(url):
    try:
        # Send request with timeout
        response = requests.get(url, timeout=5)

        # Raise error for bad HTTP status codes (404, 500, etc.)
        response.raise_for_status()

        # Try converting response to JSON
        return response.json()

    # Common Exceptions
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Host unreachable / No internet")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")

    except ValueError:
        print("❌ Error: Response is not valid JSON")

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


# -------------------------------------------
# TEST WITH GOOD & BAD URLs
# -------------------------------------------

print("\n--- Testing GOOD URL ---")
good_url = "https://jsonplaceholder.typicode.com/posts/1"
print(fetch_api(good_url))

print("\n--- Testing BAD URL (Host unreachable) ---")
bad_url1 = "https://thiswebsite-does-not-exist123.com"
fetch_api(bad_url1)

print("\n--- Testing BAD URL (404 Error) ---")
bad_url2 = "https://jsonplaceholder.typicode.com/postsss"
fetch_api(bad_url2)

print("\n--- Testing BAD URL (Not JSON) ---")
bad_url3 = "https://google.com"
fetch_api(bad_url3)
