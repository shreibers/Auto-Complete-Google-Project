
from auto_compliete_data import AutoCompleteData
from init_data import Init


AMOUNT_COMPLETIONS = 5

init = Init()
init.init_data()


def replace_min_score(res, score, index):
    min_score = min(res.values())
    if min_score < score:
        for key, value in res.items():
            if value == min_score:
                del res[key]
                break
        res[init.list_data[index]] = score
    return res


def with_delete(substring, num_to_search, best_k_completions):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        index_substring_for_search = init.data.get(substring[:i] + "" + substring[i+1:])

        if index_substring_for_search:
            for index in index_substring_for_search:
                if init.list_data[index] not in best_k_completions.keys():
                    score = (len_ - 1) * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                    res[init.list_data[index]] = score

                    if len(res.keys()) == num_to_search:
                        replace_min_score(res, score, index)

    return res


def with_replace(substring, num_to_search, best_k_completions):
    res = {}
    len_ = len(substring)

    for i in range(len_):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = init.data.get(substring[:i] + chr(char) + substring[i+1:])

            if index_substring_for_search:

                for index in index_substring_for_search:
                    if init.list_data[index] not in best_k_completions.keys():
                        score = (len_ - 1) * 2 - (5 - index) if i < 4 else (len_ - 1) * 2 - 1
                        res[init.list_data[index]] = score

                        if len(res.keys()) == num_to_search:
                            replace_min_score(res, score, index)

    return res


def with_add(substring, num_to_search, best_k_completions):
    res = {}
    len_ = len(substring)

    for i in range(len_+1):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = init.data.get(substring[:i] + chr(char) + substring[i:])

            if index_substring_for_search:
                for index in index_substring_for_search:
                    score = (len_ - 1) * 2 - (5 - index) if i < 4 else (len_ - 1) * 2 - 1
                    res[init.list_data[index]] = score
                    if len(res.keys()) == num_to_search:
                        replace_min_score(res, score, index)

                    score = len_ * 2 - (10 - 2 * index) if i < 4 else (len_ - 1) * 2 - 2
                    res[init.list_data[index]] = score

                    if len(res.keys()) == num_to_search:
                        replace_min_score(res, score, index)

    return res


def get_completions_without_changes(substring):
    best_k_completions = {}
    indexes = []
    max_score = 0
    if init.data.get(substring):
        indexes = list(init.data[substring])
        max_score = len(substring)*2
    len_ = len(indexes)
    for j in range(len_):
        best_k_completions[init.list_data[indexes[j]]] = max_score

    return best_k_completions


def get_completions_with_changes(substring, num_to_search, best_k_completions):

    res = with_replace(substring, num_to_search, best_k_completions)
    res.update(with_add(substring, num_to_search, best_k_completions))
    res.update(with_delete(substring, num_to_search, best_k_completions))
    max_scores = sorted(res.values(), reverse=True)
    best_amount_completion = {}

    min_ = min(num_to_search, len(max_scores))
    for i in range(min_):
        for name, score in res.items():
            if score == max_scores[i]:
                best_amount_completion[name] = score
                res[name] = 0
    return best_amount_completion


def get_best_k_completions(substring):
    substring = substring.capitalize()
    best_k_completions = get_completions_without_changes(substring)
    len_ = len(best_k_completions.keys())

    if len_ < AMOUNT_COMPLETIONS:
        best_k_completions.update(get_completions_with_changes(substring, AMOUNT_COMPLETIONS - len_, best_k_completions))

    return sorted(best_k_completions.keys())


suggestions = get_best_k_completions(input("The system is ready. Enter your text:\n"))
len_suggestions = len(suggestions)

print(f"Here are {len_suggestions} suggestions")

for i in range(len_suggestions):
    print(f'{i+1}. {suggestions[i]}')







