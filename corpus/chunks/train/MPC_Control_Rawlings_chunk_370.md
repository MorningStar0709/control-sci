As in the deterministic case studied in Chapter 2, we are interested in obtaining sufficient conditions that ensure that the RHC law $\kappa _ { N } ( \cdot )$ is stabilizing. We wish to replace the stabilizing Assumptions 2.12 and 2.13 in Section 2.4.3 of Chapter 2 by conditions appropriate to the robust control problem. The presence of a disturbance requires us to generalize some earlier definitions; we therefore define the terms robust control invariant and robust positive invariant that generalize our previous definitions of control invariant and positive invariant respectively.

Definition 3.6 (Robust control invariance). A set $X \subseteq \mathbb { R } ^ { n }$ is robust control invariant for $x ^ { + } = f ( x , u , w )$ , w ∈ W if, for every $x \in X$ , there exists a $u \in \mathbb { U }$ such that $f ( x , u , \mathbb { W } ) \subseteq X .$ .

Definition 3.7 (Robust positive invariance). A set X is robust positive invariant for $x ^ { + } = f ( x , w ) , w \in \mathbb { W }$ if, for every $x \in X , f ( x , \mathbb { W } ) \subseteq X$ .

Stabilizing conditions are imposed on the ingredients $\ell ( \cdot ) , V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ of the optimal control problem to ensure that the resultant controlled system has desirable stability properties. Our generalization of the stabilizing Assumptions 2.12 and 2.13 that we wish to employ, at least for certain problems, are the following Assumptions 3.8 and 3.9.

Assumption 3.8 (Basic stability assumption; robust case).

(a) For all $\boldsymbol { x } \in \mathbb { X } _ { f }$

$$\min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} [ \Delta V _ {f} + \ell ] (x, u, w) \leq 0$$

in which $\Delta V _ { f } ( x , u , w ) = V _ { f } ( f ( x , u , w ) ) - V _ { f } ( x ) . ^ { 4 }$

(b) $\mathbb { X } _ { f } \subseteq \mathbb { X } .$

Assumption 3.8 implicitly requires that for each $x \in \mathbb { X } _ { f }$ , there exists a $u \in \mathbb { V }$ such that $f ( x , u , \mathbb { W } ) \subseteq \mathbb { X } _ { f }$ , i.e., Assumption 3.8 implicitly implies Assumption 3.9.

Assumption 3.9 (Implied stability assumption; robust case). The set $\mathbb { X } _ { f }$ is robust control invariant for $x ^ { + } = f ( x , u , w ) , w \in \mathbb { W }$ .

Before proceeding to analyze stability, we should ask if there are any examples that satisfy these conditions. There is at least one important example. Assume that $f ( x , u , w ) = A x + B u + G w$ is linear and the cost is

$$\ell (x, u) = (1 / 2) \left(| x | _ {Q} ^ {2} + | u | _ {R} ^ {2} - \rho^ {2} | w | ^ {2}\right) \tag {3.21}$$
