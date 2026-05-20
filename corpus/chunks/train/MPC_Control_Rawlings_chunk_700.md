$$
\min _ {\mathbf {u} _ {2}} V (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1}, \mathbf {u} _ {2})
\text {s.t.} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] u _ {1} + \left[ \begin{array}{c} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] u _ {2}
\mathbf {u} _ {2} \in \mathbb {U} _ {2}S _ {j 2} ^ {\prime} x _ {j 2} (N) = 0 \quad j \in \mathbb {I} _ {1: 2}\left| \mathbf {u} _ {2} \right| \leq d _ {2} \left(\left| x _ {2 1} (0) \right| + \left| x _ {2 2} (0) \right|\right) \quad x _ {1 2} (0), x _ {2 2} (0) \in r \mathcal {B}
$$

We denote the solutions to these problems as

$$\mathbf {u} _ {1} ^ {0} (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {2}) \quad \mathbf {u} _ {2} ^ {0} (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1})$$

The feasible set $x _ { N }$ for the unstable system is the set of states for which the unstable modes can be brought to zero in N moves while satisfying the input constraints.

Given an initial iterate, $( \mathbf { u } _ { 1 } ^ { p } , \mathbf { u } _ { 2 } ^ { p } )$ , the next iterate is defined to be

$$(\mathbf {u} _ {1}, \mathbf {u} _ {2}) ^ {p + 1} = w _ {1} (\mathbf {u} _ {1} ^ {0} (x _ {1} (0), x _ {2} (0), \mathbf {u} _ {2} ^ {p}), \mathbf {u} _ {2} ^ {p}) +w _ {2} \left(\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {0} \left(x _ {1} (0), x _ {2} (0), \mathbf {u} _ {1} ^ {p}\right)\right)$$

To reduce the notational burden we denote this as

$$(\mathbf {u} _ {1}, \mathbf {u} _ {2}) ^ {p + 1} = w _ {1} (\mathbf {u} _ {1} ^ {0}, \mathbf {u} _ {2} ^ {p}) + w _ {2} (\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {0})$$

and the functional dependencies of ${ \bf u } _ { 1 } ^ { 0 }$ and ${ \bf u } _ { 2 } ^ { 0 }$ should be kept in mind.

This procedure provides three important properties, which we establish next.

1. The iterates are feasible: $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } ) ^ { p } \in ( \mathbb { U } _ { 1 } , \mathbb { U } _ { 2 } )$ implies $( { \mathbf { u } } _ { 1 } , { \mathbf { u } } _ { 2 } ) ^ { p + 1 } \in$ $( \mathbb { U } _ { 1 } , \mathbb { U } _ { 2 } )$ . This follows from convexity of $\mathbb { U } _ { 1 } , \ \mathbb { U } _ { 2 }$ and the convex combination of the feasible points $( \mathbf { u } _ { 1 } ^ { p } , \mathbf { u } _ { 2 } ^ { p } )$ and $( \mathbf { u } _ { 1 } ^ { 0 } , \mathbf { u } _ { 2 } ^ { 0 } )$ to make (u1, u2)p+1. $( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p + 1 }$
