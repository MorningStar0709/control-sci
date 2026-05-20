An algorithm that maximizes det $( W _ { 1 } ^ { \sim } W _ { 1 } )$ det $( W _ { 2 } W _ { 2 } ^ { \sim } )$ has been developed by Goddard and Glover [1993]. The procedure below, devised directly from the preceding theorem, can be used to generate a required reduced-order controller that will preserve the closed-loop $\mathcal { H } _ { \infty }$ performance bound $\left\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \right\| _ { \infty } < \gamma$ .

1. Let $K _ { 0 }$ be a full-order controller such that $\begin{array} { r } { \left. \mathcal { F } _ { \ell } ( G , K _ { 0 } ) \right. _ { \infty } < \gamma ; } \end{array}$   
2. Compute $W _ { 1 }$ and $W _ { 2 }$ so that $\tilde { R }$ is a contraction;   
3. Use the weighted model reduction method in Chapter $7$ or any other methods to find a $\hat { K }$ so that $\left\| \mathbfcal { W } _ { 2 } ^ { - 1 } ( \hat { K } - K _ { 0 } ) \boldsymbol { W } _ { 1 } ^ { - 1 } \right\| _ { \infty } < 1$ .

Note that all controller reduction methods introduced in this book are only sufficient; that is, there may be desired reduced-order controllers that cannot be found from the proposed procedures.
