import requests
from bs4 import BeautifulSoup
import csv

# Hockey Teams page 
url = "https://www.scrapethissite.com/pages/forms/"

# Send request to the website
response = requests.get(url)

# Check if page loaded successfully
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all rows containing team data
rows = soup.find_all("tr", class_="team")

# Create empty list to store extracted data
teams_data = []

# Loop through each row and extract information
for row in rows:
    name = row.find("td", class_="name").text.strip()
    year = row.find("td", class_="year").text.strip()
    wins = row.find("td", class_="wins").text.strip()
    losses = row.find("td", class_="losses").text.strip()
    pct = row.find("td", class_="pct").text.strip()

    teams_data.append([name, year, wins, losses, pct])

# Save data into CSV file
with open("hockey_teams.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Team Name", "Year", "Wins", "Losses", "Win Percentage"])

    # Write actual data
    writer.writerows(teams_data)

print("Scraping complete! File 'hockey_teams.csv' created.")