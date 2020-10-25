def replace_min(sentences, res, index, score):
    for item in res:
        if item.get_score() < score:
            res.remove(item)
            res.append(sentences[index])
    return res


def get_score_for_add_delete(index, len_substring):
    return (len_substring * 2 - (10 - 2 * index)) if index < 4 else (len_substring * 2 - 2)


def get_score_for_replace(index, len_substring):
    return ((len_substring - 1) * 2 - 5 - index) if index < 4 else ((len_substring - 1) * 2 - 1)


def get_options_to_change(sentences, indexes_of_sentences, amount, complete_list, score):
    res = []
    for index in indexes_of_sentences:

        if sentences[index].get_completed() not in complete_list:
            sentences[index].set_score(score)
            if len(res) == amount:
                res = replace_min(sentences, res, index, score)
            else:
                res.append(sentences[index])
    return res


def init_complete_list(best_k_completions):
    return [item.get_completed() for item in best_k_completions]
