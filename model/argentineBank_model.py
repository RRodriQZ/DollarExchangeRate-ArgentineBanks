from dataclasses import dataclass


@dataclass
class ArgentineBank(object):
    """Class represents ArgentineBank model fields: bank_name, time, buy, sell, purchase_with_taxes"""

    bank_name: str
    time: str
    buy: float
    sell: float
    purchase_with_taxes: float

    def get_bank_name(self) -> str:
        return self.bank_name

    def get_time(self) -> str:
        return self.time

    def get_buy(self) -> float:
        return self.buy

    def get_sell(self) -> float:
        return self.sell

    def get_purchase_with_taxes(self) -> float:
        return self.purchase_with_taxes

    def __str__(self) -> str:
        return (
            f'[Bank]: "{self.get_bank_name()}" [Time]: "{self.get_time()}" [Buy]: ${self.get_buy()} '
            f"[Sell]: ${self.get_sell()} [Purchase with taxes]: ${self.get_purchase_with_taxes()}"
        )
