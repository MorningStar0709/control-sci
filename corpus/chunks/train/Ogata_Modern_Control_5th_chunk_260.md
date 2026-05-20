$$
\begin{array}{l} x (4 T) = x (0) e ^ {- \zeta \omega_ {n} 4 T} = x (0) e ^ {- (0. 1) (1 0) (4) (0. 6 3 1 5)} \\ = 0. 0 5 e ^ {- 2. 5 2 6} = 0. 0 5 \times 0. 0 7 9 9 8 = 0. 0 0 4 \mathrm{m} \\ \end{array}
$$

A–5–8. Obtain both analytically and computationally the unit-step response of tbe following higher-order system:

$$\frac {C (s)}{R (s)} = \frac {3 s ^ {3} + 2 5 s ^ {2} + 7 2 s + 8 0}{s ^ {4} + 8 s ^ {3} + 4 0 s ^ {2} + 9 6 s + 8 0}$$

[Obtain the partial-fraction expansion of C(s) with MATLAB when $R ( s )$ is a unit-step function.]

Solution. MATLAB Program 5–18 yields the unit-step response curve shown in Figure 5–56. It also yields the partial-fraction expansion of C(s) as follows:

$$
\begin{array}{l} C (s) = \frac {3 s ^ {3} + 2 5 s ^ {2} + 7 2 s + 8 0}{s ^ {4} + 8 s ^ {3} + 4 0 s ^ {2} + 9 6 s + 8 0} \frac {1}{s} \\ = \frac {- 0 . 2 8 1 3 - j 0 . 1 7 1 9}{s + 2 - j 4} + \frac {- 0 . 2 8 1 3 + j 0 . 1 7 1 9}{s + 2 + j 4} \\ + \frac {- 0 . 4 3 7 5}{s + 2} + \frac {- 0 . 3 7 5}{(s + 2) ^ {2}} + \frac {1}{s} \\ = \frac {- 0 . 5 6 2 6 (s + 2)}{(s + 2) ^ {2} + 4 ^ {2}} + \frac {(0 . 3 4 3 8) \times 4}{(s + 2) ^ {2} + 4 ^ {2}} \\ - \frac {0 . 4 3 7 5}{s + 2} - \frac {0 . 3 7 5}{(s + 2) ^ {2}} + \frac {1}{s} \\ \end{array}
$$

MATLAB Program 5–18   
015 % ---- Unit-Step Response of C(s)/R(s) and Partial-Fraction Expansion of C(s) ----
015 num = [3 25 72 80];
015 den = [1 8 40 96 80];
015 step(num,den);
015 v = [0 3 0 1.2]; axis(v), grid;
015 % To obtain the partial-fraction expansion of C(s), enter commands
015 num1 = [3 25 72 80];
015 den1 = [1 8 40 96 80 0];
015 [r,p,k] = residue(num1,den1)
015 num1 = [25 72 80];
015 den1 = [1 8 40 96 80 0];
[ r,p,k] = residue(num1,den1 )
015 r =
-0.2813 - 0.1719i
-0.2813 + 0.1719i
-0.4375
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.3750
-0.
-2.0000 + 4.0000i
-2.0000 - 4.0000i
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.
-2.0000 + 4.0000i
-2.0000 - 4.0000i
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
-2.0000
k =

![](image/064a768a244b07a3dfc12c0cec4d12abfbeea293cc1da02abe12f52d3d980906.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 0.9 |
| 1.5 | 0.95 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>

Figure 5–56 Unit-step response curve.

Hence, the time response c(t) can be given by

$$c (t) = - 0. 5 6 2 6 e ^ {- 2 t} \cos 4 t + 0. 3 4 3 8 e ^ {- 2 t} \sin 4 t- 0. 4 3 7 5 e ^ {- 2 t} - 0. 3 7 5 t e ^ {- 2 t} + 1$$
