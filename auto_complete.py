# import glob
#
#
#
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#
#
#
#
# big_data = list()
#
#
#
#
#
#
#
# def delete(substring, data):
#     length = len(substring)
#
#     for i in range(length):
#         intersection_set = set()
#         if data.get(substring[:i+1]) and data.get(substring[i+2:length]):
#             intersection_set = data[substring[:i+1]].intersection(data[substring[i+2:length]])
#         for index_sub_str in intersection_set:
#             if substring[:i+1] + substring[i+2:length] in big_data[index_sub_str]:
#                 return big_data[index_sub_str]
#
#
# def replace(substring, data):
#     length = len(substring)
#
#     for i in range(length):
#         intersection_set = set()
#         if data.get(substring[:i + 1]) and data.get(substring[i + 2:length]):
#             intersection_set = data[substring[:i + 1]].intersection(data[substring[i + 2:length]])
#         for index in intersection_set:
#             for char in chars:
#                 if substring[:i + 1] + char + substring[i + 2:length] in big_data[index]:
#                     return big_data[index]
#
#
# def add_letter(substring, data):
#     length = len(substring)
#
#     for i in range(length):
#         intersection_set = set()
#         if data.get(substring[:i]) and data.get(substring[i:length]):
#             intersection_set = data[substring[:i]].intersection(data[substring[i:length]])
#         for index in intersection_set:
#             for char in chars:
#                 if substring[:i] + char + substring[i:length] in big_data[index]:
#                     return big_data[index]
#
#
# def get_best_k_completions(substring, data):
#     new_substring = add_letter(substring)
#     if new_substring:
#         return new_substring
#
#     if data.get(substring):
#         return big_data[list(data[substring])[0]]
#     return ""
#
#
#  class Init:
#         def __init__(self):
#             self.sub_str_data = {}
#
#
#         def data_from_file(self, file_name):
#             with open(file_name) as f:
#                 sentences = f.readlines()
#             return [x.strip() for x in sentences]
#
#
#         def init_data(self):
#             txt_files = glob.glob("python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")
#
#             for file in txt_files:
#                 big_data += self.data_from_file(file)
#
#             for index, sentence in enumerate(big_data):
#                 length = len(sentence)
#                 for i in range(length):
#                     for j in range(i, length):
#                         if not self.sub_str_data.get(sentence[i:j + 1]):
#                             data[sentence[i:j + 1]] = set()
#                             data[sentence[i:j + 1]].add(index)
#                         else:
#                             data[sentence[i:j + 1]].add(index)
#
#
#
#
# class AutoCompleteData:
#          def __init__(self, completed_sentence, source_text, offset, score):
#              self.completed_sentence = completed_sentence
#              self.source_text =  source_text
#              self.offset =  offset
#              self.score = score
#
#
# Init data
# init_data()
#
# print(get_best_k_completions("Hello"))
#
#
#

import glob
def data_from_file(file):
    with open(file) as the_file:
        sentences = the_file.readlines()
    return [x.strip() for x in sentences]
list_data = list()
# txt_files = glob.glob("python-3.8.4-docs-text/python-3.8.4-docs-text/*.txt")
# for file in txt_files:
list_data += data_from_file("copyright.txt")
data = {}
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def get_score_of_delete(input_sub, new_sub):
    score = 0
    flag = 10
    for i in range(len(input_sub)):
        if input_sub[i] != new_sub[i]:
            score -= 2 if i < 4 else flag
            flag += 2 if i < 4 else 0
        else:
            score += 2

def get_score_of_add_letter(input_sub, new_sub):
    score = 0
    flag = 10
    for i in range(len(new_sub)):
        if input_sub[i] != new_sub[i]:
                score -= 2 if i < 4 else flag
                flag -= 2 if i < 4 else 0
        else:
            score+=2







def init_data():
    for index, sentence in enumerate(list_data):
        len_ = len(sentence)
        for i in range(len_):
            for j in range(i, len_):
                if not data.get(sentence[i:j + 1]):
                    data[sentence[i:j + 1]] = set()
                    data[sentence[i:j + 1]].add(index)
                else:
                    data[sentence[i:j + 1]].add(index)


def with_delete(substring):
    len_ = len(substring)
    for i in range(len_):
        sub_cuts_set = set()
        if data.get(substring[:i+1]) and data.get(substring[i+2:len_]):
            sub_cuts_set = data.get(substring[:i+1]).intersection(data.get(substring[i+2:len_]))
        for index in sub_cuts_set:
            if substring[:i+1]+substring[i+2:len_] in list_data[index]:
                return list_data[index]
    return ""


def with_replace(substring):
    len_ = len(substring)
    for i in range(len_):
        sub_cuts_set = set()
        if data.get(substring[:i + 1]) and data.get(substring[i + 2:len_]):
            sub_cuts_set = data.get(substring[:i + 1]).intersection(data.get(substring[i + 2:len_]))
        for index in sub_cuts_set:
            for char in chars:
                if substring[:i + 1] + char + substring[i + 2:len_] in list_data[index]:
                    return list_data[index]
    return ""


def with_add(substring):
    len_ = len(substring)
    for i in range(len_):
        sub_cuts_set = set()
        if data.get(substring[:i]) and data.get(substring[i:len_]):
            sub_cuts_set = data.get(substring[:i]).intersection(data.get(substring[i:len_]))
        for index in sub_cuts_set:
            for char in chars:
                if substring[:i] + char + substring[i:len_] in list_data[index]:
                    return list_data[index]
    return ""


def search(substring):
    max_scores = {}
    indexes = [5]
    if data.get(substring):
        if len(list(data[substring])) <= 5:
            indexes = list(data[substring])
        else:
            indexes = list(data[substring])[:5]
    max_score = len(substring)
    len_ = len(indexes)
    for i in range(len_):
        max_scores[list_data[indexes[i]]] = max_score*2

    if len(max_scores) < 5:

    return sorted(max_scores.keys())


    # res = with_delete(substring)
    # if res:
    #     return res
    # res = with_replace(substring)
    # if res:
    #     return res
    # res = with_add(substring)
    # if res:
    #     return res
    # if data.get(substring):
    #     return list_data[list(data[substring])[0]]
    # return ""

# def get_score():


init_data()
print(search("All"))
