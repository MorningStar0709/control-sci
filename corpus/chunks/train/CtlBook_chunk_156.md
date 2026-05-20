# 5.4.8 Poles or zeros at the origin

It is slightly trickier to draw the Bode plots when there are one or more poles at $s = 0$ because the rst asymptotic approximation $\omega < < a$ does not apply. In this case, there is a multiplicative term $1 / s ^ { n }$ , where n is negative for poles at $s = 0$ and positive for zeros at $s = 0$ . For each value of $n ,$ the slope changes. However, in all cases

$$| s ^ {n} | = 1 \quad \mathrm{for} \omega = 1 \quad \mathrm{and} \quad | s ^ {n} | = \omega^ {n}$$

Figure 5.7 (Left) shows several Bode Magnitude plots of $s ^ { n }$ . Each plot is a straight line passing through the point, $\{ 0 d B , \omega = 1 \}$ .

For transfer functions containing poles or zeros at the origin, we need to choose a specic frequency (often $\omega = 1 )$ at which to evaluate the magnitude of the transfer function. We also compute the slope of the low-frequency asymptote at ω ≈ 0 by looking at the exponent of the pole or zero as $\omega  0$ . The phase contribution of poles or zeros at the origin (Figure 5.7, Right) is easier because it is just a constant $9 0 °$ for each power of s in the numerator and $- \bar { 9 } 0 ^ { \circ }$ for each power of s in the denominator.
