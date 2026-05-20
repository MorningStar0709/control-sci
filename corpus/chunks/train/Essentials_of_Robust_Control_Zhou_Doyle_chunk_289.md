D-K iterations proceed by performing this two-parameter minimization in sequential fashion: first minimizing over K with D fixed, then minimizing pointwise over D with K fixed, then again over $K$ , and again over $D _ { : }$ , etc. Details of this process are summarized in the following steps:

(i) Fix an initial estimate of the scaling matrix $D _ { \omega } \in \mathcal { D }$ pointwise across frequency.   
(ii) Find scalar transfer functions $d _ { i } ( s ) , d _ { i } ^ { - 1 } ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ for $i = 1 , 2 , \ldots , ( F - 1 )$ such that $| d _ { i } ( j \omega ) | \approx d _ { i } ^ { \omega }$ . This step can be done using the interpolation theory (Youla and Saito $[ 1 9 6 7 ] \div$ ; however, this will usually result in very high-order transfer functions, which explains why this process is currently done mostly by graphical matching using lower-order transfer functions.

(iii) Let

$$D (s) = \operatorname{diag} (d _ {1} (s) I, \dots , d _ {F - 1} (s) I, I).$$

Construct a state-space model for system

$$
\hat {G} (s) = \left[ \begin{array}{c c} D (s) & \\ & I \end{array} \right] G (s) \left[ \begin{array}{c c} D ^ {- 1} (s) & \\ & I \end{array} \right],
$$

as shown in Figure 10.9.

(iv) Solve an $\mathcal { H } _ { \infty } .$ -optimization problem to minimize

$$\left\| \mathcal {F} _ {\ell} (\hat {G}, K) \right\| _ {\infty}$$

over all stabilizing $K \mathrm { \mathrm { { s } . } }$ . Note that this optimization problem uses the scaled version of G. Let its minimizing controller be denoted by $\hat { K }$ .

(v) Minimize $\overline { { \sigma } } [ D _ { \omega } \mathcal { F } _ { \ell } ( G , \hat { K } ) D _ { \omega } ^ { - 1 } ]$ over $D _ { \omega } ,$ pointwise across frequency.1 Note that this evaluation uses the minimizing Kˆ from the last step, but that G is not scaled. The minimization itself produces a new scaling function. Let this new function be denoted by $\hat { D } _ { \omega }$ .

(vi) Compare $\hat { D } _ { \omega }$ with the previous estimate $D _ { \omega }$ . Stop if they are close, but otherwise replace $D _ { \omega }$ with $\hat { D } _ { \omega }$ and return to step (ii).
