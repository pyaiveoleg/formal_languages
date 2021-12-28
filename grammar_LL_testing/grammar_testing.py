def plus_k(k: int, set1: set, set2: set):
    res = set()
    for x in set1:
        for y in set2:
            res.add((x + y)[:k])
    return res


def f(l_: set, k: int, beta: str, gamma: str, grammar: dict, terminals: set, nonterminals: set):
    a = plus_k(k, first(k, beta, grammar, terminals, nonterminals), l_)
    b = plus_k(k, first(k, gamma, grammar, terminals, nonterminals), l_)
    return a.intersection(b)


from copy import deepcopy


def first(k, beta, grammar: dict, terminals: set, nonterminals: set):
    n = len(beta)
    ans = {""}
    for i in range(n):
        ans = plus_k(k, ans, first_x(k, beta[i], grammar, terminals, nonterminals))
    return ans


def first_x(k: int, x: str, grammar: dict, terminals: set, nonterminals: set):
    if x == "" or x.islower():
        return {x}

    # инициализировали F_0
    F = {a: {a} for a in terminals}
    for A in nonterminals:
        result = set()
        for beta in grammar[A]:
            if beta.islower():
                result.add(beta)
        F[A] = result

    completed = False
    while not completed:
        G = {a: {a} for a in terminals}
        for A in nonterminals:
            G[A] = deepcopy(F[A])
            for beta in grammar[A]:
                m = len(beta)
                ans = {""}
                for i in range(m):
                    ans = plus_k(k, ans, F[beta[i]])
                G[A].update(ans)
        if G == F:
            completed = True
        else:
            F = G

    return F[x]


def get_grammar(file_pth="grammar_from_homework.txt"):
    grammar_dict = {}
    with open(file_pth, "r", encoding="utf-8") as fin:
        for line in fin:
            nonterminal, chain = line.strip("\n").split(" -> ")  # remove enter in the end of line
            if chain == "`":
                chain = ""
            if nonterminal not in grammar_dict:
                grammar_dict[nonterminal] = []
            grammar_dict[nonterminal].append(chain)
    return grammar_dict


def get_terminals(file_pth="grammar_from_homework.txt"):
    terminals: set = set()
    with open(file_pth, "r", encoding="utf-8") as fin:
        for line in fin:
            nonterminal, chain = line.strip("\n").split(" -> ")  # remove enter in the end of line
            if chain == "`":
                chain = ""
            for x in chain:
                if x.islower():
                    terminals.add(x)
    return terminals


def get_nonterminals(file_pth="grammar_from_homework.txt"):
    nonterminals: set = set()
    with open(file_pth, "r", encoding="utf-8") as fin:
        for line in fin:
            nonterminal, chain = line.strip("\n").split(" -> ")  # remove enter in the end of line
            if chain == "`":
                chain = ""
            nonterminals.add(nonterminal)
            for x in chain:
                if not x.islower():
                    nonterminals.add(nonterminal)
    return nonterminals


def sigma_streak(k: int, A: str, B: str, grammar: dict, terminals: set, nonterminals: set):
    # инициализируем сигма_0
    sigma_ = dict()
    for A_ in nonterminals:
        for B_ in nonterminals:
            sigma_[A_, B_] = set()
            left_part: str
            for left_part in grammar[A_]:
                if B_ in left_part:
                    alpha = left_part[left_part.index(B_) + len(B_):]
                    sigma_[A_, B_].update(first(k, alpha, grammar, terminals, nonterminals))

    completed = False
    while not completed:
        sigma_next = deepcopy(sigma_)
        for A_ in nonterminals:
            for B_ in nonterminals:
                for left_part in grammar[A_]:
                    m = len(left_part)
                    for p in range(m):
                        alpha = left_part[p]
                        if alpha.isupper():
                            l_streak = sigma_[alpha, B_]
                            sigma_next[A_, B_].update(
                                plus_k(k, l_streak, first(k, left_part[p + 1:], grammar, terminals, nonterminals)))
        if sigma_next == sigma_:
            completed = True
        else:
            sigma_ = sigma_next
    return sigma_[A, B]


def sigma(k: int, A: str, grammar: dict, terminals: set, nonterminals: set):
    r = sigma_streak(k, "S", A, grammar, terminals, nonterminals)
    if A == "S":
        r.update("")
    return r


def get_nonterminals_with_2_or_more_alternatives(grammar: dict):
    for A in grammar:
        if len(grammar[A]) >= 2:
            yield A


def _test_ll(k: int, grammar: dict, terminals: set, nonterminals: set):
    for A in get_nonterminals_with_2_or_more_alternatives(grammar):
        for l_ in sigma(k, A, grammar, terminals, nonterminals):
            for beta in grammar[A]:
                for gamma in grammar[A]:
                    if beta == gamma:
                        continue
                    s: set = f(l_, k, beta, gamma, grammar, terminals, nonterminals)
                    # print(s)
                    if s:  # not empty
                        return False
    return True


def test_ll(k: int, grammar: dict, terminals: set, nonterminals: set):
    if _test_ll(k, grammar, terminals, nonterminals):
        print(f"Да. Данная грамматика является LL-{k}.")
    else:
        print(f"Нет. Данная грамматика не является LL-{k}")


def run_tests():
    grammar = get_grammar(file_pth="grammars/simple_grammar.txt")
    # print(grammar)
    terminals = get_terminals(file_pth="grammars/simple_grammar.txt")
    nonterminals = get_nonterminals(file_pth="grammars/simple_grammar.txt")
    assert plus_k(2, {"", "abb"}, {"b", "bab"}) == {"b", "ab", "ba"}
    assert first(2, "aAaa", grammar, terminals, nonterminals) == {'aa', 'ab'}
    assert first(2, "bAba", grammar, terminals, nonterminals) == {'bb'}
    # print(first(3, "S", get_grammar(), get_terminals(), get_nonterminals()))
    # print(sigma(3, "A", get_grammar(), get_terminals(), get_nonterminals()))
    path = "grammars/sigma_testing_grammar.txt"
    assert sigma(1, "A", get_grammar(path), get_terminals(path), get_nonterminals(path)) == {"", "a", "b"}
    assert sigma(1, "S", get_grammar(path), get_terminals(path), get_nonterminals(path)) == {""}

    path = "grammars/grammar_from_homework.txt"
    path = "grammars/simple_grammar.txt"
    path = "grammars/not_ll_grammar.txt"
    print(test_ll(1, get_grammar(path), get_terminals(path), get_nonterminals(path)))


path = "input.txt"
print(f"Данная программа предназначена для тестирования грамматики на принадлежность классу LL(k).")
print(f"Используется грамматика из файла {path}.")
k = int(input("Введите k."))
test_ll(k, get_grammar(path), get_terminals(path), get_nonterminals(path))
input("Нажмите Enter для выхода.")
