import requests

def fetch_data(url, label):
    print(f"\n--- Testing: {label} ---")
    try:
        print(f"Trying URL: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
            print("✔ Valid JSON received")
            return data
        except ValueError:
            print("❌ NON-JSON Response")
            return None

    except requests.exceptions.Timeout:
        print("❌ TIMEOUT – Server took too long to respond")

    except requests.exceptions.ConnectionError:
        print("❌ BAD URL / HOST UNREACHABLE")

    except requests.exceptions.HTTPError as e:
        print(f"❌ STATUS FAIL – HTTP Error: {e}")

    except Exception as e:
        print(f"❌ UNKNOWN ERROR: {e}")

    return None


# ---------------------------------------
# Test all URLs with clear labels
# ---------------------------------------

fetch_data("https://jsonplaceholder.typicode.com/todos/1", "GOOD URL")
fetch_data("https://invalid-url-12345.com", "BAD URL")
fetch_data("https://example.com", "NON-JSON URL")
fetch_data("https://jsonplaceholder.typicode.com/invalid-endpoint", "STATUS FAIL URL")