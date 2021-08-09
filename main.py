from scrap.argentineBank_scrap import ArgentineBanksScrap
from controller.bank_controller import Controller
from view.bank_view import View


def main() -> None:
    controller = Controller(ArgentineBanksScrap(), View())
    controller.show_argentine_banks_values()


if __name__ == "__main__":
    main()
