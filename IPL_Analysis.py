import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Datasets
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("Matches Dataset Shape:", matches.shape)
print("Deliveries Dataset Shape:", deliveries.shape)

# ==========================
# Team Wise Wins Analysis
# ==========================

team_wins = matches['winner'].value_counts()

plt.figure(figsize=(10,6))
sns.barplot(x=team_wins.values, y=team_wins.index)
plt.title("Team Wise Wins in IPL")
plt.xlabel("Number of Wins")
plt.ylabel("Teams")
plt.tight_layout()
plt.savefig("team_wins.png")
plt.show()

# ==========================
# Top 10 Batsmen
# ==========================

top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_batsmen.values, y=top_batsmen.index)
plt.title("Top 10 Run Scorers")
plt.xlabel("Runs")
plt.ylabel("Players")
plt.tight_layout()
plt.savefig("top_batsmen.png")
plt.show()

# ==========================
# Top 10 Bowlers
# ==========================

wickets = deliveries[deliveries['is_wicket'] == 1]

top_bowlers = wickets['bowler'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_bowlers.values, y=top_bowlers.index)
plt.title("Top 10 Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Bowlers")
plt.tight_layout()
plt.savefig("top_bowlers.png")
plt.show()

# ==========================
# Toss Decision Analysis
# ==========================

toss_decision = matches['toss_decision'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    toss_decision.values,
    labels=toss_decision.index,
    autopct='%1.1f%%'
)
plt.title("Toss Decision Distribution")
plt.savefig("toss_decision.png")
plt.show()

# ==========================
# Toss Winner vs Match Winner
# ==========================

matches['toss_match_win'] = (
    matches['toss_winner'] == matches['winner']
)

result = matches['toss_match_win'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    result.values,
    labels=['Won Match','Lost Match'],
    autopct='%1.1f%%'
)
plt.title("Did Toss Winner Win the Match?")
plt.savefig("toss_match_result.png")
plt.show()

# ==========================
# Most Successful Venues
# ==========================

venue_matches = matches['venue'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=venue_matches.values, y=venue_matches.index)
plt.title("Top IPL Venues by Matches Hosted")
plt.xlabel("Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.savefig("venues.png")
plt.show()

# ==========================
# Season Wise Matches
# ==========================

season_matches = matches['season'].value_counts().sort_index()

plt.figure(figsize=(10,6))
season_matches.plot(marker='o')
plt.title("Season Wise Number of Matches")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.grid()
plt.tight_layout()
plt.savefig("season_matches.png")
plt.show()

print("\nAnalysis Completed Successfully!")
