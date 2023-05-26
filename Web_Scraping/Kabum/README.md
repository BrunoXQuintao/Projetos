Web Scraping - Kabum Gaming Chairs
<!--- --->
This project aims to perform web scraping on the Kabum website to obtain information about gaming chairs. The extracted data is processed and stored for further analysis.

## Project Objective:
<!--- --->

The objective of this project is to gather data on gaming chairs available on the Kabum website, including brand and price information. This data can be used for market analysis, price comparison, and other investigations related to the gaming chair market.

## Data Processing:
<!--- --->

After the data extraction, it undergoes processing to ensure data consistency and quality. In this project, data processing involves the following steps:

Special character cleaning: The brand and price values undergo a special character removal process using the unidecode library.
Column renaming: The column names are renamed to 'Brand' and 'Price' for better data understanding.
Output format: The processed data is stored in a CSV file with ';' as the separator and UTF-8 encoding.
Data Analysis:
<!--- --->

After the data processing, it becomes possible to perform additional analysis and investigations. Some examples of analysis that can be done with the data obtained in this project are:

Descriptive statistics: Calculate basic statistics such as mean, median, and standard deviation of gaming chair prices.
Brand comparison: Identify the most popular or expensive brands based on the collected data.
Price trends: Observe price variations across pages or over time to identify market trends.
<!--- --->

## Technologies Used:
<!--- --->

Python: The programming language used to develop the web scraping script and data manipulation.
Requests library: Used to make HTTP requests to the Kabum website and obtain page content.
BeautifulSoup library: Used to parse HTML and extract desired information.
Pandas library: Used for data manipulation and analysis, including DataFrame creation and writing to a CSV file.
Math library: Used for mathematical calculations, such as rounding the number of pages.
Unidecode library: Used to remove special characters from the data.

## Conclusion:
<!--- --->

This project demonstrates how to perform web scraping on a specific website to obtain relevant data. Through proper data processing, it becomes possible to perform analysis and gain valuable insights into the gaming chair market. However, it is important to note that the use of web scraping should be done in compliance with the terms of use of the target website and applicable laws and regulations.
