import glob


class Init:
    def __init__(self):
        self.list_data = list()
        self.data = {}

    def data_from_file(self, file_name):
        with open(file_name) as f:
            sentences = f.readlines()
        return [x.strip() for x in sentences]

    def init_data(self):
        # txt_files = glob.glob("python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")
        #
        # for file in txt_files:
        #     self.list_data += self.data_from_file(file)
        # self.list_data += self.data_from_file("copyright.txt")
        print("loading the files and preparing the system...")
        self.list_data = self.data_from_file("copyright.txt")
        for index, sentence in enumerate(self.list_data):
            length = len(sentence)
            for i in range(length):
                for j in range(i, length):
                    if not self.data.get(sentence[i:j + 1]):
                        self.data[sentence[i:j + 1]] = set()
                        self.data[sentence[i:j + 1]].add(index)
                    else:
                        self.data[sentence[i:j + 1]].add(index)







