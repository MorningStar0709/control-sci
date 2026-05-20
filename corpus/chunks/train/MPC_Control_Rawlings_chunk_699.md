# 6.3.1 Uncoupled Input Constraints

We consider convex input constraints of the following form

$$H u (k) \leq h \quad k = 0, 1, \dots , N$$

Defining convex set U

$$\mathbb {U} = \{u | H u \leq h \}$$

we express the input constraints as

$$u (k) \in \mathbb {U} \quad k = 0, 1, \dots , N$$

We drop the time index and indicate the constraints are applied over the entire input sequence using the notation $\mathbf { u } \in \mathbb { U }$ . In the uncoupled constraint case, the two players’ inputs must satisfy

$$\mathbf {u} _ {1} \in \mathbb {U} _ {1} \quad \mathbf {u} _ {2} \in \mathbb {U} _ {2}$$

in which $\mathbb { U } _ { 1 }$ and $\mathbb { U } _ { 2 }$ are convex subsets of $\mathbb { R } ^ { m _ { 1 } }$ and $\mathbb { R } ^ { m _ { 2 } }$ , respectively. The constraints are termed uncoupled because there is no interaction or coupling of the inputs in the constraint relation. Player one then solves the following constrained optimization

$$
\begin{array}{l} \min _ {\mathbf {u} _ {1}} V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2}) \\ \text {s.t.} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] u _ {1} + \left[ \begin{array}{c} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] u _ {2} \\ \mathbf {u} _ {1} \in \mathbb {U} _ {1} \\ S _ {j 1} ^ {u ^ {\prime}} x _ {j 1} (N) = 0 \quad j \in \mathbb {I} _ {1: 2} \\ \left| \mathbf {u} _ {1} \right| \leq d _ {1} \left(\left| x _ {1 1} (0) \right| + \left| x _ {2 1} (0) \right|\right) \quad x _ {1 1} (0), x _ {2 1} (0) \in r \mathcal {B} \\ \end{array}
$$

in which we include the system’s hard input constraints, the stability constraint on the unstable modes, and the Lyapunov stability constraints. Exercise 6.22 discusses how to write the constraint $| \mathbf { u } _ { 1 } | \ \leq$ $d _ { 1 } \left| x _ { 1 } ( 0 ) \right|$ as a set of linear inequalities on $\mathbf { u } _ { 1 }$ . Similarly, player two

solves
