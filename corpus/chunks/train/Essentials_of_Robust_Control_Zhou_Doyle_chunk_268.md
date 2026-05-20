As the “perturbation” $\Delta _ { 2 }$ deviates from zero, the matrix $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ deviates from $M _ { 1 1 }$ . The range of values that $\mu _ { 1 } \left( \mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right) \right)$ takes on is intimately related to $\mu _ { \Delta } ( M )$ , as shown in the following theorem:

Theorem 10.6 (main loop theorem) The following are equivalent:

$$
\mu_ {\mathbf {\Delta}} (M) <   1 \qquad \Longleftrightarrow \qquad \left\{ \begin{array}{l l} \mu_ {2} (M _ {2 2}) <   1, \mathrm{and} \\ \max _ {\Delta_ {2} \in \mathbf {B} \mathbf {\Delta} _ {2}} \mu_ {1} (\mathcal {F} _ {\ell} (M, \Delta_ {2})) <   1 \end{array} \right.

\mu_ {\boldsymbol {\Delta}} (M) \leq 1 \qquad \Longleftrightarrow \qquad \left\{ \begin{array}{l} \mu_ {2} \left(M _ {2 2}\right) \leq 1, \text { and } \\ \sup _ {\Delta_ {2} \in \mathbf {B} ^ {0} \boldsymbol {\Delta} _ {2}} \mu_ {1} \left(\mathcal {F} _ {\ell} \left(M, \Delta_ {2}\right)\right) \leq 1. \end{array} \right.
$$

Proof. We shall only prove the first part of the equivalence. The proof for the second part is similar.

⇐ Let $\Delta _ { i } \in \Delta _ { i }$ be given, with $\overline { { \sigma } } \left( \Delta _ { i } \right) \leq 1$ , and define $\Delta = \mathrm { d i a g \ [ } \Delta _ { 1 } , \Delta _ { 2 } ]$ . Obviously $\Delta \in \Delta$ . Now

$$
\det (I - M \Delta) = \det \left[ \begin{array}{c c} I - M _ {1 1} \Delta_ {1} & - M _ {1 2} \Delta_ {2} \\ - M _ {2 1} \Delta_ {1} & I - M _ {2 2} \Delta_ {2} \end{array} \right]. \tag {10.15}
$$

By hypothesis $I - M _ { 2 2 } \Delta _ { 2 }$ is invertible, and hence det $( I - M \Delta )$ becomes

$$\det \left(I - M _ {2 2} \Delta_ {2}\right) \det \left(I - M _ {1 1} \Delta_ {1} - M _ {1 2} \Delta_ {2} \left(I - M _ {2 2} \Delta_ {2}\right) ^ {- 1} M _ {2 1} \Delta_ {1}\right).$$

Collecting the $\Delta _ { 1 }$ terms leaves

$$\det \left(I - M \Delta\right) = \det \left(I - M _ {2 2} \Delta_ {2}\right) \det \left(I - \mathcal {F} _ {\ell} \left(M, \Delta_ {2}\right) \Delta_ {1}\right). \tag {10.16}$$

But $\mu _ { 1 } \left( \mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right) \right) < 1$ and $\Delta _ { 1 } \in \mathbf { B } \Delta _ { 1 } .$ , so $I - \mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right) \Delta _ { 1 }$ must be nonsingular. Therefore, $I - M \Delta$ is nonsingular and, by definition, $\mu _ { \Delta } ( M ) < 1$ .
