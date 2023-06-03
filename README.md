Project Name: Kinoparser

Description:
This project is a data parser that extracts information about movies from the web page "https://www.kinopoisk.ru/lists/movies/genre--anime/" on the Kinopoisk website. The project was developed during learning and written in Python.

The main functionality of the project includes:

Using the requests library to send GET requests to the web page and retrieve the HTML content.
Using the BeautifulSoup library for parsing the HTML content and extracting data.
Using the time module to add a delay between server requests to avoid blocking.
Creating an empty list called data to store movie data.
Iterating through pages (from 1 to 5) and retrieving data for each movie.
Extracting information about movies such as link, Russian name, original name, country, and rating.
Appending the extracted data to the data list.
Creating a DataFrame object using the pandas library to organize the data.
Exporting the data to a CSV file with ";" as the delimiter and UTF-8 encoding.
Printing the number of extracted movies to the console.
This project serves as an example of web scraping for data extraction and further processing in a structured format. 😄
