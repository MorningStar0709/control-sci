The particular value of K that will yield multiple roots of the characteristic equation is obtained from Equation (6–8) as

$$K = - \frac {B ^ {\prime} (s)}{A ^ {\prime} (s)}$$

If we substitute this value of K into Equation (6–6), we get

$$f (s) = B (s) - \frac {B ^ {\prime} (s)}{A ^ {\prime} (s)} A (s) = 0$$

or

$$B (s) A ^ {\prime} (s) - B ^ {\prime} (s) A (s) = 0 \tag {6-9}$$

If Equation (6–9) is solved for s, the points where multiple roots occur can be obtained. On the other hand, from Equation (6–6) we obtain

$$K = - \frac {B (s)}{A (s)}$$

and

$$\frac {d K}{d s} = - \frac {B ^ {\prime} (s) A (s) - B (s) A ^ {\prime} (s)}{A ^ {2} (s)}$$

If dK/ds is set equal to zero, we get the same equation as Equation (6–9). Therefore, the breakaway points can be simply determined from the roots of

$$\frac {d K}{d s} = 0$$

It should be noted that not all the solutions of Equation (6–9) or of dK/ds=0 correspond to actual breakaway points. If a point at which $d K / d s = 0$ is on a root locus, it is an actual breakaway or break-in point. Stated differently, if at a point at which dK $/ d s = 0$ the value of K takes a real positive value, then that point is an actual breakaway or break-in point.

For the present example, the characteristic equation $G ( s ) + 1 = 0$ is given by

$$\frac {K}{s (s + 1) (s + 2)} + 1 = 0$$

or

$$K = - \left(s ^ {3} + 3 s ^ {2} + 2 s\right)$$

By setting $d K / d s = 0 .$ we obtain

$$\frac {d K}{d s} = - (3 s ^ {2} + 6 s + 2) = 0$$

or

$$s = - 0. 4 2 2 6, \quad s = - 1. 5 7 7 4$$

Since the breakaway point must lie on a root locus between 0 and –1, it is clear that $s = - 0 . 4 2 2 6$ corresponds to the actual breakaway point. Point s=–1.5774 is not on the root locus. Hence, this point is not an actual breakaway or break-in point. In fact, evaluation of the values of K corresponding to $s = - 0 . 4 2 2 6$ and s=–1.5774 yields

$$K = 0. 3 8 4 9, \quad \text { for } s = - 0. 4 2 2 6K = - 0. 3 8 4 9, \quad \text { for } s = - 1. 5 7 7 4$$

4. Determine the points where the root loci cross the imaginary axis. These points can be found by use of Routh’s stability criterion as follows: Since the characteristic equation for the present system is

$$s ^ {3} + 3 s ^ {2} + 2 s + K = 0$$

the Routh array becomes

$$
\begin{array}{c c c} s ^ {3} & 1 & 2 \\ s ^ {2} & 3 & K \\ s ^ {1} & \frac {6 - K}{3} \\ s ^ {0} & K \end{array}
$$

The value of K that makes the $s ^ { 1 }$ term in the first column equal zero is K=6. The crossing points on the imaginary axis can then be found by solving the auxiliary equation obtained from the $s ^ { 2 }$ row; that is,

$$3 s ^ {2} + K = 3 s ^ {2} + 6 = 0$$

which yields
