import requests
import logging

# Step 3: Simple Logging Setup
logging.basicConfig(
    filename="apilog.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 2 & 4: API Function with Basic Logs
def fetch_api(url):
    logging.info(f"Trying URL: {url}")

    try:
        r = requests.get(url, timeout=3)

        if not r.ok:
            logging.error(f"Bad status code: {r.status_code}")
            return None

        try:
            data = r.json()
            logging.info("Valid JSON received")
            return data
        except:
            logging.error("Response is NOT JSON")
            return None

    except requests.exceptions.Timeout:
        logging.warning("Timeout happened")
    except requests.exceptions.ConnectionError:
        logging.error("Cannot reach host")
    except Exception as e:
        logging.error(f"Unexpected: {e}")

# Step 5: Test URLs
fetch_api("https://jsonplaceholder.typicode.com/todos/1")
fetch_api("https://invalid-domain-09876.com")
fetch_api("https://google.com")
fetch_api("https://httpbin.org/status/500")

print("Check apilog.txt for output")