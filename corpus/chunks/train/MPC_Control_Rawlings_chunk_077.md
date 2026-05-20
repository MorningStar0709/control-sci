# 1.3.4 The Infinite Horizon LQ Problem

Let us motivate the infinite horizon problem by showing a weakness of the finite horizon problem. Kalman (1960b, p.113) pointed out in his classic 1960 paper that optimality does not ensure stability.

In the engineering literature it is often assumed (tacitly and incorrectly) that a system with optimal control law (6.8) is necessarily stable.

Assume that we use as our control law the first feedback gain of the finite horizon problem, K(0),

$$u (k) = K (0) x (k)$$

Then the stability of the closed-loop system is determined by the eigenvalues of $A + B K ( 0 )$ . We now construct an example that shows choosing $Q > 0 , R > 0$ , and $N \geq 1$ does not ensure stability. In fact, we can find reasonable values of these parameters such that the controller destabilizes a stable system.2 Let

$$
A = \left[ \begin{array}{c c} 4 / 3 & - 2 / 3 \\ 1 & 0 \end{array} \right] \qquad B = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \qquad C = [ - 2 / 3 1 ]
$$

This system is chosen so that $G ( z )$ has a zero at $z = 3 / 2 , \mathrm { i . e . }$ , an unstable zero. We now construct an LQ controller that inverts this zero and hence produces an unstable system. We would like to choose $Q = C ^ { \prime } C$ so that y itself is penalized, but that Q is only semidefinite. We add a small positive definite piece to $C ^ { \prime } C$ so that Q is positive definite, and choose a small positive R penalty (to encourage the controller to misbehave), and $N = 5$ ,

$$
Q = C ^ {\prime} C + 0. 0 0 1 I = \left[ \begin{array}{c c} 4 / 9 +. 0 0 1 & - 2 / 3 \\ - 2 / 3 & 1. 0 0 1 \end{array} \right] \quad R = 0. 0 0 1
$$

We now iterate the Riccati equation four times starting from $\Pi = P _ { f } =$ Q and compute K(0) for $N = 5 ;$ ; then we compute the eigenvalues of $A + B K ( 0 )$ and achieve3

$$\operatorname{eig} (A + B K _ {5} (0)) = \{1. 3 0 7, 0. 0 0 1 \}$$

Using this controller the closed-loop system evolution is $x ( k ) = ( A +$ $B K _ { 5 } ( 0 ) ) ^ { k } x _ { 0 }$ . Since an eigenvalue of $A + B K _ { 5 } ( 0 )$ is greater than unity, $x ( k ) \to \infty$ as $k  \infty$ . In other words the closed-loop system is unstable.

If we continue to iterate the Riccati equation, which corresponds to increasing the horizon in the controller, we obtain for $N = 7$

$$\operatorname{eig} (A + B K _ {7} (0)) = \{0. 9 8 9, 0. 0 0 1 \}$$

and the controller is stabilizing. If we continue iterating the Riccati equation, we converge to the following steady-state closed-loop eigenvalues

$$\operatorname{eig} (A + B K _ {\infty} (0)) = \{0. 6 6 4, 0. 0 0 1 \}$$
