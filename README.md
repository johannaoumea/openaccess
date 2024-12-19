# openaccess
# Short description
The goal of this program is to analyze and visualize the distribution of open access articles versus total articles over a series of years. The data is provided in an Excel file (AssignmentOpenAccess.xlsx), which contains columns for the year, the number of open access articles, and the total number of articles published each year. 

# Design
BEGIN

  IMPORT necessary libraries (pandas, matplotlib.pyplot, numpy, mpl_toolkits.mplot3d)

  SET file_path to 'AssignmentOpenAccess.xlsx'
  READ Excel file into 'data'

  EXTRACT 'Year' column from 'data' and convert to numpy array 'years'
  EXTRACT 'OA' column from 'data' and convert to numpy array 'open_access_articles'
  EXTRACT 'Total' column from 'data' and convert to numpy array 'total_articles'

  CALCULATE percentage of open access articles as (open_access_articles / total_articles) * 100
  CALCULATE average percentage of open access articles as mean of percentage_oa

  IF average_percentage_oa > 50 THEN
    PRINT "Open Access is a success."
  ELSE IF average_percentage_oa == 0 THEN
    PRINT "There are no Open Access articles."
  ELSE
    PRINT "Open Access is soon a success."
  END IF

  CREATE a new figure for plotting with size (12, 8)
  ADD a 3D subplot to the figure

  DEFINE x_pos as range of length of 'years'
  DEFINE y_pos as zeros of length of 'years'
  DEFINE z_pos as zeros of length of 'years'

  DEFINE dx as ones of length of 'years'
  DEFINE dy as ones of length of 'years'
  DEFINE dz_oa as 'open_access_articles'
  DEFINE dz_total as 'total_articles'

  PLOT 3D bars for open access articles with x_pos, y_pos, z_pos, dx, dy, dz_oa, color 'b', alpha 0.7, label 'Open Access Articles'
  PLOT 3D bars for total articles with x_pos, y_pos, dz_oa, dx, dy, dz_total - dz_oa, color 'r', alpha 0.7, label 'Total Articles'

  SET x-axis label to 'Year'
  SET y-axis label to ''
  SET z-axis label to 'Number of Articles'
  SET x-axis ticks to x_pos
  SET x-axis tick labels to 'years'
  SET title to 'Open Access Articles vs Total Articles per Year'

  ADD legend to the plot

  DISPLAY the plot
END


# Testing/verification
Debugging: white box testing was completed.

Checking results: a comparison was made with a similar graph in excel based on the same data, i.e. black box testing. Although the graph in Excel is not in 3d, these two graphs seem very similar in the way they are built.
