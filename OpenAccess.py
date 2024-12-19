# This is an example of adata visualization on the growth of open access articles.
# Programmer: Johanna Österåker, ORCID 0009-0007-1951-5214
# Date: 2024-12-19



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# Upload the Excel file 

file_path = 'AssignmentOpenAccess.xlsx'  
data = pd.read_excel(file_path)


# Extracting the columns and converting them to numpy arrays

years = np.array(data['Year'].tolist())
open_access_articles = np.array(data['OA'].tolist())
total_articles = np.array(data['Total'].tolist())


# Decision on success based on the percentage of open access articles

percentage_oa = (open_access_articles / total_articles) * 100
average_percentage_oa = np.mean(percentage_oa)

if average_percentage_oa > 50:
    print("Open Access is a success.")
elif average_percentage_oa == 0:
    print("There are no Open Access articles.")
else: 
    print("Open Access is soon a success")


# Plot the data using a 3D bar chart

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')


# Define the positions of the bars

x_pos = np.arange(len(years))
y_pos = np.zeros(len(years))
z_pos = np.zeros(len(years))


# Define the bar heights

dx = np.ones(len(years))
dy = np.ones(len(years))
dz_oa = open_access_articles
dz_total = total_articles


# Plot the bars

ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz_oa, color='b', alpha=0.7, label='Open Access Articles')
ax.bar3d(x_pos, y_pos, dz_oa, dx, dy, dz_total - dz_oa, color='r', alpha=0.7, label='Total Articles')


# Set the labels

ax.set_xlabel('Year')
ax.set_ylabel('')  
ax.set_zlabel('Number of Articles')
ax.set_xticks(x_pos)
ax.set_xticklabels(years)
ax.set_title('Open Access Articles vs Total Articles per Year')


# Add a legend

ax.legend()

plt.show()




