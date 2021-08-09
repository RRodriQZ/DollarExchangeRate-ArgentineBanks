from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from log.logger import Log


# GLOBAL VALUES #
logger = Log().get_logger(__name__)
time_out = 10


def get_str_time_now() -> str:
    """Return the moment when scraping extracts the data

    :return: str
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def get_response_by_url(url: str) -> BeautifulSoup:
    """Return the response of the call to the bank's URL

    :param url: str
    :return: BeautifulSoup
    """
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(request, timeout=time_out).read()
        response = BeautifulSoup(webpage, "html.parser")
        return response

    except Exception as e:
        logger.error(f'Error returning the Response of url: "{url}", error: "{e}"')


def clean_values_scraping_bank(value: str) -> float:
    """Return the clean scraping values in numeric format

    :param value: str
    :return: float
    """
    try:
        format_value = ((value.strip()).split(" "))[1].replace(",", ".")
        value_split = format_value.split("\r\n")[0]
        value = value_split.replace(",", ".")
        return float(value)

    except Exception as e:
        logger.error(
            f'Error cleaning return values from scraping, error "{e}"'
        )


def get_partial_values_from_banks(url: str) -> list:
    """Return the list of partial values from scraping

    :param url: str
    :return: list[float]
    """
    try:
        response = get_response_by_url(url)
        partial_list = []
        for i in range(0, 4):
            dollar_value = (
                response.find("table").find_all("td", {"class": "colCompraVenta"})
            )[i].text
            value = clean_values_scraping_bank(dollar_value)
            partial_list.append(value)

        return partial_list

    except Exception as e:
        logger.error(
            f'Error in the return of scraping values: "{url}" ,error: "{e}"'
        )
