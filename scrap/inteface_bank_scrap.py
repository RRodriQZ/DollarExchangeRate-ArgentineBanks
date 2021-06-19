from abc import ABCMeta, abstractmethod
from configparser import ConfigParser
from log.logger import Log


class Banks(object):
    __metaclass__ = ABCMeta

    def __init__(self, log=Log()) -> None:
        config = ConfigParser()
        config.read('config.ini')

        self.logger = log.get_logger(__name__)

        self.argentine_banks_pages = {
            'Banco Nacion': config['ArgentineBanks']['banco_nacion'],
            'Banco Ciudad': config['ArgentineBanks']['banco_ciudad'],
            'Banco Provincia': config['ArgentineBanks']['banco_provincia'],
            'Banco Santander Rio': config['ArgentineBanks']['santander_rio'],
            'Banco Galicia': config['ArgentineBanks']['banco_galicia'],
            'BBVA Banco Frances': config['ArgentineBanks']['bbva_banco_frances'],
            'Banco Comafi': config['ArgentineBanks']['banco_comafi'],
            'Banco Patagonia': config['ArgentineBanks']['banco_patagonia'],
            'Banco ICBC': config['ArgentineBanks']['banco_icbc'],
            'Banco Supervielle': config['ArgentineBanks']['banco_supervielle'],
            'Banco Hipotecario': config['ArgentineBanks']['banco_hipotecario']
        }

    @abstractmethod
    def get_dollar_values_of_banks(self) -> list: pass
