class View(object):
    @staticmethod
    def show_banks_values(bank_names, bank_times, compras, ventas, compras_con_imp):
        for i in range(len(bank_names)):
            print(f"\n")
            print(f"******************[ {bank_names[i].upper()} ]******************")
            print(f'* "Crypto":              "{bank_names[i]}"')
            print(f'* "Tiempo":              "{bank_times[i]}"')
            print(f'* "Compra":              $ {compras[i]}')
            print(f'* "Ventas":              $ {ventas[i]}')
            print(f'* "Compras C/impuestos": $ {compras_con_imp[i]}')
            print(f"*********************************************************")
