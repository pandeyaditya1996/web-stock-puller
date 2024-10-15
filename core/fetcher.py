
import yfinance as yf

def get_financial_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        hist = ticker.history(period="1d")

        if not info or hist.empty:
            raise ValueError("Unable to fetch data")

        company_name = info.get('longName', 'Unknown')
        current_price = hist['Close'][0]
        previous_close = info.get('previousClose')
        value_change = current_price - previous_close
        percentage_change = (value_change / previous_close) * 100

        return {
            'company_name': company_name,
            'current_price': current_price,
            'value_change': value_change,
            'percentage_change': percentage_change
        }

    except Exception as e:
        raise ValueError(f"Error fetching data: {str(e)}")
