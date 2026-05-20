# Design Procedure:

Let P be a family of parametric uncertain systems and let $P _ { 0 }$ be a nominal model.

(a) Loop-Shaping: The singular values of the nominal plant are shaped, using a precompensator $W _ { 1 }$ and/or a postcompensator $W _ { 2 } ,$ to give a desired open-loop shape. The nominal plant $P _ { 0 }$ and the shaping functions $W _ { 1 } , W _ { 2 }$ are combined to form the shaped plant, $P _ { s } .$ , where $P _ { s } = W _ { 2 } P _ { 0 } W _ { 1 }$ . We assume that $W _ { 1 }$ and $W _ { 2 }$ are such that $P _ { s }$ contains no hidden modes.

(b) Compute frequency-by-frequency:

$$f (\omega) = \sup _ {P \in \mathcal {P}} \psi (P _ {s} (j \omega), W _ {2} (j \omega) P (j \omega) W _ {1} (j \omega)).$$

Set $\alpha = 0 .$ .

(b) Fit a stable and minimum phase rational transfer function $W ( s )$ so that

$$| W (j \omega) | \geq \sin (\arcsin f (\omega) + \arcsin \alpha) \forall \omega .$$

(c) Find a $K _ { \infty }$ such that

$$
\beta := \inf _ {K _ {\infty}} \left\| \left[ \begin{array}{c} I \\ K _ {\infty} \end{array} \right] (I + P _ {0} K _ {\infty}) ^ {- 1} \tilde {M} _ {0} ^ {- 1} W \right\| _ {\infty}.
$$

(d) If $\beta \approx 1$ , stop and the final controller is $K = W _ { 1 } K _ { \infty } W _ { 2 } . \mathrm { ~ I f ~ } \beta \ll 1$ , increase α and go back to (b). If $\beta \gg 1$ , decrease α and $_ \mathrm { g o }$ back to (b).
