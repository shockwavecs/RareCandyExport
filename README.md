# Rare Candy Portfolio Scraper

A Python automation tool built with **Playwright** that logs into [Rare Candy](https://rarecandy.com/), scrolls through your entire card portfolio, extracts card details (names, set names, quantities, and market values), calculates your total portfolio valuation, and exports a clean CSV report.

---

## Features

* **Persistent Browser Session:** Uses a local user data directory so you only have to log in manually once—subsequent runs reuse your session cookies.
* **Full DOM Inspection:** Prompts you to load your portfolio page fully before scraping, ensuring all lazy-loaded card elements and asset images are available.
* **Accurate Quantity & Price Extraction:** Pulls card stack quantities and market valuations while safely ignoring collection set numbers and IDs.
* **Total Portfolio Valuation:** Automatically aggregates and prints your total estimated portfolio value directly in the console.
* **Structured Export:** Generates a complete CSV file (`tcgplayer_import_with_prices.csv`) containing your quantities, product names, set names, conditions, and individual card market prices.

---

## Prerequisites

* Python 3.8 or higher
* Playwright for Python
* Pandas

> **💡 Pro-Tip:** Using **PyCharm** makes managing this script, installing requirements, and running your virtual environment (`.venv`) seamless. You can open your project directory directly in PyCharm, use the built-in terminal to install dependencies, and run or debug your script with a single click.

---

## Installation & Setup

1. **Clone or download** this repository into your PyCharm project directory.
2. **Install dependencies** via the PyCharm terminal:
   ```bash
   pip install playwright pandas
   playwright install chromium

<img width="796" height="299" alt="Screenshot 2026-10-10 120703" src="https://github.com/user-attachments/assets/187a2768-0887-45f1-a377-57c56c7aeab1" />


<img width="1274" height="841" alt="Screenshot 2026-10-10 120650" src="https://github.com/user-attachments/assets/95a69662-8d23-4861-91c0-ab6dcf1fdc11" />


<img width="762" height="461" alt="Screenshot 2026-10-10 121411" src="https://github.com/user-attachments/assets/a6152e86-3db2-4a81-a4f5-171d5d46d970" />
