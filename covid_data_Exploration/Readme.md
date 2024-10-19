# COVID Data Exploration Project

This project involves the exploration and analysis of COVID-19 data using SQL. The dataset includes information on COVID cases, deaths, and vaccinations, allowing for an in-depth analysis of various metrics such as infection rates, death rates, and vaccination coverage across different locations and continents.

## Dataset

The data used for this project is sourced from:

- **COVID Deaths Dataset** (`Covid..CovidDeaths`)
- **COVID Vaccinations Dataset** (`Covid..CovidVaccination`)

## SQL Queries

### 1. **Total Cases and Deaths by Continent**

- Filters data to show total cases and deaths per continent and country.
- Uses `MAX` to find the highest death count and infection count.

### 2. **Death Percentage Calculation**

- Calculates the likelihood of dying if infected with COVID-19 for a specific country (`India` in this case).
- Shows total deaths vs. total cases, along with the calculated death percentage.

### 3. **Infection Rate Compared to Population**

- Analyzes what percentage of a country's population contracted COVID-19.
- Highlights countries with the highest infection rates in relation to their population.

### 4. **Highest Death Count per Country and Continent**

- Displays countries and continents with the highest death counts.

### 5. **Global COVID Statistics**

- Aggregates global COVID numbers, including total cases, deaths, and death percentage globally.

### 6. **Vaccination Data**

- Joins the COVID Deaths and Vaccination datasets to show the total number of vaccinations by country and continent.
- Uses a common table expression (CTE) and a temporary table to calculate the percentage of population vaccinated.

### 7. **View Creation for Future Analysis**

- A SQL view `PercentPopulationVaccinated` is created to store data for later use in visualizations or further analysis.

## Key SQL Concepts Used

- **Aggregate Functions**: `SUM()`, `MAX()`
- **Window Functions**: `SUM() OVER (PARTITION BY)`
- **Joins**: Combining the Deaths and Vaccination datasets
- **Common Table Expressions (CTE)**: To structure the vaccination data for easier queries
- **Temporary Tables**: For temporary storage of percentage population vaccinated
- **Views**: For storing cleaned data for future visualizations

## How to Use

Clone this repository and run the SQL scripts on your preferred SQL environment. The datasets should be in a database format similar to `Covid..CovidDeaths` and `Covid..CovidVaccination`. Adjust the table names accordingly if needed.
