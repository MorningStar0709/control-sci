# B.3.1 Lyapunov Function for Linear Systems

We review some facts involving the discrete matrix Lyapunov equation and stability of the linear system

$$x ^ {+} = A x$$

in which $\boldsymbol { x } \in \mathbb { R } ^ { n }$ . The discrete time system is asymptotically stable if and only if the magnitudes of the eigenvalues of A are strictly less than unity. Such an A matrix is called stable, convergent, or discrete time Hurwitz.

In the following, $A , S , Q \in \mathbb { R } ^ { n \times n }$ . The following matrix equation is known as a discrete matrix Lyapunov equation,

$$A ^ {\prime} S A - S = - Q$$

The properties of solutions to this equation allow one to draw conclusions about the stability of A without computing its eigenvalues. Sontag (1998a, p. 231) provides the following lemma

Lemma B.15 (Lyapunov function for linear systems). The following statements are equivalent (Sontag, 1998a).

(a) A is stable.

(b) For each $Q \in \mathbb { R } ^ { n \times n }$ , there is a unique solution S of the discrete matrix Lyapunov equation

$$A ^ {\prime} S A - S = - Q$$

and $i f Q > 0$ then $S > 0$ .

(c) There is some $S > 0$ such that $A ^ { \prime } S A - S < 0$ .

(d) There is some $S > 0$ such that $V ( x ) = x ^ { \prime } S x$ is a Lyapunov function for the system $x ^ { + } = A x$ .

Exercise B.1 asks you to establish the equivalence of (a) and (b).
