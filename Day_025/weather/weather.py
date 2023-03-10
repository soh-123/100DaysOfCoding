# with open("Day_025/weather_data.csv") as weater_data:
#     data = weater_data.readlines()
#     print(data)

# import csv

# with open("Day_025/weather_data.csv") as weater_data:
#     data = csv.reader(weater_data)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas

data = pandas.read_csv("Day_025/weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
sum_temp = 0
# average = sum(temp_list)/ len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
