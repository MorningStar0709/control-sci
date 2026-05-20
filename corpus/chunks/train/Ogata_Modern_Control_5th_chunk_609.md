Using this expression, the response $y ( t )$ to a unit-step disturbance input can be obtained as shown in Figure $8 { - } 3 5 ( \mathrm { b } )$ .

Figure $8 { - } 3 6 ( \mathrm { a } )$ shows the response of the system to the unit-step reference input when $a , b ,$ and c are chosen as

$$a = 3. 2, \qquad b = 2, \qquad c = 1 2$$

Figure 8–36(b) shows the response of this system when it is subjected to a unit-step disturbance input. Comparing Figures $8 { - } 3 5 ( \mathrm { a } )$ and Figure $8 { - } 3 6 ( \mathrm { a } )$ ), we find that they are about the same. However, comparing Figures 8–35(b) and $8 \mathrm { - } 3 6 ( \mathrm { b } )$ , we find the former to be a little bit better than the latter. Comparing the responses of systems with each set in the table, we conclude the first set of values $( a = 4 . 2 , b = 2 , c = 1 2 )$ to be one of the best. Therefore, as the solution to this problem, we choose

$$a = 4. 2, \quad b = 2, \quad c = 1 2$$

Design Step 2: Next, we determine $G _ { c 1 }$ . Since $Y ( s ) / R ( s )$ can be given by

$$
\begin{array}{l} \frac {Y (s)}{R (s)} = \frac {G _ {p} G _ {c 1}}{1 + G _ {p} G _ {c}} \\ = \frac {\frac {1 0}{s (s + 1)} G _ {c 1}}{1 + \frac {1 0}{s (s + 1)} \frac {1 . 9 4 s ^ {2} + 1 2 . 2 4 4 s + 2 5 . 9 6 8}{s}} \\ = \frac {1 0 s G _ {c 1}}{s ^ {3} + 2 0 . 4 s ^ {2} + 1 2 2 . 4 4 s + 2 5 9 . 6 8} \\ \end{array}
$$

![](image/f49ebad7183b997df17178e728ae8f626baae4ab3c7152358b8705e0b1a71a74.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.2 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
</details>

(a)

![](image/c85972797100d01186dbffbda9a2e866214ace7ebc1ed60fe882c79cb91fea8e.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0850 |
| 1.0 | 0.0250 |
| 1.5 | 0.0050 |
| 2.0 | 0.0010 |
| 2.5 | 0.0005 |
| 3.0 | 0.0002 |
| 3.5 | 0.0001 |
| 4.0 | 0.0000 |
</details>

(b)   
Figure 8–36

(a) Response to unit-step reference input

(a=3.2, b=2, c=12);

(b) response to unit-step disturbance input

(a=3.2, b=2, c=12).

our problem becomes that of designing $G _ { c 1 } ( s )$ to satisfy the requirements on the responses to the step, ramp, and acceleration inputs.
