Note that the closed-loop poles with $\zeta = 0 . 4$ must lie on straight lines passing through the origin and making the angles with the negative real axis. In the present case, there are two;66.42° intersections of the root-locus branch in the upper half s plane and the straight line of angle 66.42°. Thus, two values of K will give the damping ratio z of the closed-loop poles equal to 0.4.At point P, the value of K is

$$K = \left| \frac {(s + j 2) (s - j 2) (s + 5)}{s} \right| _ {s = - 1. 0 4 9 0 + j 2. 4 0 6 5} = 8. 9 8 0 1$$

Hence

$$k = \frac {K}{2 0} = 0. 4 4 9 0 \quad \text { at point } P$$

![](image/65282c0514ee028f24afc56c7c2dc13a74a4f274dd065eb7bd31bc5e909879aa.jpg)

<details>
<summary>line</summary>

| Point | Value |
| --- | --- |
| Q | -2.1589 + j4.9652 |
| P | -1.0490 + j2.4065 |
| s | -2.9021 |
| 66.42° | (labeled point) |
</details>

Figure 6–62 Root-locus plot for the system shown in Figure 6–61.

At point Q, the value of K is

$$K = \left| \frac {(s + j 2) (s - j 2) (s + 5)}{s} \right| _ {s = - 2. 1 5 8 9 + j 4. 9 6 5 2} = 2 8. 2 6 0$$

Hence

$$k = \frac {K}{2 0} = 1. 4 1 3 0 \quad \text { at point } Q$$

Thus, we have two solutions for this problem. For k=0.4490, the three closed-loop poles are located at

$$s = - 1. 0 4 9 0 + j 2. 4 0 6 5, \quad s = - 1. 0 4 9 0 - j 2. 4 0 6 5, \quad s = - 2. 9 0 2 1$$

For k=1.4130, the three closed-loop poles are located at

$$s = - 2. 1 5 8 9 + j 4. 9 6 5 2, \quad s = - 2. 1 5 8 9 - j 4. 9 6 5 2, \quad s = - 0. 6 8 2 3$$

It is important to point out that the zero at the origin is the open-loop zero, but not the closed-loop zero. This is evident, because the original system shown in Figure 6–61 does not have a closed-loop zero, since

$$\frac {G (s)}{R (s)} = \frac {2 0}{s (s + 1) (s + 4) + 2 0 (1 + k s)}$$

The open-loop zero at $s = 0$ was introduced in the process of modifying the characteristic equation such that the adjustable variable $K = 2 0 k$ was to appear as a multiplying factor.

We have obtained two different values of k to satisfy the requirement that the damping ratio of the dominant closed-loop poles be equal to 0.4. The closed-loop transfer function with $k = 0 . 4 4 9 0$ is given by

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {2 0}{s ^ {3} + 5 s ^ {2} + 1 2 . 9 8 s + 2 0} \\ = \frac {2 0}{(s + 1 . 0 4 9 0 + j 2 . 4 0 6 5) (s + 1 . 0 4 9 0 - j 2 . 4 0 6 5) (s + 2 . 9 0 2 1)} \\ \end{array}
$$

The closed-loop transfer function with k=1.4130 is given by

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {2 0}{s ^ {3} + 5 s ^ {2} + 3 2 . 2 6 s + 2 0} \\ = \frac {2 0}{(s + 2 . 1 5 8 9 + j 4 . 9 6 5 2) (s + 2 . 1 5 8 9 - j 4 . 9 6 5 2) (s + 0 . 6 8 2 3)} \\ \end{array}
$$
