# 4.4 Computing $\mathcal { L } _ { \infty }$ and $\mathcal { H } _ { \infty }$ Norms

We shall first consider, as in the $\mathcal { L } _ { 2 }$ case, how to compute the $\infty$ norm of an $\mathcal { R L } _ { \infty }$ transfer matrix. Let $G ( s ) \in \mathcal { R } \mathcal { L } _ { \infty }$ and recall that the $\mathcal { L } _ { \infty }$ norm of a matrix rational transfer function G is defined as

$$\| G \| _ {\infty} := \sup _ {\omega} \overline {{\sigma}} \{G (j \omega) \}.$$

The computation of the $\mathcal { L } _ { \infty }$ norm of G is complicated and requires a search. A control engineering interpretation of the infinity norm of a scalar transfer function G is the distance in the complex plane from the origin to the farthest point on the Nyquist plot of $G ,$ and it also appears as the peak value on the Bode magnitude plot of |G(jω)|. Hence the ∞ norm of a transfer function can, in principle, be obtained graphically.

To get an estimate, set up a fine grid of frequency points:

$$\{\omega_ {1}, \dots , \omega_ {N} \}.$$

Then an estimate for $\| G \| _ { \infty }$ is

$$\max _ {1 \leq k \leq N} \overline {{\sigma}} \{G (j \omega_ {k}) \}.$$

This value is usually read directly from a Bode singular value plot. The $\mathcal { R L } _ { \infty }$ norm can also be computed in state-space.

Lemma 4.5 Let $\gamma > 0$ and

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right] \in \mathcal {R L} _ {\infty}. \tag {4.2}
$$

Then $\| G \| _ { \infty } < \gamma$ if and only $i f \overline { { \sigma } } ( D ) < \gamma$ and the Hamiltonian matrix H has no eigenvalues on the imaginary axis where

$$
H := \left[ \begin{array}{c c} A + B R ^ {- 1} D ^ {*} C & B R ^ {- 1} B ^ {*} \\ - C ^ {*} (I + D R ^ {- 1} D ^ {*}) C & - (A + B R ^ {- 1} D ^ {*} C) ^ {*} \end{array} \right] \tag {4.3}
$$

and $R = \gamma ^ { 2 } I - D ^ { * } D$ .

Proof. Let $\Phi ( s ) = \gamma ^ { 2 } I - G ^ { \sim } ( s ) G ( s )$ . Then it is clear that $\| G \| _ { \infty } < \gamma$ if and only if $\Phi ( j \omega ) > 0$ for all $\omega \in \mathbb { R }$ . Since $\Phi ( \infty ) = R > 0$ and since $\Phi ( j \omega )$ is a continuous function of $\omega , \Phi ( j \omega ) > 0$ for all $\omega \in \mathbb { R }$ if and only if $\Phi ( j \omega )$ is nonsingular for all $\omega \in \mathbb { R } \cup \{ \infty \}$ ; that is, $\Phi ( s )$ has no imaginary axis zero. Equivalently, $\Phi ^ { - 1 } ( s )$ has no imaginary axis pole. It is easy to compute by some simple algebra that
