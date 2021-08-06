from functions.functions import get_partial_values_from_banks, get_str_time_now
from model.argentineBank_model import ArgentineBank
from schemas.validator import ArgentineBankSchema
from scrap.inteface_bank_scrap import Banks
from log.logger import Log


class ArgentineBanksScrap(Banks):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Log().get_logger(__name__)

    def get_dollar_values_of_banks(self) -> list[ArgentineBank]:
        try:
            self.logger.info(
                f"**********[ INICIADO EL SCRAPING DE BANCOS ARGENTINOS ]**********"
            )

            argentine_banks_list = []

            for name_page, url in self.argentine_banks_pages.items():
                try:
                    time_now = get_str_time_now()

                    partial_values = get_partial_values_from_banks(url=url)

                    new_argentine_bank = ArgentineBankSchema().load(
                        {
                            "bank_name": name_page,
                            "time": time_now,
                            "compra": partial_values[0],
                            "venta": partial_values[1],
                            "valor_con_impuestos": partial_values[3],
                        }
                    )

                    argentine_banks_list.append(new_argentine_bank)

                    self.logger.info(
                        f"* Se extrajeron los valores de compra: {new_argentine_bank.__str__()}"
                    )

                except Exception as e:
                    self.logger.error(
                        f'Error ocurrio un error en el Scraping url: "{url}", error: "{e}"'
                    )

            self.logger.info(
                f"*****************************************************************"
            )

            return argentine_banks_list

        except Exception as e:
            self.logger.error(f'Error en el Scraping de datos, error: "{e}"')
