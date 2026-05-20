![](image/033291a1b613f4e24fd1c224501076e874b5cddaaee61f427b165e31659fe08b.jpg)

<details>
<summary>text_image</summary>

A
P
φ/2
φ/2
-1/αT
-1/T
C
B
D
O
σ
jω
</details>

Figure 6–41 Determination of the pole and zero of a lead network.

Thus, if we need to force the root locus to go through the desired closed-loop pole, the lead compensator must contribute $\phi = 4 0 . 8 9 4 ^ { \circ }$ at this point. By following the foregoing design procedure, we can determine the zero and pole of the lead compensator.

Referring to Figure 6–42, if we bisect angle APO and take $4 0 . 8 9 4 ^ { \circ } / 2$ each side, then the locations of the zero and pole are found as follows:

$$\text { zero at } s = - 1. 9 4 3 2\text { pole at } s = - 4. 6 4 5 8$$

Thus, $G _ { c } ( s )$ can be given as

$$G _ {c} (s) = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}} = K _ {c} \frac {s + 1 . 9 4 3 2}{s + 4 . 6 4 5 8}$$

(For this compensator the value of a is $\alpha = 1 . 9 4 3 2 / 4 . 6 4 5 8 = 0 . 4 1 8 . )$

The value of $K _ { c }$ can be determined by use of the magnitude condition.

$$\left| K _ {c} \frac {s + 1 . 9 4 3 2}{s + 4 . 6 4 5 8} \frac {1 0}{s (s + 1)} \right| _ {s = - 1. 5 + j 2. 5 9 8 1} = 1$$

or

$$K _ {c} = \left| \frac {(s + 4 . 6 4 5 8) s (s + 1)}{1 0 (s + 1 . 9 4 3 2)} \right| _ {s = - 1. 5 + j 2. 5 9 8 1} = 1. 2 2 8 7$$

Hence, the lead compensator $G _ { c } ( s )$ just designed is given by

$$G _ {c} (s) = 1. 2 2 8 7 \frac {s + 1 . 9 4 3 2}{s + 4 . 6 4 5 8}$$

Then, the open-loop transfer function of the designed system becomes

$$G _ {c} (s) G (s) = 1. 2 2 8 7 \left(\frac {s + 1 . 9 4 3 2}{s + 4 . 6 4 5 8}\right) \frac {1 0}{s (s + 1)}$$

and the closed-loop transfer function becomes

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {1 2 . 2 8 7 (s + 1 . 9 4 3 2)}{s (s + 1) (s + 4 . 6 4 5 8) + 1 2 . 2 8 7 (s + 1 . 9 4 3 2)} \\ = \frac {1 2 . 2 8 7 s + 2 3 . 8 7 6}{s ^ {3} + 5 . 6 4 6 s ^ {2} + 1 6 . 9 3 3 s + 2 3 . 8 7 6} \\ \end{array}
$$

![](image/becd333cfefff31f611acaf54c8f8fbb5447ac5e2edaaf49dc0f93e10d035a24.jpg)  
Figure 6–42 Determination of the pole and zero of the lead compensator.

Figure 6–43 Root-locus plot of the designed system.   
![](image/3097c9e1308b2a53e24e7b33f6bd175bc0f8e45b133eacc8fcf293bab879e182.jpg)  
Figure 6–43 shows the root-locus plot for the designed system.

It is worthwhile to check the static velocity error constant $K _ { v }$ for the system just designed.

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s \left[ 1. 2 2 8 7 \frac {s + 1 . 9 4 3 2}{s + 4 . 6 4 5 8} \frac {1 0}{s (s + 1)} \right] \\ = 5. 1 3 9 \\ \end{array}
$$
