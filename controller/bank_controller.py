class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_argentine_banks_values(self):
        argentine_banks_values = self.model.get_dollar_values_of_banks()

        bank_names = [value.get_bank_name() for value in argentine_banks_values]
        bank_times = [value.get_time() for value in argentine_banks_values]
        compras = [value.get_compra() for value in argentine_banks_values]
        ventas = [value.get_venta() for value in argentine_banks_values]
        compras_con_imp = [value.get_valor_con_impuesto() for value in argentine_banks_values]

        self.view.show_banks_values(bank_names,
                                    bank_times,
                                    compras,
                                    ventas,
                                    compras_con_imp)
