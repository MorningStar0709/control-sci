and $\| \Delta _ { \mathrm { r e l } } \| _ { \infty }$ is made as small as possible. $\Delta _ { \mathrm { r e l } }$ is usually called the relative error. In the case where $G$ is square and invertible, this problem can be simply formulated as

$$\min _ {\deg G _ {r} \leq r} \left\| G ^ {- 1} (G - G _ {r}) \right\| _ {\infty}.$$

Of course, the dual approximation problem

$$G _ {r} = (I + \Delta_ {\mathrm{rel}}) G$$

can be obtained by taking the transpose of G. It turns out that the approximation $G _ { r }$ obtained below also serves as a multiplicative approximation:

$$G = G _ {r} (I + \Delta_ {\mathrm{mul}})$$

where $\Delta _ { \mathrm { m u l } }$ is usually called the multiplicative error.

Error bounds can be derived if the frequency-weighted balanced truncation method is applied to the relative and multiplicative approximations.

Theorem 7.13 Let $G , G ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ be an nth-order square transfer matrix with a state-space realization

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right]
$$

Let P and Q be the solutions to

$$P A ^ {*} + A P + B B ^ {*} = 0 \tag {7.23}Q (A - B D ^ {- 1} C) + (A - B D ^ {- 1} C) ^ {*} Q + C ^ {*} (D ^ {- 1}) ^ {*} D ^ {- 1} C = 0 \tag {7.24}$$

Suppose

$$P = Q = \operatorname{diag} \left(\sigma_ {1} I _ {s _ {1}}, \dots , \sigma_ {r} I _ {s _ {r}}, \sigma_ {r + 1} I _ {s _ {r + 1}}, \dots , \sigma_ {N} I _ {s _ {N}}\right) = \operatorname{diag} \left(\Sigma_ {1}, \Sigma_ {2}\right)$$

with $\sigma _ { 1 } > \sigma _ { 2 } > . . . > \sigma _ { N } \geq 0$ , and let the realization of G be partitioned compatibly with $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ as

$$
G (s) = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right]
$$

Then

$$
G _ {r} (s) = \left[ \begin{array}{c c} A _ {1 1} & B _ {1} \\ \hline C _ {1} & D \end{array} \right]
$$

is stable and minimum phase. Furthermore,

$$
\begin{array}{l} \| \Delta_ {\mathrm{rel}} \| _ {\infty} \leq \prod_ {i = r + 1} ^ {N} \left(1 + 2 \sigma_ {i} (\sqrt {1 + \sigma_ {i} ^ {2}} + \sigma_ {i})\right) - 1 \\ \| \Delta_ {\mathrm{mul}} \| _ {\infty} \leq \prod_ {i = r + 1} ^ {N} \left(1 + 2 \sigma_ {i} (\sqrt {1 + \sigma_ {i} ^ {2}} + \sigma_ {i})\right) - 1 \\ \end{array}
$$

Related MATLAB Commands: srelbal, sfrwtbal
