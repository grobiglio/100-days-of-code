import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
squirrel_list = squirrel_data["Primary Fur Color"].to_list()
squirrel_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [squirrel_list.count("Gray"), squirrel_list.count("Cinnamon"), squirrel_list.count("Black")],
}
squirrel_df = pd.DataFrame(squirrel_dict)
print(squirrel_df)
squirrel_df.to_csv("squirrel_count.csv")


"""
import csv

with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    header = next(data)
    temperature = []
    for row in data:
        temperature.append(int(row[1]))
    print(temperature)
"""

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
"""
temp_list = data["temp"].to_list()
avearge_temp = sum(temp_list)/len(temp_list)
print(avearge_temp)
"""
# Get data in columns
"""
print(data["temp"].max()) # Dict like
print(data["temp"].mean())
print(data.temp.max()) # Object like

# Get data in rows
print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()]) # Dict like
print(data[data.temp == data.temp.max()]) # Object like

monday = data[data.day == "Monday"]
monday_temp_celcius = int(monday.temp)
monday_temp_farenheit = monday_temp_celcius * 9/5 + 32
print(monday_temp_farenheit)
"""