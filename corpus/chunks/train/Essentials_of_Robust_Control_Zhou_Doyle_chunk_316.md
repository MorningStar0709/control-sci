$$
W ^ {- 1} (s) = \left[ \begin{array}{c c} A + B R ^ {- 1} (B ^ {*} X + D ^ {*} C) & B R ^ {- 1} \\ \hline R ^ {- 1} (B ^ {*} X + D ^ {*} C) & R ^ {- 1} \end{array} \right]
$$

has no poles on the imaginary axis. Next, note that

$$- X (j \omega I - A) - (j \omega I - A) ^ {*} X + X B R ^ {- 1} D ^ {*} C + C ^ {*} D R ^ {- 1} B ^ {*} X+ X B R ^ {- 1} B ^ {*} X + C ^ {*} (I + D R ^ {- 1} D ^ {*}) C = 0.$$

Multiplying $B ^ { * } \{ ( j \omega I { - } A ) ^ { * } \} ^ { - 1 }$ on the left and $( j \omega I - A ) ^ { - 1 } B$ on the right of the preceding equation and completing square, we have

$$G ^ {*} (j \omega) G (j \omega) = \gamma^ {2} I - W ^ {*} (j \omega) R ^ {- 1} W (j \omega).$$

Since $W ( s )$ has no zeros on the imaginary axis, we conclude that $\| G \| _ { \infty } < \gamma$

The equivalence between (vi) and (vii) follows from Schur complement. It is also easy to show that (vi) implies (i) by following the similar procedure as above. To show that (i) implies (vi), let

$$
\hat {G} = \left[ \begin{array}{c c} A & B \\ \hline C & D \\ \epsilon I & 0 \end{array} \right].
$$

Then there exists an $\epsilon > 0$ such that $\left\| \hat { G } \right\| _ { \infty } < \gamma$ . Now (vi) follows by applying part (v) to $\hat { G } .$ ✷

Theorem 12.4 Suppose H has the form

$$
H = \left[ \begin{array}{c c} A & - B B ^ {*} \\ - C ^ {*} C & - A ^ {*} \end{array} \right].
$$

Then $H \in \operatorname { d o m } ( \operatorname { R i c } )$ iff (A, B) is stabilizable and $( C , A )$ has no unobservable modes on the imaginary axis. Furthermore, $X = \operatorname { R i c } ( H ) \geq 0 ~ i f H \in \operatorname { d o m } ( \operatorname { R i c } )$ , and $\operatorname { K e r } ( X ) = \{ 0 \}$ $i f$ and only $i f \left( C , A \right)$ has no stable unobservable modes.

Note that $\operatorname { K e r } ( X ) \subset \operatorname { K e r } ( C )$ , so that the equation $X M = C ^ { * }$ always has a solution for M, and a minimum F -norm solution is given by $X ^ { + } C ^ { * }$ .

Proof. It is clear from Theorem 12.2 that the stabilizability of $( A , B )$ is necessary, and it is also sufficient if H has no eigenvalues on the imaginary axis. So we only need to show that, assuming $( A , B )$ is stabilizable, H has no imaginary eigenvalues iff $( C , A )$ has no unobservable modes on the imaginary axis. Suppose that $j \omega$ is an eigenvalue and $0 \neq { \left[ \begin{array} { l } { x } \\ { z } \end{array} \right] }$ is a corresponding eigenvector. Then

$$A x - B B ^ {*} z = j \omega x- C ^ {*} C x - A ^ {*} z = j \omega z.$$

Rearrange:

$$(A - j \omega I) x = B B ^ {*} z \tag {12.11}- (A - j \omega I) ^ {*} z = C ^ {*} C x. \tag {12.12}$$

Thus
