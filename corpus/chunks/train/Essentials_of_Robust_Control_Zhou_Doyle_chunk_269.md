⇒ Basically, the argument above is reversed. Again let $\Delta _ { 1 } ~ \in ~ \mathbf { B } \Delta _ { 1 }$ 1 and $\Delta _ { 2 } \in \mathbf { B } \Delta _ { 2 }$ be given, and define $\Delta = \mathrm { d i a g \ [ } \Delta _ { 1 } , \Delta _ { 2 } ]$ . Then $\Delta \in \mathbf { B } \Delta$ and, by hypothesis, det $( I - M \Delta ) \neq 0$ . It is easy to verify from the definition of $\mu$ that (always)

$$\mu (M) \geq \max \left\{\mu_ {1} \left(M _ {1 1}\right), \mu_ {2} \left(M _ {2 2}\right) \right\}.$$

We can see that $\mu _ { 2 } \left( M _ { 2 2 } \right) < 1$ , which gives that $I { - } M _ { 2 2 } \Delta _ { 2 }$ is also nonsingular. Therefore, the expression in equation (10.16) is valid, giving

$$\det \left(I - M _ {2 2} \Delta_ {2}\right) \det \left(I - \mathcal {F} _ {\ell} (M, \Delta_ {2}) \Delta_ {1}\right) = \det (I - M \Delta) \neq 0.$$

Obviously, $I - \mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right) \Delta _ { 1 }$ is nonsingular for all $\Delta _ { i } \in \mathbf { B } \Delta _ { i }$ , which indicates that the claim is true. ✷

Remark 10.3 This theorem forms the basis for all uses of $\mu$ in linear system robustness analysis, whether from a state-space, frequency domain, or Lyapunov approach. ✸

The role of the block structure $\Delta _ { 2 }$ in the main loop theorem is clear — it is the structure that the perturbations come from; however, the role of the perturbation structure $\Delta _ { 1 }$ is often misunderstood. Note that $\mu _ { 1 } \left( \cdot \right)$ appears on the right-hand side of the theorem, so that the set $\Delta _ { 1 }$ defines what particular property of $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ is considered. As an example, consider the theorem applied with the two simple block structures considered right after Lemma 10.1. Define $\Delta _ { 1 } : = \{ \delta _ { 1 } I _ { n } : \delta _ { 1 } \in \mathbb { C } \}$ . Hence, for $A \in \mathbb { C } ^ { n \times n } , \mu _ { 1 } \left( A \right) = \rho \left( A \right)$ . Likewise, define $\begin{array} { r } { \Delta _ { 2 } = \mathbb { C } ^ { m \times m } ; } \end{array}$ ; then for $D \in \mathbb { C } ^ { m \times m }$ , $\mu _ { 2 } \left( D \right) = \overline { { \sigma } } ( D )$ . Now, let $\pmb { \Delta }$ be the diagonal augmentation of these two sets, namely

$$
\boldsymbol {\Delta} := \left\{\left[ \begin{array}{c c} \delta_ {1} I _ {n} & 0 _ {n \times m} \\ 0 _ {m \times n} & \Delta_ {2} \end{array} \right]: \delta_ {1} \in \mathbb {C}, \Delta_ {2} \in \mathbb {C} ^ {m \times m} \right\} \subset \mathbb {C} ^ {(n + m) \times (n + m)}.
$$
