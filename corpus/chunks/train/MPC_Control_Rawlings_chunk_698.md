$$
A _ {i j} = \left[ \begin{array}{l l} S _ {i j} ^ {s} & S _ {i j} ^ {u} \end{array} \right] \left[ \begin{array}{c c} A _ {i j} ^ {s} & - \\ & A _ {i j} ^ {u} \end{array} \right] \left[ \begin{array}{l} S _ {i j} ^ {s ^ {\prime}} \\ S _ {i j} ^ {u ^ {\prime}} \end{array} \right] \tag {6.19}
$$

in which $A _ { i j } ^ { s }$ is upper triangular and stable, and $A _ { i j } ^ { u }$ is upper triangular with all unstable eigenvalues.3 Given the Schur decomposition (6.19), we define the matrices

$$
\begin{array}{l} S _ {i} ^ {s} = \operatorname{diag} (S _ {i 1} ^ {s}, S _ {i 2} ^ {s}) \quad A _ {i} ^ {s} = \operatorname{diag} (A _ {i 1} ^ {s}, A _ {i 2} ^ {s}) \quad i \in \mathbb {I} _ {1: 2} \\ S _ {i} ^ {u} = \operatorname{diag} (S _ {i 1} ^ {u}, S _ {i 2} ^ {u}) \quad A _ {i} ^ {u} = \operatorname{diag} (A _ {i 1} ^ {u}, A _ {i 2} ^ {u}) \quad i \in \mathbb {I} _ {1: 2} \\ \end{array}
$$

These matrices satisfy the Schur decompositions

$$
A _ {i} = \left[ \begin{array}{c c} S _ {i} ^ {s} & S _ {i} ^ {u} \end{array} \right] \left[ \begin{array}{c c} A _ {i} ^ {s} & - \\ & A _ {i} ^ {u} \end{array} \right] \left[ \begin{array}{c} S _ {i} ^ {s ^ {\prime}} \\ S _ {i} ^ {u ^ {\prime}} \end{array} \right] \quad i \in \mathbb {I} _ {1: 2}
$$

We further define the matrices $\Sigma _ { 1 } , \Sigma _ { 2 }$ as the solutions to the Lyapunov equations

$$A _ {1} ^ {s ^ {\prime}} \Sigma_ {1} A _ {1} ^ {s} - \Sigma_ {1} = - S _ {1} ^ {s ^ {\prime}} Q _ {1} S _ {1} ^ {s} \quad A _ {2} ^ {s ^ {\prime}} \Sigma_ {2} A _ {2} ^ {s} - \Sigma_ {2} = - S _ {2} ^ {s ^ {\prime}} Q _ {2} S _ {2} ^ {s} \tag {6.20}$$

We then choose the terminal penalty for each subsystem to be the cost to go under zero control

$$P _ {1 f} = S _ {1} ^ {s} \Sigma_ {1} S _ {1} ^ {s ^ {\prime}} \quad P _ {2 f} = S _ {2} ^ {s} \Sigma_ {2} S _ {2} ^ {s ^ {\prime}}$$
