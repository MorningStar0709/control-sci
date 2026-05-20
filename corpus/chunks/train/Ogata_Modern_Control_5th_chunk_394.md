Notice that the system has a zero at $s = 0$ and two poles at $s = - 0 . 5 \pm j 3 . 1 2 2 5$ Since this system. involves two poles and one zero, there is a possibility that a circular root locus exists. In fact, this system has a circular root locus, as will be shown. Since the angle condition is

$$\left\lfloor \frac {K s}{s ^ {2} + s + 1 0} = \pm 1 8 0 ^ {\circ} (2 k + 1) \right.$$

we have

$$\underline {{s}} - \underline {{s + 0 . 5 + j 3 . 1 2 2 5}} - \underline {{s + 0 . 5 - j 3 . 1 2 2 5}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

By substituting $s = \sigma + j \omega$ into this last equation and rearranging, we obtain

$$\underline {{\sigma + 0 . 5 + j (\omega + 3 . 1 2 2 5)}} + \underline {{\sigma + 0 . 5 + j (\omega - 3 . 1 2 2 5)}} = \underline {{\sigma + j \omega}} \pm 1 8 0 ^ {\circ} (2 k + 1)$$

which can be rewritten as

$$\tan^ {- 1} \left(\frac {\omega + 3 . 1 2 2 5}{\sigma + 0 . 5}\right) + \tan^ {- 1} \left(\frac {\omega - 3 . 1 2 2 5}{\sigma + 0 . 5}\right) = \tan^ {- 1} \left(\frac {\omega}{\sigma}\right) \pm 1 8 0 ^ {\circ} (2 k + 1)$$

Taking tangents of both sides of this last equation, we obtain

$$\frac {\frac {\omega + 3 . 1 2 2 5}{\sigma + 0 . 5} + \frac {\omega - 3 . 1 2 2 5}{\sigma + 0 . 5}}{1 - \left(\frac {\omega + 3 . 1 2 2 5}{\sigma + 0 . 5}\right) \left(\frac {\omega - 3 . 1 2 2 5}{\sigma + 0 . 5}\right)} = \frac {\omega}{\sigma}$$

which can be simplified to

$$\frac {2 \omega (\sigma + 0 . 5)}{(\sigma + 0 . 5) ^ {2} - \left(\omega^ {2} - 3 . 1 2 2 5 ^ {2}\right)} = \frac {\omega}{\sigma}$$

or

$$\omega \left(\sigma^ {2} - 1 0 + \omega^ {2}\right) = 0$$

which yields

$$\omega = 0 \quad \text { or } \quad \sigma^ {2} + \omega^ {2} = 1 0$$

Notice that $\omega = 0$ corresponds to the real axis.The negative real axis (between $s = 0$ and $s = - \infty )$ corresponds to $K \geq 0$ , and the positive real axis corresponds to $K < 0 .$ . The equation

$$\sigma^ {2} + \omega^ {2} = 1 0$$

is an equation of a circle with center at $\sigma = 0 , \omega = 0$ with the radius equal to ${ \sqrt { 1 0 } } . \mathbf { A }$ portion of this circle that lies to the left of the complex poles corresponds to the root locus for $K > 0 .$ . (The portion of the circle which lies to the right of the complex poles corresponds to the root locus for $K < 0 . )$ Figure 6–99(b) shows a sketch of the root loci for $K > 0$ .

Since we require $\zeta = 0 . 7$ for the closed-loop poles, we find the intersection of the circular root locus and a line having an angle of $4 5 . 5 7 ^ { \circ }$ (note that cos $4 5 . 5 7 ^ { \circ } = 0 . 7 )$ with the negative real axis. The intersection is at $s = - 2 . 2 1 4 + j 2 . 2 5 8$ . The gain K corresponding to this point is 3.427. Hence, the desired value of the velocity feedback gain k is

$$k = \frac {K}{1 0} = 0. 3 4 2 7$$
