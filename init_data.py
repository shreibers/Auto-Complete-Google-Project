from auto_compliete_data import AutoCompleteData
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
        print("loading the files and preparing the system...")

        self.data_from_file("copyright.txt")
        for index, sentence in enumerate(self.list_data):
            sentence.set_completed_sentence(sentence.get_completed_sentence().capitalize())
            length = len(sentence.get_completed_sentence())
            for i in range(length):
                for j in range(i, length):
                    if not self.data.get(sentence.get_completed_sentence()[i:j + 1]):
                        self.data[sentence.get_completed_sentence()[i:j + 1]] = set()
                        self.data[sentence.get_completed_sentence()[i:j + 1]].add(index)

                    elif len(self.data[sentence.get_completed_sentence()[i:j + 1]]) < k:
                        self.data[sentence.get_completed_sentence()[i:j + 1]].add(index)








