import string

def eliminate_left_recursion(grammar):
    nonterminals = list(grammar.keys())
    new_grammar = {}

    # Lista de nuevos no terminales disponibles: Z, Y, X, W, ...
    available_nt = list(reversed(string.ascii_uppercase))

    # Procesar cada no terminal en orden para manejar recursión indirecta
    for i, Ai in enumerate(nonterminals):
        # Sustituir producciones indirectas
        for j in range(i):
            Aj = nonterminals[j]
            new_productions = []
            for prod in grammar[Ai]:
                if prod.startswith(Aj):
                    for beta in new_grammar[Aj]:
                        new_productions.append(beta + prod[len(Aj):])
                else:
                    new_productions.append(prod)
            grammar[Ai] = new_productions

        # Eliminar recursión directa
        recursive = []
        non_recursive = []
        for prod in grammar[Ai]:
            if prod.startswith(Ai):
                recursive.append(prod[len(Ai):])
            else:
                non_recursive.append(prod)

        if recursive:
            
            new_nt = available_nt.pop(0)
            while new_nt in grammar or new_nt in new_grammar:
                new_nt = available_nt.pop(0)

            new_grammar[Ai] = [b + new_nt for b in non_recursive]
            new_grammar[new_nt] = [a + new_nt for a in recursive] + ["e"]
        else:
            new_grammar[Ai] = grammar[Ai]

    return new_grammar


def main():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f if line.strip()]

    i = 0
    t = int(data[i]); i += 1
    for _ in range(t):
        k = int(data[i]); i += 1
        grammar = {}
        for _ in range(k):
            line = data[i]; i += 1
            nt, rhs = line.split("->")
            nt = nt.strip()
            productions = rhs.strip().split()
            grammar[nt] = productions

        result = eliminate_left_recursion(grammar)

        for nt in result:
            print(f"{nt} -> {' '.join(result[nt])}")
        print() 


if __name__ == "__main__":
    main()
