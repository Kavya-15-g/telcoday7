import logging
import requests

# Logging setup
logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_api(url):
    logging.info(f"Checking URL: {url}")

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()

        try:
            return r.json()
        except:
            logging.error("Response is NOT JSON")
            return None

    except Exception as e:
        logging.error(f"Error: {e}")
        return None


# Testing
print(fetch_api("https://jsonplaceholder.typicode.com/todos/1"))   # Good
print(fetch_api("https://example.com"))                            # Not JSON
print(fetch_api("https://invalid-url.com"))                        # Bad URL