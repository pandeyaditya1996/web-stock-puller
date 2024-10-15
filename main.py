
from core.fetcher import get_financial_data
import datetime, pytz

def main():
    symbol = input("Please enter a symbol: ")
    try:
        data = get_financial_data(symbol)
        current_time = datetime.datetime.now(pytz.timezone('US/Pacific'))  # Adjust 'US/Pacific' to your desired timezone
        print(current_time.strftime('%c %Z'))
        print(f"{data['company_name']} ({symbol})")
        print(f"{data['current_price']:.2f} {'+' if data['value_change'] >= 0 else '-'}{abs(data['value_change']):.2f} ({'+' if data['percentage_change'] >= 0 else '-'}{abs(data['percentage_change']):.2f}%)")

    except ValueError as ve:
        print(str(ve))

if __name__ == '__main__':
    main()
