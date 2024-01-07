"""
Class definitions related to files
"""
import json

from data_define import Record


# define an abstract class for top-level design, to determine which functionalities need to be implemented
class FileReader:

    def read_data(self) -> list[Record]:
        """read data from a file, each read data is converted into a Record object, and they are all encapsulated into a list and returned"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    # override (implement abstract method) the method from the parent class
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # remove the '\n' from each line of data read
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("Jan2022SalesData.txt")
    json_file_reader = JsonFileReader("Feb2022SalesDataJSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
