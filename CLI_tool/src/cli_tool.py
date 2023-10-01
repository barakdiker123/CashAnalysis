"""CLI tools."""


class TickerOBJ:
    """Save current working tickers ."""

    def __init__(self):
        """Init the created tickers."""
        self.current_ticker = None
        self.history_tickers = []


def print_help():
    """Help the user."""
    command = input("Venus Terminal: ")
    match (command):
        case ("smooth"):
            print("Barak")
        case ("plot"):
            print("Diker")


def terminal_cli():
    """Create interface and user experience ."""
    print_help()


terminal_cli()
barak = TickerOBJ()


# def test():
#    barak = input()
#    print(barak)
#
#
# test()
