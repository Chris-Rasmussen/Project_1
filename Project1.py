#Project 1

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading CSV File
df = pd.read_csv('top100.csv')

#Print most consistent artists
print(df["Artist"].value_counts())

#Creating average listens of songs per day
df['Per Day'] = df['Total Streams'] / df['Days']

#Printing 
print(df[['Song Name','Artist','Per Day']])

#Creating Bar Graph

artist = df['Artist'].head(10)
streams = df['Per Day'].head(10)

fig = plt.figure(figsize =(10,10))

plt.bar(artist[0:10], streams[0:10])

plt.xlabel("Artists\n", fontweight ="bold")
plt.ylabel("Average Streams Per Day \n", fontweight ="bold")
plt.title("Top 7 Most Streamed Spotify Artist's Average Streams", fontweight ="bold")
plt.show()