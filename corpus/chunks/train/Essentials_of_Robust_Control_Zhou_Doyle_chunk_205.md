$$
\Delta (s) = \frac {1}{\sigma_ {1}} \left[ \begin{array}{c} v _ {1 1} \frac {\alpha_ {1} - s}{\alpha_ {1} + s} \\ \vdots \\ v _ {1 q} \frac {\alpha_ {q} - s}{\alpha_ {q} + s} \end{array} \right] \left[ \begin{array}{c c c} u _ {1 1} \frac {\beta_ {1} - s}{\beta_ {1} + s} & \dots & u _ {1 p} \frac {\beta_ {p} - s}{\beta_ {p} + s} \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

$\begin{array} { r } { \mathrm { T h e n } \left\| \Delta \right\| _ { \infty } = 1 / \sigma _ { 1 } \le 1 \mathrm { a n d } \Delta ( j \omega _ { 0 } ) = \frac { 1 } { \sigma _ { 1 } } v _ { 1 } u _ { 1 } ^ { * } . } \end{array}$

✷

The theorem still holds even if $\Delta$ and M are infinite dimensional. This is summarized as the following corollary.

Corollary 8.2 The following statements are equivalent:

(i) The system is well-posed and internally stable for all $\Delta \in \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1 / \gamma ;$   
(ii) The system is well-posed and internally stable for all $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1 / \gamma _ { ; }$   
(iii) The system is well-posed and internally stable for all $\Delta \in \mathbb { C } ^ { q \times p }$ with $\| \Delta \| < 1 / \gamma ;$   
(iv) $\| M \| _ { \infty } \leq \gamma .$

Remark 8.1 It can be shown that the small gain condition is sufficient to guarantee internal stability even if ∆ is a nonlinear and time-varying “stable” operator with an appropriately defined stability notion, see Desoer and Vidyasagar [1975]. ✸

The following lemma shows that if $\left\| M \right\| _ { \infty } > \gamma ,$ there exists a destabilizing ∆ with $\| \Delta \| _ { \infty } < 1 / \gamma$ such that the closed-loop system has poles in the open right-half plane. (This is stronger than what is given in the proof of Theorem 8.1.)

Lemma 8.3 Suppose $M \in \mathcal { R } \mathcal { H } _ { \infty }$ and $\| M \| _ { \infty } > \gamma$ . Then there exists a $\sigma _ { 0 } > 0$ such that for any given $\sigma \in [ 0 , \sigma _ { 0 } ]$ there exists a $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1 / \gamma$ such that de $( I - M ( s ) \Delta ( s ) )$ has a zero on the axis $\operatorname { R e } ( s ) = \sigma$ .

Proof. Without loss of generality, assume $\gamma \ = \ 1$ . Since $M \in \mathcal { R } \mathcal { H } _ { \infty }$ and $\| M \| _ { \infty } > 1$ , there exists a $0 < \omega _ { 0 } < \infty$ such that $\| M ( j \omega _ { 0 } ) \| > 1$ . Given any γ such that $1 < \gamma < \| M ( j \omega _ { 0 } ) \|$ , there is a sufficiently small $\sigma _ { 0 } > 0$ such that
