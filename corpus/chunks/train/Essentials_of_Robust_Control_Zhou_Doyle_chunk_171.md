Since the last diagonal term of P can be made arbitrarily small by making α small, the controllability of the corresponding state can be made arbitrarily weak. If the state corresponding to the last diagonal term of $P$ is removed, we get a transfer function

$$
\hat {G} = \left[ \begin{array}{c c} - 1 & 1 \\ \hline - 1 & 0 \end{array} \right] = \frac {- 1}{s + 1},
$$

which is not close to the original transfer function in any sense. The problem may be easily detected if one checks the observability Gramian $Q ,$ which is

$$
Q = \left[ \begin{array}{c c} 0. 5 & \\ & 1 / \alpha^ {2} \end{array} \right].
$$

Since $1 / \alpha ^ { 2 }$ is very large if α is small, this shows that the state corresponding to the last diagonal term is strongly observable.

This example shows that the controllability (or observability) Gramian alone cannot give an accurate indication of the dominance of the system states in the input/output behavior. This motivates the introduction of a balanced realization that gives balanced Gramians for controllability and observability.

Suppose $G = \left[ { \frac { A \left. B \right. } { C \left. D \right. } } \right]$ is stable $( \mathrm { i . e . , ~ } A$ is stable). Let P and $Q$ denote the controllability Gramian and observability Gramian, respectively. Then by Lemma 7.1, $P$ and $Q$ satisfy the following Lyapunov equations:

$$A P + P A ^ {*} + B B ^ {*} = 0 \tag {7.2}A ^ {*} Q + Q A + C ^ {*} C = 0, \tag {7.3}$$

and $P \geq 0 , Q \geq 0$ . Furthermore, the pair $( A , B )$ is controllable iff $P > 0$ , and $( C , A )$ is observable iff $Q > 0$ .

Suppose the state is transformed by a nonsingular T to $\hat { x } = T x$ to yield the realization

$$
G = \left[ \begin{array}{c c} \hat {A} & \hat {B} \\ \hline \hat {C} & \hat {D} \end{array} \right] = \left[ \begin{array}{c c} T A T ^ {- 1} & T B \\ \hline C T ^ {- 1} & D \end{array} \right].
$$

Then the Gramians are transformed to $\hat { P } = T P T ^ { * }$ and $\hat { Q } = ( T ^ { - 1 } ) ^ { * } Q T ^ { - 1 }$ . Note that $\hat { P } \hat { Q } \ = \ T P Q T ^ { - 1 }$ , and therefore the eigenvalues of the product of the Gramians are invariant under state transformation.

Consider the similarity transformation T , which gives the eigenvector decomposition

$$P Q = T ^ {- 1} \Lambda T, \Lambda = \mathrm{diag} (\lambda_ {1} I _ {s _ {1}}, \ldots , \lambda_ {N} I _ {s _ {N}}).$$
