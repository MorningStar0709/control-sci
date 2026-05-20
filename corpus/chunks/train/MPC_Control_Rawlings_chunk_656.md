$$
\left[ \begin{array}{c c c c} & R & B ^ {\prime} & \\ A & B & & - I \\ & & - I & \Pi (N) \end{array} \right] \left[ \begin{array}{c} x (N - 1) \\ u (N - 1) \\ \lambda (N) \\ x (N) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right]
$$

We can eliminate this small set of equations and solve for $u ( N - 1 )$ , $\lambda ( N ) , x ( N )$ in terms of $x ( N - 1 )$ , resulting in

$$
\left[ \begin{array}{c} u (N - 1) \\ \lambda (N) \\ x (N) \end{array} \right] = \left[ \begin{array}{c} - (B ^ {\prime} \Pi (N) B + R) ^ {- 1} B ^ {\prime} \Pi (N) A \\ \Pi (N) (I - B (B ^ {\prime} \Pi (N) B + R) ^ {- 1} B ^ {\prime} \Pi (N)) A \\ (I - B (B ^ {\prime} \Pi (N) B + R) ^ {- 1} B ^ {\prime} \Pi (N)) A \end{array} \right] x (N - 1)
$$

Notice that in terms of the Riccati matrix, we also have the relationship

$$A ^ {\prime} \lambda (N) = \Pi (N - 1) x (N - 1) - Q x (N - 1)$$

We then proceed to the next to last block of three equations

$$
\left[ \begin{array}{c c c c c} & R & B ^ {\prime} & & \\ A & B & & - I & \\ & & - I & Q & A ^ {\prime} \end{array} \right] \left[ \begin{array}{l} x (N - 2) \\ u (N - 2) \\ \lambda (N - 1) \\ x (N - 1) \\ u (N - 1) \\ \lambda (N) \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right]
$$

Note that the last equation gives

$$\lambda (N - 1) = Q x (N - 1) + A ^ {\prime} \lambda (N) = \Pi (N - 1) x (N - 1)$$

Using this relationship and continuing on to solve for $x ( N - 1 ) , \lambda ( N - 1 )$ , $u ( N - 2 )$ in terms of $x ( N - 2 )$ gives

$$
\left[ \begin{array}{c} u (N - 2) \\ \lambda (N - 1) \\ x (N - 1) \end{array} \right] = \left[ \begin{array}{c} - (B ^ {\prime} \Pi (N - 1) B + R) ^ {- 1} B ^ {\prime} \Pi (N - 1) A \\ \Pi (N - 1) (I - B (B ^ {\prime} \Pi (N - 1) B + R) ^ {- 1} B ^ {\prime} \Pi (N - 1)) A \\ (I - B (B ^ {\prime} \Pi (N - 1) B + R) ^ {- 1} B ^ {\prime} \Pi (N - 1)) A \end{array} \right] x (N - 2)
$$

Continuing on through each previous block of three equations produces the Riccati iteration and feedback gains of (1.11)–(1.14). The other unknowns, the multipliers, are simply

$$\lambda (k) = \Pi (k) x (k) \quad k = 1, 2, \dots , N$$

so the cost to go at each stage is simply $x ( k ) ^ { \prime } \lambda ( k )$ , and we see the nice connection between the Lagrange multipliers and the cost of the LQR control problem.
