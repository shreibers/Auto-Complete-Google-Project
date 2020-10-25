import json
import pickle as pkl
from dataclasses import dataclass


@dataclass
class DataFiles:
    sentences = list()
    sub_sentences = dict()

    @staticmethod
    def load_sentences():
        with open("../utils/data.pkl", 'rb') as file:
            DataFiles.sentences = pkl.load(file)

    @staticmethod
    def load_sub_sentences():
        with open("../utils/sub_strings.json", 'r') as file:
            DataFiles.sub_sentences = json.load(file)

