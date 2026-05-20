Hence the filtering problem can be regarded as a special $\mathcal { H } _ { \infty }$ problem. However, compared with control problems, there is no internal stability requirement in the filtering problem. Hence the solution to the above filtering problem can be obtained from the $\mathcal { H } _ { \infty }$ solution in the previous sections by setting $B _ { 2 } = 0$ and dropping the internal stability requirement.

Theorem 14.8 Suppose $( C _ { 2 } , A )$ is detectable and

$$
\left[ \begin{array}{c c} A - j \omega I & B _ {1} \\ C _ {2} & D _ {2 1} \end{array} \right]
$$

has full row rank for all ω. Let $D _ { 2 1 }$ be normalized and $D _ { 1 1 }$ partitioned conformably as

$$
\left[ \begin{array}{c} D _ {1 1} \\ D _ {2 1} \end{array} \right] = \left[ \begin{array}{c c} D _ {1 1 1} & D _ {1 1 2} \\ \hdashline 0 & I \end{array} \right].
$$

Then there exists a causal $F ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ such that $J < \gamma ^ { 2 }$ if and only if $\overline { { \sigma } } ( D _ { 1 1 1 } ) < \gamma$ and $J _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } )$ with $Y _ { \infty } = \operatorname { R i c } ( J _ { \infty } ) \geq 0$ , where

$$
\tilde {R} := \left[ \begin{array}{c} D _ {1 1} \\ D _ {2 1} \end{array} \right] \left[ \begin{array}{c} D _ {1 1} \\ D _ {2 1} \end{array} \right] ^ {*} - \left[ \begin{array}{c c} \gamma^ {2} I & 0 \\ 0 & 0 \end{array} \right]

\begin{array}{r l r} {J _ {\infty}} & {:=} & {\left[ \begin{array}{c c} A ^ {*} & 0 \\ - B _ {1} B _ {1} ^ {*} & - A \end{array} \right] - \left[ \begin{array}{c c} C _ {1} ^ {*} & C _ {2} ^ {*} \\ - B _ {1} D _ {1 1} ^ {*} & - B _ {1} D _ {2 1} ^ {*} \end{array} \right] \tilde {R} ^ {- 1} \left[ \begin{array}{c c} D _ {1 1} B _ {1} ^ {*} & C _ {1} \\ D _ {2 1} B _ {1} ^ {*} & C _ {2} \end{array} \right].} \end{array}
$$

Moreover, if the above conditions are satisfied, then a rational causal filter $F ( s )$ satisfying $J < \gamma ^ { 2 }$ is given by

$$
\hat {z} = F (s) y = \left[ \begin{array}{c c} A + L _ {2 \infty} C _ {2} + L _ {1 \infty} D _ {1 1 2} C _ {2} & - L _ {2 \infty} - L _ {1 \infty} D _ {1 1 2} \\ \hline C _ {1} - D _ {1 1 2} C _ {2} & D _ {1 1 2} \end{array} \right] y
$$

where

$$
\left[ \begin{array}{c c} L _ {1 \infty} & L _ {2 \infty} \end{array} \right] := - \left[ \begin{array}{c c} B _ {1} D _ {1 1} ^ {*} + Y _ {\infty} C _ {1} ^ {*} & B _ {1} D _ {2 1} ^ {*} + Y _ {\infty} C _ {2} ^ {*} \end{array} \right] \tilde {R} ^ {- 1}.
$$

In the case where $D _ { 1 1 } = 0$ and $B _ { 1 } D _ { 2 1 } ^ { * } = 0$ the filter becomes much simpler:

$$
\hat {z} = \left[ \begin{array}{c c} A - Y _ {\infty} C _ {2} ^ {*} C _ {2} & Y _ {\infty} C _ {2} ^ {*} \\ \hline C _ {1} & 0 \end{array} \right] y
$$

where $Y _ { \infty }$ is the stabilizing solution to

$$Y _ {\infty} A ^ {*} + A Y _ {\infty} + Y _ {\infty} (\gamma^ {- 2} C _ {1} ^ {*} C _ {1} - C _ {2} ^ {*} C _ {2}) Y _ {\infty} + B _ {1} B _ {1} ^ {*} = 0.$$
