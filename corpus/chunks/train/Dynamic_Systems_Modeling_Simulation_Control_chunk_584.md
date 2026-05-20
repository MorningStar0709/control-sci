# Root-locus rules

1. The number of paths (loci) is n, the number of open-loop poles of $G ( s ) H ( s )$ .   
2. The root locus is symmetric about the real axis.   
3. The n loci begin at the open-loop poles $p _ { i }$ with gain $K = 0$ .   
4. The n loci terminate at the m (finite) open-loop zeros $z _ { j }$ or the $n - m$ “zeros at infinity” as the gain $K  \infty$ .   
5. The $n - m$ loci that approach infinity do so along radial, straight-line asymptotes that intersect the real axis at

$$\sigma_ {a} = \frac {\sum_ {i = 1} ^ {n} p _ {i} - \sum_ {j = 1} ^ {m} z _ {j}}{n - m} \text { with angle } \theta = \pm \frac {k 1 8 0 ^ {\circ}}{n - m}, k = 1, 3, 5, \dots$$

6. A point on the real axis is on the root locus if there is an odd number of open-loop poles and zeros to the right of that point.

7. “Breakaway” and “break-in” points at which the root locus leaves/enters the real axis satisfy the equation

$$\frac {d}{d s} [ G (s) H (s) ] = 0$$

We can use the above mentioned root-locus rules to develop the recommended steps for sketching a rootlocus plot:

1. Given the open-loop transfer function G(s)H(s), determine the n open-loop poles $p _ { i }$ and the m openloop zeros $z _ { j } .$ .   
2. Sketch the open-loop poles and zeros on the complex plane. Use “×” for an open-loop pole, and “o” for an open-loop zero. The root loci start at the n open-loop poles with gain K = 0 (Rule 3). Open-loop poles act as “sources” and zeros act as “sinks.”   
3. Sketch the real-axis root locus using Rule 6.   
4. Compute the asymptotes using Rule 5.   
5. Complete the approximate root-locus sketch (experience helps here). With enough experience, one does not need to exactly compute the breakaway/break-in points using Rule 7.

Before the advent of computer software such as MATLAB, a great deal of emphasis was placed on sketching a root locus by using these rules and recommended construction steps (similarly, general rules were developed for sketching a Bode diagram). As we shall see shortly, MATLAB has a command that produces the root-locus plot from the open-loop transfer function G(s)H(s). Therefore, we will not emphasize sketching the root locus by using a set of construction rules. Instead, we will focus on using the root locus with two specific goals in mind: (1) characterizing the effect that varying the parameter K has on the closed-loop transient response, and (2) understanding how adding a dynamic controller (i.e., transfer function $G _ { C } ( s )$ with poles and/or zeros) affects the closed-loop transient response.
