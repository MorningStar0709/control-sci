Definition B.26 (Positive invariance (disturbance and control)). The set A is positive invariant for $x ^ { + } \ = \ f ( x , u , w ) , \ w \ \in \ \mathbb { W }$ (or for $x ^ { + } \in$ $F ( x , u ) )$ if for all $x \in \mathcal A$ there exists a $u \in \mathbb { U }$ such that $f ( x , u , w ) \in \mathcal { A }$ for all $w \in \mathbb { W }$ (or $F ( x , u ) \subseteq { \mathcal { A } } )$ .

Definition B.27 (CLF (disturbance and control)). A function $V : \mathbb { R } ^ { n } $ $\mathbb { R } _ { \geq 0 }$ is said to be a control-Lyapunov function for the system $\begin{array} { r l } { x ^ { + } } & { { } = } \end{array}$ $f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W } ( \mathrm { o r } x ^ { + } \in F ( x , u ) , u \in \mathbb { U } )$ and set A if there exist functions $\alpha _ { i } \in \mathcal { K } _ { \infty } , i = 1 , 2$ and $\alpha _ { 3 } ~ \in ~ \mathcal { P D }$ such that for any $\boldsymbol { x } \in \mathbb { R } ^ { n }$ ,

$$V (x) \geq \alpha_ {1} (| x | _ {\mathcal {A}})V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}})\inf _ {u \in \mathbb {U}} \sup _ {z \in F (x, u)} V (z) \leq V (x) - \alpha_ {3} (| x | _ {\mathcal {A}}) \tag {B.11}$$

Remark B.28 (CLF implies control law). Given a global control-Lyapunov function V (·), one can choose a control law $\kappa : \mathbb { R } ^ { n }  \mathbb { U }$ satisfying

$$\sup _ {z \in F (x, \kappa (x))} V (z) \leq V (x) - \alpha_ {3} (| x | _ {\mathcal {A}}) / 2$$

for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ . Since U is compact, $\kappa ( \cdot )$ is locally bounded and, hence, so is $x \mapsto f ( x , \kappa ( x ) )$ . Thus we may use Theorem B.23 to deduce that A is globally asymptotically stable for $x ^ { + } = f ( x , \kappa ( x ) , w ) , w \in \mathbb { W }$ (for $x ^ { + } \in F ( x , \kappa ( x ) ) )$ .

These results can be further extended to deal with the constrained case. First, we generalize the definitions of positive invariance of a set.

Definition B.29 (Positive invariance (constrained)). The set A is control invariant for $x ^ { + } = f ( x , u ) , u \in \mathbb { U }$ if, for all $x \in \mathcal A$ , there exists a $u \in \mathbb { U }$ such that $f ( x , u ) \in \mathcal { A }$ .
