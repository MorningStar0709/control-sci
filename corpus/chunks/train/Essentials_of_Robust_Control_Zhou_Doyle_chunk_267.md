# 10.2.3 Well-Posedness and Performance for Constant LFTs

Let M be a complex matrix partitioned as

$$
M = \left[ \begin{array}{l l} M _ {1 1} & M _ {1 2} \\ M _ {2 1} & M _ {2 2} \end{array} \right] \tag {10.13}
$$

and suppose there are two defined block structures, $\Delta _ { 1 }$ and $\Delta _ { 2 } .$ , which are compatible in size with $M _ { 1 1 }$ and $M _ { 2 2 }$ , respectively. Define a third structure $\pmb { \Delta }$ as

$$
\boldsymbol {\Delta} = \left\{\left[ \begin{array}{c c} \Delta_ {1} & 0 \\ 0 & \Delta_ {2} \end{array} \right]: \Delta_ {1} \in \boldsymbol {\Delta} _ {1}, \Delta_ {2} \in \boldsymbol {\Delta} _ {2} \right\}. \tag {10.14}
$$

Now we may compute $\mu$ with respect to three structures. The notations we use to keep track of these computations are as follows: $\mu _ { 1 } \left( \cdot \right)$ is with respect to $\Delta _ { 1 } , \mu _ { 2 } ( \cdot )$ is with respect to $\Delta _ { 2 } .$ and $\mu _ { \Delta } ( \cdot )$ is with respect to $\pmb { \Delta }$ . In view of these notations, $\mu _ { 1 } \left( M _ { 1 1 } \right)$ , $\mu _ { 2 } \left( M _ { 2 2 } \right)$ , and $\mu _ { \Delta } ( M )$ all make sense, though, for instance, $\mu _ { 1 } \left( M \right)$ does not.

This section is interested in following constant matrix problems:

• Determine whether the LFT $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ is well-defined for all $\Delta _ { 2 } ~ \in ~ \Delta _ { 2 }$ with $\overline { { \sigma } } ( \Delta _ { 2 } ) \leq \beta \ : ( < \beta )$ .   
• If so, determine how “large” $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ can get for this norm-bounded set of perturbations.

Let $\Delta _ { 2 } \in \Delta _ { 2 }$ . Recall that $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ is well-defined if $I - M _ { 2 2 } \Delta _ { 2 }$ is invertible. The first theorem is nothing more than a restatement of the definition of $\mu$ .

Theorem 10.5 The linear fractional transformation $\mathcal { F } _ { \ell } \left( M , \Delta _ { 2 } \right)$ is well-defined

(a) for all $\Delta _ { 2 } \in \mathbf { B } \Delta _ { 2 }$ if and only if $\mu _ { 2 } \left( M _ { 2 2 } \right) < 1$ .   
(b) for all $\Delta _ { 2 } \in { \bf B } ^ { \mathrm { o } } \Delta _ { 2 }$ if and only if $\mu _ { 2 } \left( M _ { 2 2 } \right) \leq 1$ .
