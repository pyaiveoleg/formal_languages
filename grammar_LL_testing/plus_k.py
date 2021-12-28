def plus_k(k: int, set1: set, set2: set):
    res = set()
    for x in set1:
        for y in set2:
            res.add((x + y)[:k])
    return res
