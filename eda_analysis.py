import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
data = pd.read_csv("hockey_teams.csv")
print("Dataset Loaded Successfully!\n")

#View first few Rows
print("First 5 Rows of Data:")
print(data.head())

#this is for understand Dataset Structure
print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

#Data Cleaning (Convert to Numbers)
data["Wins"] = pd.to_numeric(data["Wins"])
data["Losses"] = pd.to_numeric(data["Losses"])
data["Win Percentage"] = pd.to_numeric(data["Win Percentage"])
data["Year"] = pd.to_numeric(data["Year"])

print("\nData Types Corrected!\n")

#Now we ask the ask meaningful Questions (EDA)

# 1.Team with Highest wins
top_team = data.loc[data["Wins"].idxmax()]
print("Team with Highest Wins:")
print(top_team)

# 2.Average Wins across all Teams
avg_wins = data["Wins"].mean()
print("\nAverage Wins of Teams:", avg_wins)

# 3.Team with best win Percentage
best_team = data.loc[data["Win Percentage"].idxmax()]
print("\nBest Performing Team:")
print(best_team)

#Identify trends using Visualization

# Distribution of Wins
plt.figure()
plt.hist(data["Wins"])
plt.title("Distribution of Wins")
plt.xlabel("Number of Wins")
plt.ylabel("Frequency")
plt.show()

# Wins vs Losses Comparison
plt.figure()
plt.scatter(data["Wins"], data["Losses"])
plt.title("Wins vs Losses relationship")
plt.xlabel("Wins")
plt.ylabel("Losses")
plt.show()

print("\nEDA Analysis Completed Successfully!")