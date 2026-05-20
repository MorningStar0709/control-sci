# Example 2.9

Two sliding masses.

![](image/69a625708e6a0c1ce25517174ab9a1ba83e12ca2282a0af14f213750ed0c04b9.jpg)

<details>
<summary>text_image</summary>

XIN
K1
M1
X1
K2
M2
Xat
B1
B2
</details>

(Note that in this diagram, we used hatching between the mass and ground to indicate damping $( B _ { 1 } , B _ { 2 } )$ . This symbol is commonly used because it visually suggests sliding friction.

Find

$$G (s) = \frac {X _ {o u t} (s)}{X _ {i n} (s)}$$

Normalize the Denominator of the solution.

EOM:

$$
M _ {1}: \quad M _ {1} \dot {X} _ {1} + B _ {1} (X _ {1} - 0) + K _ {1} (X _ {1} - X _ {m}) + K _ {2} (X _ {1} - X _ {m}) = 0M _ {2}: \quad M _ {2} \dot {X} _ {\text { out }} + B _ {2} (\dot {X} _ {\text { out }} - 0) + K _ {2} (X _ {\text { out }} - X _ {1}) = 0\text { Laplace } + \text { Collect }
\begin{array}{l} M _ {1}: \quad X _ {1} (s) (M, s ^ {2} + B, s + k _ {1} + k _ {2}) + X _ {\mathrm{out}} (s) (- k _ {2}) + X _ {\mathrm{in}} (s) (- k _ {1}) = 0 \\ - M _ {2}: \quad X _ {\text { out }} (s) (M _ {2} s ^ {2} + B _ {2} s + K _ {2}) + X _ {1} (s) (- K _ {2}) = 0 \\ \begin{array}{r l}{\mathrm{Eliminate}}&{X _ {1} (s)}\\{\rightarrow}&{X _ {1} (s) = \frac {(M _ {2} s ^ {2} + B _ {2} s + K _ {2}) X _ {\mathrm{out}} (s)}{K _ {2}}}\end{array} \\ X _ {\mathrm{out}} \left(\frac {1}{k _ {2}}\right) \left[ \begin{array}{c} M _ {1} M _ {2} s ^ {4} + M _ {1} B _ {2} s ^ {3} + M _ {1} k _ {2} s ^ {2} + M _ {1} B _ {1} s ^ {3} + B _ {1} B _ {2} s ^ {2} + (k _ {1} + k _ {2}) M _ {2} s ^ {2} \\ + (k _ {1} + k _ {2}) B _ {2} s + (k _ {1} + k _ {2}) k _ {2} \end{array} \right] \\ \end{array}
+ X _ {\text { out }} (- k _ {2}) = K _ {1} X _ {\text { in }} (s)
\begin{array}{l} \frac {X _ {\mathrm{out}} (s)}{X _ {\mathrm{in}} (s)} = \frac {K _ {1} K _ {2}}{M _ {1} M _ {2} s ^ {4} + (M _ {1} B _ {2} + M _ {2} B _ {1}) s ^ {3} + (M _ {1} k _ {2} + B _ {1} B _ {2} + (k _ {1} + k _ {2}) M _ {2}) s ^ {2}} \\ + (B _ {1} k _ {2} + (k _ {1} + k _ {2}) B _ {2}) S + (k _ {1} + k _ {2}) k _ {2} - k _ {2} ^ {2} \\ \end{array}
= \frac {\frac {K _ {1} K _ {2}}{M _ {1} M _ {2}}}{S ^ {4} + \left(\frac {M _ {1} B _ {2} + M _ {2} B _ {1}}{M _ {1} M _ {2}}\right) S ^ {3} + \left(\frac {K _ {2}}{M _ {2}} + \frac {B _ {1} B _ {2}}{M _ {1} M _ {2}} + \frac {(C _ {1} + K _ {2})}{M _ {1}}\right) S ^ {2}}+ \left(\frac {B _ {1} k _ {2}}{m _ {1} m _ {2}} + \frac {(k _ {1} + k _ {2}) B _ {2}}{m _ {1} m _ {2}}\right) s + \frac {k _ {1} k _ {2}}{m _ {1} m _ {2}}
$$
