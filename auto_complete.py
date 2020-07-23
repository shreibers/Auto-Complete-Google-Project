
from auto_compliete_data import AutoCompleteData
from init_data import Init
import itertools
import collections

AMOUNT_COMPLETIONS = 5


def data_from_file(file_name):
    with open(file_name) as the_file:
        sentences = the_file.readlines()
    return [x.strip() for x in sentences]


print("loading the files and preparing the system...")
list_data = data_from_file("copyright.txt")
data = {}


def init_data():
    for index, sentence in enumerate(list_data):
        length = len(sentence)
        for i in range(length):
            for j in range(i, length):
                if not data.get(sentence[i:j + 1]):
                    data[sentence[i:j + 1]] = set()
                    data[sentence[i:j + 1]].add(index)
                else:
                    data[sentence[i:j + 1]].add(index)



# init = Init()
# init.init_data()



def replace_min_score(res, score, index):
    min_score = min(res.values())
    if min_score < score:
        for key, value in res.items():
            if value == min_score:
                del res[key]
                break

        res[list_data[index]] = score
    else:
        res[list_data[index]] = score


def with_delete(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        index_substring_for_search = data.get(substring[:i]+"" + substring[i+1:])

        if index_substring_for_search:
            for index in index_substring_for_search:
                score = (len_ - 1) * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                res[list_data[index]] = score

                if len(res.keys()) == num_to_search:
                    replace_min_score(res, score, index)

    return res


def with_replace(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = data.get(substring[:i] + chr(char) + substring[i+1:])

            if index_substring_for_search:

                for index in index_substring_for_search:
                    score = (len_-1)*2 - (5 - index) if i < 4 else (len_-1)*2 - 1
                    res[list_data[index]] = score

                    if len(res.keys()) == num_to_search:
                        replace_min_score(res, score, index)

    return res


def with_add(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_+1):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = data.get(substring[:i] + chr(char) + substring[i:])

            if index_substring_for_search:
                for index in index_substring_for_search:

                    score = len_ * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                    res[list_data[index]] = score

                    if len(res.keys()) == num_to_search:
                        replace_min_score(res, score, index)
    return res


def get_completions_without_changes(substring):
    best_k_completions = {}
    indexes = []
    max_score = 0
    if data.get(substring):
        indexes = list(data[substring]) if len(data[substring]) <= AMOUNT_COMPLETIONS else \
            list(data[substring])[:AutoCompleteData]
        max_score = len(substring)*2
    len_ = len(indexes)
    for j in range(len_):
        best_k_completions[list_data[indexes[j]]] = max_score

    return best_k_completions


def get_completions_with_changes(substring, num_to_search):

    res = with_replace(substring, num_to_search)
    res.update(with_add(substring, num_to_search))
    res.update(with_delete(substring, num_to_search))

    return res

    # return itertools.islice(collections.OrderedDict(res).items(), num_to_search)


def get_best_k_completions(substring):
    best_k_completions = get_completions_without_changes(substring)
    len_ = len(best_k_completions.keys())

    if len_ < AMOUNT_COMPLETIONS:
        best_k_completions.update(get_completions_with_changes(substring, AMOUNT_COMPLETIONS - len_))

    return sorted(best_k_completions.keys())

init_data()
print(get_best_k_completions("aCopyright"))
# while 1:
#     input_ = input("The system is ready. Enter your text:\n")
#     while input_ != "":
#         print(input_, end='')
#         input_ += input()
#         if input_ == '#':
#               input_ = ""
#         else:
#           print(get_best_k_completions(input_))




# print("Here are 5 suggestions")
# for i in range(1):
#      print(f'{i}. {suggestions[i]}')






