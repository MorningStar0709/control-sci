These properties are similar to those required for a valid Lyapunov function. The difference is that the cost decrease here does not depend on the size of u, but only x and the first element of u, u(0). This cost decrease is sufficient to establish that $x ( k )$ and $u ( k )$ converge to zero, but allows the possibility that ${ \bf { u } } ( k )$ is large even though $x ( k )$ is small. That fact prevents us from establishing the solution $x ( k ) = 0$ for all k is Lyapunov stable. We can establish that the solution $x ( k ) = 0$ for all k is Lyapunov stable at $k = 0$ only. We cannot establish uniform Lyapunov stability nor Lyapunov stability for any $k > 0$ . The problem is not that our proof technique is deficient. There is no reason to expect that the solution $x ( k ) = 0$ for all k is Lyapunov stable for suboptimal MPC. The lack of Lyapunov stability of $x ( k ) = 0$ for all k is a subtle issue and warrants some discussion. To make these matters more precise, consider the following standard definitions of Lyapunov stability at time k and uniform Lyapunov stability (Vidyasagar, 1993, p. 136).

Definition 6.1 (Lyapunov stability). The zero solution $x ( k ) = 0$ for all k is stable (in the sense of Lyapunov) at $k = k _ { 0 }$ if for any $\varepsilon > 0$ there exists a $\delta ( k _ { 0 } , \varepsilon ) > 0$ such that

$$\left| x \left(k _ {0}\right) \right| < \delta \Rightarrow | x (k) | < \varepsilon \quad \forall k \geq k _ {0} \tag {6.5}$$

Lyapunov stability is defined at a time $k _ { 0 }$ . Uniform stability is the concept that guarantees that the zero solution is not losing stability with time. For a uniformly stable zero solution, δ in Definition 6.1 is not a function of $k _ { 0 }$ , so that (6.5) holds for all $k _ { 0 }$ .

Definition 6.2 (Uniform Lyapunov stability). The zero solution $x ( k ) =$ 0 for all k is uniformly stable (in the sense of Lyapunov) if for any $\varepsilon > 0$ there exists a $\delta ( \varepsilon ) > 0$ such that

$$| x (k _ {0}) | < \delta \implies | x (k) | < \varepsilon \quad \forall k \geq k _ {0} \quad \forall k _ {0}$$

Exercise 6.6 gives an example of a linear system for which $x ( k )$ converges exponentially to zero with increasing k for all $x ( 0 )$ , but the zero solution $x ( k ) = 0$ for all k is Lyapunov stable only at $k = 0$ . It is not uniformly Lyapunov stable nor Lyapunov stable for any $k > 0$ . Without further restrictions, suboptimal MPC admits this same type of behavior.
