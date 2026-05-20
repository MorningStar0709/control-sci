# 5.7 Notes

provided that $z ( 0 ) \in \mathcal { Z } _ { N }$ and $\hat { x } ( 0 ) \in S _ { c } ( z ( 0 ) )$ . Thus, the constraint sets $\mathbb { Z }$ and V required for the nominal optimal control problem should satisfy

$$
\begin{array}{l} \mathbb {Z} _ {f} \subseteq \mathbb {Z} \\ S _ {c} (z) \oplus \mathbb {Z} _ {x} \subseteq \mathbb {X} \quad \forall z \in \mathcal {Z} _ {N} \\ \kappa_ {N} (\hat {x}, z) \in \mathbb {U} \forall \hat {x} \in S _ {c} (z), \forall z \in \mathcal {Z} _ {N} \\ \end{array}
$$

If these conditions are satisfied, the solutions ${ \hat { x } } ( i )$ and $z ( i )$ of the controlled composite system and the associated control $u ( i ) = \kappa _ { N } ( \hat { x } ( i )$ , $z ( i ) )$ satisfy

$$
\begin{array}{l} z (i) \rightarrow 0 \text {   as   } i \rightarrow \infty \\ x (i) \in S _ {c} (z (i)) \oplus \mathbb {Z} _ {x} \subseteq \mathbb {X} \quad \forall i \in \mathbb {I} _ {\geq 0} \\ u (i) \in \mathbb {U} \quad \forall i \in \mathbb {I} _ {\geq 0} \\ \end{array}
$$

Compared with the corresponding conditions in Chapter 3, we see that the state constraint set $\mathbb { Z }$ now has to satisfy a stronger requirement than the condition $S _ { c } ( z ) \subseteq \mathbb { X }$ for all $z \in \mathbb { Z }$ precisely because of the state estimation error, which is bounded by $\mathbb { \Sigma } _ { x }$ . Hence the state constraint set $\mathbb { Z }$ required here is smaller than that required in Chapter 3.
