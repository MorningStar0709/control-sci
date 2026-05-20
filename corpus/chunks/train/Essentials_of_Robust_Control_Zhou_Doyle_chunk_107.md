# 4.3 Computing $\mathcal { L } _ { 2 }$ and $\mathcal { H } _ { 2 }$ Norms

Let $G ( s ) \in { \mathcal { L } } _ { 2 }$ and recall that the $\mathcal { L } _ { 2 }$ norm of G is defined as

$$
\begin{array}{l} \| G \| _ {2} := \sqrt {\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{trace} \{G ^ {*} (j \omega) G (j \omega) \} d \omega} \\ = \quad \| g \| _ {2} \\ = \sqrt {\int_ {- \infty} ^ {\infty} \mathrm{trace} \{g ^ {*} (t) g (t) \} d t} \\ \end{array}
$$

where $g ( t )$ denotes the convolution kernel of $G .$ .

It is easy to see that the $\mathcal { L } _ { 2 }$ norm defined previously is finite iff the transfer matrix G is strictly proper; that is, $G ( \infty ) = 0$ . Hence, we will generally assume that the transfer matrix is strictly proper whenever we refer to the $\mathcal { L } _ { 2 }$ norm of G (of course, this also applies to $\mathcal { H } _ { 2 }$ norms). One straightforward way of computing the $\mathcal { L } _ { 2 }$ norm is to use contour integral. Suppose $G$ is strictly proper; then we have

$$
\begin{array}{l} \| G \| _ {2} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{trace} \{G ^ {*} (j \omega) G (j \omega) \} d \omega \\ { = } { \frac { 1 } { 2 \pi j } \oint \mathrm{trace} \{ G ^ { \sim } ( s ) G ( s ) \} d s . } \\ \end{array}
$$

The last integral is a contour integral along the imaginary axis and around an infinite semicircle in the left-half plane; the contribution to the integral from this semicircle equals zero because G is strictly proper. By the residue theorem, $\| G \| _ { 2 } ^ { 2 }$ equals the sum of the residues of trace $\{ G ^ { \sim } ( s ) G ( s ) \}$ } at its poles in the left-half plane.

Although $\| G \| _ { 2 }$ can, in principle, be computed from its definition or from the method just suggested, it is useful in many applications to have alternative characterizations and to take advantage of the state-space representations of G. The computation of a $\mathcal { R } \mathcal { H } _ { 2 }$ transfer matrix norm is particularly simple.

Lemma 4.4 Consider a transfer matrix

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & 0 \end{array} \right]
$$

with A stable. Then we have

$$\| G \| _ {2} ^ {2} = \operatorname{trace} (B ^ {*} Q B) = \operatorname{trace} (C P C ^ {*}) \tag {4.1}$$

where $Q$ and $P$ are observability and controllability Gramians that can be obtained from the following Lyapunov equations:

$$A P + P A ^ {*} + B B ^ {*} = 0 \quad A ^ {*} Q + Q A + C ^ {*} C = 0.$$

Proof. Since G is stable, we have
