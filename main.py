from scrap.argentine_banks_scrap import ArgentineBanksScrap
from controller.bank_controller import Controller
from view.bank_view import View


if __name__ == '__main__':
    controller = Controller(ArgentineBanksScrap(), View())
    controller.show_argentine_banks_values()
