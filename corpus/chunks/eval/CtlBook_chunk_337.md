# Example 9.15 cont.

The root locus is now:

Root locus plot for ECE 447 Example   
![](image/32d2f9ebb279a3a376626fcbc7b7d2fca2fdcdaf77a6ca9b166895cb9d27cb15.jpg)

<details>
<summary>line</summary>

| Real | Imaginary |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 1.5 |
| 2.0 | 2.0 |
| 2.5 | 2.5 |
| 3.0 | 3.0 |
| 3.5 | 3.5 |
| 4.0 | 4.0 |
| 4.5 | 4.5 |
| 5.0 | 5.0 |
| 5.5 | 5.5 |
| 6.0 | 6.0 |
| 6.5 | 6.5 |
| 7.0 | 7.0 |
| 7.5 | 7.5 |
| 8.0 | 8.0 |
| 8.5 | 8.5 |
| 9.0 | 9.0 |
| 9.5 | 9.5 |
| 10.0 | 10.0 |
</details>

which allows the CC poles starting from $s = - 1 \pm 1 . 5 j$ to move into the target performance zone. Using the mouse to click on the part of the RL indicated gives $K = K _ { D } = 5 . 7 7 .$ .

$$K _ {P} = - z K _ {D} = 0. 1 K _ {D} = 0. 5 7 7K _ {P} = 0. 5 7 7, K _ {I} = 0. 0, K _ {D} = 5. 7 7$$

You might notice that the pole at the origin moves only slightly and arrives at the very close PD controller zero we placed at σ = −0.1. This pole does not lie in the performance region. Why doesn't that matter? One way to look at this is that the pole and zero being very close to each other cancel each other out in the closed loop response (imagine what a close pole and zero do to the Bode plot!). This exposes a limitation of the s-plane region approach to control design, which is that the regions are only truly valid with a pure second order system with two poles and no zeros. For all other systems the regions are really only approximate.

At this point we have reached a good starting point for computer optimization which will NOT make simplifying assumptions about the system dynamics or performance regions.
