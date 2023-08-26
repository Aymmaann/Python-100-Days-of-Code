from requests import get
from pprint import PrettyPrinter

Base_URL = "https://free.currconv.com/"
API_key = "39953ea77af3e249a9b6"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_key}"
    url = Base_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id_ = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id_} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_key}"
    url = Base_URL + endpoint
    data = get(url).json()
    if len(data) == 0:
        print('Invalid currencies.')
        return
    rate = list(data.values())[0]
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    exchange = rate * amount
    print(f"{amount} {currency1} is equal to {exchange} {currency2}")
    return exchange


def main():
    currencies = get_currencies()
    print("Welcome to our currency converter!")
    while True:
        print("\nList - list out all the currencies")
        print("Convert - convert from one currency to another")
        print("Rate - get the exchange rate of two currencies")
        command = input("Enter a command (e to Exit): ").lower()
        
        if command == 'list':
            print_currencies(currencies)

        elif command == 'convert':
            curr1 = input("Enter base currency: ").upper()
            curr2 = input("Enter currency to be converted to: ").upper()
            amount = input(f"Enter amount(in {curr1}): ")
            convert(curr1, curr2, amount)

        elif command == 'rate':
            curr1 = input("Enter currency 1: ").upper()
            curr2 = input("Enter currency 2: ").upper()
            exchange_rate(curr1, curr2)
            rate = exchange_rate(curr1, curr2)
            print(f"The current exchange rate of {curr1} to {curr2} is {rate}")

        elif command == 'e':
            print("Thank you for using currency converter!")
            return False

        else:
            print("Invalid command\n")


main()
