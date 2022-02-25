# surfs_up
Module 9: Surf's Up with Advanced Data Storage and Retrieval

## Overview of the analysis
The purpose of the challenge was to retrieve temperature information for the months of June and December from the available weather data, which contained records from 2010 to 2017.  The analysis of the temperature results would help determine if the surf and ice cream shop business would be sustainable year-round.  The dataset provided was in a **SQLite** database, which is a flat file.  Via Python, **SQLAlchamy** dependencies were added and used to connect and query the SQLite database.  Libraries, such as **Pandas** and **datetime** were also imported and used to filter, convert and create statistics from the extracted data.


## Results
The analysis results are as follows:

- Temperature for the months of June
    - <image src="./Results/Months_of_June_Temps.PNG"><b></b>
- Temperature for the months of December
    - <image src="./Results/Months_of_December_Temps.PNG"><b></b>

The following are three major points that can be said when comparing both month's analysis:
1) June has more data points than December, but since the counts are relatively high for both, it should not have too much impact on the analysis results.
2) The average temperature between the months of June and December are very similar, with December being on average lower, but only by about 4(°f) degrees
3) Based on the comparison for both months, we can say that December has lower temperatures compared to June.  The minimum temperature of December is 56(°f) while June is 64(°f).

## Summary
In summary, the weather is very similar between both months, with December being a little colder than June, but should still be good enough for surfing and ice cream making the business sustainable year-round.

Additional queries can be performed to gather more data for June and December as follows:
- Gather precipitation statistics for both months and compare the results.
- The temperate and precipitation statistics can be filtered by stations that are closer to the potential business location to see if there are any major changes to the results.
