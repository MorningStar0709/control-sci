Rule 5 is Modified as Follows: When calculating the angle of departure (or angle of arrival) from a complex open-loop pole (or at a complex zero), subtract from $0 ^ { \circ }$ the sum of all angles of the vectors from all the other poles and zeros to the complex pole (or complex zero) in question, with appropriate signs included.

Other rules for constructing the root-locus plot remain the same. We shall now apply the modified rules to construct the root-locus plot.

1. Plot the open-loop poles $( s = - 1 + j , s = - 1 - j , s = - 3 )$ and zero $( s = - 2 )$ in the complex plane.As K is increased from 0 to q, the closed-loop poles start at the open-loop poles and terminate at the open-loop zeros (finite or infinite), just as in the case of negative-feedback systems.   
2. Determine the root loci on the real axis. Root loci exist on the real axis between –2 and ±q and between –3 and –q.   
3. Determine the asymptotes of the root loci. For the present system,

$$\text { Angles of asymptote } = \frac {\pm k 3 6 0 ^ {\circ}}{3 - 1} = \pm 1 8 0 ^ {\circ}$$

This simply means that asymptotes are on the real axis.

4. Determine the breakaway and break-in points. Since the characteristic equation is

$$(s + 3) \left(s ^ {2} + 2 s + 2\right) - K (s + 2) = 0$$

we obtain

$$K = \frac {(s + 3) (s ^ {2} + 2 s + 2)}{s + 2}$$

By differentiating K with respect to s, we obtain

$$\frac {d K}{d s} = \frac {2 s ^ {3} + 1 1 s ^ {2} + 2 0 s + 1 0}{(s + 2) ^ {2}}$$

Note that

$$
\begin{array}{l} 2 s ^ {3} + 1 1 s ^ {2} + 2 0 s + 1 0 = 2 (s + 0. 8) \left(s ^ {2} + 4. 7 s + 6. 2 4\right) \\ = 2 (s + 0. 8) (s + 2. 3 5 + j 0. 7 7) (s + 2. 3 5 - j 0. 7 7) \\ \end{array}
$$

Point s=–0.8 is on the root locus. Since this point lies between two zeros (a finite zero and an infinite zero), it is an actual break-in point. Points $s = - 2 . 3 5 \pm j 0 . 7 7$ do not satisfy the angle condition and, therefore, they are neither breakaway nor break-in points.

5. Find the angle of departure of the root locus from a complex pole. For the complex pole at s=–1+j, the angle of departure u is

$$\theta = 0 ^ {\circ} - 2 7 ^ {\circ} - 9 0 ^ {\circ} + 4 5 ^ {\circ}$$

or

$$\theta = - 7 2 ^ {\circ}$$

(The angle of departure from the complex pole at s=–1-j is 72°.)

6. Choose a test point in the broad neighborhood of the jv axis and the origin and apply the angle condition. Locate a sufficient number of points that satisfy the angle condition.

Figure 6–31 shows the root loci for the given positive-feedback system.The root loci are shown with dashed lines and a curve.

Note that if
