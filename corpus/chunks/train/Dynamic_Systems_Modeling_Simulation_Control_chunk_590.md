# Example 10.11

Figure 10.37 shows a unity-feedback closed-loop system with proportional control and plant dynamics represented by G(s). Use the root-locus construction rules to develop the basic structure of the root locus and use MATLAB to create the root locus. Finally, use the root-locus plot to characterize the closed-loop transient response and closed-loop stability.

As before, we start with the open-loop transfer function

$$G (s) H (s) = \frac {s + 6}{2 s ^ {2} + 4 s} = \frac {s + 6}{2 s (s + 2)} \tag {10.44}$$

The two open-loop poles $( n = 2 )$ are $p _ { 1 } = 0$ and $p _ { 2 } = - 2$ , and the single open-loop zero $( m = 1 )$ is $z _ { 1 } = - 6$ . Consequently, a sketch of the root locus begins with two open-loop $\mathbf { \bar { \Sigma } } ^ { \left. } \mathbf { x } ^ { \right. }$ markers at $s = 0$ and $s = - 2$ , and one open-loop $" \boldsymbol { \mathrm { O } } ^ { , , }$ marker at $s = - 6$ . Because we have three open-loop poles and zeros on the real axis, Rule 6 tells us that a root-locus branch lies on the real axis to the left of –6 and in between –2 and the origin. Rule 5 states that we have $n - m$ or only one asymptote with the angle

$$\theta = \pm \frac {1 8 0 ^ {\circ}}{n - m} = \pm 1 8 0 ^ {\circ}$$

Hence, the single asymptote is the negative real axis and there is no need to compute the real-axis intersection point $\sigma _ { a } .$ .

The following MATLAB commands create the root-locus plot:

$$> > \text { sysGH } = t f ([ 1 6 ], [ 2 4 0 ])\% \text { create } G (s) H (s)> > \text { rlocus(sysGH) }\% \text{ create and draw the root locus}$$
