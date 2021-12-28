from sigma import sigma
from input_output import get_grammar, get_terminals, get_nonterminals
from f import f
from plus_k import plus_k
from first import first


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


# if __name__ == "__main__":
    # path = "grammars/grammar_from_homework.txt"
path = "input.txt"
print(f"Используется грамматика из файла {path}")
test_ll(3, get_grammar(path), get_terminals(path), get_nonterminals(path))
# input("Нажмите Enter для выхода.")
# run_tests()
