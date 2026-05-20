# 6.4 Constrained M-Player Game

We have set up the constrained two-player game so that the approach generalizes naturally to the M-player game. We do not have a lot of work left to do to address this general case. Recall $\mathbb { I } _ { 1 : M }$ denotes the set of integers $\lbrace 1 , 2 , \dots , M \rbrace$ . We define the following systemwide variables

$$
\begin{array}{l} \boldsymbol {x} (0) = \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \\ \vdots \\ x _ {M} (0) \end{array} \right] \qquad \mathbf {u} = \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \\ \vdots \\ \mathbf {u} _ {M} \end{array} \right] \qquad B _ {i} = \left[ \begin{array}{c} \overline {{B}} _ {1 i} \\ \overline {{B}} _ {2 i} \\ \vdots \\ \overline {{B}} _ {M i} \end{array} \right] \quad \underline {{B}} _ {i} = \left[ \begin{array}{c} B _ {1 i} \\ B _ {2 i} \\ \vdots \\ B _ {M i} \end{array} \right] \quad i \in \mathbb {I} _ {1: M} \\ V (x (0), \mathbf {u}) = \sum_ {j \in \mathbb {I} _ {1: M}} \rho_ {j} V _ {j} (x _ {j} (0), \mathbf {u}) \\ \end{array}
$$

Each player solves a similar optimization, so for $i \in \mathbb { I } _ { 1 : M }$

$$
\begin{array}{l} \min _ {\mathbf {u} _ {i}} V (x (0), \mathbf {u}) \\ \text { s.t. } x ^ {+} = A x + \sum_ {j \in \mathbb {I} _ {1: M}} B _ {j} u _ {j} \\ \mathbf {u} _ {i} \in \mathbb {U} _ {i} \\ S _ {j i} ^ {u ^ {\prime}} x _ {j i} (N) = 0 \quad j \in \mathbb {I} _ {1: M} \\ | \mathbf {u} _ {i} | \leq d _ {i} \sum_ {j \in \mathbb {I} _ {1: M}} \left| x _ {j i} (0) \right| \quad \text { if } x _ {j i} (0) \in r \mathcal {B}, j \in \mathbb {I} _ {1: M} \\ \end{array}
$$

This optimization can be expressed as a quadratic program, whose constraints and linear cost term depend affinely on parameter x. The warm start for each player at the next sample is generated from purely local information

$$\tilde {\mathbf {u}} _ {i} ^ {+} = \left\{u _ {i} (1), u _ {i} (2), \dots , u _ {i} (N - 1), 0 \right\} \quad i \in \mathbb {I} _ {1: M}$$

The controller iteration is given by

$$\mathbf {u} ^ {p + 1} = \sum_ {j \in \mathbb {I} _ {1: M}} w _ {j} \left(\mathbf {u} _ {1} ^ {p}, \dots , \mathbf {u} _ {j} ^ {0}, \dots , \mathbf {u} _ {M} ^ {p}\right)$$

in which $\mathbf { u } _ { i } ^ { 0 } = \mathbf { u } _ { i } ^ { 0 } \left( x ( 0 ) , \mathbf { u } _ { j \in \mathbb { I } _ { 1 : M } , j \neq i } ^ { p } \right)$ . The plantwide cost function then satisfies for any $p \geq 0$
