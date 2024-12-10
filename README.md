🚀 Stock and News Alert System

🌟 Overview

    The Stock and News Alert System is a Python-based application designed to monitor stock price fluctuations and deliver timely updates via WhatsApp. When a significant price change is detected, the system fetches the latest news headlines related to the stock and sends a curated WhatsApp message.

🛠 Features

    Real-time stock monitoring: Tracks the daily closing price of a specified stock.
    Percentage-based alerts: Calculates price change percentage and triggers alerts for significant changes.
    Automated news retrieval: Fetches the latest news articles related to the stock using the News API.
    WhatsApp notifications: Sends alerts with stock trends and news summaries via Twilio's WhatsApp API.
🎯 Why This Project?

    This project serves as a practical example of integrating APIs to build real-world applications. It demonstrates:
    
    How to work with financial and news data APIs.
    Effective usage of environment variables for sensitive data.
    Sending automated messages using Twilio's WhatsApp API.
📂 Project Structure

    .
    ├── main.py                # Main application logic
    ├── requirements.txt       # Dependencies
    └── README.md              # Project documentation
🔧 Setup Guide

    Prerequisites
    Python 3.x installed.
    API keys for:
    Alpha Vantage
    News API
    Twilio
    Twilio WhatsApp account for sending messages.
Installation
1. Clone this repository:

        git clone https://github.com/matanohana433/stock-news-alert.git
        cd stock-news-alert
2. Install dependencies:
   
         pip install -r requirements.txt
3. Configure environment variables: Create a .env file and add:


      AV_API_KEY=your_alpha_vantage_api_key
      NEWS_API_KEY=your_news_api_key
      TWILIO_AUTH_TOKEN=your_twilio_auth_token
      TWILIO_ACCOUNT_SID=your_twilio_account_sid
      TWILIO_PHONE=whatsapp:+14155238886
      MY_PHONE=whatsapp:+1234567890
🚀 Usage

1. Run the script:


      python main.py
2. The script performs the following:

         - Fetches the latest stock data for the specified stock (default: Tesla).
         - Calculates the percentage change between yesterday's and the previous day's closing prices.
         - Retrieves the top 3 news headlines if the percentage change exceeds the threshold (default: 4.9%).
         - Sends a WhatsApp message with the stock trend and news articles.
📊 Example Output

WhatsApp Notification



      TSLA: 🔺5.34%
      Headline: Tesla launches new Model X
      Brief: Tesla announces the launch of its new Model X with improved features.
      Headline: Tesla stock surges 6% after earnings
      Brief: Tesla's Q3 earnings report exceeds expectations.
      Headline: Tesla expands Gigafactory in Texas
      Brief: Tesla plans to expand its production facilities in Austin, Texas.
🔍 Key Learnings


      - API Integration: Demonstrates how to use REST APIs like Alpha Vantage and News API.
      - Automation: Automates message delivery with Twilio’s WhatsApp API.
      - Secure Coding: Uses environment variables to protect sensitive API keys.
🤔 FAQs

      Q: How do I get my Alpha Vantage API key?
      A: Sign up at Alpha Vantage, and get your free API key under the "My Account" section.
      Q: What is the free tier limit for Twilio?
      A: Twilio's free tier allows limited WhatsApp message sends. Upgrade your plan for higher limits.
🚀 Future Enhancements


      - Add support for monitoring multiple stocks.
      - Implement advanced error handling for API failures.
      - Allow users to configure stock and threshold percentage dynamically.
🤝 Contributing


      Contributions are welcome! Feel free to submit a pull request or open an issue.


📬 Contact


      Have questions? Feel free to reach out:
      Email: matanohana433@gmail.com
      GitHub: matanohana433