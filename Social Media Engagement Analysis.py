#Post_ID,Platform,Likes,Comments
#1,Facebook,120,30
#2,Instagram,200,45
#3,Twitter,150,25
#4,Facebook,180,40
#5,Instagram,220,55
#6,Twitter,170,35

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read data from Excel file
data = pd.read_csv("Social Media Engagement Analysis.read.csv")

# Step 2: Calculate Total Engagement (Likes + Comments)
data["Total_Engagement"] = data["Likes"] + data["Comments"]

# Step 3: Find the most liked post
most_liked = data.loc[data["Likes"].idxmax()]
print("Most Liked Post:")
print(most_liked)

# Step 4: Group by platform and calculate total engagement
platform_engagement = data.groupby("Platform")["Total_Engagement"].sum()
print("\nTotal Engagement by Platform:")
print(platform_engagement)

# Step 5: Calculate average engagement by platform
average_engagement = data.groupby("Platform")["Total_Engagement"].mean()
print("\nAverage Engagement by Platform:")
print(average_engagement)

# Step 6: Bar chart for platform engagement
platform_engagement.plot(kind="bar")
plt.title("Platform-wise Total Engagement")
plt.xlabel("Platform")
plt.ylabel("Total Engagement")
plt.show()

# Step 7: Line chart for engagement trend
plt.plot(data["Post_ID"], data["Total_Engagement"])
plt.title("Engagement Trend Across Posts")
plt.xlabel("Post ID")
plt.ylabel("Total Engagement")
plt.show()
