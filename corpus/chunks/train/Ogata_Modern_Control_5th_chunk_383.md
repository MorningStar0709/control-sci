The lead portion must satisfy the following conditions:

$$\left| 1 2 8 \left(\frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\beta}{T _ {1}}}\right) G (s _ {1}) \right| _ {s _ {1} = - 2 + j 2 \sqrt {3}} = 1$$

and

$$
\left| \begin{array}{l} s _ {1} + \frac {1}{T _ {1}} \\ \hline s _ {1} + \frac {\beta}{T _ {1}} \end{array} \right| _ {s _ {1} = - 2 + j 2 \sqrt {3}} = 6 0 ^ {\circ}
$$

The first condition can be simplified as

$$\left| \frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\beta}{T _ {1}}} \right| _ {s _ {1} = - 2 + j 2 \sqrt {3}} = \frac {1}{1 3 . 3 3 3 3}$$

By using the same approach as used in Section 6–8, the zero $\left( s = 1 / T _ { 1 } \right)$ and pole $\left( s = \beta / T _ { 1 } \right)$ can be determined as follows:

$$\frac {1}{T _ {1}} = 3. 7 0, \quad \frac {\beta}{T _ {1}} = 5 3. 3 5$$

See Figure 6–87. The value of $\beta$ is thus determined as

$$\beta = 1 4. 4 1 9$$

For the lag portion of the compensator, we may choose

$$\frac {1}{\beta T _ {2}} = 0. 0 1$$

Figure 6–87

Graphical determination of the zero and pole of the lead portion of the compensator.

![](image/9ba4d42c39d664a44a64e66943d69a580e1508ec0e7d5c7e39f1d7f3b2a18196.jpg)

<details>
<summary>text_image</summary>

13.3333x
-53.35
-3.70
jω
s₁
60°
x
0
σ
</details>

Then

$$\frac {1}{T _ {2}} = 0. 1 4 4 2$$

Noting that

$$\left| \frac {s _ {1} + 0 . 1 4 4 2}{s _ {1} + 0 . 0 1} \right| _ {s _ {1} = - 2 + j 2 \sqrt {3}} = 0. 9 8 3 7\left. \frac {s _ {1} + 0 . 1 4 4 2}{s _ {1} + 0 . 0 1} \right| _ {s _ {1} = - 2 + j 2 \sqrt {3}} = - 1. 6 9 7 ^ {\circ}$$

the angle contribution of the lag portion is $- 1 . 6 9 7 ^ { \circ }$ and the magnitude contribution is 0.9837.This means that the dominant closed-loop poles lie close to the desired location $s = - 2 \pm j 2 { \sqrt { 3 } }$ . Thus the compensator designed,

$$G _ {c} (s) = 1 2 8 \left(\frac {s + 3 . 7 0}{s + 5 3 . 3 5}\right) \left(\frac {s + 0 . 1 4 4 2}{s + 0 . 0 1}\right)$$

is acceptable. The feedforward transfer function of the compensated system becomes

$$G _ {c} (s) G (s) = \frac {1 2 8 0 (s + 3 . 7) (s + 0 . 1 4 4 2)}{s (s + 5 3 . 3 5) (s + 0 . 0 1) (s + 2) (s + 8)}$$

A root-locus plot of the compensated system is shown in Figure 6–88(a). An enlarged root-locus plot near the origin is shown in Figure 6–88(b).

Root-Locus Plot of Compensated System   
![](image/6369dda285186fb1dcc1098767ab406bd62f49ecfdf2153a1c63c4cb2261af9e.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -50 | 0 |
| 0 | 0 |
| 0 | 0 |
</details>

(a)
