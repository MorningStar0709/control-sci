Remark 10.1 Without a loss in generality, the full blocks in the minimal norm $\Delta$ can each be chosen to be dyads $( \mathrm { r a n k } = 1 )$ . To see this, assume $S = 0 ~ { \mathrm { ( i . e . } }$ , all blocks are full blocks). Suppose that $I - M \Delta$ is singular for some $\Delta \in \Delta$ . Then there is an $x \in \mathbb { C } ^ { n }$ such that $M \Delta x = x$ . Now partition x conformably with $\Delta { : }$

$$
x = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {F} \end{array} \right], x _ {i} \in \mathbb {C} ^ {m _ {i}}, i = 1, \ldots , F
$$

and let

$$
\tilde {\Delta} _ {i} = \left\{ \begin{array}{l l} \frac {\Delta_ {i} x _ {i} x _ {i} ^ {*}}{\| x _ {i} \| ^ {2}}, & x _ {i} \neq 0; \\ 0, & x _ {i} = 0 \end{array} \right. \quad \text {for i = 1,2,\ldots,F.}
$$

Define

$$\tilde {\Delta} = \operatorname{diag} \left\{\tilde {\Delta} _ {1}, \tilde {\Delta} _ {2}, \dots , \tilde {\Delta} _ {F} \right\}.$$

Then $\overline { { \sigma } } ( \tilde { \Delta } ) \leq \overline { { \sigma } } ( \Delta ) , \tilde { \Delta } x = \Delta x ,$ and thus $( I - M \tilde { \Delta } ) x = ( I - M \Delta ) x = 0 \ ( \mathrm { i . e . , ~ } I - M \tilde { \Delta }$ is also singular). Hence we have replaced a general perturbation ∆ that satisfies the singularity condition with a perturbation $\tilde { \Delta }$ that is no larger [in the $\overline { { \sigma } } ( \cdot )$ sense] and has rank 1 for each block but still satisfies the singularity condition. ✸

Lemma 10.1 $\mu _ { \Delta } ( M ) = \operatorname* { m a x } _ { \Delta \in \mathbf { B } \Delta } \rho ( M \Delta )$

In view of this lemma, continuity of the function $\mu : \mathbb { C } ^ { n \times n } \longrightarrow \mathbb { R }$ is apparent. In general, though, the function $\mu : \mathbb { C } ^ { n \times n } \longrightarrow \mathbb { R }$ is not a norm, since it does not satisfy the triangle inequality; however, for any $\alpha \in \mathbb { C } , \mu \left( \alpha M \right) = | \alpha | \mu \left( M \right)$ , so in some sense, it is related to how $\mathrm { ^ { 6 6 } b i g ^ { 3 } }$ the matrix is.

We can relate $\mu _ { \Delta } ( M )$ to familiar linear algebra quantities when $\pmb { \Delta }$ is one of two extreme sets.

$\bullet \ \mathrm { I f } \ \Delta = \{ \delta I : \delta \in \mathbb { C } \} \ ( S = 1 , F = 0 , r _ { 1 } = n )$ , then $\mu _ { \pmb { \Delta } } ( M ) = \rho \left( M \right)$ , the spectral radius of $M$ .
