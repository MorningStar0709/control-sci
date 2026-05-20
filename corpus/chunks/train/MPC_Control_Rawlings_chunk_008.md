# Example 1: The case of the linear quadratic regulator

Consider the linear, time invariant model $x ^ { + } = A x + B u , y = C x$ with quadratic penalties $\ell ( y , u ) = ( 1 / 2 ) ( y ^ { \prime } Q y + u ^ { \prime } R u )$ for both the finite and infinite horizon cases. What do the assumptions of Theorem 7(b) imply in this case? Compare these assumptions to the standard LQR assumptions listed in Exercise 1.20 (b).

Assumption 2.2 is satisfied for $f ( x , u ) = A x + B u$ for all $A \in \mathbb { R } ^ { n \times n } , B \in \mathbb { R } ^ { n \times m } ;$ ; we have ${ \mathbb X } = { \mathbb R } ^ { n }$ , and $\mathbb { U } = \mathbb { R } ^ { m }$ . Assumption 6(b) implies that $Q > 0$ and $R > 0$ . The system being IOSS implies that $( A , C )$ is detectable (see Exercise 4.5). We can choose $\mathbb { X } _ { f }$ to be the stabilizable subspace of $( A , B )$ and Assumption 2.13 is satisfied. The set $x _ { N }$ contains the system controllability information. The set $x _ { N }$ is the stabilizable subspace of $( A , B )$ , and we can satisfy Assumption 6(a) by choosing $V _ { f } ( x ) = x ^ { \prime } \Pi x$ in which Π is the solution to the steady-state Riccati equation for the stabilizable modes of $( A , B )$ .

In particular, if $( A , B )$ is stabilizable, then $\mathbb { X } _ { f } = \mathbb { R } ^ { n } , \mathbb { X } _ { N } = \mathbb { R } ^ { n }$ for all $N \in \mathbb { I } _ { 0 : \infty }$ , and $V _ { f }$ can be chosen to be $V _ { f } ( x ) ~ = ~ x ^ { \prime } \Pi x$ in which Π is the solution to the steady-state Riccati equation (1.19). The horizon N can be finite or infinite with this choice of $V _ { f } ( \cdot )$ and the control law is invariant with respect to the horizon length, $\begin{array} { r } { \kappa _ { N } ( x ) = K x } \end{array}$ in which K is the steady-state linear quadratic regulator gain given in (1.19). Theorem 7(b) then gives that the origin of the closed-loop system $x ^ { + } = f ( x , \kappa _ { N } ( x ) ) = ( A + B K ) x$ is globally, exponentially stable.

The standard assumptions for the LQR with stage cost $l ( y , u ) = ( 1 / 2 ) ( y ^ { \prime } Q y +$ $u ^ { \prime } R u )$ are

$$Q > 0 \quad R > 0 \quad (A, C) \text { detectable } \quad (A, B) \text { stabilizable }$$

and we see that this case is subsumed by Theorem 7(b).
