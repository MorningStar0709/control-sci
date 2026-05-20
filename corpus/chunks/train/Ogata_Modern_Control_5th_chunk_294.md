7. Determine a pair of dominant complex-conjugate closed-loop poles such that the damping ratio $\zeta$ is 0.5. Closed-loop poles with $\zeta = 0 . 5$ lie on lines passing through the origin and making the angles $\pm \cos ^ { - 1 } \zeta = \pm \mathrm { c o s } ^ { - 1 } 0 . 5 = \pm 6 0 ^ { \circ }$ with the negative real axis. From Figure 6–6, such closedloop poles having $\zeta = 0 . 5$ are obtained as follows:

$$s _ {1} = - 0. 3 3 3 7 + j 0. 5 7 8 0, \quad s _ {2} = - 0. 3 3 3 7 - j 0. 5 7 8 0$$

The value of K that yields such poles is found from the magnitude condition as follows:

$$K = | s (s + 1) (s + 2) | _ {s = - 0. 3 3 3 7 + j 0. 5 7 8 0}= 1. 0 3 8 3$$

Using this value of K, the third pole is found at $s = - 2 . 3 3 2 6$

Note that, from step 4, it can be seen that for $K = 6$ the dominant closed-loop poles lie on the imaginary axis at $s = \pm j \sqrt { 2 }$ With this value of K, the system will exhibit sustained oscillations.. For $K > 6$ , the dominant closed-loop poles lie in the right-half s plane, resulting in an unstable system.

Finally, note that, if necessary, the root loci can be easily graduated in terms of K by use of the magnitude condition. We simply pick out a point on a root locus, measure the magnitudes of the three complex quantities $s , s + 1$ , and $s + 2 .$ , and multiply these magnitudes; the product is equal to the gain value K at that point, or

$$| s | \cdot | s + 1 | \cdot | s + 2 | = K$$

Graduation of the root loci can be done easily by use of MATLAB. (See Section 6–3.)
