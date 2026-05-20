# 1.3.6 Convergence of the Linear Quadratic Regulator

We now show that the infinite horizon regulator asymptotically stabilizes the origin for the closed-loop system. Define the infinite horizon objective function

$$V (x, \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {\infty} x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k)$$

subject to

$$x ^ {+} = A x + B ux (0) = x$$

with $Q , R > 0$ . If (A, B) is controllable, the solution to the optimization problem

$$\min _ {\mathbf {u}} V (x, \mathbf {u})$$

exists and is unique for all x. We denote the optimal solution by $\mathbf { u } ^ { 0 } ( x )$ , and the first input in the optimal sequence by $u ^ { 0 } ( x )$ . The feedback control law $\kappa _ { \infty } ( \cdot )$ for this infinite horizon case is then defined as $u = \kappa _ { \infty } ( x )$ in which $K _ { \infty } ( x ) = u ^ { 0 } ( x ) = \mathbf { u } ^ { 0 } ( 0 ; x )$ . As stated in the following lemma, this infinite horizon linear quadratic regulator (LQR) is stabilizing.

Lemma 1.3 (LQR convergence). For $( A , B )$ controllable, the infinite horizon LQR with $Q , R > 0$ gives a convergent closed-loop system

$$x ^ {+} = A x + B \kappa_ {\infty} (x)$$

Proof. The cost of the infinite horizon objective is bounded above for $\mathrm { { a l l } } x ( 0 )$ because (A, B) is controllable. Controllability implies that there exists a sequence of n inputs {u(0), u(1), . . . , u(n − 1)} that transfers the state from any $x ( 0 )$ to $x ( n ) = 0$ . A zero control sequence after $k = n$ for {u(n + 1), u(n + 2), . . .} generates zero cost for all terms in V after $k = n$ , and the objective function for this infinite control sequence is therefore finite. The cost function is strictly convex in u because $R > 0$ so the solution to the optimization is unique.

If we consider the sequence of costs to go along the closed-loop trajectory, we have

$$V _ {k + 1} = V _ {k} - (1 / 2) \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k)\right)$$

in which $V _ { k } ~ = ~ V ^ { 0 } ( x ( k ) )$ is the cost at time k for state value $x ( k )$ and $u ( k ) = u ^ { 0 } ( x ( k ) )$ is the optimal control for state $x ( k )$ . The cost along the closed-loop trajectory is nonincreasing and bounded below (by zero). Therefore, the sequence $\{ V _ { k } \}$ converges and

$$x (k) ^ {\prime} Q x (k) \rightarrow 0 \quad u (k) ^ {\prime} R u (k) \rightarrow 0 \quad \text { as } k \rightarrow \infty$$

Since $Q , R > 0$ , we have

$$x (k) \rightarrow 0 \quad u (k) \rightarrow 0 \quad \text { as } k \rightarrow \infty$$

and closed-loop convergence is established.
