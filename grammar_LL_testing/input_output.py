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
