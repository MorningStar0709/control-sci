MATLAB Program 5–7 yields the rise time, peak time, maximum overshoot, and settling time. A unit-step response curve for this system is given in Figure 5–23 to verify the results obtained with MATLAB Program 5–7. (Note that this program can also be applied to higher-order systems. See Problem A–5–10.)

MATLAB Program 5–7   
```matlab
% ---- This is a MATLAB program to find the rise time, peak time,
% maximum overshoot, and settling time of the second-order system
% and higher-order system ----
% ---- In this example, we assume zeta = 0.6 and wn = 5 ----
num = [25];
den = [1 6 25];
t = 0:0.005:5;
[y,x,t] = step(num,den,t);
r = 1; while y(r) < 1.0001; r = r + 1; end;
rise_time = (r - 1)*0.005
rise_time =
    0.5550
[ymax,tp] = max(y);
peak_time = (tp - 1)*0.005
peak_time =
    0.7850
max_overshoot = ymax-1
max_overshoot =
    0.0948
s = 1001; while y(s) > 0.98 & y(s) < 1.02; s = s - 1; end;
settling_time = (s - 1)*0.005
settling_time =
    1.1850 
```

![](image/b62c51d46620108b5d2a2789d22109f7b8618114675477ad3abc3e0d31e21a2a.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 1.1 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

Figure 5–23 Unit-step response curve.

Impulse Response. The unit-impulse response of a control system may be obtained by using any of the impulse commands such as

$$\text { impulse(num,den) }\operatorname{impulse} (A, B, C, D)[ y, x, t ] = \text { impulse } (\text { num }, \text { den })[ y, x, t ] = \text { impulse } (\text { num }, \text { den }, t) \tag {5-41}[ y, x, t ] = \text { impulse } (A, B, C, D)[ \mathrm{y}, \mathrm{x}, \mathrm{t} ] = \text { impulse } (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{iu}) \tag {5-42}[ \mathrm{y}, \mathrm{x}, \mathrm{t} ] = \text { impulse } (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{iu}, \mathrm{t}) \tag {5-43}$$

The command impulse(num,den) plots the unit-impulse response on the screen. The command impulse(A,B,C,D) produces a series of unit-impulse-response plots, one for each input and output combination of the system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

Note that in Equations (5–42) and (5–43) the scalar iu is an index into the inputs of the system and specifies which input to be used for the impulse response.
