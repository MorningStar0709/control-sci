in which the set $\mathbb { Z } _ { N } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { N m }$ is defined by

$$
\begin{array}{l} \mathbb {Z} _ {N} := \left\{(x, \mathbf {u}) \mid u (k) \in \mathbb {U}, \quad \phi (k; x, \mathbf {u}) \in \mathbb {X}, \quad \forall k \in \mathbb {I} _ {0: N - 1}, \right. \\ \text { and } \phi (N; x, \mathbf {u}) \in \mathbb {X} _ {f} \} \tag {2.7} \\ \end{array}
$$

The optimal control problem $\mathbb { P } _ { N } ( x )$ , is, therefore

$$\mathbb {P} _ {N} (x): \quad V _ {N} ^ {0} (x) := \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \right\} \tag {2.8}$$

Problem $\mathbb { P } _ { N } ( x )$ is a parametric optimization problem in which the decision variable is u, and both the cost and the constraint set depend on the parameter x. The set $\mathbb { Z } _ { N }$ is the set of admissible $( x , \mathbf { u } )$ , i.e., the set of $( x , \mathbf { u } )$ for which $x \in \mathbb { X }$ and the constraints of $\mathbb { P } _ { N } ( x )$ are satisfied. Let $x _ { N }$ be the set of states in X for which $\mathbb { P } _ { N } ( x )$ has a solution

$$\mathcal {X} _ {N} := \{x \in \mathbb {X} \mid \mathcal {U} _ {N} (x) \neq \emptyset \} \tag {2.9}$$

It follows from (2.8) and (2.9) that

$$\mathcal {X} _ {N} = \{x \in \mathbb {R} ^ {n} \mid \exists \mathbf {u} \in \mathbb {R} ^ {N m} \text {such that} (x, \mathbf {u}) \in \mathbb {Z} _ {N} \}$$

which is the orthogonal projection of $\mathbb { Z } _ { N } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { N m }$ onto $\mathbb { R } ^ { n }$ . The domain of $V _ { N } ^ { 0 } ( \cdot )$ , i.e., the set of states in X for which $\mathbb { P } _ { N } ( x )$ has a solution, is $x _ { N }$ .

Not every optimization problem has a solution. For example, the problem min $\{ x \ | \ x \in ( 0 , 1 ) \}$ does not have a solution; inf $\{ x \mid x \in$ $( 0 , 1 ) \} \ = \ 0$ but $x ~ = ~ 0$ does not lie in the constraint set (0, 1). By Weierstrass’s theorem, however, an optimization problem does have a solution if the cost is continuous (in the decision variable) and the constraint set compact (see Proposition A.7). This is the case for our problem as shown subsequently in Proposition 2.4. We assume, without further comment, that the following standing conditions are satisfied in the sequel.
