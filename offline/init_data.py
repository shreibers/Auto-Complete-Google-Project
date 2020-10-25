
import glob
import pickle as pkl
import json

from offline.auto_complete_data import AutoCompleteData
k = 5


class Init:
    def __init__(self):
        self.sentences = list()
        self.sub_sentences = dict()


    def data_from_file(self, file_name):
        with open(file_name) as file_in:
            offset = 1
            for line in file_in:
                self.sentences.append(AutoCompleteData(line.strip(), file_name, offset, 0))
                offset += 1

    def init_data(self):
        txt_files = glob.glob("../data/python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")

        for file in txt_files:
            self.data_from_file(file)

        with open("../utils/data.pkl", 'wb') as file:
            pkl.dump(self.sentences, file)

        for index, sentence in enumerate(self.sentences):
            length = len(sentence.get_completed())

            for i in range(length):
                for j in range(i, length):
                    sub_str = (sentence.get_completed()[i:j + 1]).lower()
                    if not self.sub_sentences.get(sub_str):
                        self.sub_sentences[sub_str] = list()
                        self.sub_sentences[sub_str].append(index)

                    elif len(self.sub_sentences.get(sub_str)) < k:
                        self.sub_sentences[sub_str].append(index)
                        self.sub_sentences[sub_str] = list(set(self.sub_sentences[sub_str]))

        with open("../utils/sub_strings.json", 'w') as file:
            json.dump(self.sub_sentences, file)
