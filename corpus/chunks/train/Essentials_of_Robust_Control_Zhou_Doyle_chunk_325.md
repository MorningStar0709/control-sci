Problem 12.4 Suppose $( A , B , C , D )$ is a minimal realization of $G ( s )$ with A stable and $G ( s )$ positive real. Show that there exist $X \geq 0 , Q$ , and W such that

$$X A + A ^ {*} X = - Q ^ {*} QB ^ {*} X + W ^ {*} Q = CD + D ^ {*} = W ^ {*} W$$

and

$$G (s) + G ^ {\sim} (s) = M ^ {\sim} (s) M (s)$$

with $M ( s ) = \left[ \frac { A \ \biggr | \ B } { Q \ \biggr | \ { W } } \right]$ . Furthermore, if $G ( s )$ is strictly positive real, then $M ( j \omega )$ has full-column rank for all $\mathbf { \bar { \boldsymbol { \omega } } } _ { \omega } \in \mathbb { R }$ .

Problem 12.5 Let $\left\lceil { \frac { A } { C } } \right\rceil { \frac { B } { D } }$ be a state-space realization of $G ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ with A stable and $R : = D + \bar { D } ^ { * } > \mathbf { \bar { 0 } }$ . Show that $G ( s )$ is strictly positive real if and only if there exists a stabilizing solution to the following Riccati equation:

$$X (A - B R ^ {- 1} C) + (A - B R ^ {- 1} C) ^ {*} X + X B R ^ {- 1} B ^ {*} X + C ^ {*} R ^ {- 1} C = 0.$$

Moreover, $M ( s ) = \left[ \frac { A } { R ^ { - \frac { 1 } { 2 } } ( C - B ^ { * } X ) \ \Big | \ R ^ { \frac { 1 } { 2 } } } \right]$ is minimal phase and R 12

$$G (s) + G ^ {\sim} (s) = M ^ {\sim} (s) M (s).$$

Problem 12.6 Assume $p \geq m$ . Show that there exists an rcf $G = N M ^ { - 1 }$ such that N is an inner if and only if $G ^ { \sim } G > 0$ on the $j \omega$ axis, including at ∞. This factorization is unique up to a constant unitary multiple. Furthermore, assume that the realization of $G = \left\lceil { \frac { A \left\lfloor B \right\rceil } { C \left\lceil D \right\rceil } } \right\rceil$ is stabilizable and that $\left\lceil \begin{array} { c c } { A - j \omega I } & { B } \\ { C } & { D } \end{array} \right\rceil$ has full column rank for all $\omega \in \mathbb { R } .$ Then a particular realization of the desired coprime factorization is

$$
\left[ \begin{array}{c} M \\ N \end{array} \right] := \left[ \begin{array}{c c} A + B F & B R ^ {- 1 / 2} \\ \hline F & R ^ {- 1 / 2} \\ C + D F & D R ^ {- 1 / 2} \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

where

$$R = D ^ {*} D > 0F = - R ^ {- 1} (B ^ {*} X + D ^ {*} C)$$

and

$$
X = \operatorname{Ric} \left[ \begin{array}{c c} A - B R ^ {- 1} D ^ {*} C & - B R ^ {- 1} B ^ {*} \\ - C ^ {*} (I - D R ^ {- 1} D ^ {*}) C & - (A - B R ^ {- 1} D ^ {*} C) ^ {*} \end{array} \right] \geq 0.
$$

Moreover, a complementary inner factor can be obtained as

$$
N _ {\perp} = \left[ \begin{array}{c c} A + B F & - X ^ {\dagger} C ^ {*} D _ {\perp} \\ \hline C + D F & D _ {\perp} \end{array} \right]
$$

if $p > m$ .
