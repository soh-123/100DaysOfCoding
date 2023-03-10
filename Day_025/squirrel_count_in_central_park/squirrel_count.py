import pandas

data = pandas.read_csv("Day_025/squirrel_count_in_central_park/Central_Park_Squirrel.csv")

Fur_Color = ["Gray", "Cinnamon", "Black"]
titles = ["Fur Colors", "Count"]
count = []

gray_num = len(data[data["Primary Fur Color"]== "Gray"])

cinnamon_num = len(data[data["Primary Fur Color"]== "Cinnamon"])

black_num = len(data[data["Primary Fur Color"]== "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_num, cinnamon_num, black_num]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Day_025/squirrel_count_in_central_park/squirrel_colors.csv")
