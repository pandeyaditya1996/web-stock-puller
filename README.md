# Web Stock Puller

Web Stock Puller is a Python-based application that retrieves financial data for a given stock symbol. The data includes the company's full name, its current stock price, value changes, and percentage changes. The application can be accessed both via the command line and through a web interface.

## Features

- Fetches real-time financial data for any stock symbol.
- Provides both CLI and web-based interfaces.
- Displays the current date and time along with the financial data.
- Error handling for scenarios like no network, invalid symbol, etc.

## Installation

1. Navigate to the project directory:

   ```
   cd web-stock-puller
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface:

Run the `main.py` script:

```
python main.py
```

Follow the on-screen prompts to enter the stock symbol.

### Web Interface:

1. Run the Flask app:

   ```
   python web_interface/routes.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter the stock symbol in the provided input box and click "Fetch Data".

## Deployment

The application is ready for deployment on platforms like Heroku. Follow the [official Heroku documentation](https://devcenter.heroku.com/categories/python-support) for deploying Python apps.

We will add the link here if we deploy it on heroku.

## License

[MIT](https://choosealicense.com/licenses/mit/)
