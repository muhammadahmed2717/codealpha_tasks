# Hockey Teams Data Scraping & Analysis

This project was completed during my **CodeAlpha Internship** to practice collecting real-world data and analyzing it using Python.

# What This Project Does

* Scrapes hockey team statistics from a website using **BeautifulSoup**
* Saves the extracted data into a CSV file
* Performs **Exploratory Data Analysis (EDA)** using Pandas
* Creates visualizations to understand team performance

# Tools & Libraries Used

* Python
* requests
* BeautifulSoup
* Pandas
* Matplotlib

# Key Analysis

* Identified the team with the highest wins
* Calculated average wins across teams
* Found the best-performing team by win percentage
* Visualized:

  * Distribution of wins (Histogram)
  * Wins vs Losses relationship (Scatter Plot)

# How to Run

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

Run scraping:

```bash
python scraper.py
```

Run analysis:

```bash
python eda_analysis.py
```

# Files Included

* `scraper.py` → collects data from the website
* `eda_analysis.py` → performs analysis & visualization
* `hockey_teams.csv` → generated dataset

---

This project helped me understand the complete workflow from **data collection → cleaning → analysis → visualization**.

