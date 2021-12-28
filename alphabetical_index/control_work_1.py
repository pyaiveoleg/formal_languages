from typing import Dict


def remove_punctuation(string: str):
    filtered_string = ""
    for char in string:
        if char.isalpha() or char == " ":  # если символ является буквой или пробелом, оставляем его, иначе - убираем
            filtered_string += char
    return filtered_string.lower()  # приводим строку к нижнему регистру и возвращаем результат


def read_text(file_path):
    d = {}  # словарь, сопоставляющий слову список строк, в которых оно встречается
    with open(file_path, "r", encoding="utf-8") as text:
        for line_number, line in enumerate(text, start=1):
            # удаляем символы, не являющиеся буквами и пробелами, разделяем строку на слова (разделитель - пробел)
            for word in remove_punctuation(line).split():
                # если после фильтрации осталась пустая строка, то в исходной строке это был знак препинания, а не слово
                if not word:
                    continue

                # если слово в тексте встречается впервые, создаем для него запись в словаре
                if word not in d:
                    d[word] = []

                # если слово ещё не встречалось в этой строке, добавляем номер этой строки в список
                if line_number not in d[word]:
                    d[word].append(line_number)
    return d


def enumerate_lines(file_path, out_file):
    # читаем файл, расположенный по переданному пути
    with open(file_path, "r", encoding="utf-8") as text:
        # нумеруем в нём строки
        for line_number, line in enumerate(text, start=1):
            # выводим результат в выходной файл
            out_file.write(f"{line_number}: {line}")


def print_alphabetical_index(d: Dict, out_file):
    # сортируем словарь (сопоставляющий слову список предложений, в которых оно встречается) по алфавиту
    for k, v in sorted(d.items()):
        out_file.write(f"{k} -> {v}\n")  # выводим результат в выходной файл


if __name__ == "__main__":
    # открываем выходной файл на запись с кодировкой utf-8
    with open("output.txt", "w", encoding="utf-8") as fout:
        # нумеруем строки исходного файла и выводим результат в файл
        fout.write("Исходный текст с занумерованными строками:\n")
        enumerate_lines("input_text.txt", fout)

        # создаём алфавитный указатель и выводим результат в файл
        fout.write("\nАлфавитный указатель:\n")
        print_alphabetical_index(read_text("input_text.txt"), fout)
