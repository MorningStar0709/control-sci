# 5.5.3 The Nyquist Contour

The Nyquist criterion is an application of the principle of the argument to the following problem: find the number of RHP zeros of $1 + L(s)$ .

![](image/9b60cfc97d232f698ca0d3cd2e6dbffae7658b0058f227fef32f13ce626d1bdf.jpg)

<details>
<summary>text_image</summary>

D
R
</details>

Figure 5.14 The Nyquist contour

Figure 5.14 shows the Nyquist contour D. The semicircle has a radius R tending to infinity, so D encompasses the whole RHP. If Z is the (unknown) number of RHP zeros of $1 + L(s)$ , then

$$Z = N + P \tag {5.19}$$

according to Equation 5.18.

Now, $P$ is the number of RHP poles of $1 + L(s)$ . The poles of $1 + L(s)$ are also the poles of $L(s)$ ; the values of $s$ that make $L(s)$ "blow up" are also the ones that make $1 + L(s)$ "blow up." Therefore,

$$P = \text { number of poles of } L (s) \text { in the open RHP. }$$

It is assumed that $L(s)$ has no poles or zeros on the $j$ -axis, as the principle of the argument does not allow poles or zeros on $D$ .

To apply Equation 5.19, we need to know $N$ . The Nyquist contour $D$ is mapped through $1 + L(s)$ in a second complex plane. Figure 5.15 shows the mapping $C_L$ through $L(s)$ and $C_{L'}$ through $1 + L(s)$ : the second is just the first shifted to the right by 1. The number $N$ is the number of encirclements of the origin by $C_{L'}$ . From Figure 5.15, it is easy to see that $N$ is also the number of encirclements of the point $(-1,0)$ by $C_L$ .

To apply the Nyquist criterion, we map the Nyquist contour through $L(s)$ and count encirclements of the point $(-1, 0)$ by $C_{L}$ to obtain N. It is assumed that P, the number of RHP poles of $L(s)$ , is known, so Equation 5.19 can be applied. For stability, $Z = N + P = 0$ , so N, the net (algebraic) number of encirclements, must be -P. In particular, if $L(s)$ is stable (P = 0), N must be zero for closed-loop stability.

![](image/647fbb81b0f481183cafce657a5d4dbd7003f9b125fd406e6750316ed4f6d16a.jpg)

<details>
<summary>text_image</summary>

C_L
(-1, 0)
C_L'
</details>

Figure 5.15 Maps through the mappings $L(s)$ and $1 + L(s)$
