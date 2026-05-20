$$
\hat {d} _ {\omega} = \left\{ \begin{array}{l l} \sqrt {\frac {\| G _ {2 1} (j \omega) \|}{\| G _ {1 2} (j \omega) \|}} & \text { if } G _ {1 2} \neq 0 \& G _ {2 1} \neq 0, \\ 0 & \text { if } G _ {2 1} = 0, \\ \infty & \text { if } G _ {1 2} = 0. \end{array} \right. \tag {10.21}
$$

(2) Alternative approximation can be obtained by using the Frobenius norm:

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) \leq \inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \left\| \left[ \begin{array}{c c} G _ {1 1} (j \omega) & d _ {\omega} G _ {1 2} (j \omega) \\ \frac {1}{d _ {\omega}} G _ {2 1} (j \omega) & G _ {2 2} (j \omega) \end{array} \right] \right\| _ {F}

\begin{array}{l} = \sqrt {\inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \left(\| G _ {1 1} (j \omega) \| _ {F} ^ {2} + d _ {\omega} ^ {2} \| G _ {1 2} (j \omega) \| _ {F} ^ {2} + \frac {1}{d _ {\omega} ^ {2}} \| G _ {2 1} (j \omega) \| _ {F} ^ {2} + \| G _ {2 2} (j \omega) \| _ {F} ^ {2}\right)} \\ { = } { \sqrt { \| G _ { 1 1 } ( j \omega ) \| _ { F } ^ { 2 } + \| G _ { 2 2 } ( j \omega ) \| _ { F } ^ { 2 } + 2 \| G _ { 1 2 } ( j \omega ) \| _ { F } \| G _ { 2 1 } ( j \omega ) \| _ { F } } } \\ \end{array}
$$

with the minimizing $d _ { \omega }$ given by

$$
\tilde {d} _ {\omega} = \left\{ \begin{array}{l l} \sqrt {\frac {\| G _ {2 1} (j \omega) \| _ {F}}{\| G _ {1 2} (j \omega) \| _ {F}}} & \text { if } G _ {1 2} \neq 0 \& G _ {2 1} \neq 0, \\ 0 & \text { if } G _ {2 1} = 0, \\ \infty & \text { if } G _ {1 2} = 0. \end{array} \right. \tag {10.22}
$$

It can be shown that the approximations for the scalar $d _ { \omega }$ obtained previously are exact for a $2 \times 2$ matrix $G .$ For higher dimensional $G ,$ the approximations for $d _ { \omega }$ are still reasonably good. Hence an approximation of $\mu$ can be obtained as

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) \leq \overline {{\sigma}} \left(\left[ \begin{array}{c c} G _ {1 1} (j \omega) & \hat {d} _ {\omega} G _ {1 2} (j \omega) \\ \frac {1}{\hat {d} _ {\omega}} G _ {2 1} (j \omega) & G _ {2 2} (j \omega) \end{array} \right]\right) \tag {10.23}
$$

or, alternatively, as

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) \leq \overline {{\sigma}} \left(\left[ \begin{array}{c c} G _ {1 1} (j \omega) & \tilde {d} _ {\omega} G _ {1 2} (j \omega) \\ \frac {1}{\tilde {d} _ {\omega}} G _ {2 1} (j \omega) & G _ {2 2} (j \omega) \end{array} \right]\right). \tag {10.24}
$$

We can now see how these approximated $\mu$ tests are compared with the sufficient conditions obtained in Chapter 8.
