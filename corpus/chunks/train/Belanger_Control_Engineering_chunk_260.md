# 5.5.2 The Principle of the Argument

The roots of the closed-loop characteristic polynomial satisfy the characteristic equation

$$D _ {L} (s) + N _ {L} (s) = 0.$$

Suppose $s_0$ is such a root. Then

$$D _ {L} (s _ {0}) + N _ {L} (s _ {0}) = 0. \tag {5.16}$$

We claim that, if $N_{\dot{L}}$ and $D_{L}$ are coprime, $s_0$ also satisfies

$$1 + \frac {N _ {L} (s _ {0})}{D _ {L} (s _ {0})} = 1 + L (s _ {0}) = 0. \tag {5.17}$$

The progression from Equation 5.16 to Equation 5.17 is simple if $D_L(s_0) \neq 0$ ; we need only divide by $D_L(s_0)$ . To understand that $D_L(s_0)$ must be nonzero, note that, if it were zero, $N_L(s_0)$ would also have to be zero to satisfy Equation 5.16, and $s_0$ would then be a common root of $D_L$ and $N_L$ . That is excluded because $D_L$ and $N_L$ are coprime. Therefore, division by $D_L(s_0)$ is allowed, and Equation 5.17 is justified.

Henceforth in this section, we shall seek roots of $1 + L(s)$ rather than $N_{L}(s) + D_{L}(s)$ .

Figure 5.9 illustrates the concept of a mapping from one complex plane to another. A closed contour $C_s$ is defined in the $s$ -plane. For every point (e.g., $s_1, s_2, s_3$ ) on $C_s$ , a complex number $L(s)$ is calculated [e.g., $L(s_1), L(s_2), L(s_3)$ ] and plotted in a second complex plane, the $L$ -plane. The mapping of the points on $C_s$ defines a contour $C_L$ in the $L$ -plane. If $L(s)$ is a single-valued function of $s$ , $C_L$ must begin and end at $L(s_1)$ ; i.e., $C_L$ is also a closed contour.

The contour $C_s$ is traversed in the clockwise direction. As drawn in Figure 5.9, its image $C_L$ is also traversed in the clockwise direction, but that need not be the case; it is quite possible for $C_{L}$ to be traversed in the counterclockwise direction as $C_{s}$ is traversed clockwise.

![](image/dd36d916a707da1762443d9a1e9788d89012011c56c009cc76da6cffe1089307.jpg)

<details>
<summary>text_image</summary>

C_s
s_1
s_2
s_3
</details>

s-plane

![](image/4cef86a723815562b90fca91c6ef5c2f10de48250f454b6a796f5bcde4ff1386.jpg)

<details>
<summary>text_image</summary>

L(s₃)
C₂
L(s₁)
L(s₂)
</details>

$L(s)$ -plane   
Figure 5.9 Mapping a contour from the s-plane to the $L(s)$ -plane
