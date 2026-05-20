# Exercise 1.25: Rate-of-change penalty

Consider the generalized LQR problem with the cross term between $x ( k )$ and $u ( k )$

$$V (x (0), \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) + 2 x (k) ^ {\prime} M u (k)\right) + (1 / 2) x (N) ^ {\prime} P _ {f} x (N)$$

(a) Solve this problem with backward DP and write out the Riccati iteration and feedback gain.

(b) Control engineers often wish to tune a regulator by penalizing the rate of change of the input rather than the absolute size of the input. Consider the additional positive definite penalty matrix S and the modified objective function

$$
\begin{array}{l} V (x (0), \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) + \Delta u (k) ^ {\prime} S \Delta u (k)\right) \\ + (1 / 2) x (k) ^ {\prime} P _ {f} x (k) \\ \end{array}
$$

in which $\Delta u ( k ) = u ( k ) - u ( k - 1 )$ . Show that you can augment the state to include u(k − 1) via

$$
\tilde {\boldsymbol {x}} (\boldsymbol {k}) = \left[ \begin{array}{c} \boldsymbol {x} (\boldsymbol {k}) \\ \boldsymbol {u} (\boldsymbol {k} - 1) \end{array} \right]
$$

and reduce this new problem to the standard LQR with the cross term. What are $\tilde { { A } } , \tilde { { B } } , \tilde { { Q } } , \tilde { { R } } ,$ , and $\tilde { M }$ for the augmented problem (Rao and Rawlings, 1999)?
