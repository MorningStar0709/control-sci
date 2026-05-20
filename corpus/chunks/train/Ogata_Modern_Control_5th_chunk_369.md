Solution. Open-loop poles are located at $s = 1 , s = - 2 + j \sqrt { 3 }$ and, $s = - 2 - j \sqrt { 3 }$ A root locus. exists on the real axis between points s=1 and $s = - \infty .$ . The asymptotes of the root-locus branches are found as follows:

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{3} = 6 0 ^ {\circ}, - 6 0 ^ {\circ}, 1 8 0 ^ {\circ}$$

The intersection of the asymptotes and the real axis is obtained as

$$s = - \frac {- 1 + 2 + 2}{3} = - 1$$

The breakaway and break-in points can be located from $d K / d s = 0 .$ Since.

$$K = - (s - 1) \left(s ^ {2} + 4 s + 7\right) = - \left(s ^ {3} + 3 s ^ {2} + 3 s - 7\right)$$

we have

$$\frac {d K}{d s} = - (3 s ^ {2} + 6 s + 3) = 0$$

which yields

$$(s + 1) ^ {2} = 0$$

![](image/600c2c7389a66adc16360249d5f1b39f8c5bec4d74aaec5c3c9c4f2683271f88.jpg)  
Figure 6–69   
(a) Control system; (b) root-locus plot.

Thus the equation $d K / d s = 0$ has a double root at $s = - 1$ . (This means that the characteristic equation has a triple root at $s = - 1 . )$ The breakaway point is located at $s = - 1$ . Three root-locus branches meet at this breakaway point.The angles of departure of the branches at the breakaway point are $\pm 1 8 0 ^ { \circ } / 3$ —that is, 60° and –60°.

We shall next determine the points where root-locus branches may cross the imaginary axis. Noting that the characteristic equation is

$$(s - 1) \big (s ^ {2} + 4 s + 7 \big) + K = 0$$

or

$$s ^ {3} + 3 s ^ {2} + 3 s - 7 + K = 0$$

we substitute into it and obtains = jv

$$(j \omega) ^ {3} + 3 (j \omega) ^ {2} + 3 (j \omega) - 7 + K = 0$$

By rewriting this last equation, we have

$$(K - 7 - 3 \omega^ {2}) + j \omega (3 - \omega^ {2}) = 0$$

This equation is satisfied when

$$\omega = \pm \sqrt {3}, \quad K = 7 + 3 \omega^ {2} = 1 6 \quad \text { or } \quad \omega = 0, \quad K = 7$$

The root-locus branches cross the imaginary axis at $\omega = \pm \sqrt { 3 }$ (where K=16) and $\omega = 0$ (where K=7). Since the value of gain K at the origin is 7, the range of gain value K for stability is

$$7 < K < 1 6$$

Figure $6 { \ - } 6 9 ( \mathrm { b } )$ shows a sketch of the root loci for the system. Notice that all branches consist of parts of straight lines.

The fact that the root-locus branches consist of straight lines can be verified as follows: Since the angle condition is

$$\left\lfloor \frac {K}{(s - 1) (s + 2 + j \sqrt {3}) (s + 2 - j \sqrt {3})} = \pm 1 8 0 ^ {\circ} (2 k + 1) \right.$$

we have

$$- \underline {{s - 1}} - \underline {{s + 2 + j \sqrt {3}}} - \underline {{s + 2 - j \sqrt {3}}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

By substituting into this last equation,s = s + jv
