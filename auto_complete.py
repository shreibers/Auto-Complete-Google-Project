
from init_data import Init


k = 5

init = Init()
init.init_data()


def replace_min_score(res, score, index):
    for item in res:
        if item.get_score() < score:
            res.remove(item)
            res.append(init.list_data[index])

    return res


def with_delete(substring, num_to_search, best_k_completions):
    res = []
    len_ = len(substring)

    for i in range(len_):
        indexes_of_sentences = init.data.get(substring[:i] + substring[i + 1:])
        if indexes_of_sentences:
            for index in indexes_of_sentences:
                complete_list = [item.get_completed_sentence() for item in best_k_completions]
                if init.list_data[index].get_completed_sentence() not in complete_list:
                    score = ((len_ - 1) * 2 - (10 - 2 * i)) if i < 4 else ((len_ - 1) * 2 - 2)
                    init.list_data[index].set_score(score)
                    if len(res) == num_to_search:
                        res = replace_min_score(res, index, score)
                    else:
                        res.append(init.list_data[index])
    return res


def with_replace(substring, num_to_search, best_k_completions):
    res = []
    len_ = len(substring)
    for i in range(len_):
        for letter in range(ord('a'), ord('z') + 1):
            indexes_of_sentences = init.data.get(substring[:i] + chr(letter) + substring[i+1:])
            if indexes_of_sentences:
                for index in indexes_of_sentences:
                    complete_list = [item.get_completed_sentence() for item in best_k_completions]
                    if init.list_data[index].get_completed_sentence() not in complete_list:
                        score = ((len_ - 1) * 2 - 5 - i) if i < 4 else ((len_ - 1) * 2 - 1)
                        init.list_data[index].set_score(score)
                        if len(res) == num_to_search:
                            res = replace_min_score(res, index, score)
                        else:
                            res.append(init.list_data[index])
    return res


def with_add(substring, num_to_search, best_k_completions):
    res = []
    len_ = len(substring)

    for i in range(len_+1):
        for char in range(ord('a'), ord('z') + 1):
            index_substring_for_search = init.data.get(substring[:i] + chr(char) + substring[i:])

            if index_substring_for_search:
                for index in index_substring_for_search:
                    complete_list = [item.get_completed_sentence() for item in best_k_completions]
                    if init.list_data[index].get_completed_sentence() not in complete_list:

                        score = len_ * 2 - (10 - 2 * i) if i < 4 else (len_ * 2 - 2)
                        init.list_data[index].set_score(score)

                        if len(res) == num_to_search:
                            res = replace_min_score(res, index, score)
                        else:
                            res.append(init.list_data[index])

    return res


def get_completions_without_changes(substring):
    best_k_completions = []
    if init.data.get(substring):
        sentences = init.data[substring]
        max_score = len(substring) * 2
        for index in sentences:
            init.list_data[index].set_score(max_score)
            best_k_completions.append(init.list_data[index])

    return best_k_completions[:k]


def get_completions_with_changes(substring, num_to_search, best_k_completions):

    res = with_replace(substring, num_to_search, best_k_completions)
    res += with_add(substring, num_to_search, best_k_completions)
    res += with_delete(substring, num_to_search, best_k_completions)

    max_scores = sorted(res, key=lambda a: (a.get_score(), a.get_completed_sentence()), reverse=True)

    min_ = min(num_to_search, len(max_scores))
    return max_scores[:min_]


def get_best_k_completions(substring):

    substring = substring.capitalize()
    best_k_completions = get_completions_without_changes(substring)
    len_ = len(best_k_completions)

    if len_ < k:
        best_k_completions += get_completions_with_changes(substring, k - len_, best_k_completions)
    max_scores = sorted(best_k_completions, key=lambda a: (a.get_score(), a.get_completed_sentence()), reverse=True)
    return max_scores


x = input("The system is ready. Enter your text:\n")
suggestions = get_best_k_completions(x)
len_suggestions = len(suggestions)

print(f"Here are {len_suggestions} suggestions")

for i in range(len_suggestions):
    print(f'{i+1}. {suggestions[i].get_completed_sentence()}')


