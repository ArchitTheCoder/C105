import pandas as pd
import plotly.express as plotly
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

# file_data.pop(0)
total_marks = 0
data = file_data[0]
total_entries = len(data)

for marks in data:
    total_marks += float(marks)

mean = total_marks / total_entries
print(mean)

df = pd.read_csv("data.csv")
# fig = plotly.scatter(df, x = "Student Number", y = "Marks")
# fig.update_layout(shapes = [
#     dict(
#         type = "line",
#         y0 = mean,
#         y1 = mean,
#         x0 = 0,
#         x1 = total_entries, 
#     )
# ])

# fig.show()