

import sys, os
sys.path.append('../web-stock-puller')

from flask import Flask, render_template, request
from core.fetcher import get_financial_data
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error = None
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        try:
            data = get_financial_data(symbol)
            data['current_time'] = datetime.datetime.now().strftime('%c')
            data['symbol'] = symbol
            data['current_price'] = round(data['current_price'], 2)
            data['value_change'] = round(data['value_change'], 2)
            data['percentage_change'] = round(data['percentage_change'], 2)
        except ValueError as ve:
            error = str(ve)

    return render_template('index.html', data=data, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
