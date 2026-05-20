![](image/69d49fd45ca3c4ef24f701385ac88dad64f0492d7b8bda5198d9283d68e6c493.jpg)

<details>
<summary>text_image</summary>

Im
G(s) H(s) Plane
/G(s) H(s)
= ±180° (2k + 1)
0
Re
</details>

The root loci and constant-gain loci in the s plane are conformal mappings of the loci of $/ G ( s ) H ( s ) = \pm 1 8 0 ^ { \circ } ( 2 k + 1 )$ and of $| G ( s ) H ( s ) | =$ constant in the $G ( s ) H ( s )$ plane.

Since the constant-phase and constant-gain loci in the $G ( s ) H ( s )$ plane are orthogonal, the root loci and constant-gain loci in the s plane are orthogonal. Figure $6 { - } 2 9 ( \mathrm { a } )$ shows the root loci and constant-gain loci for the following system:

$$G (s) = \frac {K (s + 2)}{s ^ {2} + 2 s + 3}, \quad H (s) = 1$$

![](image/08363151264c4db82bdbe5c16a5664df9b7f70db19c2510faff9b99420d8551b.jpg)

<details>
<summary>text_image</summary>

jω
j6
K = 6
j4
A
K = 1
B
J2
K = 2
-6 -4 -2 0 2 4 6 σ
C
J2
J4
K = 1
-j6
</details>

(a)

![](image/52bf003659e7b844dcd528556fc4f5661fbcd268bdd30722bd16f05f751437f1.jpg)

<details>
<summary>other</summary>

| σ | jω | K |
| --- | --- | --- |
| -3 | j3 | 0.3 |
| -2 | j2 | 0.3 |
| -1 | j1 | 0.3 |
| 0 | j1 | 0.3 |
| 1 | j2 | 10 |
| 2 | j3 | 0.3 |
| 1 | -j1 | 0.3 |
| 0 | -j2 | 0.3 |
| -1 | -j3 | 0.3 |
</details>

(b)   
Figure 6–29 Plots of root loci and constant-gain loci. (a) System with $G ( s ) = K ( s + 2 ) / \bigl ( s ^ { 2 } + 2 s + 3 \bigr )$ , $H ( s ) = 1 ; ( \mathsf { b } )$ system with $G ( s ) = { K } / { [ { s ( s + 1 ) ( s + 2 ) } ] } , \dot { H ( s ) } = 1 $ .

Notice that since the pole–zero configuration is symmetrical about the real axis, the constant-gain loci are also symmetrical about the real axis.

Figure 6–29(b) shows the root loci and constant-gain loci for the system:

$$G (s) = \frac {K}{s (s + 1) (s + 2)}, \quad H (s) = 1$$

Notice that since the configuration of the poles in the s plane is symmetrical about the real axis and the line parallel to the imaginary axis passing through point (s=–1, $\omega = 0 )$ , the constant-gain loci are symmetrical about the v=0 line (real axis) and the s=–1 line.

From Figures 6–29(a) and (b), notice that every point in the s plane has the corresponding K value. If we use a command rlocfind (presented next), MATLAB will give the K value of the specified point as well as the nearest closed-loop poles corresponding to this K value.
