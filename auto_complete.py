
from auto_compliete_data import AutoCompleteData
from init_data import Init

print("loading the files and preparing the system...")

init = Init()
init.init_data()



def get_score_of_replace_letter(input_string, after_changed):
    num_for_reduce = 5
    len_input = len(input_string)
    for i in range(len_input):
        if not input_string[i] == after_changed[i]:
            return (len_input-1) * 2 - num_for_reduce
        num_for_reduce = num_for_reduce - 1 if i < 4 else 2

    return (len_input-1) * 2 - num_for_reduce


def with_delete(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        index_substring_for_search = init.data.get(substring.replace(substring[i], "", 1))
        if index_substring_for_search:
            for index in index_substring_for_search:
                score = (len_ - 1) * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                res[init.list_data[index]] = score
                if len(res.keys()) == num_to_search:
                    min_score = min(res.values())
                    if min_score < score:
                        for key, value in res.items():
                            if value == min_score:
                                del res[key]
                                break

                    res[init.list_data[index]] = score
    return res


def with_replace(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = init.data.get(substring.replace(substring[i], chr(char), 1))
            if index_substring_for_search:
                for index in index_substring_for_search:
                    score = (len_-1)*2 - (5 - index) if i < 4 else (len_-1)*2 - 1
                    res[init.list_data[index]] = score
                    if len(res.keys()) == num_to_search:
                        min_score = min(res.values())
                        if min_score < score:
                            for key, value in res.items():
                                if value == min_score:
                                    del res[key]
                                    break

                        res[init.list_data[index]] = score

                    else:
                        res[init.list_data[index]] = score
    return res


def with_add(substring, num_to_search):
    res = {}
    len_ = len(substring)

    for i in range(len_+1):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = init.data.get(substring[:i] + chr(char) + substring[i:])
            if index_substring_for_search:
                for index in index_substring_for_search:
                    score = len_ * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                    res[init.list_data[index]] = score
                    if len(res.keys()) == num_to_search:
                        min_score = min(res.values())
                        if min_score < score:
                            for key, value in res.items():
                                if value == min_score:
                                    del res[key]
                                    break

                        res[init.list_data[index]] = score

                    else:
                        res[init.list_data[index]] = score
    return res

def search(substring):
    max_scores = {}
    indexes = [5]
    if init.data.get(substring):
        indexes = list(init.data[substring]) if len(init.data[substring]) <= 5 else list(init.data[substring])[:5]
    max_score = len(substring)
    len_ = len(indexes)
    for i in range(len_):
        max_scores[init.list_data[indexes[i]]] = max_score*2

    if len(max_scores) < 5:
        max_scores = with_replace(substring, 5-len(max_scores))

    return sorted(max_scores.keys())


while 1:
    input_ = input("The system is ready. Enter your text:\n")
    if input_ == '#':
        break
    else:

        print(search(input_))




# print("Here are 5 suggestions")
# for i in range(1):
#      print(f'{i}. {suggestions[i]}')






