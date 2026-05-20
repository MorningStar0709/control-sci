# Solution

It is not difficult to calculate $L(s)$ by straightforward numerical calculations, but more insight is generated if we use the vector representation of complex numbers. Recall (see, for instance, Bélanger [6]) that $s + a$ is a complex number represented by the vector drawn from point $a$ to point $s$ . The vectors $s_1 + 1$ and $s_2 + 1$ are shown in Figure 5.10.

![](image/393ddec2351468381a1898b06879abdf48f379683b3de6158c63156e41a7df65.jpg)

<details>
<summary>text_image</summary>

s5
-2
s4
x
-1
s1 + 1
s1
s2 + 1
s2
j
s3
</details>

Figure 5.10 Contour in the s-plane

Now, we know that

$$\left| \frac {1}{s + 1} \right| = (\text { length of vector } s + 1) ^ {- 1}\neq \frac {1}{s + 1} = - (\text { angle of vector } s + 1).$$

By inspection, we have

$$L (s _ {1}) = 1; \quad L (s _ {2}) = \frac {1}{\sqrt {2}} \neq 4 5 ^ {\circ}; \quad L (s _ {3}) = \frac {1}{\sqrt {2}} \neq 1 3 5 ^ {\circ}L (s _ {4}) = 1 \neq 1 8 0 ^ {\circ}; \quad L (s _ {5}) = \frac {1}{\sqrt {2}} \neq - 1 3 5 ^ {\circ}; \quad L (s _ {6}) = \frac {1}{\sqrt {2}} \neq - 4 5 ^ {\circ}.$$

Figure 5.11 shows the mapping $C_L$ . Note that the right-angle turns of $C_s$ also appear in $C_L$ ; that angle-preservation property is general to a conformal mapping. [A mapping through $L(s)$ is conformal at all points when $L$ is analytic and has a nonzero derivative.]

![](image/16f7501b526d2be24be40ad1da161bc5d54ac2b0fb448d4e18dc1be1c0678dc5.jpg)

<details>
<summary>contour</summary>

| Region | Label |
| --- | --- |
| L(s₁) |  |
| L(s₂) |  |
| L(s₃) |  |
| L(s₄) |  |
| L(s₅) |  |
| L(s₆) |  |
</details>

Figure 5.11 Map of s-plane contour in the $L(s)$ -plane

Example 5.10 Repeat Example 5.9 for $L(s) = 1 / (s + 3)$ .

Solution From Figure 5.12,

$$L (s _ {1}) = \frac {1}{3}; \quad L (s _ {2}) = \frac {1}{\sqrt {1 0}} \neq \tan^ {- 1} \frac {1}{3}; \quad L (s _ {3}) = \frac {1}{\sqrt {2}} \neq - 4 5 ^ {\circ}L \left(s _ {4}\right) = 1; \quad L \left(s _ {5}\right) = \frac {1}{\sqrt {2}} \neq - 4 5 ^ {\circ}; \quad L \left(s _ {6}\right) = \frac {1}{\sqrt {1 0}} \neq - \tan^ {- 1} \frac {1}{3}.$$

Figure 5.13 shows the contour $C_L$ .

![](image/4414a3349595c28c64a34fa33171a710a9bfa71246db075cca08b3ebf6ded17d.jpg)

<details>
<summary>text_image</summary>

s5
s6
j
-3
s4
s1
s3
s2 + 3
-j
</details>

Figure 5.12 Contour in the s-plane
