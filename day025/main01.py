# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)

# Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 76]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = sum(data["Primary Fur Color"] == "Gray")
cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")
black = sum(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("squirrel_count.csv")