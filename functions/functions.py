from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from log.logger import Log


# GLOBAL VALUES #
logger = Log().get_logger(__name__)
time_out = 10


def get_str_time_now() -> str:
    """ Retorno el momento en el que el scraping extrae los datos.

    :return: str
    """
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


def get_response_by_url(url: str) -> BeautifulSoup:
    """ Retorno el response del llamado a la URL del banco.

    :param url: str
    :return: BeautifulSoup
    """
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(request, timeout=time_out).read()
        response = BeautifulSoup(webpage, 'html.parser')
        return response

    except Exception as e:
        logger.error(f'Error al devolver el Response de url: "{url}", error: "{e}"')


def clean_values_scraping_bank(value: str) -> float:
    """ Retorno los valores limpios del scraping en formato numerico.

    :param value: str
    :return: float
    """
    try:
        value_split = ((((value.strip()).split(" "))[1].replace(',', '.')).split('\r\n')[0])
        value_replace = value_split.replace(',', '.')
        value = float(value_replace)
        return value

    except Exception as e:
        logger.error(f'Error en la limpieza de valores de retorno del scraping, error "{e}"')


def get_partial_values_from_banks(url: str) -> list[float]:
    """ Retorno la lista de valores parciales del scraping.

    :param url: str
    :return: list[float]
    """
    try:
        response = get_response_by_url(url)
        partial_list = []
        for i in range(0, 4):
            dollar_value = (response.find('table').find_all('td', {'class': 'colCompraVenta'}))[i].text
            value = clean_values_scraping_bank(dollar_value)
            partial_list.append(value)

        return partial_list

    except Exception as e:
        logger.error(f'Error en el retorno de valores del scraping: "{url}" ,error: {e}')
