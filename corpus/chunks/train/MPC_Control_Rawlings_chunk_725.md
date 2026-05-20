# Exercise 6.4: Reparameterizing an unstable system

Consider again the LQR problem with cross term

$$\min _ {\mathbf {u}} V = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) + 2 x (k) ^ {\prime} M u (k)\right) + (1 / 2) x (N) ^ {\prime} P _ {f} x (N)$$

subject to

$$x ^ {+} = A x + B u$$

and the three approaches of Exercise 6.1:

1. The method described in Section 6.1.1 in which you eliminate the state and solve the problem for the decision variable

$$\mathbf {u} = \{u (0), u (1), \dots , u (N - 1) \}$$

2. The method described in Section 6.1.1 in which you do not eliminate the state and solve the problem for

$$\mathbf {z} = \{u (0), x (1), u (1), x (2), \dots , u (N - 1), x (N) \}$$

3. The method of DP and the Riccati iteration to compute the closed-form solution for u(k) and x(k).

(a) You found that unstable A causes numerical problems in the first method using large horizons. So let’s consider a fourth method. Reparameterize the input in terms of a state feedback gain via

$$u (k) = K x (k) + v (k)$$

in which K is chosen so that $A + B K$ is a stable matrix. Consider the matrices in a transformed LQ problem

$$\min _ {\mathbf {v}} V = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} \tilde {Q} x (k) + v (k) ^ {\prime} \tilde {R} v (k) + 2 x (k) ^ {\prime} \tilde {M} v (k)\right) + (1 / 2) x (N) ^ {\prime} \tilde {P} _ {f} x (N)$$

subject to $\begin{array} { r } { { \boldsymbol { x } } ^ { + } = \stackrel { \sim } { A } { \boldsymbol { x } } + \stackrel { \sim } { B } { \boldsymbol { \nu } } . } \end{array}$

What are the matrices $\tilde { \lambda } , \tilde { B } , \tilde { Q } , \tilde { P } _ { f } , \tilde { R } , \tilde { M }$ such that the two problems give the same solution (state trajectory)?

(b) Solve the following problem using the first method and the fourth method and describe differences between the two solutions. Compare your results to the DP approach. Plot x(k) and u(k) versus k.

$$
A = \left[ \begin{array}{c c c} 2 7. 8 & - 8 2. 6 & 3 4. 6 \\ 2 5. 6 & - 7 6. 8 & 3 2. 4 \\ 4 0. 6 & - 1 2 2. 0 & 5 1. 9 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 0. 5 2 7 & 0. 5 4 8 \\ 0. 6 1 3 & 0. 5 3 0 \\ 1. 0 6 & 0. 8 2 8 \end{array} \right] \qquad x (0) = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right]
$$

Consider regulator tuning parameters and constraints

$$Q = P _ {f} = I \quad R = I \quad M = 0 \quad N = 5 0$$
