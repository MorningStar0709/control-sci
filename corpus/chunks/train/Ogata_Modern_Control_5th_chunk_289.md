Because graphical measurements of angles and magnitudes are involved in the analysis, we find it necessary to use the same divisions on the abscissa as on the ordinate axis when sketching the root locus on graph paper.

Consider the negative feedback system shown in Figure 6–3. (We assume that the value of gain K is nonnegative.) For this system,

$$G (s) = \frac {K}{s (s + 1) (s + 2)}, \quad H (s) = 1$$

Let us sketch the root-locus plot and then determine the value of K such that the damping ratio z of a pair of dominant complex-conjugate closed-loop poles is 0.5.

For the given system, the angle condition becomes

$$
\begin{array}{l} \underline {{G (s)}} = \left\lfloor \frac {K}{s (s + 1) (s + 2)} \right. \\ = - \underline {{\left\lfloor s \right.}} - \underline {{\left\lfloor s + 1 \right.}} - \underline {{\left\lfloor s + 2 \right.}} \\ = \pm 1 8 0 ^ {\circ} (2 k + 1) \quad (k = 0, 1, 2, \dots) \\ \end{array}
$$

The magnitude condition is

$$| G (s) | = \left| \frac {K}{s (s + 1) (s + 2)} \right| = 1$$

A typical procedure for sketching the root-locus plot is as follows:

1. Determine the root loci on the real axis. The first step in constructing a root-locus plot is to locate the open-loop poles, s=0, s=–1, and s=–2, in the complex plane. (There are no openloop zeros in this system.) The locations of the open-loop poles are indicated by crosses. (The locations of the open-loop zeros in this book will be indicated by small circles.) Note that the starting points of the root loci (the points corresponding to K=0) are open-loop poles. The number of individual root loci for this system is three, which is the same as the number of open-loop poles.

To determine the root loci on the real axis, we select a test point, s. If the test point is on the positive real axis, then

$$\underline {{s}} = \underline {{s + 1}} = \underline {{s + 2}} = 0 ^ {\circ}$$

This shows that the angle condition cannot be satisfied. Hence, there is no root locus on the positive real axis. Next, select a test point on the negative real axis between 0 and –1. Then

$$\underline {{{s}}} = 1 8 0 ^ {\circ}, \quad \underline {{{s + 1}}} = \underline {{{s + 2}}} = 0 ^ {\circ}$$

Thus

$$- \underline {{s}} - \underline {{s + 1}} - \underline {{s + 2}} = - 1 8 0 ^ {\circ}$$

and the angle condition is satisfied.Therefore, the portion of the negative real axis between 0 and –1 forms a portion of the root locus. If a test point is selected between –1 and –2, then
