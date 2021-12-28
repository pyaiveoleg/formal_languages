from first import first
from plus_k import plus_k
from copy import deepcopy


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
                            sigma_next[A_, B_].update(plus_k(k, l_streak, first(k, left_part[p + 1:], grammar, terminals, nonterminals)))
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
