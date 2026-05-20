The value of K should be adjusted so that system performance is optimum according to a given performance index.

A–6–2. Sketch the root loci for the system shown in Figure $6 { \ - } 6 5 ( \mathrm { a } )$ .

Solution. A root locus exists on the real axis between points s=–1 and s=–3.6. The asymptotes can be determined as follows:

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{3 - 1} = 9 0 ^ {\circ}, - 9 0 ^ {\circ}$$

The intersection of the asymptotes and the real axis is found from

$$s = - \frac {0 + 0 + 3 . 6 - 1}{3 - 1} = - 1. 3$$

![](image/9def940f5d28be08f56d9152662433292ee9a701bd1de3df4efd14a036667999.jpg)  
Figure 6–65   
(a) Control system; (b) root-locus plot.

Since the characteristic equation is

$$s ^ {3} + 3. 6 s ^ {2} + K (s + 1) = 0$$

we have

$$K = - \frac {s ^ {3} + 3 . 6 s ^ {2}}{s + 1}$$

The breakaway and break-in points are found from

$$\frac {d K}{d s} = - \frac {(3 s ^ {2} + 7 . 2 s) (s + 1) - (s ^ {3} + 3 . 6 s ^ {2})}{(s + 1) ^ {2}} = 0$$

or

$$s ^ {3} + 3. 3 s ^ {2} + 3. 6 s = 0$$

from which we get

$$s = 0, \quad s = - 1. 6 5 + j 0. 9 3 6 7, \quad s = - 1. 6 5 - j 0. 9 3 6 7$$

Point s=0 corresponds to the actual breakaway point. But points $s = 1 . 6 5 \pm j 0 . 9 3 6 7$ are neither breakaway nor break-in points, because the corresponding gain values K become complex quantities.

To check the points where root-locus branches may cross the imaginary axis, substitute $s = j \omega$ into the characteristic equation, yielding.

$$(j \omega) ^ {3} + 3. 6 (j \omega) ^ {2} + K j \omega + K = 0$$

or

$$\left(K - 3. 6 \omega^ {2}\right) + j \omega \left(K - \omega^ {2}\right) = 0$$

Notice that this equation can be satisfied only if v=0, K=0. Because of the presence of a double pole at the origin, the root locus is tangent to the jv axis at v=0. The root-locus branches do not cross the jv axis. Figure 6–65(b) is a sketch of the root loci for this system.

A–6–3. Sketch the root loci for the system shown in Figure 6–66(a).

Solution. A root locus exists on the real axis between point $s = - 0 . 4 \mathrm { a n d } s = - 3 . 6 .$ . The angles of asymptotes can be found as follows:

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{3 - 1} = 9 0 ^ {\circ}, - 9 0 ^ {\circ}$$

The intersection of the asymptotes and the real axis is obtained from

$$s = - \frac {0 + 0 + 3 . 6 - 0 . 4}{3 - 1} = - 1. 6$$

Next we shall find the breakaway points. Since the characteristic equation is

$$s ^ {3} + 3. 6 s ^ {2} + K s + 0. 4 K = 0$$

we have

$$K = - \frac {s ^ {3} + 3 . 6 s ^ {2}}{s + 0 . 4}$$
