
mockData = ["Hello nice World", "Hello World"]
data = {}


def init_data():
    for index, sentence in enumerate(mockData):
        length = len(sentence)
        for i in range(length):
            for j in range(i, length):
                if not data.get(sentence[i:j + 1]):
                    data[sentence[i:j + 1]] = set()
                    data[sentence[i:j + 1]].add(index)
                else:
                    data[sentence[i:j + 1]].add(index)


def get_best_k_completions(substring):
    if data.get(substring):
        return mockData[list(data[substring])[0]]
    return ""



init_data()
print(get_best_k_completions("lo W"))




