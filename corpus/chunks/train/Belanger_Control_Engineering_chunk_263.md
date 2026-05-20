The contour $C_{L}$ in Figure 5.9 encircles the origin once, clockwise; that is defined as one positive encirclement. In contrast, the contour $C_{L}$ in Figure 5.13 encircles the origin once, counterclockwise; that is tallied as one negative encirclement.

In general, the principle of the argument relates the (algebraic) number of encirclements of the origin by $C_{L}$ to the number of poles and zeros of $L(s)$ within the contour $C_{s}$ . It is stated as follows:

Let $C_s$ be a closed contour in the $s$ -plane, and let $L(s)$ be a rational function of $s$ , analytic and nonzero on the contour $C_s$ and with finite numbers $P$ of poles and $Z$ of zeros within $C_s$ . Also, let $N$ be the number of positive encirclements of the origin of the $L(s)$ -plane by the contour $C_L$ . Then

$$N = Z - P. \tag {5.18}$$

In Example 5.9, $L(s)$ has one pole and no zeros within $C_s$ , so that $Z = 0$ and $P = 1$ . Therefore, $N = -1$ ; the origin is encircled once in the negative (counterclockwise) direction in the $L$ -plane. In Example 5.10, $Z = P = 0$ , so $N = 0$ ; the origin is not encircled.

![](image/760cdce9ccf86e5b10f8c795481f74a13174720562a66f383889a9e921bcf123.jpg)

<details>
<summary>line</summary>

| Label | Real | Imaginary |
| --- | --- | --- |
| L(s₁) | 0.3 | 0.0 |
| L(s₂) | 0.3 | 0.1 |
| L(s₃) | 0.5 | 0.5 |
| L(s₄) | 0.95 | 0.2 |
| L(s₅) | 0.5 | -0.5 |
| L(s₆) | 0.3 | -0.1 |
</details>

Figure 5.13 Map of s-plane contour in the $L(s)$ -plane

A heuristic explanation of the principle of the argument is gleaned from Examples 5.9 and 5.10. As s goes around $C_{s}$ , the angle of the complex number $1/(s+1)$ in Example 5.9 goes through all positive values from 0 to 360°, so $C_{L}$ describes a counterclockwise path around the origin. On the other hand, as s goes around $C_{s}$ , the angle of $1/(s+3)$ in Example 5.10 increases from zero, reaches a 45° maximum, goes back through zero to -45°, and finally ends at zero. The angle never “flips around,” because the pole at -3 is outside the contour.

If, in Example 5.9, $L(s)$ is changed to $s + 1$ , the diagram of Figure 5.10 does not change. In this case, however,

$$\neq (s + 1) = \text { angle of vector } (s + 1)$$

so that, for example, $\angle L(s_2) = -45^\circ$ (instead of $+45^\circ$ ). The result is that $C_L$ is traversed clockwise instead of counterclockwise; i.e., $N = 1$ .

We see that every pole of $L(s)$ inside $C_{s}$ generates one negative encirclement, while every zero inside $C_{s}$ produces one positive encirclement. The poles and zeros of $L(s)$ that lie outside $C_{s}$ produce no encirclements. The formula N = Z - P follows.
