# yahoo-finance-scraper

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📖 Introduction

This project is a Yahoo Finance data scraper that fetches real-time and historical stock market data. It saves the data in .parquet format for analysis.

You can use this tool to:

-Retrieve stock prices, volumes, and trends.

-Collect financial news headlines.

-Store data efficiently for further analysis.

-Combine with my another project 'GDG_stock_tech_analysis' to form an automated real-time stock analysis system

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Features

✔️ Fetch news and stock data from Yahoo Finance

✔️ Save data in Parquet format for better performance

✔️ Automate daily scraping using GitHub Actions

✔️ Organize data into downloads/data/ folder

✔️ Simple and easy-to-use Python scripts

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Installation

🔹 Prerequisites

Python 3.8+

pip (Python package manager)

Git (optional, for cloning the repository)

feedparser

pandas

yfinance

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

▶️ Usage

1️⃣ Run the Stock Data Scraper
```sh
python scripts/stock_data_scraper.py
```
This will fetch stock data and save it to downloads/data/.

2️⃣ Run the News Scraper
```sh
python scripts/news_scraper.py
```
This will fetch financial news headlines and store them in data/news/

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure

```
yahoo-finance-scraper/
│── data/             # Folder for scraped stock data
│   ├── data/              # Stores stock_data_*.parquet files
│   ├── news/              # Stores news in .txt files
│── scripts/               # Python scripts for scraping
│   ├── stock_data_scraper.py
│   ├── news_scraper.py
│── .github/workflows/     # GitHub Actions automation scripts
│   ├── stock_data_scraper.yml
│   ├── news_scraper.yml
│── .gitignore             # Ignore unnecessary files
│── README.md              # Project documentation
│── requirements.txt       # Required Python packages
```
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🤝 Contributing

Contributions are welcome! 🚀

To contribute:

Fork the repository

Create a new branch (git checkout -b feature-branch)

Make your changes

Commit your changes (git commit -m "Added new feature")

Push to GitHub (git push origin feature-branch)

Open a Pull Request


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
