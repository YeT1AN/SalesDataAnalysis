"""
1. Design a class that can handle data encapsulation.
2. Design an abstract class to define file reading-related functionalities and implement specific functionalities using subclasses.
3. Read files and create data objects.
4. Perform logical calculations for data requirements (calculate daily sales amounts).
5. Use PyEcharts to create graphical visualizations.
"""
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, LabelOpts, TitleOpts

text_file_reader = TextFileReader("Jan2022SalesData.txt")
json_file_reader = JsonFileReader("Feb2022SalesDataJSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# combine data from both months into a single list
all_data: list[Record] = jan_data + feb_data


# data computation
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # if a record for the current date exists, accumulate the sales amount
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money


# develop visualizations using PyEcharts
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))  # add x-axis data
bar.add_yaxis("Sales", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # add y-axis data
bar.set_global_opts(
    title_opts=TitleOpts(title="Provincial Daily Sales Summaries for January-February", pos_left="center",
                         pos_bottom="1%")
)

bar.set_global_opts(
    title_opts=TitleOpts(
        title="Provincial Daily Sales Summaries for January-February",
        pos_left="center",
        pos_bottom="1%"
    ),
    xaxis_opts=AxisOpts(name="Date"),
    yaxis_opts=AxisOpts(
        name="Sales per Day",
    ),
)

bar.render("Provincial Daily Sales Summaries for January-February 2022.html")
