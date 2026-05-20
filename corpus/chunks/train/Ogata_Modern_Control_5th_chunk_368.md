# A–6–6. Sketch the root loci for the system shown in Figure 6–68(a).

Solution. The open-loop poles are located at $s = 0 , s = - 1 , s = - 2 + j 3$ , and $s = - 2 - j 3 .$ . A root locus exists on the real axis between points s=0 and $s = - 1$ . The angles of the asymptotes are found as follows:

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{4} = 4 5 ^ {\circ}, - 4 5 ^ {\circ}, 1 3 5 ^ {\circ}, - 1 3 5 ^ {\circ}$$

![](image/789f75117cf7f80e09d1c91e1381ec664f32df013ad8e382e4f21b1125fa317b.jpg)  
Figure 6–68   
(a) Control system; (b) root-locus plot.

The intersection of the asymptotes and the real axis is found from

$$s = - \frac {0 + 1 + 2 + 2}{4} = - 1. 2 5$$

The breakaway and break-in points are found from $d K / d s = 0$ Noting that.

$$K = - s (s + 1) \left(s ^ {2} + 4 s + 1 3\right) = - \left(s ^ {4} + 5 s ^ {3} + 1 7 s ^ {2} + 1 3 s\right)$$

we have

$$\frac {d K}{d s} = - \left(4 s ^ {3} + 1 5 s ^ {2} + 3 4 s + 1 3\right) = 0$$

from which we get

$$s = - 0. 4 6 7, \quad s = - 1. 6 4 2 + j 2. 0 6 7, \quad s = - 1. 6 4 2 - j 2. 0 6 7$$

Point $s = - 0 . 4 6 7$ is on a root locus. Therefore, it is an actual breakaway point. The gain values K corresponding to points $s = - 1 . 6 4 2 \pm j 2 . 0 6 7$ are complex quantities. Since the gain values are not real positive, these points are neither breakaway nor break-in points.

The angle of departure from the complex pole in the upper-half s plane is

$$\theta = 1 8 0 ^ {\circ} - 1 2 3. 6 9 ^ {\circ} - 1 0 8. 4 4 ^ {\circ} - 9 0 ^ {\circ}$$

or

$$\theta = - 1 4 2. 1 3 ^ {\circ}$$

Next we shall find the points where root loci may cross the $j \omega$ axis. Since the characteristic equation is

$$s ^ {4} + 5 s ^ {3} + 1 7 s ^ {2} + 1 3 s + K = 0$$

by substituting s=jv into it we obtain

$$(j \omega) ^ {4} + 5 (j \omega) ^ {3} + 1 7 (j \omega) ^ {2} + 1 3 (j \omega) + K = 0$$

or

$$\left(K + \omega^ {4} - 1 7 \omega^ {2}\right) + j \omega (1 3 - 5 \omega^ {2}) = 0$$

from which we obtain

$$\omega = \pm 1. 6 1 2 5, \quad K = 3 7. 4 4 \quad \text { or } \quad \omega = 0, \quad K = 0$$

The root-locus branches that extend to the right-half s plane cross the imaginary axis at $\omega = \pm 1 . 6 1 2 5$ Also, the root-locus branch on the real axis touches the imaginary axis at. $\omega = 0$ . Figure 6–68(b) shows a sketch of the root loci for the system. Notice that each root-locus branch that extends to the right-half s plane crosses its own asymptote.

A–6–7. Sketch the root loci of the control system shown in Figure 6–69(a). Determine the range of gain K for stability.
