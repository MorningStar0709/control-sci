$$
\left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] \left[ \begin{array}{c} x \\ u \end{array} \right] = 0.
$$

Moreover, $i f u = 0$ , then $z _ { \mathrm { 0 } }$ is also a nonobservable mode.

Proof. By definition, $z _ { \mathrm { 0 } }$ is an invariant zero if there is a vector ${ \left[ \begin{array} { l } { x } \\ { u } \end{array} \right] } \neq 0$ such that

$$
\left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] \left[ \begin{array}{c} x \\ u \end{array} \right] = 0
$$

$\left[ \begin{array} { l l } { A - s I } & { B } \\ { C } & { D } \end{array} \right]$ has full-column normal rank.

On the other hand, suppose $z _ { 0 }$ is an invariant zero; then there is a vector ${ \left[ \begin{array} { l } { x } \\ { u } \end{array} \right] } \neq 0$ such that

$$
\left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] \left[ \begin{array}{c} x \\ u \end{array} \right] = 0.
$$

We claim that $x \neq 0$ . Otherwise, $\left[ \begin{array} { l } { B } \\ { D } \end{array} \right] u = 0 \mathrm { ~ o r ~ } u = 0$ since $\left[ \begin{array} { l l } { A - s I } & { B } \\ { C } & { D } \end{array} \right]$ has full-column normal rank $( \mathrm { i . e . , } \left[ \begin{array} { l } { x } \\ { u } \end{array} \right] ^ { - } = 0 )$ , which is a contradiction.

Finally, note that if $u = 0 .$ , then

$$
\left[ \begin{array}{c} A - z _ {0} I \\ C \end{array} \right] x = 0
$$

and $z _ { 0 }$ is a nonobservable mode by PBH test.

![](image/85f7c754c770590953a0b2b4675c917d9097ce238bd7c81b8d7f093e381b1fcd.jpg)

When the system is square, the invariant zeros can be computed by solving a generalized eigenvalue problem:

$$
\underbrace {\left[ \begin{array}{c c} A & B \\ C & D \end{array} \right]} _ {M} \left[ \begin{array}{l} x \\ u \end{array} \right] = z _ {0} \underbrace {\left[ \begin{array}{c c} I & 0 \\ 0 & 0 \end{array} \right]} _ {N} \left[ \begin{array}{l} x \\ u \end{array} \right]
$$

using a Matlab command: eig(M, N).

Lemma 3.8 Suppose $\left\lceil \begin{array} { c c } { { A - s I } } & { { B } } \\ { { C } } & { { D } } \end{array} \right\rceil$ has full-row normal rank. Then $z _ { 0 } \in \mathbb { C }$ is an invariant zero of a realization $( A , B , { \overline { { C } } } , D )$ if and only if there exist $0 \neq y \in \mathbb { C } ^ { n }$ and $v \in \mathbb { C } ^ { p }$ such that

$$
\left[ \begin{array}{c c} y ^ {*} & v ^ {*} \end{array} \right] \left[ \begin{array}{c c} A - z _ {0} I & B \\ C & D \end{array} \right] = 0.
$$

Moreover, $i f v = 0$ , then z0 is also a noncontrollable mode.
