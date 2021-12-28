
def only_terminals(chain):
    return all(x.islower() for x in chain)  # все символы - нетерминалы, в нижнем регистре


def first(k: int, s: str, grammar: dict):
    alpha = s
    result = set()
    for nonterminal in grammar:
        alpha = s.replace(nonterminal, grammar[nonterminal], __count=1)  # replace only left occurrence
    return result


def replace_left_nonterminal(string: str, grammar: dict):
    for char in string:
        if char.isupper():
            return [string.replace(char, variant, 1) for variant in grammar[char]]


def replace_all_nonterminals(k: int, string: str, grammar: dict):
    res = []
    for char in string[:k]:
        if char.isupper():
            res += [string.replace(char, variant, 1) for variant in grammar[char]]
    return res


def apply_rules_recursively(k: int, grammar: dict, results):
    if all(only_terminals(x[:k]) for x in results):
        return results
    res = results[0]
    results.remove(res)
    for t in replace_all_nonterminals(k, res, grammar):
        if t not in results:
            results.append(t)
    apply_rules_recursively(k, grammar, results)


def follow(k: int, beta: str, grammar: dict):
    s = beta
    result = set()
    print(apply_rules_recursively(k, grammar, result))
    # for nonterminal in grammar:
    #     alpha = s.replace(nonterminal, grammar[nonterminal], __count=1)  # replace only left occurrence

    return result


def check_ll(k: int, grammar: dict):
    # return not first(k, "S", grammar).intersection(follow(k, "S", grammar))
    if not first(k, "S", grammar).intersection(follow(k, "S", grammar)):  # if this intersection is empty
        return True  # если условия более сложные, в одну строку не напишешь
    else:
        return False


def run():
    k = 3
    grammar_dict = {}
    with open("input.txt", "r", encoding="utf-8") as fin:
        for line in fin:
            nonterminal, chain = line.strip("\n").split(" -> ")  # remove enter in the end of line
            if nonterminal not in grammar_dict:
                grammar_dict[nonterminal] = []
            grammar_dict[nonterminal].append(chain)
    # print(grammar_dict)

    results = ["A"]
    apply_rules_recursively(k, grammar_dict, results)
    print(set(map(lambda x: x[:3], results)))  # все возможные результаты

    return
    # if check_ll(k, grammar_dict):
    #     print(f"Данная грамматика является LL({k})")
    # else:
    #     print(f"Данная грамматика не является LL({k})")


if __name__ == "__main__":
    # print(all(only_terminals(x[:3]) for x in ["aaAb"]))
    # print("aa"[:3])
    run()
