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
    user_input = input("Enter the URL you want to check: ")
    check_website(user_input)
    # check_website("https://httpbin.org/anything")     # test for everything
    # check_website("https://httpbin.org/delay/5")      # test for delays
    # check_website('http://nonexistentwebsite123456.com')      # test for nonexistent website
    # check_website('sdhksjh')      # test for invalid url
    # check_website('https://httpbin.org/status/404')      # test for 404 status code
