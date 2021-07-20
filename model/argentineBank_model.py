class ArgentineBank(object):
    def __init__(self, bank_name: str, time: str, compra: float, venta: float, valor_con_impuestos: float) -> None:
        self._bank_name = bank_name
        self._time = time
        self._compra = compra
        self._venta = venta
        self._valor_con_impuestos = valor_con_impuestos

    def get_bank_name(self) -> str:
        return self._bank_name

    def get_time(self) -> str:
        return self._time

    def get_compra(self) -> float:
        return self._compra

    def get_venta(self) -> float:
        return self._venta

    def get_valor_con_impuesto(self) -> float:
        return self._valor_con_impuestos

    def __str__(self) -> str:
        return (
            f'[Bank]: "{self.get_bank_name()}" [Time]: "{self.get_time()}" [Compra]: ${self.get_compra()} '
            f'[Venta]: ${self.get_venta()} [Compra C/Impuestos]: ${self.get_valor_con_impuesto()}'
        )
