from plus_k import plus_k
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
