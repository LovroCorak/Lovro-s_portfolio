# Lovro-s_portfolio  
#Lovro's webscraper file 
This project implements a web scraping script designed to extract contact information, specifically phone numbers and logo URLs, from websites.  The script is written in Python and leverages the requests library for fetching website content and BeautifulSoup for parsing the HTML structure.  Regular expressions are employed for robust phone number identification, accommodating various formats.  The script iterates through user-provided URLs, extracting the desired information and printing it to the console.  Error handling is incorporated to gracefully manage potential issues such as website unavailability or unexpected HTML structures.  The code prioritizes efficiency by first searching for phone numbers in <a> tags with "tel:", "fax:", or "phone:" prefixes before exploring other tags.  Similarly, logo identification prioritizes <img> tags with "logo" in the alt or class attributes, followed by a search within the <header> tag. This approach balances accuracy and performance. This script provides a foundation for automated contact information gathering and can be further extended to include additional data points or integrated into larger data processing pipelines.  I am prepared to discuss the design choices, potential improvements, and error handling strategies in more detail during the interview
