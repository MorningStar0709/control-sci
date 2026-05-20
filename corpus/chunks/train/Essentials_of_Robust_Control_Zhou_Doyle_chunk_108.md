$$
g (t) = \mathcal {L} ^ {- 1} (G) = \left\{ \begin{array}{l l} C e ^ {A t} B, & t \geq 0 \\ 0, & t <   0 \end{array} \right.
$$

and

$$
\begin{array}{l} \| G \| _ {2} ^ {2} = \int_ {0} ^ {\infty} \operatorname{trace} \left\{g ^ {*} (t) g (t) \right\} d t = \int_ {0} ^ {\infty} \operatorname{trace} \left\{g (t) g (t) ^ {*} \right\} d t \\ = \int_ {0} ^ {\infty} \mathrm{trace} \{B ^ {*} e ^ {A ^ {*} t} C ^ {*} C e ^ {A t} B \} d t = \int_ {0} ^ {\infty} \mathrm{trace} \{C e ^ {A t} B B ^ {*} e ^ {A ^ {*} t} C ^ {*} \} d t. \\ \end{array}
$$

The lemma follows from the fact that the controllability Gramian of $( A , B )$ and the observability Gramian of $( C , A )$ can be represented as

$$Q = \int_ {0} ^ {\infty} e ^ {A ^ {*} t} C ^ {*} C e ^ {A t} d t, P = \int_ {0} ^ {\infty} e ^ {A t} B B ^ {*} e ^ {A ^ {*} t} d t,$$

which can also be obtained from

$$A P + P A ^ {*} + B B ^ {*} = 0 \quad A ^ {*} Q + Q A + C ^ {*} C = 0.$$

![](image/147f28c28508dc6ad5543667b8d08cb125f24e2579f08889ef33623b99ba7e15.jpg)

To compute the $\mathcal { L } _ { 2 }$ norm of a rational transfer function, $G ( s ) \in \mathcal { R } \mathcal { L } _ { 2 }$ , using the state-space approach, let $G ( s ) = [ G ( s ) ] _ { + } + [ G ( s ) ]$ − with $G _ { + } \in \mathcal { R } \mathcal { H } _ { 2 }$ and $G _ { - } \in \mathcal { R } \mathcal { H } _ { 2 } ^ { \perp }$ ; then

$$\| G \| _ {2} ^ {2} = \| [ G (s) ] _ {+} \| _ {2} ^ {2} + \| [ G (s) ] _ {-} \| _ {2} ^ {2}$$

where $\left\| \left[ G ( s ) \right] \right\| _ { 2 }$ and $\| [ G ( s ) ] _ { - } \| _ { 2 } = \| [ G ( - s ) ] _ { + } \| _ { 2 } = \| ( [ G ( s ) ] _ { - } ) ^ { \sim } \| _ { 2 }$ can be computed using the preceding lemma.

Still another useful characterization of the $\mathcal { H } _ { 2 }$ norm of G is in terms of hypothetical input-output experiments. Let $e _ { i }$ denote the ith standard basis vector of $\mathbb { R } ^ { m }$ , where m is the input dimension of the system. Apply the impulsive input $\delta ( t ) e _ { i } ~ [ \delta ( t )$ is the unit impulse] and denote the output by $\begin{array} { r } { z _ { i } ( t ) ( = g ( t ) e _ { i } ) } \end{array}$ . Assume $D = 0 ;$ then $z _ { i } \in \mathcal { L } _ { 2 + }$ and

$$\| G \| _ {2} ^ {2} = \sum_ {i = 1} ^ {m} \| z _ {i} \| _ {2} ^ {2}.$$

Note that this characterization of the $\mathcal { H } _ { 2 }$ norm can be appropriately generalized for nonlinear time-varying systems; see Chen and Francis [1992] for an application of this norm in sampled-data control.

Example 4.1 Consider a transfer matrix

$$
G = \left[ \begin{array}{c c} \frac {3 (s + 3)}{(s - 1) (s + 2)} & \frac {2}{s - 1} \\ \frac {s + 1}{(s + 2) (s + 3)} & \frac {1}{s - 4} \end{array} \right] = G _ {s} + G _ {u}
$$

with

$$
G _ {s} = \left[ \begin{array}{c c c c} - 2 & 0 & - 1 & 0 \\ 0 & - 3 & 2 & 0 \\ \hline 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{array} \right], \quad G _ {u} = \left[ \begin{array}{c c c c} 1 & 0 & 4 & 2 \\ 0 & 4 & 0 & 1 \\ \hline 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right].
$$

Then the command h2norm $\left( \mathbf { G _ { s } } \right)$ gives $\| G _ { s } \| _ { 2 } = 0 . 6 0 5 5$ and h2norm $\big ( \mathbf { c j t } ( \mathbf { G } _ { \mathbf { u } } ) \big )$ gives $\| G _ { u } \| _ { 2 } = 3 . 1 8 2$ . Hence $\| G \| _ { 2 } = \sqrt { \| G _ { s } \| _ { 2 } ^ { 2 } + \| G _ { u } \| _ { 2 } ^ { 2 } = 3 . 2 3 9 3 }$ .
