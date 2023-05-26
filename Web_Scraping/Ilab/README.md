## Web Scraping of Antique Booksellers
<!--- --->

This project focuses on collecting information on antique booksellers from around the world. The website chosen for data extraction is ilab.org. The objective is to gather data on various booksellers, including their business type, name, phone number, website, email, and address.

## Objective
<!--- --->
The objective of this project is to scrape data from ilab.org to create a comprehensive database of antique booksellers. By automating the data extraction process, we aim to gather information efficiently and effectively.

##Solution
<!--- --->

To achieve the objective, a web scraping solution was implemented using Python 3 along with Scrapy and BeautifulSoup libraries. Scrapy provides a powerful framework for web scraping, while BeautifulSoup helps in parsing the HTML content.

##Methodology
<!--- --->

The project utilizes a spider called "SellersSpider," which is a subclass of the scrapy.Spider class. The spider is configured with the following properties and methods:

# name: Defines the name of the spider.
# allowed_domains: Specifies the domains the spider is allowed to access.
# start_urls: Specifies the initial URL for data extraction.
# parse: The method responsible for extracting information from the HTML page and returning it.
# Parsing with BeautifulSoup is employed to remove extra characters from the bookseller information. The "clear_address" method is responsible for removing HTML tags and unwanted characters from the address information.

## Data Extraction
<!--- --->
Within the "parse" method, the bookseller data is extracted using Scrapy's response object and CSS selectors. The "response.css" method fetches the CSS selectors corresponding to the desired data, and the ".get()" method retrieves the text inside the corresponding HTML element.

Each bookseller is represented by an item containing the following information:

# business: Type of bookseller business.
# name: Name of the bookseller.
# phone: Phone number of the bookseller.
# site: Website of the bookseller.
# email: Email of the bookseller.
# address: Address of the bookseller.
# Pagination
To navigate through all the pages listing the booksellers, the site's pagination logic is utilized. The initial URL contains the "page=1" parameter, representing the first page. The spider follows the link to the next page using the "response.follow" method, and data extraction continues in the "parse" method using the "callback" parameter.

## Technologies Used
<!--- --->

Python 3
Scrapy
BeautifulSoup
Result
The result of the web scraping process is a JSON file containing the extracted bookseller information. Each line in the JSON file represents a bookseller and their corresponding information.

## Conclusion
<!--- --->

By leveraging web scraping techniques and utilizing Scrapy and BeautifulSoup libraries, we successfully collected comprehensive data on antique booksellers from ilab.org. The automated data extraction process allows for efficient and accurate gathering of information. This dataset can be further analyzed or used for various purposes related to antique booksellers.

The implemented solution demonstrates the power of web scraping in data collection and the importance of selecting appropriate tools and libraries for the task at hand.
