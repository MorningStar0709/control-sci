MATLAB Program 5–22   
% ---- Unit-Ramp Response ----
num = [1 10];
den = [1 6 9 10];
t = 0:0.1:10;
r = t;
y = lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid
title('Unit-Ramp Response by Use of Command "lsim")'
xlabel('t Sec')
ylabel('Output')
text(3.2,6.5,'Unit-Ramp Input')
text(6.0,3.1,'Output')

% ---- Response to Input r1 = exp(-0.5t). ----
num = [0 0 1 10];
den = [1 6 9 10];
t = 0:0.1:12;
r1 = exp(-0.5*t);
y1 = lsim(num,den,r1,t);
plot(t,r1,'-',t,y1,'o')
grid
title('Response to Input r1 = exp(-0.5t)')
xlabel('t Sec')
ylabel('Input and Output')
text(1.4,0.75,'Input r1 = exp(-0.5t)')
text(6.2,0.34,'Output')

Unit-Ramp Response by Use of Command “lsim”   
![](image/63e1d628bcfc2bb433846e04509fcd2934203d00306a296b934696bfa9d3edb5.jpg)

<details>
<summary>line</summary>

| t Sec | Unit-Ramp Input | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 0.5 |
| 2 | 2 | 1.5 |
| 3 | 3 | 2.5 |
| 4 | 4 | 3.5 |
| 5 | 5 | 4.5 |
| 6 | 6 | 5.5 |
| 7 | 7 | 6.5 |
| 8 | 8 | 7.5 |
| 9 | 9 | 8.5 |
| 10 | 10 | 9.5 |
</details>

![](image/302447256c20fffb04b821659d6d2942a3bf09e8ba29f48a4f0b771f79290268.jpg)

<details>
<summary>line</summary>

| t Sec | Input | Output |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 1 | 0.7 | 0.2 |
| 2 | 0.65 | 0.3 |
| 3 | 0.5 | 0.4 |
| 4 | 0.3 | 0.5 |
| 5 | 0.2 | 0.6 |
| 6 | 0.15 | 0.7 |
| 7 | 0.1 | 0.8 |
| 8 | 0.08 | 0.9 |
| 9 | 0.06 | 1.0 |
| 10 | 0.04 | 1.1 |
| 11 | 0.03 | 1.2 |
| 12 | 0.02 | 1.3 |
</details>

Figure 5–60

(a) Unit-ramp response curve;

(b) response to exponential input

r =e–0.5t. $r _ { 1 } = e ^ { - 0 . 5 t } .$

A–5–13. Obtain the response of the closed-loop system defined by

$$\frac {C (s)}{R (s)} = \frac {5}{s ^ {2} + s + 5}$$

when the input r(t) is given by

$$r (t) = 2 + t$$

[The input r(t) is a step input of magnitude 2 plus unit-ramp input.]

Solution. A possible MATLAB program is shown in MATLAB Program 5–23. The resulting response curve, together with a plot of the input function, is shown in Figure 5–61.

MATLAB Program 5–23   
```matlab
num = [5];
den = [1 1 5];
t = 0:0.05:10;
r = 2 + t;
c = lsim(num, den, r, t);
plot(t, r, '-', t, c, 'o')
grid
title('Response to Input r(t) = 2 + t')
xlabel('t Sec')
ylabel('Output c(t) and Input r(t) = 2 + t') 
```

![](image/8b375ef9f3157d40b7a407baa5ab3157fe284f9a0236acc538fcb27c8ffec6e5.jpg)

<details>
<summary>line</summary>

| t Sec | Output c(t) | Input r(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 3 | 3 |
| 2 | 4 | 4 |
| 3 | 4 | 4 |
| 4 | 6 | 6 |
| 5 | 7 | 7 |
| 6 | 8 | 8 |
| 7 | 9 | 9 |
| 8 | 10 | 10 |
| 9 | 11 | 11 |
| 10 | 12 | 12 |
</details>

Figure 5–61

Response to input

$$r (t) = 2 + t.$$
