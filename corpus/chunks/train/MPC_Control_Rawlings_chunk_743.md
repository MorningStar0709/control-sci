# Exercise 6.21: Stable interaction models

In some industrial applications it is preferable to partition the plant so that there are no unstable connections between subsystems. Any inputs $u _ { j }$ that have unstable connections to outputs $y _ { i }$ should be included in the ith subsystem inputs. Allowing an unstable connection between two subsystems may not be robust to faults and other kinds of system failures.4 To implement this design idea in the two-player case, we replace Assumption 6.12 (b) with the following

Assumption 6.12 (Constrained two-player game).

(b’) The interaction models $A _ { i j } , i \neq j$ are stable.

Prove that Assumption 6.12 (b’) implies Assumption 6.12 (b). It may be helpful to first prove the following lemma.

Lemma 6.17 (Local detectability). Given partitioned system matrices

$$
\boldsymbol {A} = \left[ \begin{array}{c c} A & 0 \\ 0 & A _ {s} \end{array} \right] \quad \boldsymbol {C} = \left[ \begin{array}{c c} C & C _ {s} \end{array} \right]
$$

in which $A _ { s }$ is stable, the system (A, C) is detectable if and only if the system (A, C) is detectable.

Hint: use the Hautus lemma as the test for detectability.

Next show that this lemma and Assumption 6.12 (b’) establishes the distributed detectability assumption 6.12 (b).
