# Movie Data Scraper

## Script Functionality

- The script scrapes movie information from The Movie Database (TMDb).
- It retrieves data from multiple pages and collects the following details for each movie:
  - **MOVIE NAME**: The name of the movie.
  - **Ratings**: The rating of the movie.
  - **GENRES**: The genres associated with the movie.
  - **RELEASE DATE**: The release date of the movie.
  - **RUNTIME**: The duration of the movie.
  - **DIRECTOR**: The director of the movie.
  - **Url**: The URL to the movie's page on TMDb.
- The script uses BeautifulSoup for parsing HTML content and requests for making HTTP requests.
- The collected data is compiled into a pandas DataFrame.
- The DataFrame is saved into an Excel file named `MovieProject.xlsx`.

## Languages and Technologies

This project involves scraping movie data using the following languages and technologies:

- **Python**: The programming language used for scripting.
- **Requests**: A Python library used for making HTTP requests.
- **BeautifulSoup4**: A library used for parsing HTML and extracting data.
- **Pandas**: A data manipulation library used to handle data and export it to Excel.
- **Excel**: The format used to save the scraped data.

## Built With

- Python
- BeautifulSoup4 - For web scraping
- Requests - For handling HTTP requests
- Pandas - For data manipulation and exporting to Excel

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.


## Acknowledgments

- Thanks to the open-source community for the tools and libraries used in this project.
- Inspired by the need to gather and analyze movie data from TMDb.
