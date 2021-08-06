class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_argentine_banks_values(self):
        argentine_banks_values = self.model.get_dollar_values_of_banks()

        bank_name_list = [value.get_bank_name() for value in argentine_banks_values]
        time_list = [value.get_time() for value in argentine_banks_values]
        buy_list = [value.get_buy() for value in argentine_banks_values]
        sell_list = [value.get_sell() for value in argentine_banks_values]
        purchase_with_taxes_list = [
            value.get_purchase_with_taxes() for value in argentine_banks_values
        ]

        self.view.show_banks_values(
            bank_name_list, time_list, buy_list, sell_list, purchase_with_taxes_list
        )
