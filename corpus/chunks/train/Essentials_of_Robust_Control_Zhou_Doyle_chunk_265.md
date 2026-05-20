The preceding bounds are much more than just computational schemes. They are also theoretically rich and can unify a number of apparently different results in linear systems theory. There are several connections with Lyapunov asymptotic stability, two of which were hinted at previously, but there are further connections between the upper-bound scalings and solutions to Lyapunov and Riccati equations. Indeed, many major theorems in linear systems theory follow from the upper-bounds and from some results of linear fractional transformations. The lower bound can be viewed as a natural generalization of the maximum modulus theorem.

Of course, one of the most important uses of the upper-bound is as a computational scheme when combined with the lower bound. For reliable use of the $\mu$ theory, it is essential to have upper and lower bounds. Another important feature of the upperbound is that it can be combined with $H _ { \infty }$ controller synthesis methods to yield an ad hoc µ-synthesis method. Note that the upper-bound when applied to transfer functions is simply a scaled $H _ { \infty }$ norm. This is exploited in the $D - K$ iteration procedure to perform approximate $\mu$ synthesis (Doyle [1982]), which will be briefly introduced in Section 10.4.

The upper and lower bounds of the structured singular value and the scaling matrix D can be computed using the MATLAB command

$$\gg [ \text { bounds }, \text { rowd } ] = \text { mu } (\text { M }, \text { blk })$$

where the structure of the $\Delta$ is specified by a two-column matrix blk. for example, a

$$
\Delta = \left[ \begin{array}{c c c c c c} \delta_ {1} I _ {2} & 0 & 0 & 0 & 0 & 0 \\ 0 & \delta_ {2} & 0 & 0 & 0 & 0 \\ 0 & 0 & \Delta_ {3} & 0 & 0 & 0 \\ 0 & 0 & 0 & \Delta_ {4} & 0 & 0 \\ 0 & 0 & 0 & 0 & \delta_ {5} I _ {3} & 0 \\ 0 & 0 & 0 & 0 & 0 & \Delta_ {6} \end{array} \right]
\delta_ {1}, \delta_ {2}, \delta_ {5}, \in \mathbb {C}, \Delta_ {3} \in \mathbb {C} ^ {2 \times 3}, \Delta_ {4} \in \mathbb {C} ^ {3 \times 3}, \Delta_ {6} \in \mathbb {C} ^ {2 \times 1}
$$

can be specified by

$$
\mathbf {b l k} = \left[ \begin{array}{c c} 2 & 0 \\ 1 & 1 \\ 2 & 3 \\ 3 & 3 \\ 3 & 0 \\ 2 & 1 \end{array} \right].
$$

Note that $\Delta _ { j }$ is not required to be square. The outputs of the program include a $2 \times 1$ vector bounds containing the upper and lower bounds of $\mu _ { \Delta } ( M )$ and the row vector rowd containing the scaling $D$ . The $D$ matrix can be recovered by
