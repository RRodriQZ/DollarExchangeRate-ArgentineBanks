class View(object):
    @staticmethod
    def show_banks_values(bank_name, time, buy, sell, purchase_with_taxes):
        for i in range(len(bank_name)):
            print(f"\n")
            print(f"******************[ {bank_name[i].upper()} ]******************")
            print(f'* "BANK":                "{bank_name[i]}"')
            print(f'* "TIME":                "{time[i]}"')
            print(f'* "BUY":                 $ {buy[i]}')
            print(f'* "SELL":                $ {sell[i]}')
            print(f'* "PURCHASE WHIT TAXES": $ {purchase_with_taxes[i]}')
            print(f"*********************************************************")
