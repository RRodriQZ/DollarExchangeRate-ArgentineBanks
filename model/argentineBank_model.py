class ArgentineBank(object):
    def __init__(self, bank_name: str, time: str, buy: float, sell: float, purchase_with_taxes: float) -> None:
        self._bank_name = bank_name
        self._time = time
        self._buy = buy
        self._sell = sell
        self._purchase_with_taxes = purchase_with_taxes

    def get_bank_name(self) -> str:
        return self._bank_name

    def get_time(self) -> str:
        return self._time

    def get_buy(self) -> float:
        return self._buy

    def get_sell(self) -> float:
        return self._sell

    def get_purchase_with_taxes(self) -> float:
        return self._purchase_with_taxes

    def __str__(self) -> str:
        return (
            f'[Bank]: "{self.get_bank_name()}" [Time]: "{self.get_time()}" [Buy]: ${self.get_buy()} '
            f'[Sell]: ${self.get_sell()} [Purchase with taxes]: ${self.get_purchase_with_taxes()}'
        )
