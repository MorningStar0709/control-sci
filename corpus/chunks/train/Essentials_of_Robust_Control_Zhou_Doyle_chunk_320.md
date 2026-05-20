$$
\begin{array}{l} H = \left[ \begin{array}{c c} A & 0 \\ - C ^ {*} C & - A ^ {*} \end{array} \right] - \left[ \begin{array}{c} B \\ - C ^ {*} D \end{array} \right] R ^ {- 1} \left[ \begin{array}{c c} D ^ {*} C & B ^ {*} \end{array} \right] \\ = \left[ \begin{array}{c c} A - B R ^ {- 1} D ^ {*} C & - B R ^ {- 1} B ^ {*} \\ - C ^ {*} (I - D R ^ {- 1} D ^ {*}) C & - (A - B R ^ {- 1} D ^ {*} C) ^ {*} \end{array} \right]. \\ \end{array}
$$

Then $H \in \operatorname { d o m } ( \operatorname { R i c } ) \ i f f \left( A , B \right)$ is stabilizable and $\left\lceil \begin{array} { c c } { A - j \omega I } & { B } \\ { C } & { D } \end{array} \right\rceil$ has full-column rank for all ω. Furthermore, $X = \operatorname { R i c } ( H ) \geq 0$ if $H \in \mathsf { d o m } ( \mathrm { R i c } )$ , and $\operatorname { K e r } ( X ) = \{ 0 \}$ if and only $i f \left( D _ { \perp } ^ { * } C , A - B R ^ { - 1 } D ^ { * } C \right)$ has no stable unobservable modes.

Proof. This is the consequence of Lemma 12.6 and Theorem 12.4.

![](image/d9e90f04c8b1cee8f56b5440b16eaab66dee52bbb40d03bc2d9afa0d196dd4ec.jpg)

Remark 12.3 It is easy to see that the detectability (observability) of $( D _ { \perp } ^ { * } C , A - B R ^ { - 1 } D ^ { * } C )$ implies the detectability (observability) of $( C , A )$ ; however, the converse is, in general, not true. Hence the existence of a stabilizing solution to the Riccati equation in the preceding corollary is not guaranteed by the stabilizability of $( A , B )$ and detectability of $( C , A )$ . Furthermore, even if a stabilizing solution exists, the positive definiteness of the solution is not guaranteed by the observability of (C, A) unless $D ^ { * } C = 0$ . As an example, consider

$$
A = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], B = \left[ \begin{array}{l} 0 \\ - 1 \end{array} \right], C = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right], D = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right].
$$

Then (C, A) is observable, (A, B) is controllable, and

$$
A - B D ^ {*} C = \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right], D _ {\perp} ^ {*} C = \left[ \begin{array}{c c} 0 & 0 \end{array} \right].
$$

A Riccati equation with the preceding data has a nonnegative definite stabilizing solution since $( D ^ { * } C , A - B R ^ { - 1 } D ^ { * } C )$ has no unobservable modes on the imaginary axis. However, the solution is not positive definite since $( D _ { \perp } ^ { * } C , A - B R ^ { - 1 } D ^ { * } C )$ has a stable unobservable mode. On the other hand, if the B matrix is changed to

$$
B = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right],
$$

then the corresponding Riccati equation has no stabilizing solution since, in this case, $\left( A - B D ^ { * } C \right)$ has eigenvalues on the imaginary axis although $( A , B )$ is controllable and $( C , A )$ is observable. ✸

Related MATLAB Commands: ric eig, are
