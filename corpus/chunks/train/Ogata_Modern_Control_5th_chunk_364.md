![](image/4fcef6d2cce9b010e798d54f52113b57fc23b324dce8a48b015aa815c7390edf.jpg)  
Figure 6–66   
(a) Control system; (b) root-locus plot.

The breakaway and break-in points are found from

$$\frac {d K}{d s} = - \frac {(3 s ^ {2} + 7 . 2 s) (s + 0 . 4) - (s ^ {3} + 3 . 6 s ^ {2})}{(s + 0 . 4) ^ {2}} = 0$$

from which we get

$$s ^ {3} + 2. 4 s ^ {2} + 1. 4 4 s = 0$$

or

$$s (s + 1. 2) ^ {2} = 0$$

Thus, the breakaway or break-in points are at s=0 and s=–1.2. Note that s=–1.2 is a double root.When a double root occurs in $d K / d s = 0$ at point $s = - 1 . 2 , d ^ { 2 } K / ( d s ^ { 2 } ) = 0$ at this point. The value of gain K at point s=–1.2 is

$$K = - \frac {s ^ {3} + 3 . 6 s ^ {2}}{s + 4} \Bigg | _ {s = - 1. 2} = 4. 3 2$$

This means that with K=4.32 the characteristic equation has a triple root at point $s = - 1 . 2 .$ . This can be easily verified as follows:

$$s ^ {3} + 3. 6 s ^ {2} + 4. 3 2 s + 1. 7 2 8 = (s + 1. 2) ^ {3} = 0$$

Hence, three root-locus branches meet at point s=–1.2. The angles of departures at point $s = - 1 . 2$ of the root locus branches that approach the asymptotes are $\pm 1 8 0 ^ { \circ } / 3$ that, $\mathrm { i s } , 6 0 ^ { \circ }$ and $- 6 0 ^ { \circ }$ . (See Problem A–6–4.)

Finally, we shall examine if root-locus branches cross the imaginary axis. By substituting $s = j \omega$ into the characteristic equation, we have

$$(j \omega) ^ {3} + 3. 6 (j \omega) ^ {2} + K (j \omega) + 0. 4 K = 0$$

or

$$\left(0. 4 K - 3. 6 \omega^ {2}\right) + j \omega (K - \omega^ {2}) = 0$$

This equation can be satisfied only if v=0, K=0. At point v=0, the root locus is tangent to the jv axis because of the presence of a double pole at the origin.There are no points where rootlocus branches cross the imaginary axis.

A sketch of the root loci for this system is shown in Figure 6–66(b).

A–6–4. Referring to Problem A–6–3, obtain the equations for the root-locus branches for the system shown in Figure 6–66(a). Show that the root-locus branches cross the real axis at the breakaway point at angles ; 60°.

Solution. The equations for the root-locus branches can be obtained from the angle condition

$$\frac {K (s + 0 . 4)}{s ^ {2} (s + 3 . 6)} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

which can be rewritten as

$$\underline {{s + 0 . 4}} - 2 \underline {{s}} - \underline {{s + 3 . 6}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

By substituting $s = \sigma + j \omega _ { ; }$ we obtain,

$$\left\lfloor \sigma + j \omega + 0. 4 - 2 \right\rfloor \left\lfloor \sigma + j \omega - \right. \left\lfloor \sigma + j \omega + 3. 6 = \pm 1 8 0 ^ {\circ} (2 k + 1) \right.$$

or
