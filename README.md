# news_scraper
This repository contains a Python script that scrapes the top news links from Y Combinator's Hacker News website, summarizes the news articles, and sends the summaries to your email inbox.

# Setup
Uses Python 3.10 but other versions may work.  
After cloning the repository, pip install the requirements.txt file.  
  
A .env file will need to be made with the following keys in the same directory as the main.py file(BE SURE TO INSERT YOUR OWN VALUES!):  
EMAIL_HOST  
EMAIL_HOST_USER  
EMAIL_HOST_PASSWORD  
EMAIL_PORT  

# Usage
Run main.py; a summary.txt file will be made in the current directory and be emailed using the credentials provided.
