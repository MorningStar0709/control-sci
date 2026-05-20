# Stability Margins

Phase and amplitude margins are traditional measures that are used to express the sensitivity of a system to modeling errors. The sensitivity function introduced in Sec. 3.3 is another measure.

$$S = \frac {A R}{A R + B S} = \frac {1}{1 + B S / A R} = \frac {A R}{A _ {c l}} \tag {5.39}$$

The inverse value of $|S(e^{i\omega})|$ represents the distance from a point of the Nyquist curve of the loop-transfer function $BS / AR$ to the critical point -1. The maximum value of $|S(e^{i\omega})|$ is thus the reciprocal of the smallest distance from the critical point -1 to the Nyquist curve. To have a reasonable robustness against instability, the largest value of $|S(e^{i\omega})|$ should therefore not be too large. A typical requirement is that $|S(e^{i\omega})| < 2$ . In all design work it is therefore useful to investigate $|S(e^{i\omega})|$ and make sure that it is not too large.

Control-system design is normally an iterative procedure. In a typical case we start with a nominal design. By calculating the sensitivity function we may find that the sensitivity is too large for some frequencies. It follows from Eq. (5.39) that a large sensitivity can be reduced by making R or S small at some frequencies. Making R small means that the controller gain is increased; making S small means that the controller gain is decreased. To avoid the large sensitivity we can introduce additional constraints on polynomials R and S in some frequency ranges and repeat the design.
