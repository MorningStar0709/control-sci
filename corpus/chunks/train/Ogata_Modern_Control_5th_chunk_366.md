represent the complex branches for $0 \leq K \leq \infty .$ . These two branches lie between $\sigma = - 1 . 6$ and $\sigma = 0 .$ . [See Figure 6–66(b).] The slopes of the complex root-locus branches at the breakaway point $( \sigma = - 1 . 2 )$ can be found by evaluating of Equation (6–29) at pointdvds $\sigma = - 1 . 2$ .

$$\left. \frac {d \omega}{d \sigma} \right| _ {\sigma = - 1. 2} = \pm \sqrt {\frac {- \sigma}{\sigma + 1 . 6}} \Bigg | _ {\sigma = - 1. 2} = \pm \sqrt {\frac {1 . 2}{0 . 4}} = \pm \sqrt {3}$$

Since $\tan ^ { - 1 } { \sqrt { 3 } } = 6 0 ^ { \circ }$ the root-locus branches intersect the real axis with angles, $\pm 6 0 ^ { \circ }$ .

A–6–5. Consider the system shown in Figure $6 { \ - } 6 7 ( \mathrm { a } )$ . Sketch the root loci for the system. Observe that for small or large values of K the system is underdamped and for medium values of K it is overdamped.

Solution. A root locus exists on the real axis between the origin and –q. The angles of asymptotes of the root-locus branches are obtained as

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{3} = 6 0 ^ {\circ}, - 6 0 ^ {\circ}, - 1 8 0 ^ {\circ}$$

The intersection of the asymptotes and the real axis is located on the real axis at

$$s = - \frac {0 + 2 + 2}{3} = - 1. 3 3 3 3$$

The breakaway and break-in points are found from $d K / d s = 0$ Since the characteristic equation is.

$$s ^ {3} + 4 s ^ {2} + 5 s + K = 0$$

![](image/6b4edc3ba337486402d28d25d7fa176b5359b3b53e4cdc7a7594b1772eb2557d.jpg)

<details>
<summary>line</summary>

| Point | Value |
| --- | --- |
| K | 1.852 |
</details>

Figure 6–67   
(a) Control system;   
(b) root-locus plot.

we have

$$K = - \left(s ^ {3} + 4 s ^ {2} + 5 s\right)$$

Now we set

$$\frac {d K}{d s} = - (3 s ^ {2} + 8 s + 5) = 0$$

which yields

$$s = - 1, \quad s = - 1. 6 6 6 7$$

Since these points are on root loci, they are actual breakaway or break-in points. (At point s=–1, the value of K is 2, and at point s=–1.6667, the value of K is 1.852.)

The angle of departure from a complex pole in the upper-half s plane is obtained from

$$\theta = 1 8 0 ^ {\circ} - 1 5 3. 4 3 ^ {\circ} - 9 0 ^ {\circ}$$

or

$$\theta = - 6 3. 4 3 ^ {\circ}$$

The root-locus branch from the complex pole in the upper-half s plane breaks into the real axis at s=–1.6667.

Next we determine the points where root-locus branches cross the imaginary axis. By substituting s=jv into the characteristic equation, we have

$$(j \omega) ^ {3} + 4 (j \omega) ^ {2} + 5 (j \omega) + K = 0$$

or

$$\left(K - 4 \omega^ {2}\right) + j \omega (5 - \omega^ {2}) = 0$$

from which we obtain
