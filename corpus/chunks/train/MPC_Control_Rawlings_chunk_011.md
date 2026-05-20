# Appendix B. Stability Theory

Asymptotic stability. For several of the stability theorems appearing in the first printing’s Appendix $\mathtt { B } , { } ^ { 3 }$ we used the classical definition of global asymptotic stability (GAS), given in Definition B.6. The following stronger definition of GAS has recently started to become popular.

Definition 9 (Global asymptotic stability (KL version)). The (closed, positive invariant) set A is globally asymptotically stable (GAS) for $x ^ { + } = f ( x )$ if there exists a KL function $\beta ( \cdot )$ such that, for each $\boldsymbol { x } \in \mathbb { R } ^ { n }$

$$\left| \phi (i; x) \right| _ {\mathcal {A}} \leq \beta (| x | _ {\mathcal {A}}, i) \quad \forall i \in \mathbb {I} _ {\geq 0} \tag {B.1}$$

Notice that this inequality appears as (B.1) in Appendix B.

Teel and Zaccarian (2006) provide further discussion of these definitional issues. It is also interesting to note that although the KL definitions may have become popular only recently, Hahn (1967, p. 8) used K and L comparison functions as early as 1967 to define asymptotic stability.4 For continuous $f ( \cdot )$ , we show in Proposition B.8 that these two definitions are equivalent. But we should bear in mind that for nonlinear models, the function $f ( \cdot )$ defining the closed-loop system evolution under MPC, $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ , may be discontinuous because the control law $\kappa _ { N } ( \cdot )$ may be discontinuous (see Example 2.8 in Chapter 2 for an example). Also, when using suboptimal MPC, the control law is a point to set map and is not a continuous function (Rawlings and Mayne, 2009, pp. 156, 417). For discontinuous $f ( \cdot )$ , the two definitions are not equivalent. Consider the following example to make this clear.
