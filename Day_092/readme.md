# Top Anime Scraper

This project is a Python script that uses BeautifulSoup, requests, and pandas libraries to scrape data from the IMDb website and create a CSV file containing information about the top anime TV series.

## Description

The script retrieves data from the IMDb website's search results page for anime TV series. It specifically targets TV series with the genre "animation" and the keyword "anime," sorted by user rating and a minimum of 1000 votes. The resulting data includes the anime's title, genre, release year, and number of votes.

The script performs the following steps:

1. Imports the necessary libraries: BeautifulSoup, requests, and pandas.
2. Sends a GET request to the IMDb website's search page, specifying the desired filters and headers.
3. Parses the HTML content of the response using BeautifulSoup.
4. Extracts the titles and release years of the anime from the HTML elements using appropriate selectors.
5. Extracts the genres and number of votes using similar selectors.
6. Organizes the scraped data into a pandas DataFrame.
7. Saves the DataFrame as a CSV file named "top_anime_list.csv" in the "Day_092" directory.

## Dependencies

This project requires the following dependencies:

- Python 3.x
- BeautifulSoup
- requests
- pandas

Feel free to modify the script and adapt it to your specific needs.

## Disclaimer

This project is intended for educational purposes only. The scraping of websites may be against the terms of service of certain websites, so please ensure you are in compliance with the website's policies before using or modifying this script.

Please use responsibly and with respect for the targeted website's resources.