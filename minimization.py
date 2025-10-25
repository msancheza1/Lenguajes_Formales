def minimize_dfa(n, alphabet, final_states, transitions):
    all_states = set(range(n))
    F = set(final_states)
    NF = all_states - F
    P = [F, NF]
    W = [F.copy(), NF.copy()]

    def get_block(state):
        for block in P:
            if state in block:
                return block
        return None

    while W:
        A = W.pop()
        for c in alphabet:
            X = set()
            for s in all_states:
                if transitions[s][c] in A:
                    X.add(s)

            new_P = []
            for Y in P:
                inter = Y & X
                diff = Y - X
                if inter and diff:
                    new_P.extend([inter, diff])
                    if Y in W:
                        W.remove(Y)
                        W.extend([inter, diff])
                    else:
                        if len(inter) <= len(diff):
                            W.append(inter)
                        else:
                            W.append(diff)
                else:
                    new_P.append(Y)
            P = new_P

    equivalent_pairs = []
    for block in P:
        block_list = sorted(block)
        for i in range(len(block_list)):
            for j in range(i + 1, len(block_list)):
                equivalent_pairs.append((block_list[i], block_list[j]))

    equivalent_pairs.sort()
    return equivalent_pairs


def main():
    with open("input.txt", "r") as file:
        data = file.read().strip().splitlines()

    i = 0
    c = int(data[i]); i += 1
    for _ in range(c):
        n = int(data[i]); i += 1
        alphabet = data[i].strip().split(); i += 1
        final_states = list(map(int, data[i].strip().split())); i += 1

        transitions = []
        for _ in range(n):
            row = list(map(int, data[i].strip().split()))
            transitions.append({alphabet[j]: row[j] for j in range(len(alphabet))})
            i += 1

        pairs = minimize_dfa(n, alphabet, final_states, transitions)
        output = " ".join(f"({a}, {b})" for a, b in pairs)
        print(output)


if __name__ == "__main__":
    main()
