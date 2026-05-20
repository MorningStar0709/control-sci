A general procedure for determining the lead compensator is as follows: First, find the sum of the angles at the desired location of one of the dominant closed-loop poles with the open-loop poles and zeros of the original system, and determine the necessary angle f to be added so that the total sum of the angles is equal $\mathrm { t o } \pm 1 8 0 ^ { \circ } ( 2 k + 1 )$ The lead compensator must contribute this). angle f. (If the angle f is quite large, then two or more lead networks may be needed rather than a single one.)

Assume that the lead compensator $G _ { c } ( s )$ has the transfer function as follows:

$$G _ {c} (s) = K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}}, \quad (0 < \alpha < 1)$$

The angle from the pole at the origin to the desired dominant closed-loop pole at $s = - 1 . 5 + j 2$ .5981 is 120°. The angle from the pole at $s = - 1$ to the desired closed-loop pole is 100.894°. Hence, the angle deficiency is

$$\text { Angle deficiency } = 1 8 0 ^ {\circ} - 1 2 0 ^ {\circ} - 1 0 0. 8 9 4 ^ {\circ} = - 4 0. 8 9 4 ^ {\circ}$$

Deficit angle $4 0 . 8 9 4 ^ { \circ }$ must be contributed by a lead compensator.

Note that the solution to such a problem is not unique. There are infinitely many solutions. We shall present two solutions to the problem in what follows.

Method 1. There are many ways to determine the locations of the zero and pole of the lead compensator. In what follows we shall introduce a procedure to obtain a largest possible value for a. (Note that a larger value of a will produce a larger value of $K _ { v }$ . In most cases, the larger the $K _ { v }$ is, the better the system performance.) First, draw a horizontal line passing through point P, the desired location for one of the dominant closed-loop poles. This is shown as line PA in Figure 6–41. Draw also a line connecting point P and the origin. Bisect the angle between the lines PA and PO, as shown in Figure 6–41. Draw two lines PC and PD that make angles with the bisector PB.The;f2 intersections of PC and PD with the negative real axis give the necessary locations for the pole and zero of the lead network.The compensator thus designed will make point P a point on the root locus of the compensated system.The open-loop gain is determined by use of the magnitude condition.

In the present system, the angle of $G ( s )$ at the desired closed-loop pole is

$$\left. \frac {1 0}{s (s + 1)} \right| _ {s = - 1. 5 + j 2. 5 9 8 1} = - 2 2 0. 8 9 4 ^ {\circ}$$
