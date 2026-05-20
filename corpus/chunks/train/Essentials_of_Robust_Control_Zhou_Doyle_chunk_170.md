Now partition the realization $( A , B , C , D )$ compatibly with $Q$ as

$$
\left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right].
$$

Then $[ { \frac { A _ { 1 1 } } { C _ { 1 } } } | { \frac { B _ { 1 } } { D } } ]$ is also a realization of G. Moreover, $( C _ { 1 } , A _ { 1 1 } )$ is observable $i f A _ { 1 1 }$ is stable.

The preceding two lemmas suggest that to obtain a minimal realization from a stable nonminimal realization, one only needs to eliminate all states corresponding to the zero block diagonal term of the controllability Gramian $P$ and the observability Gramian $Q .$ . In the case where P is not block diagonal, the following procedure can be used to eliminate noncontrollable subsystems:

$G ( s ) = \left[ { \frac { A \mid B } { C \mid D } } \right]$ be a stable realization.   
2. Compute the controllability Gramian $P \geq 0$ from

$$A P + P A ^ {*} + B B ^ {*} = 0.$$

3. Diagonalize P to get $P = { \left[ \begin{array} { l l } { U _ { 1 } } & { U _ { 2 } } \end{array} \right] } { \left[ \begin{array} { l l } { \Lambda _ { 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { U _ { 1 } } & { U _ { 2 } } \end{array} \right] } ^ { * }$ with $\Lambda _ { 1 } > 0$ and $\left[ \begin{array} { l l } { U _ { 1 } } & { U _ { 2 } } \end{array} \right]$ unitary.

4. Then $G ( s ) = \left[ \frac { U _ { 1 } ^ { * } A U _ { 1 } } { C U _ { 1 } } \left. \frac { U _ { 1 } ^ { * } B } { D } \right. \right]$ is a controllable realization.

A dual procedure can also be applied to eliminate nonobservable subsystems.

Now assume that $\Lambda _ { 1 } > 0$ is diagonal and is partitioned as $\Lambda _ { 1 } = \mathrm { d i a g } ( \Lambda _ { 1 1 } , \Lambda _ { 1 2 } )$ such that $\lambda _ { \operatorname* { m a x } } ( \Lambda _ { 1 2 } ) \ll \lambda _ { \operatorname* { m i n } } ( \Lambda _ { 1 1 } )$ ; then it is tempting to conclude that one can also discard those states corresponding to $\Lambda _ { 1 2 }$ without causing much error. However, this is not necessarily true, as shown in the following example.

Example 7.1 Consider a stable transfer function

$$G (s) = \frac {3 s + 1 8}{s ^ {2} + 3 s + 1 8}.$$

Then $G ( s )$ has a state-space realization given by

$$
G (s) = \left[ \begin{array}{c c c} - 1 & - 4 / \alpha & 1 \\ 4 \alpha & - 2 & 2 \alpha \\ \hline - 1 & 2 / \alpha & 0 \end{array} \right]
$$

where α is any nonzero number. It is easy to check that the controllability Gramian of the realization is given by

$$
P = \left[ \begin{array}{c c} 0. 5 & \\ & \alpha^ {2} \end{array} \right].
$$
