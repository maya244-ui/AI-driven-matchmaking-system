import matplotlib.pyplot as plt # Movie names and their ratings
movies = ['Interstellar (2014)', 'The Matrix (1999)', 'Inception (2010)']
ratings = [8.6, 8.7, 8.8]import matplotlib.pyplot as plt # Movie names and their ratings
movies = ['Interstellar (2014)', 'The Matrix (1999)', 'Inception (2010)']
ratings = [8.6, 8.7, 8.8]

# Create a horizontal bar chart plt.barh(movies, ratings, color='skyblue')
# Add title and labels
plt.title('	Recommended Movies for You') plt.xlabel('Rating')
# Display rating values on the bars
for index, value in enumerate(ratings): plt.text(value + 0.05, index, str(value))
# Set x-axis limits plt.xlim(0, 10)
# Show the plot plt.show()
Heat map Program

import matplotlib.pyplot as plt import seaborn as sns
import numpy as np import pandas as pd
# Movie names and their ratings
movies = ['Interstellar (2014)', 'The Matrix (1999)', 'Inception (2010)']

ratings = [8.6, 8.7, 8.8]
# Create a DataFrame for the heatmap
df = pd.DataFrame([ratings], columns=movies) # Set up the matplotlib figure plt.figure(figsize=(8, 2))
# Draw the heatmap
sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True, linewidths=0.5, vmin=0, vmax=10) # Add title
plt.title('Recommended Movies for You') # Show the plot
plt.show()
Kernel Dencity Program import matplotlib.pyplot as plt import seaborn as sns
# Sample list of movie ratings (could be from a larger dataset) ratings = [8.6, 8.7, 8.8, 7.5, 9.0, 6.5, 8.0, 7.8, 9.2, 8.3]
# Create the Kernel Density Estimate plot sns.kdeplot(ratings, fill=True, color='skyblue') # Add labels and title
plt.title('Distribution of Movie Ratings') plt.xlabel('Rating')
plt.ylabel('Density') # Show the plot plt.show()

Outlier visualization

import matplotlib.pyplot as plt

# Sample movie ratings including some potential outliers movie_ratings = [7.5, 8.6, 8.7, 8.8, 9.5, 4.2, 8.1, 9.0, 3.5, 8.4]
# Create a boxplot to visualize outliers plt.figure(figsize=(8, 5))
plt.boxplot(movie_ratings, vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue'),
flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none')) # Add title and labels
plt.title('Outlier Detection in Movie Ratings') plt.xlabel('Rating')
# Set x-axis limits plt.xlim(0, 10)
# Show the plot plt.show()

# Create a horizontal bar chart plt.barh(movies, ratings, color='skyblue')
# Add title and labels
plt.title('	Recommended Movies for You') plt.xlabel('Rating')
# Display rating values on the bars
for index, value in enumerate(ratings): plt.text(value + 0.05, index, str(value))
# Set x-axis limits plt.xlim(0, 10)
# Show the plot plt.show()