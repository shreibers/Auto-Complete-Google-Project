import glob

from offline.auto_compliete_data import AutoCompleteData
k = 5


class Init:
    def __init__(self):
        self.list_data = list()
        self.data = {}

    def data_from_file(self, file_name):
        with open(file_name) as file_in:
            offset = 1
            for line in file_in:
                self.list_data.append(AutoCompleteData(line.strip(), file_name, offset, 0))
                offset += 1

    def init_data(self):
        txt_files = glob.glob("../python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")
        for file in txt_files:
            self.data_from_file(file)
        # data_from_file("copyright.txt")
        for index, sentence in enumerate(self.list_data):
            length = len(sentence.get_completed())

            for i in range(length):
                for j in range(i, length):
                    sub_str = (sentence.get_completed()[i:j + 1]).lower()
                    if not self.data.get(sub_str):
                        self.data[sub_str] = set()
                        self.data[sub_str].add(index)

                    elif len(self.data.get(sub_str)) < k:
                        self.data[sub_str].add(index)
