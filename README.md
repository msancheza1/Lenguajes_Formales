# Formal Languages and Compilers Assignment 1 and 2  
Student: Mariana Sánchez Araque  
Class: Si2002-5730 
Instructor: Cesar Guerra Villa

# Assignment 1 – DFA Minimization  
# Description
This program implements the DFA minimization algorithm presented in Kozen (1997), Lecture 14.  
Given a deterministic finite automaton (DFA) with no inaccessible states, the program finds equivalent states and merges them to produce a minimal DFA.

# Algorithm Explanation
The algorithm is based on partition refinement, as follows:

1. **Initialization:**  
   - Create an initial partition with two sets:  
     - F: set of final states.  
     - Q - F: set of non-final states.  

2. **Refinement:**  
   - Iteratively split partitions by checking transitions under each alphabet symbol.  
   - Two states are equivalent if, for every input symbol, their transitions go to the same partition.

3. **Termination:**  
   - The process stops when no further refinement occurs.  
   - The result is the list of **pairs of equivalent states**.

# Input Format
1. A number c > 0 representing how many cases you will receive.  
2. For each case:
   - A number n > 0 for the number of states.  
   - A line with the alphabet symbols separated by spaces.  
   - A line with the final states separated by spaces.  
   - n lines representing the transition table, in the same order as the alphabet.

# Output Format
For each case, print the pairs of equivalent states in lexicographical order, separated by spaces.  
Each case should be printed on a single line.

# Example
- Input (tarea1/input.txt)

# Output
(1, 2) (3, 4)
(1, 2) (3, 4) (3, 5) (4, 5)
(0, 3) (1, 4) (2, 5)
(0, 1)

# How to Run
1. Open the folder tarea1 in Visual Studio Code.  
2. Ensure the files minimization.py and input.txt are in the folder.  
3. Run the following command in the terminal:
   python minimization.py

# Environment
OS: Windows 10
Language: Python 3.11
Editor: Visual Studio Code

---------

# Assignment 2 – Left Recursion Elimination
# Description
This program implements the Left Recursion Elimination Algorithm described in Aho et al. (2006), Section 4.3.3.
The algorithm removes both direct and indirect left recursion from context-free grammars (CFGs) and outputs an equivalent grammar that has no left recursion. The implementation follows the input/output specifications provided in the course assignment document.

# Algorithm Explanation
Given a grammar 𝐺 =(𝑁,Σ,𝑃,𝑆) with no ε-productions or cycles:
**Indirect Left Recursion Removal:**
For each nonterminal 𝐴𝑖:
- Replace productions that begin with earlier nonterminals 𝐴𝑗(where 𝑗 < 𝑖 ) by expanding 𝐴𝑗’s productions.

**Direct Left Recursion Elimination:**  
   If any production has the form:
A → Aα1 | Aα2 | β1 | β2
A → β1Z | β2Z
Z → α1Z | α2Z | e

Here:
- Z is a new nonterminal (chosen from unused uppercase letters such as Z, Y, X, …).  
- e represents the empty string (ε).

3. **Repeat for All Nonterminals:**  
Apply the process iteratively until no left recursion remains.

# Input Format  
1. A line with a number n > 0 indicating how many cases you will receive.  
**2. For each case:**
- A natural number k > 0 representing the number of nonterminals.  
- Then k lines, each with a production in the format:
 
# Output Format  
For each case, print an equivalent grammar without left recursion following the same format as the input.  
Use single uppercase letters (Z, Y, X, …) for newly created nonterminals.  
Separate cases with a blank line.

# Example  
# Input (tarea2/input.txt)

# Output
S -> bZ
Z -> aZ e

S -> Aa b
A -> bdZ mZ
Z -> cZ adZ e

S -> AbZ
A -> cY
Z -> aZ e
Y -> cY bZcY e

# How to Run  
1. Open the folder tarea2 in Visual Studio Code.  
2. Ensure the files left_recursion.py and input.txt are present.  
3. Open the integrated terminal (Ctrl + ñ) and run:
   python left_recursion.py

# References
Aho, Alfred V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006).
Compilers: Principles, Techniques, and Tools (2nd Edition). Addison-Wesley.
Kozen, Dexter C. (1997). Automata and Computability. Springer-Verlag.
Additional clarification and testing support provided by ChatGPT (OpenAI, 2025).

