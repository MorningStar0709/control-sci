# 6.2.4 Frequency Response and the Nichols Chart

Closed-loop frequency response specifications were discussed in Chapter 4. Constraints were placed on $|T(j\omega)|$ and/or $|S(j\omega)|$ , depending on the frequency. This can be related to the foregoing discussion in the following way. The presence of complex poles near the $j$ -axis (small $\zeta$ ) results in sharp, high peaks in both $|T(j\omega)|$ and $|S(j\omega)|$ . Figure 6.6 shows the magnitude Bode plot for the all-pole second-order system, for several values of $\zeta$ . As $\zeta \to 0$ , the peak tends to infinity.

The peak value of $|T(j\omega)|$ is denoted by $M_{p}$ . For the all-pole second-order system, it is given (see Problem 6.6) by

$$M _ {p} = 1 + e ^ {- \zeta \pi / \sqrt {1 - \zeta^ {2}}} \tag {6.18}$$

![](image/e8923fe72c8a508b2420885d8cc68ec903eb57bb0cbd0b80c14e31cf39e94d5c.jpg)

<details>
<summary>natural_image</summary>

Pure geometric lines forming a symmetrical V-shape with tick marks, intersected by two perpendicular axes (no text or symbols)
</details>

Figure 6.4 Illustration of the undesirable region (hatched) of the complex plane

![](image/0e1d8da42e60208d8c842e9640c49a0a9f8f1a2fcdcce29ff46dbfdba8ce5180.jpg)

<details>
<summary>line</summary>

| Time(s) | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.9 |
| 1.0 | 1.7 |
| 2.0 | 1.3 |
| 3.0 | 1.1 |
| 4.0 | 1.0 |
| 5.0 | 1.0 |
| 6.0 | 1.0 |
| 7.0 | 1.0 |
| 8.0 | 1.0 |
</details>

Figure 6.5 Step response

for $\zeta < 1 / \sqrt{2}$ . The frequency response magnitude has its maximum at $\omega = 0$ if $\zeta \geq 1 / \sqrt{2}$ .

For the 1-DOF system, frequency response specifications are often given in terms of $S(j\omega)$ and/or $T(j\omega)$ . Let us now explore the relationship between $L(j\omega)$ and

![](image/97cd38eb29653eeef3917d69d9735e264a987277417c8774200d89ec37005eca.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (db) for ζ = .1 | Magnitude (db) for ζ = .2155 | Magnitude (db) for ζ = .707 | Magnitude (db) for ζ = .9 |
| --- | --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~0 | ~0 |
| 1 | ~14 | ~8 | ~6 | ~4 |
| 10 | ~-40 | ~-30 | ~-25 | ~-20 |
</details>

Figure 6.6 Frequency response magnitude for Butterworth second-order transfer function

![](image/625323baaa4ad02395bd7e56baf1236e4b838e3acc23b65581ab700f6f2b5334.jpg)

<details>
<summary>text_image</summary>

I_m
-1
1 + L(j0)
L(j0)
R_e
</details>

Figure 6.7 Showing $L(j\omega)$ and $1 + L(j\omega)$
