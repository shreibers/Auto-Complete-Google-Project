import glob


data = {}
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def data_from_file(file):
    with open(file) as f:
        sentences = f.readlines()
    f.close()
    return [x.strip() for x in sentences]


big_data = list()
txt_files = glob.glob("python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")
for file in txt_files:
    big_data += data_from_file(file)


def init_data():
    for index, sentence in enumerate(big_data):
        length = len(sentence)
        for i in range(length):
            for j in range(i, length):
                if not data.get(sentence[i:j + 1]):
                    data[sentence[i:j + 1]] = set()
                    data[sentence[i:j + 1]].add(index)
                else:
                    data[sentence[i:j + 1]].add(index)


def delete(substring):
    length = len(substring)

    for i in range(length):
        intersection_set = set()
        if data.get(substring[:i+1]) and data.get(substring[i+2:length]):
            intersection_set = data[substring[:i+1]].intersection(data[substring[i+2:length]])
        for index_sub_str in intersection_set:
            if substring[:i+1] + substring[i+2:length] in big_data[index_sub_str]:
                return big_data[index_sub_str]


def replace(substring):
    length = len(substring)

    for i in range(length):
        intersection_set = set()
        if data.get(substring[:i + 1]) and data.get(substring[i + 2:length]):
            intersection_set = data[substring[:i + 1]].intersection(data[substring[i + 2:length]])
        for index in intersection_set:
            for char in chars:
                if substring[:i + 1] + char + substring[i + 2:length] in big_data[index]:
                    return big_data[index]


def add_letter(substring):
    length = len(substring)

    for i in range(length):
        intersection_set = set()
        if data.get(substring[:i]) and data.get(substring[i:length]):
            intersection_set = data[substring[:i]].intersection(data[substring[i:length]])
        for index in intersection_set:
            for char in chars:
                if substring[:i] + char + substring[i:length] in big_data[index]:
                    return big_data[index]


def get_best_k_completions(substring):
    new_substring = add_letter(substring)
    if new_substring:
        return new_substring

    if data.get(substring):
        return big_data[list(data[substring])[0]]
    return ""

# @dataclass
# class AutoCompleteData:
#         def __init__(self, completed_sentence, source_text, offset, score):
#             self.name = name
#             self.age = age
#     completed_sentence: str  source_text: str     offset: int score: int
#

init_data()

print(get_best_k_completions("Hello"))




