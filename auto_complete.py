
from auto_compliete_data import AutoCompleteData
from init_data import Init

print("loading the files and preparing the system...")

init = Init()
init.init_data()


def get_score_of_delete(input_string, after_changed):
    num_for_reduce = 10
    len_change = len(after_changed)
    for i in range(len_change):
        if not input_string[i] == after_changed[i]:
            return len_change * 2 - num_for_reduce
        num_for_reduce = num_for_reduce-2 if i < 4 else 1

    return len_change * 2 - num_for_reduce


def get_score_of_add_letter(input_string, after_changed):
    num_for_reduce = 10
    len_input = len(input_string)
    for i in range(len_input):
        if not input_string[i] == after_changed[i]:
            return len_input * 2 - num_for_reduce
        num_for_reduce = num_for_reduce - 2 if i < 4 else 1

    return len_input * 2 - num_for_reduce


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
    flag = num_to_search
    for j in range(num_to_search):

        for i in range(len_):
            substring_for_search = init.data.get(substring.replace(substring[i], "", 1))
            for index in substring_for_search:
                if len(res.keys()) == num_to_search:
                    return res
                if (substring[:i + 1] + substring[i + 2:len_] in init.list_data[index]) and flag:
                    res[init.list_data[index]] = get_score_of_delete(substring, substring[:i + 1] + substring[i + 2:len_])
                    flag -= 1

    return res


def with_replace(substring, num_to_search):
    res = {}
    len_ = len(substring)
    flag = num_to_search
    for j in range(num_to_search):
        for i in range(len_):
            sub_cuts_set = set()
            if init.data.get(substring[:i + 1]) and init.data.get(substring[i + 2:len_]):
                sub_cuts_set = init.data.get(substring[:i + 1]).intersection(init.data.get(substring[i + 2:len_]))

            for index in sub_cuts_set:
                if (substring[:i + 1] + substring[i + 2:len_] in init.list_data[index]) and flag:
                    res[init.list_data[index]] = get_score_of_delete(substring, substring[:i + 1] + substring[i + 2:len_])
                    flag -= 1

    return res


def with_add(substring):
    len_ = len(substring)
    for i in range(len_):
        sub_cuts_set = set()
        if init.data.get(substring[:i]) and init.data.get(substring[i:len_]):
            sub_cuts_set = init.data.get(substring[:i]).intersection(init.data.get(substring[i:len_]))
        for index in sub_cuts_set:
            for char in range(ord('a'), ord('z') + 1):
                if substring[:i] + char + substring[i:len_] in init.list_data[index]:
                    return init.list_data[index]
    return ""


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
        max_scores = with_delete(substring, 5-len(max_scores))

    return sorted(max_scores.keys())


suggestions = search(input("The system is ready. Enter your text:\n"))

print("Here are 5 suggestions")

for i in range(5):
    print(f'{i}. {suggestions[i]}')






