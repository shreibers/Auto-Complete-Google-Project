from typing import List, Any

from online.auto_complete import get_best_k_completions, init


def main():
    print("loading the files and preparing the system...")
    init.init_data()

    print("The system is ready. Enter your text:")
    input_ = ''

    while 1:
        print(input_, end='')
        input_ += input()
        if input_[-1] == '#':
            input_ = ''
            continue

        suggestions: List[Any] = get_best_k_completions(input_)
        len_suggestions = len(suggestions)

        if not input_:
            print(f"Here are {len_suggestions} suggestions")

        for i in range(len_suggestions):
            print(f'{i + 1}. {suggestions[i].get_completed()} '
                  f' source_text: {suggestions[i].get_source_text()} '
                  f' offset: {suggestions[i].get_offset()} '
                  f' score:{suggestions[i].get_score()}')

        if 0 == len_suggestions:
            print(f"There are no suggestions!!")
            input_ = ''


if __name__ == '__main__':
    main()
