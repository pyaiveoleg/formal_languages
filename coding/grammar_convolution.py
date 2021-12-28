import re
from copy import deepcopy


def get_type(token: str) -> str:
    if token.startswith("'") and token.endswith("'"):  # re.match(r"^[a-z]*$", token) or
        return "terminal"
    elif token.startswith("$"):
        return "semantic"
    else:
        return "not_terminal"


def run(res_file):
    base_codes = {
        ":": 1,
        "(": 2,
        ")": 3,
        ".": 4,
        "*": 5,
        ";": 6,
        ",": 7,
        "#": 8,
        "[": 9,
        "]": 10,
        "Eofgram": 1000
    }
    codes = deepcopy(base_codes)
    last_index = {
        "not_terminal": 10,
        "terminal": 50,
        "semantic": 100
    }
    result = [[]]
    print("Производится свёртка грамматики из файла grammar.txt")
    try:
        with open("grammar.txt") as fin:
            text = fin.read().split()
            for index, token in enumerate(text):
                if token not in codes:
                    token_type = get_type(token)
                    last_index[token_type] += 1
                    codes[token] = last_index[token_type]
                if token != "Eofgram":
                    result[-1].append(codes[token])
                if token == ".":
                    result.append([])
        print("Результат свёртки согласно таблице кодов: ", file=res_file)
        for rule in result:
            print(", ".join(map(str, rule)), file=res_file)
        print("Таблица кодов:", file=res_file)
        print("{", file=res_file)
        for k, v in sorted(codes.items(), key=lambda x: x[1]):
            print(f'\t"{k}": {v}', file=res_file)
        print("}", file=res_file)
    except:
        print("Пожалуйста, разместите файл grammar.txt в папке рядом с данным исполняемым файлом и перезапустите его.")
    print("Результат находится в файле result.txt")
    input("Для выхода нажмите Enter.")


if __name__ == "__main__":
    with open("result.txt", "w", encoding="utf-8") as fout:
        run(fout)
