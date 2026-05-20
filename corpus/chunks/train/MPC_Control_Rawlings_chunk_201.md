The next ingredient of the optimal control problem is the cost function. Practical considerations require that the cost be defined over a finite horizon N — to ensure the resultant optimal control problem can be solved sufficiently rapidly to permit effective control. We consider initially the regulation problem where the target state is the origin. If x is the current state and i the current time, then the optimal control problem may be posed as minimizing a cost defined over the interval from time i to time $N + i$ . The optimal control problem $\mathbb { P } _ { N } ( x , i )$ at event $( x , i )$ is the problem of minimizing the cost

$$\sum_ {k = i} ^ {i + N - 1} \ell (x (k), u (k)) + V _ {f} (x (N + i))$$

with respect to the sequences x $\therefore = \{ x ( i ) , x ( i { + } 1 ) , \ldots , x ( i { + } N ) \}$ and ${ \textbf { u } } : =$ $\{ u ( i ) , u ( i + 1 ) , \ldots , u ( i + N - 1 ) \}$ subject to the constraints that x and u satisfy the difference equation (2.1), the initial condition $x ( i ) = x$ , and the state and control constraints (2.2). We assume that $\ell ( \cdot )$ is continuous and that $\ell ( 0 , 0 ) = 0$ . The optimal control and state sequences, obtained by solving $\mathbb { P } _ { N } ( x , i )$ , are functions of the initial event $( x , i )$

$$
\begin{array}{l} \mathbf {u} ^ {0} (x, i) = \left\{u ^ {0} (i; (x, i)), u ^ {0} (i + 1; (x, i)), \dots , u ^ {0} (i + N - 1; (x, i)) \right\} \\ \mathbf {x} ^ {0} (x, i) = \{x ^ {0} (i; (x, i)), x ^ {0} (i + 1; (x, i)), \dots , x ^ {0} (i + N; (x, i)) \} \\ \end{array}
$$

where $x ^ { 0 } ( i ; ( x , i ) ) \ = \ x$ . In MPC, the first control action $u ^ { 0 } ( i ; ( x , i ) )$ in the optimal control sequence ${ \mathbf { u } } ^ { 0 } ( x , i )$ is applied to the plant, i.e., $u ( i ) = u ^ { 0 } ( i ; ( x , i ) )$ . Because the system $x ^ { + } = f ( x , u )$ , the stage cost $\ell ( \cdot )$ , and the terminal cost $V _ { f } ( \cdot )$ are all time invariant, however, the solution of $\mathbb { P } _ { N } ( x , i )$ , for any time $i \in \mathbb { I } _ { \geq 0 }$ , is identical to the solution of $\mathbb { P } _ { N } ( x , 0 )$ so that

$$
\begin{array}{l} \mathbf {u} ^ {0} (x, i) = \mathbf {u} ^ {0} (x, 0) \\ \mathbf {x} ^ {0} (x, i) = \mathbf {x} ^ {0} (x, 0) \\ \end{array}
$$
