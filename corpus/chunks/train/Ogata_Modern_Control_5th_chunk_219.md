```matlab
MATLAB Program 5-6
% ---- Two-dimensional plot and three-dimensional plot of unit-step
% response curves for the standard second-order system with wn = 1
% and zeta = 0, 0.2, 0.4, 0.6, 0.8, and 1. ----
t = 0:0.2:10;
zeta = [0 0.2 0.4 0.6 0.8 1];
for n = 1:6;
num = [1];
den = [1 2*zeta(n) 1];
[y(1:51,n),x,t] = step(num,den,t);
end
% To plot a two-dimensional diagram, enter the command plot(t,y).
plot(t,y)
grid
title('Plot of Unit-Step Response Curves with \omega_n = 1 and \zeta = 0, 0.2, 0.4, 0.6, 0.8, 1')
xlabel('t (sec)')
ylabel('Response')
text(4.1,1.86,'\zeta = 0')
text(3.5,1.5,'0.2')
text(3 .5,1.24,'0.4')
text(3.5,1.08,'0.6')
text(3.5,0.95,'0.8')
text(3.5,0.86,'1.0')
% To plot a three-dimensional diagram, enter the command mesh(t,zeta,y').
mesh(t,zeta,y')
title('Three-Dimensional Plot of Unit-Step Response Curves')
xlabel('t Sec')
ylabel('\zeta')
zlabel('Response') 
```

Plot of Unit-Step Response Curves with n = 1 and 
 = 0, 0.2, 0.4, 0.6, 0.8, 1   
![](image/e998a0f7bb535bba1aa05636ee5603f27798aec909b287d675fdda10d2516e1a.jpg)

<details>
<summary>line</summary>

| t (sec) | ζ = 0 | ζ = 0.2 | ζ = 0.4 | ζ = 0.6 | ζ = 0.8 | ζ = 1.0 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 1 | ~0.5 | ~0.4 | ~0.3 | ~0.2 | ~0.1 | ~0.05 |
| 2 | ~1.2 | ~1.0 | ~0.8 | ~0.6 | ~0.4 | ~0.2 |
| 3 | ~2.0 | ~1.5 | ~1.2 | ~1.0 | ~0.8 | ~0.6 |
| 4 | ~1.8 | ~1.4 | ~1.1 | ~1.0 | ~0.9 | ~0.8 |
| 5 | ~1.2 | ~1.1 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| 6 | ~0.7 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| 7 | ~1.5 | ~1.2 | ~1.1 | ~1.0 | ~1.0 | ~1.0 |
| 8 | ~2.0 | ~1.5 | ~1.2 | ~1.1 | ~1.0 | ~1.0 |
| 9 | ~2.0 | ~1.8 | ~1.3 | ~1.2 | ~1.1 | ~1.0 |
| 10 | ~1.8 | ~1.5 | ~1.2 | ~1.1 | ~1.0 | ~1.0 |
</details>

(a)

Three-Dimensional Plot of Unit-Step Response Curves   
![](image/1a9e35dcc843074a78aae815b58cf6371afd1b2aeba6d3298060cc583bfef870.jpg)

<details>
<summary>surface_3d</summary>

| t Sec | Response |
| --- | --- |
| 0 | 0 |
| 2 | 0.5 |
| 4 | 1.0 |
| 6 | 1.5 |
| 8 | 2.0 |
| 10 | 1.5 |
</details>

Figure 5–22   
(a) Two-dimensional plot of unit-step response curves for $\zeta = 0 , 0 . 2 , 0 . 4 , 0 . 6 , 0 . 8 ,$ and 1.0; (b) threedimensional plot of unit-step response curves.

Obtaining Rise Time, Peak Time, Maximum Overshoot, and Settling Time with MATLAB. MATLAB can conveniently be used to obtain the rise time, peak time, maximum overshoot, and settling time. Consider the system defined by

$$\frac {C (s)}{R (s)} = \frac {2 5}{s ^ {2} + 6 s + 2 5}$$
