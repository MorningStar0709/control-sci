Figure 7–137 (a) Polar plots of a lead network and a proportional-plusderivative controller; (b) polar plots of a lag network and a proportional-plusintegral controller.   
![](image/56d224dc85e47a42ccf5678fe04efac08151ec30ec948b6485707f7dfba160e2.jpg)

<details>
<summary>text_image</summary>

Im
PD controller
Lead network
ω = 0
ω = ∞
0 α 1 Re
</details>

(a)

![](image/9e476f4c8c2c40445f1a22f1a4c0e445ed84046f3012f7f2faa4b9b68f185aa2.jpg)

<details>
<summary>text_image</summary>

Im
1/β
0
ω = ∞
1
ω = 0
Re
PI controller
Lag network
</details>

(b)

Solution. The angle of $G _ { c } ( j \omega )$ is given by

$$
\begin{array}{l} \underline {{{G _ {c} (j \omega)}}} = \left\lfloor j \omega + \frac {1}{T _ {1}} + \right. \left\lfloor j \omega + \frac {1}{T _ {2}} - \right. \left\lfloor j \omega + \frac {\beta}{T _ {1}} - \right. \left\lfloor j \omega + \frac {1}{\beta T _ {2}} \right. \\ = \tan^ {- 1} \omega T _ {1} + \tan^ {- 1} \omega T _ {2} - \tan^ {- 1} \omega T _ {1} / \beta - \tan^ {- 1} \omega T _ {2} \beta \\ \end{array}
$$

At $\omega = \omega _ { 1 } = 1 / \sqrt { T _ { 1 } T _ { 2 } }$ we have,

$$\underline {{{G _ {c} (j \omega_ {1})}}} = \tan^ {- 1} \sqrt {\frac {T _ {1}}{T _ {2}}} + \tan^ {- 1} \sqrt {\frac {T _ {2}}{T _ {1}}} - \tan^ {- 1} \frac {1}{\beta} \sqrt {\frac {T _ {1}}{T _ {2}}} - \tan^ {- 1} \beta \sqrt {\frac {T _ {2}}{T _ {1}}}$$

Since

$$\tan \left(\tan^ {- 1} \sqrt {\frac {T _ {1}}{T _ {2}}} + \tan^ {- 1} \sqrt {\frac {T _ {2}}{T _ {1}}}\right) = \frac {\sqrt {\frac {T _ {1}}{T _ {2}}} + \sqrt {\frac {T _ {2}}{T _ {1}}}}{1 - \sqrt {\frac {T _ {1}}{T _ {2}}} \sqrt {\frac {T _ {2}}{T _ {1}}}} = \infty$$

or

$$\tan^ {- 1} \sqrt {\frac {T _ {1}}{T _ {2}}} + \tan^ {- 1} \sqrt {\frac {T _ {2}}{T _ {1}}} = 9 0 ^ {\circ}$$

and also

$$\tan^ {- 1} \frac {1}{\beta} \sqrt {\frac {T _ {1}}{T _ {2}}} + \tan^ {- 1} \beta \sqrt {\frac {T _ {2}}{T _ {1}}} = 9 0 ^ {\circ}$$

we have

$$\underline {{G _ {c} (j \omega_ {1})}} = 0 ^ {\circ}$$

Thus, the angle of $G _ { c } \big ( j \omega _ { 1 } \big )$ becomes $0 ^ { \circ }$ at $\omega = \omega _ { 1 } = 1 / \sqrt { T _ { 1 } T _ { 2 } }$ .

A–7–22. Consider the control system shown in Figure 7–138. Determine the value of gain K such that the phase margin is $6 0 ^ { \circ }$ . What is the gain margin with this value of gain $K ?$

Solution. The open-loop transfer function is

$$
\begin{array}{l} G (s) = K \frac {s + 0 . 1}{s + 0 . 5} \frac {1 0}{s (s + 1)} \\ = \frac {K (1 0 s + 1)}{s ^ {3} + 1 . 5 s ^ {2} + 0 . 5 s} \\ \end{array}
$$
