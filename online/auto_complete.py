from typing import List, Any

from offline.init_data import Init

init = Init()


k = 5


def replace_min(res, index, score):
    for item in res:
        if item.get_score() < score:
            res.remove(item)
            res.append(init.list_data[index])
    return res


def get_score_for_add_delete(index, len_substring):
    return (len_substring * 2 - (10 - 2 * index)) if index < 4 else (len_substring * 2 - 2)


def get_score_for_replace(index, len_substring):
    return ((len_substring - 1) * 2 - 5 - index) if index < 4 else ((len_substring - 1) * 2 - 1)


def get_options_to_change(indexes_of_sentences, amount, complete_list, score):
    res = []
    for index in indexes_of_sentences:

        if init.list_data[index].get_completed() not in complete_list:
            init.list_data[index].set_score(score)
            if len(res) == amount:
                res = replace_min(res, index, score)
            else:
                res.append(init.list_data[index])
    return res


def init_complete_list(best_k_completions):
    return [item.get_completed() for item in best_k_completions]


def completions_with_delete(best_k_completions, substring, amount):
    res = []
    len_substring = len(substring)
    complete_list = init_complete_list(best_k_completions)

    for i in range(len_substring):
        indexes_of_sentences = init.data.get(substring[:i]+substring[i+1:])
        if indexes_of_sentences:
            score = get_score_for_add_delete(i, len_substring)
            res += get_options_to_change(indexes_of_sentences, amount, complete_list, score)
    return res


def completions_with_replace(best_k_completions, substring, amount):

    res = []
    len_substring = len(substring)
    complete_list = init_complete_list(best_k_completions)

    for i in range(len_substring):
        for letter in range(ord('a'), ord('z') + 1):
            indexes_of_sentences = init.data.get(substring[:i] + chr(letter) + substring[i+1:])
            if indexes_of_sentences:
                score = get_score_for_replace(i, len_substring)
                res += get_options_to_change(indexes_of_sentences, amount, complete_list, score)

    return res


def completions_with_add(best_k_completions, substring, amount):
    res = []
    len_substring = len(substring)
    complete_list = init_complete_list(best_k_completions)
    for i in range(len_substring+1):
        for letter in range(ord('a'), ord('z') + 1):
            indexes_of_sentences = init.data.get(substring[:i] + chr(letter) + substring[i:])
            if indexes_of_sentences:
                score = get_score_for_add_delete(i, len_substring)
                res += get_options_to_change(indexes_of_sentences, amount, complete_list, score)

    return res


def get_completions_without_change(substring):
    best_k_completions = []
    if init.data.get(substring):
        indexes = init.data[substring]
        max_score = len(substring)
        for index in indexes:
            init.list_data[index].set_score(max_score * 2)
            best_k_completions.append(init.list_data[index])
    return best_k_completions[:k]


def get_completions_with_change(best_k_completions, substring, amount):
    res: List[Any] = completions_with_delete(best_k_completions, substring, amount)
    res += completions_with_replace(best_k_completions+res, substring, amount)
    res += completions_with_add(best_k_completions+res, substring, amount)
    max_scores = sorted(res, key=lambda x: (x.get_score(), x.get_completed()), reverse=True)
    min_ = min(amount, len(max_scores))
    return res[:min_]


def get_best_k_completions(substring):
    substring = " ".join("".join(filter(lambda x: x.isalnum() or x.isspace(), substring)).lower().split())
    best_k_completions = get_completions_without_change(substring)
    len_ = len(best_k_completions)
    if len_ < k:
        best_k_completions += get_completions_with_change(best_k_completions, substring, k - len_)
    return sorted(best_k_completions, key=lambda x: (x.get_score(), x.get_completed()), reverse=True)
