# 5.5.4 Construction of the Nyquist Locus

The map of a point $s = j\omega$ is simply $L(j\omega)$ . Therefore, the map of the imaginary axis is simply the frequency response plotted in the complex plane with $\omega$ as a parameter. A point $L(j\omega)$ is plotted as a point with $x$ -component $\operatorname{Re} L(j\omega)$ and $y$ -component $\operatorname{Im} L(j\omega)$ .

It is also possible, and more helpful, to view the locus as a polar plot, with $|L(j\omega)|$ as the magnitude and $\neq L(j\omega)$ as the angle. If the phase angle of $L(j\omega)$ increases as $\omega$ increases, the Nyquist locus is moving counterclockwise (in the positive-angle direction); if the phase angle is decreasing, the Nyquist locus is moving clockwise. As $\omega$ increases, the locus moves away from the origin if the magnitude is increasing with frequency, and toward the origin if it is decreasing.

Since $L(-j\omega) = L^{*}(j\omega)$ , a negative-frequency point has the same real part (x-coordinate) as $L(j\omega)$ , but an imaginary part (y-coordinate) of opposite sign. The map of the negative part of the j-axis is obtained by simply reflecting the map for positive $\omega$ about the real axis.

Before proceeding to an example, we introduce one helpful modification. It is often the case that $L(s) = kL'(s)$ , where k is a gain parameter to be determined in the design process. In such cases, the equations

$$1 + k L ^ {\prime} (s) = 0$$

and

$$\frac {1}{k} + L ^ {\prime} (s) = 0 \tag {5.20}$$

are equivalent.

Equation 5.20 suggests that encirclements of the point $(- \frac{1}{k}, 0)$ by the locus $L'(j\omega)$ be considered, rather than encirclements of $(-1, 0)$ by $L(j\omega) = kL'(j\omega)$ . That is often easier to do.
