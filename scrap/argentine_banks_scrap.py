from functions.functions import get_partial_values_from_banks, get_str_time_now
from schemas.validate import validate_argentine_banks_for_schema
from model.argentineBank_model import ArgentineBank
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

                    partial_values = get_partial_values_from_banks(url)

                    buy, sale, purchase_with_taxes = (
                        partial_values[0],
                        partial_values[1],
                        partial_values[3],
                    )

                    evaluate_bank: dict[str, str, float, float, float] = {
                        "bank_name": name_page,
                        "time": time_now,
                        "buy": buy,
                        "sale": sale,
                        "purchase_with_taxes": purchase_with_taxes,
                    }

                    validate_argentine_banks_for_schema(evaluate_bank)

                    new_argentine_bank = ArgentineBank(
                        name_page, time_now, buy, sale, purchase_with_taxes
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
