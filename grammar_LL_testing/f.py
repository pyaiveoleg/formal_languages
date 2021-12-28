from first import first
from plus_k import plus_k


def f(l_: set, k: int, beta: str, gamma: str, grammar: dict, terminals: set, nonterminals: set):
    a = plus_k(k, first(k, beta, grammar, terminals, nonterminals), l_)
    b = plus_k(k, first(k, gamma, grammar, terminals, nonterminals), l_)
    return a.intersection(b)
