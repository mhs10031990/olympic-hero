# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns=({'Total':'Total_Medals'}),inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']> data['Total_Winter'], 
                        'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 
                        'Both',data['Better_Event']) 
#print (data['Better_Event'].value_counts())
better_event = data['Better_Event'].value_counts().sort_values(ascending=False).index.tolist()[0]
#print (better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
#print (top_countries.tail(1))

top_countries.drop(top_countries.tail(1).index,inplace=True)
#print (top_countries.tail(1))

def top_ten(top_countries,column_name):
    country_list = []
    country_list = top_countries.nlargest(10,column_name)
    return country_list['Country_Name'].tolist()

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
print (top_10_summer)
print (top_10_winter)
print (top_10)
common = [x for x in top_10_summer if ((x in top_10_winter) & (x in top_10))]
print (common)




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
ax1.bar(summer_df['Country_Name'], summer_df['Total_Medals'])
ax1.set_title('Summer_Top_10')

ax2.bar(winter_df['Country_Name'], winter_df['Total_Medals'])
ax2.set_title('Winter_Top_10')

ax3.bar(top_df['Country_Name'], top_df['Total_Medals'])
ax3.set_title('Top_10')



# --------------
#Code starts here
summer_df.set_index(['Country_Name'],inplace=True)
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_country_gold = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = np.round(summer_df['Golden_Ratio'].sort_values(ascending=False)[0],2)
print (summer_country_gold,summer_max_ratio)

winter_df.set_index(['Country_Name'],inplace=True)
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_country_gold = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = np.round(winter_df['Golden_Ratio'].sort_values(ascending=False)[0],2)
print (winter_country_gold, winter_max_ratio)

top_df.set_index(['Country_Name'],inplace=True)
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_country_gold = top_df['Golden_Ratio'].idxmax()
top_max_ratio = np.round(top_df['Golden_Ratio'].sort_values(ascending=False)[0],2)
print (top_country_gold, top_max_ratio)



# --------------
#Code starts here

data = data[:-1]
data_1 = data

data_1['Total_Points'] = (3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + (data_1['Bronze_Total'])

most_points = max(data_1['Total_Points'])
#print (most_points)

best_country_df = data_1[data_1['Total_Points'] == most_points]
best_country_df1 = best_country_df.set_index(['Country_Name']).index.values
best_country = best_country_df1[0]
#print (best_country)
#print (most_points, best_country)



# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
#print (best.columns)
#print (best.values)
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


