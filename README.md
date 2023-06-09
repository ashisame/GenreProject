# Movie Profitability Analysis

The Movie Profitability Analysis project aims to identify the most profitable type of movies by analyzing a dataset of movies. The analysis focuses on action movies that are longer than 111 minutes. The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction).

## Project Structure

The project consists of the following components:

1. Data Cleaning (SQL): The initial step involves data cleaning using SQL. The dataset is imported into a MariaDB database using DBeaver for data cleaning and preparation. The SQL code for data cleaning is provided in the file `MOVIESSQL.sql`.

2. Data Analysis (Python): The cleaned and manipulated dataset is then utilized in Python for further analysis. The `PythonMovies.py` file contains the Python code for data analysis, which involves data manipulation, exploration, and the generation of insights.

3. Data Visualization (Tableau): The cleaned dataset is connected to Tableau for creating interactive visualizations, dashboards, and a compelling story around the movie profitability analysis.

## Dependencies

The following dependencies are required to run the Python code:

- pandas: Python library for data manipulation and analysis.
- mysql-connector: Python library for connecting to the MariaDB database.

Install the dependencies using the following command:

```shell
pip install pandas mysql-connector
