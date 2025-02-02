import logging
import requests

def check_website(url):
    try:
        responseHead = requests.head(url, timeout= 2)# to not keep the request just hanging there
        if responseHead.status_code == 200:
            logging.info("Server is ALive")
        else:
            logging.warning(f"URL {url} returned a status code of {responseHead.status_code} ")
        responseGet = requests.get(url, timeout= 2)
        logging.info(f"The Server Technologies are: {responseGet.headers.get('Server')}")

        responseOptions = requests.options(url, timeout= 2)
        logging.info(f"Allowed Methods: {responseOptions.headers.get('Allow')}")
    except requests.exceptions.ConnectionError:
        logging.error("Connection error accured")
    except requests.exceptions.Timeout:
        logging.error("Timeout error accured")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error accured: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    check_website("https://www.google.com")
    check_website("https://httpbin.org/delay/5")
