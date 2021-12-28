
def text_to_set(text):
    res = set()
    for line in text:
        for char in line:
            res.add(char)
    return res


def symbols_of_two_texts(text1, text2) -> set:
    symbols = set()
    symbols.update(text_to_set(text1))
    symbols.update(text_to_set(text2))
    return symbols


def symbols_only_in_first_text(text1, text2) -> set:
    symbols = set()
    symbols.update(text_to_set(text1))
    symbols = symbols.difference(text_to_set(text2))
    return symbols


def different_symbols_in_text(text) -> int:
    return len(text_to_set(text))


def run():
    with open("input_text.txt", "r", encoding="utf-8") as text1:
        with open("second_text.txt", "r", encoding="utf-8") as text2:
            print(f"Символы, встречающиеся в обоих текстах: {symbols_of_two_texts(text1, text2)}")
    with open("input_text.txt", "r", encoding="utf-8") as text1:
        with open("second_text.txt", "r", encoding="utf-8") as text2:
            print(f"Символы, встречающиеся только в первом тексте: {symbols_only_in_first_text(text1, text2)}")
    with open("input_text.txt", "r", encoding="utf-8") as text1:
        print(f"Количество различных символов в 1 тексте: {different_symbols_in_text(text1)}")


if __name__ == "__main__":
    run()
