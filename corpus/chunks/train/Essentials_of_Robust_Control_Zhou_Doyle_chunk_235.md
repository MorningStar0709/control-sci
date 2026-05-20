A useful interpretation of an LFT $[ \mathrm { e . g . } , \mathcal { F } _ { \ell } ( M , \Delta ) ]$ is that $\mathcal { F } _ { \ell } ( M , \Delta )$ has a nominal mapping, $M _ { 1 1 }$ , and is perturbed by $\Delta .$ , while $M _ { 1 2 } , M _ { 2 1 }$ , and $M _ { 2 2 }$ reflect a prior knowledge as to how the perturbation affects the nominal map, $M _ { 1 1 }$ . A similar interpretation can be applied to $\mathcal { F } _ { u } ( M , \Delta )$ . This is why LFT is particularly useful in the study of perturbations, which is the focus of the next chapter.

The physical meaning of an LFT in control science is obvious if we take M as a proper transfer matrix. In that case, the LFTs defined previously are simply the closed-loop transfer matrices from $w _ { 1 } \mapsto z _ { 1 }$ and $w _ { 2 } \mapsto z _ { 2 }$ , respectively; that is,

$$T _ {z w 1} = \mathcal {F} _ {\ell} (M, \Delta_ {\ell}), \qquad T _ {z w 2} = \mathcal {F} _ {u} (M, \Delta_ {u})$$

where M may be the controlled plant and $\Delta$ may be either the system model uncertainties or the controllers.

Definition 9.2 An LFT, $\mathcal { F } _ { \ell } ( M , \Delta )$ , is said to be well-defined (or well-posed) if $\left( I - M _ { 2 2 } \Delta \right)$ is invertible.

Note that this definition is consistent with the well-posedness definition of the feedback system, which requires that the corresponding transfer matrix be invertible in $\mathcal { R } _ { p } ( s )$ . It is clear that the study of an LFT that is not well-defined is meaningless; hence throughout this book, whenever an LFT is invoked, it will be assumed implicitly that it is well-defined. It is also clear from the definition that, for any M , $\mathcal { F } _ { \ell } ( M , 0 )$ is well-defined; hence any function that is not well-defined at the origin cannot be expressed as an LFT in terms of its variables. For example, $f ( \delta ) = 1 / \delta$ is not an LFT of $\delta .$

In some literature, LFT is used to refer to the following matrix functions:

$$(A + B Q) (C + D Q) ^ {- 1} \quad \text { or } \quad (C + Q D) ^ {- 1} (A + Q B)$$

where $C$ is usually assumed to be invertible due to practical consideration. The following results follow from some simple algebra.

Lemma 9.1 Suppose C is invertible. Then

$$(A + B Q) (C + D Q) ^ {- 1} = \mathcal {F} _ {\ell} (M, Q)(C + Q D) ^ {- 1} (A + Q B) = \mathcal {F} _ {\ell} (N, Q)$$

with

$$
M = \left[ \begin{array}{c c} A C ^ {- 1} & B - A C ^ {- 1} D \\ C ^ {- 1} & - C ^ {- 1} D \end{array} \right], N = \left[ \begin{array}{c c} C ^ {- 1} A & C ^ {- 1} \\ B - D C ^ {- 1} A & - D C ^ {- 1} \end{array} \right].
$$
