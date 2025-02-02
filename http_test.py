import logging
import requests

def check_website(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            logging.info(f"URL {url} is up and running")
        else:
            logging.warning(f"URL {url} returned a status code of {response.status_code} ")
    except:
        logging.error(f"error happened")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    check_website("https://www.google.com")
    check_website("https://www.google.com/404")
