We shall assume that the open-loop transfer function $G ( s ) H ( s )$ is representable as a ratio of polynomials in s. For a physically realizable system, the degree of the denominator polynomial of the closed-loop transfer function must be greater than or equal to that of the numerator polynomial.This means that the limit of $G ( s ) H ( s )$ as s approaches infinity is zero or a constant for any physically realizable system.

Preliminary Study. The characteristic equation of the system shown in Figure 7–44 is

$$F (s) = 1 + G (s) H (s) = 0$$

We shall show that, for a given continuous closed path in the s plane that does not go through any singular points, there corresponds a closed curve in the $F ( s )$ plane. The number and direction of encirclements of the origin of the $F ( s )$ plane by the closed curve play a particularly important role in what follows, for later we shall correlate the number and direction of encirclements with the stability of the system.

Consider, for example, the following open-loop transfer function:

$$G (s) H (s) = \frac {2}{s - 1}$$

The characteristic equation is

$$
\begin{array}{l} F (s) = 1 + G (s) H (s) \\ = 1 + \frac {2}{s - 1} = \frac {s + 1}{s - 1} = 0 \tag {7-15} \\ \end{array}
$$

![](image/b2b4c0b13cc19d93b4762fd420cf694df474775cf6196cf32e9bee2f38134c48.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -1 | -j1 |
| 1 | 0 |
</details>

(a)

![](image/44e16e37db7c8c73f55552c225107d0090504bc9c8b6b15d65611ccdbc959f8c.jpg)

<details>
<summary>text_image</summary>

Im
F(s) Plane
ω = -1
ω = -2
ω = 0
σ = -2
σ = 0
σ = -1
σ = 1
Re
-2
-1
0
1
2
3
4
Im
ω = 1
ω = 2
ω = 2
-3
-2
-1
-3
-2
-1
0
1
2
3
</details>

(b)   
Figure 7–45 Conformal mapping of the s-plane grids into the $F ( s )$ plane, where

$$F (s) = (s + 1) / (s - 1).$$

The function $F ( s )$ is analytic# everywhere in the s plane except at its singular points. For each point of analyticity in the s plane, there corresponds a point in the $F ( s )$ plane. For example, if $s = 2 + j 1$ , then $F ( s )$ becomes

$$F (2 + j 1) = \frac {2 + j 1 + 1}{2 + j 1 - 1} = 2 - j 1$$

Thus, point $s = 2 + j 1$ in the s plane maps into point $2  j 1$ in the $F ( s )$ plane.

Thus, as stated previously, for a given continuous closed path in the s plane, which does not go through any singular points, there corresponds a closed curve in the $F ( s )$ plane.
