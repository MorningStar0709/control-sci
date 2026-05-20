$$G (j \omega) = \frac {j \omega T}{1 + j \omega T}, \quad \text { for } 0 \leq \omega \leq \infty$$

is a semicircle. Find the center and radius of the circle.

Solution. The given sinusoidal transfer function $G ( j \omega )$ can be written as follows:

$$G (j \omega) = X + j Y$$

where

$$X = \frac {\omega^ {2} T ^ {2}}{1 + \omega^ {2} T ^ {2}}, \quad Y = \frac {\omega T}{1 + \omega^ {2} T ^ {2}}$$

Then

$$\left(X - \frac {1}{2}\right) ^ {2} + Y ^ {2} = \frac {\left(\omega^ {2} T ^ {2} - 1\right) ^ {2}}{4 \left(1 + \omega^ {2} T ^ {2}\right) ^ {2}} + \frac {\omega^ {2} T ^ {2}}{\left(1 + \omega^ {2} T ^ {2}\right) ^ {2}} = \frac {1}{4}$$

Hence, we see that the plot of $G ( j \omega )$ is a circle centered at (0.5,0) with radius equal to 0.5. The upper semicircle corresponds to $0 \leq \omega \leq \infty .$ , and the lower semicircle corresponds to $- \infty \leq \omega \leq 0 .$

A–7–6. Prove the following mapping theorem: Let $F ( s )$ be a ratio of polynomials in s. Let P be the number of poles and Z be the number of zeros of $F ( s )$ that lie inside a closed contour in the s plane, with multiplicity accounted for. Let the closed contour be such that it does not pass through any poles or zeros of $F ( s )$ .The closed contour in the s plane then maps into the $F ( s )$ plane as a closed curve. The number N of clockwise encirclements of the origin of the $F ( s )$ plane, as a representative point s traces out the entire contour in the s plane in the clockwise direction, is equal to $Z \mathrm { ~ - ~ } P .$ .

Solution. To prove this theorem, we use Cauchy’s theorem and the residue theorem. Cauchy’s theorem states that the integral of $F ( s )$ around a closed contour in the s plane is zero if $F ( s )$ is analytic# within and on the closed contour, or

$$\oint F (s) d s = 0$$

Suppose that $F ( s )$ is given by

$$F (s) = \frac {\left(s + z _ {1}\right) ^ {k _ {1}} \left(s + z _ {2}\right) ^ {k _ {2}} \cdots}{\left(s + p _ {1}\right) ^ {m _ {1}} \left(s + p _ {2}\right) ^ {m _ {2}} \cdots} X (s)$$

where $X ( s )$ is analytic in the closed contour in the s plane and all the poles and zeros are located in the contour. Then the ratio $F ^ { \prime } ( s ) / F ( s )$ can be written

$$\frac {F ^ {\prime} (s)}{F (s)} = \left(\frac {k _ {1}}{s + z _ {1}} + \frac {k _ {2}}{s + z _ {2}} + \dots\right) - \left(\frac {m _ {1}}{s + p _ {1}} + \frac {m _ {2}}{s + p _ {2}} + \dots\right) + \frac {X ^ {\prime} (s)}{X (s)} \tag {7-30}$$

This may be seen from the following consideration: If $\hat { F } ( s )$ is given by

$$\hat {F} (s) = \left(s + z _ {1}\right) ^ {k} X (s)$$
