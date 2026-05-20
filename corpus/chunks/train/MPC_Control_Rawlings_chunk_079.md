# 1.3.5 Controllability

A system is controllable if, for any pair of states x, z in the state space, z can be reached in finite time from x (or x controlled to z) (Sontag, 1998, p.83). A linear discrete time system $x ^ { + } = A x + B u$ is therefore controllable if there exists a finite time N and a sequence of inputs

$$\{u (0), u (1), \ldots u (N - 1) \}$$

that can transfer the system from any x to any z in which

$$
z = A ^ {N} x + \left[ \begin{array}{c c c c} B & A B & \dots & A ^ {N - 1} B \end{array} \right] \left[ \begin{array}{c} u (N - 1) \\ u (n - 2) \\ \vdots \\ u (0) \end{array} \right]
$$

We can simplify this condition by noting that the matrix powers $A ^ { k }$ for k ≥ n are expressible as linear combinations of the powers 0 to n − 1. This result is a consequence of the Cayley-Hamilton theorem (Horn and Johnson, 1985, pp. 86–87). Therefore the range of the matrix hB AB · · · $A ^ { N - 1 } B \rceil$ for N ≥ n is the same as $\left\lceil B \quad A \bar { B } \quad \cdot \cdot \cdot \quad A ^ { n - 1 } B \right\rceil$ . In other words, for an unconstrained linear system, if we cannot reach z in n moves, we cannot reach z in any number of moves. The question of controllability of a linear time-invariant system is therefore a question of existence of solutions to linear equations for an arbitrary right-hand side

$$
\left[ \begin{array}{c c c c} B & A B & \dots & A ^ {n - 1} B \end{array} \right] \left[ \begin{array}{c} u (n - 1) \\ u (n - 2) \\ \vdots \\ u (0) \end{array} \right] = z - A ^ {n} x
$$

The matrix appearing in this equation is known as the controllability matrix C

$$
C = \left[ \begin{array}{l l l l} B & A B & \dots & A ^ {n - 1} B \end{array} \right] \tag {1.17}
$$

From the fundamental theorem of linear algebra, we know a solution exists for all right-hand sides if and only if the rows of the n × nm controllability matrix are linearly independent.4 Therefore, the system (A, B) is controllable if and only if

$$\operatorname{rank} (C) = n$$

The following result for checking controllability also proves useful (Hautus, 1972).

Lemma 1.2 (Hautus Lemma for controllability). A system is controllable if and only if

$$
\operatorname{rank} \left[ \begin{array}{l l} \lambda I - A & B \end{array} \right] = n \quad \text { for   all } \lambda \in \mathbb {C} \tag {1.18}
$$

in which C is the set of complex numbers.

Notice that the first n columns of the matrix in (1.18) are linearly independent if λ is not an eigenvalue of A, so (1.18) is equivalent to checking the rank at just the eigenvalues of A

$$
\operatorname{rank} \left[ \begin{array}{l l} \lambda I - A & B \end{array} \right] = n \quad \text {   for   all   } \lambda \in \operatorname{eig} (A)
$$
