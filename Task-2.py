# Assumption: Based on the email response, I'm assuming that the flightkey is duplicated and unique for every flight.

import pandas as pd

data = pd.read_csv('Flight.csv')

result = data.sort_values('lastupdt').groupby('flightkey').tail(1)

'''Testing: Duplicated the last entry (flightkey: DL438303130ATLCLE) for testing purpose by altering the status to 'Take-off' & time to '12:25'.
print(result[result.flightkey == 'DL438303130ATLCLE'])
'''
# Total Rows -> 244078
# print(len(data))

# Number of unique Flight Keys -> 244078
# print(len(pd.unique(data['flightkey']))) 
