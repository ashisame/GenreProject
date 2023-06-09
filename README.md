# Movie Profitability Analysis

The Movie Profitability Analysis project aims to identify the most profitable type of movies by analyzing a dataset of movies. The analysis focuses on action movies that are longer than 111 minutes. The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction).

## Project Structure

The project consists of the following components:

1. Data Cleaning (SQL): The initial step involves data cleaning using SQL. The dataset is imported into a MariaDB database using DBeaver for data cleaning and preparation. The SQL code for data cleaning is provided in the file `MOVIESSQL.sql`.

2. Data Analysis (Python): The cleaned and manipulated dataset is then utilized in Python for further analysis. The `PythonMovies.py` file contains the Python code for data analysis, which involves data manipulation, exploration, and the generation of insights. **Note: The `PythonMovies.py` file requires a `config.py` file to connect to the database. Please create a `config.py` file and populate it with the necessary connection details (host, user, password, etc.) before running the script. Make sure to add `config.py` to the `.gitignore` file to prevent sensitive information from being exposed.**

3. Data Visualization (Tableau): The cleaned dataset is connected to Tableau for creating interactive visualizations, dashboards, and a compelling story around the movie profitability analysis.

## Usage

To utilize this project, follow the steps below:

1. Data Cleaning:
   - Import the dataset into a MariaDB database using DBeaver or any other compatible tool.
   - Run the SQL code provided in the `MOVIESSQL.sql` file to clean and prepare the dataset.

2. Data Analysis:
   - Open the `PythonMovies.py` file in a Python IDE (e.g., Visual Studio Code).
   - Create a `config.py` file and populate it with the necessary database connection details.
   - **Note: Make sure to add `config.py` to the `.gitignore` file to prevent sensitive information from being exposed.**
   - Run the Python code to perform data manipulation, exploration, and generate insights.

3. Data Visualization:
   - Connect the cleaned and manipulated dataset to Tableau.
   - Create visualizations, dashboards, and stories in Tableau to present the movie profitability analysis.

## Insights

Based on the analysis, the following insights were derived:

- Action movies accounted for approximately 46% of all votes.
- Movies longer than 111 minutes have an average rating (popularity) that is 0.8 higher than shorter movies.
- There is a positive correlation between the number of votes and movie ratings (popularity).
- Movies with higher ratings (popularity) tend to have higher gross earnings.


These insights provide valuable information for understanding the profitability and popularity trends in the movie industry.

## Contributing

Contributions to the Movie Profitability Analysis project are welcome! If you have any ideas for improvements, additional analysis techniques, or enhancements to the visualizations, feel free to open a pull request. Please ensure that your contributions align with the project's coding standards and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
