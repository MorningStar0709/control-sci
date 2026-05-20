This equivalence between the small gain condition, $\| G \| _ { \infty } < 1$ , and the stability robustness of the uncertain difference equation is well-known. This is the small gain theorem, in its necessary and sufficient form for linear, time invariant systems with one of the components norm bounded, but otherwise unknown. What is important to note is that both of these conditions are equivalent to a condition involving the structured singular value of the state-space matrix. Already we have seen that special cases of $\mu$ are the spectral radius and the maximum singular value. Here we see that other important linear system properties — namely, robust stability and input-output gain — are also related to a particular case of the structured singular value.

Example 10.3 Let $M , \Delta _ { 1 }$ , and $\Delta _ { 2 }$ be defined as in the beginning of this section. Now suppose $\mu _ { 2 } ( M _ { 2 2 } ) < 1$ . Find

$$\max _ {\Delta_ {2} \in \mathbf {B} \boldsymbol {\Delta} _ {2}} \mu_ {1} \left(\mathcal {F} _ {\ell} (M, \Delta_ {2})\right).$$

This can be done iteratively as follows:

$$
\max _ {\Delta_ {2} \in \mathbf {B} \Delta_ {2}} \mu_ {1} \left(\mathcal {F} _ {\ell} (M, \Delta_ {2})\right) = \alpha
\Longleftrightarrow \max _ {\Delta_ {2} \in \mathbf {B} \Delta_ {2}} \mu_ {1} \left(\mathcal {F} _ {\ell} \left(\left[ \begin{array}{c c} M _ {1 1} / \alpha & M _ {1 2} / \alpha \\ M _ {2 1} & M _ {2 2} \end{array} \right], \Delta_ {2}\right)\right) = 1

\Longleftrightarrow \mu_ {\boldsymbol {\Delta}} \left(\left[ \begin{array}{c c} M _ {1 1} / \alpha & M _ {1 2} / \alpha \\ M _ {2 1} & M _ {2 2} \end{array} \right]\right) = 1.
$$

Hence

$$
\max _ {\Delta_ {2} \in \mathbf {B} \Delta_ {2}} \mu_ {1} \left(\mathcal {F} _ {\ell} \left(M, \Delta_ {2}\right)\right) = \left\{\alpha : \mu_ {\boldsymbol {\Delta}} \left(\left[ \begin{array}{c c} M _ {1 1} / \alpha & M _ {1 2} / \alpha \\ M _ {2 1} & M _ {2 2} \end{array} \right]\right) = 1 \right\}.
$$

For example, let $\Delta _ { 1 } = \delta I _ { 2 } , \Delta _ { 2 } \in \mathbb { C } ^ { 2 \times 2 }$ :

$$
A = \left[ \begin{array}{c c} 0. 1 & 0. 2 \\ 1 & 0 \end{array} \right], B = \left[ \begin{array}{c c} 1 & 0 \\ 1 & 1 \end{array} \right], C = \left[ \begin{array}{c c} 1 & 2 \\ 1 & 3 \end{array} \right], D = \left[ \begin{array}{c c} 0. 5 & 0 \\ 0 & 0. 8 \end{array} \right].
$$

Find

$$\alpha_ {\max} = \sup _ {\overline {{\sigma}} (\Delta_ {2}) \leq 1} \rho (A + B \Delta_ {2} (I - D \Delta_ {2}) ^ {- 1} C).$$

$\Delta = \left[ \begin{array} { r r } { \delta I _ { 2 } } & { } \\ { } & { \Delta _ { 2 } } \end{array} \right]$ δI2 Define Then a bisection search can be done to find ∆2

$$
\alpha_ {\max} = \left\{\alpha : \mu_ {\boldsymbol {\Delta}} \left(\left[ \begin{array}{c c} A / \alpha & B / \alpha \\ C & D \end{array} \right]\right) = 1 \right\} = 2 1. 7 7.
$$

Related MATLAB Commands: unwrapp, muunwrap, dypert, sisorat
