# RareCandyExport
Rare Candy Portfolio Scraper and Exporter
A robust Python automation tool built with Playwright that logs into Rare Candy, scrolls through your entire card portfolio, extracts card details (names, set names, quantities, and market values), and outputs clean files ready for seamless collection tracking and valuation.

Features
Persistent Browser Session: Uses a local user data directory so you only have to log in manually once—subsequent runs reuse your session cookies.

Full DOM Inspection: Prompts you to load your portfolio page fully before scraping, ensuring all lazy-loaded card elements and asset images are available.

Accurate Quantity & Price Extraction: Pulls card stack quantities and market valuations while safely ignoring collection set numbers and IDs.

Total Portfolio Valuation: Automatically aggregates and prints your total estimated portfolio value directly in the console.

Outputs a structured CSV (tcgplayer_import_with_prices.csv)

Prerequisites
PyCharm (recommended)
Python 3.8 or higher

Playwright for Python

Installation & Setup
Clone or download this repository into your local project directory.

Install dependencies via your terminal:

Bash:
pip install playwright pandas
playwright install chromium


Run the Python script:


python scrape_portfolio.py
A browser window will launch and navigate to Rare Candy.

Log in to your account and navigate to your portfolio page.

Scroll down slowly in the browser window until your entire portfolio and all cards are fully loaded into view.

Go back to your terminal, press Enter when prompted (Did you login and load full page?).

The script will scrape the portfolio, calculate your total portfolio value, and generate:

tcgplayer_import_with_prices.csv (Full CSV export with prices)
