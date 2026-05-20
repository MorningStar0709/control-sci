The proofs of Lemmas 2.32 and 2.33 are left as Exercises 2.9 and 2.10. Determination of a time-varying terminal cost $V _ { f } ( \cdot )$ and timevarying terminal constraint set $\mathbb { X } _ { f }$ is complex. Fortunately there are a few important cases where choice of time-invariant terminal cost and constraint set is possible. The first possibility is $\mathbb { X } _ { f } ~ = ~ \{ 0 \}$ and $V _ { f } ( 0 ) = 0 ;$ this choice satisfies Assumptions 2.12 and 2.13, as already demonstrated, as well as Assumptions 2.30 and 2.31. The second possibility arises when $f ( \cdot )$ is time invariant, which is the case when output feedback rather than state feedback is employed. In this case, discussed more fully in Chapter 5, time-varying bounds on state estimation error may lead to time-varying constraints even though the underlying system is time invariant. We therefore make the following assumption.

Assumption 2.34 (Bounds on stage and terminal costs; time-varying case).

(a) The terminal cost $V _ { f } ( \cdot )$ and terminal constraint set $\mathbb { X } _ { f }$ are time invariant.

(b) The stage cost $\ell ( \cdot )$ and the terminal cost $V _ { f } ( \cdot )$ satisfy, for all $i \in \mathbb { I } _ { \geq 0 }$

$$\ell (x, u, i) \geq \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i), \forall u \in \mathbb {U} (i)V _ {f} (x, i) \leq \alpha_ {2} (| x |) \quad \forall x \in \mathbb {X} _ {f}$$

in which $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ are $\mathcal { K } _ { \infty }$ functions.

Our next result is an analog of Proposition 2.17, and follows fairly simply from Lemmas 2.32 and 2.33 and our assumptions.

Proposition 2.35 (Optimal value function properties; time-varying case). Suppose Assumptions 2.25, 2.26, 2.30, 2.31, and 2.34 are satisfied. Then there exist two $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that, for all $i \in \mathbb { I } _ { \geq 0 }$

$$
\begin{array}{l} V _ {N} ^ {0} (x, i) \geq \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i) \\ V _ {N} ^ {0} (x, i) \leq \alpha_ {2} (| x |) \quad \forall x \in \mathbb {X} _ {f} \\ V _ {N} ^ {0} (f (x, \kappa_ {N} (x, i), i)) \leq V _ {N} ^ {0} (x, i) - \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N} (i) \\ \end{array}
$$
