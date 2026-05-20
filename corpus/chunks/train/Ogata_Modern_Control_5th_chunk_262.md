Using MATLAB, plot the unit-step response curve of this system. Using MATLAB, obtain the rise time, peak time, maximum overshoot, and settling time.

Solution. MATLAB Program 5–20 plots the unit-step response curve as well as giving the rise time, peak time, maximum overshoot, and settling time. The unit-step response curve is shown in Figure 5–58.

```matlab
MATLAB Program 5-20
% ---- This program is to plot the unit-step response curve, as well as to
% find the rise time, peak time, maximum overshoot, and settling time.
% In this program the rise time is calculated as the time required for the
% response to rise from 10% to 90% of its final value. ----
num = [6.3223 18 12.811];
den = [1 6 11.3223 18 12.811];
t = 0:0.02:20;
[y,x,t] = step(num,den,t);
plot(t,y)
grid
title('Unit-Step Response')
xlabel('t (sec)')
ylabel('Output y(t)')
r1 = 1; while y(r1) < 0.1, r1 = r1+1; end;
r2 = 1; while y(r2) < 0.9, r2 = r2+1; end;
rise_time = (r2-r1)*0.02
rise_time =
    0.5800
[ymax,tp] = max(y);
peak_time = (tp-1)*0.02
peak_time =
    1.6600
max_overshoot = ymax-1
max_overshoot =
    0.6182
s = 1001; while y(s) > 0.98 & y(s) < 1.02; s = s-1; end;
settling_time = (s-1)*0.02
settling_time =
    10.0200 
```

![](image/150f1a378d8cef8e50f05cd3bdd576abb9a11ae5b488f1bc22cf7385fdcb086d.jpg)

<details>
<summary>line</summary>

| t (sec) | Output y(t) |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.6 |
| 4 | 0.7 |
| 6 | 1.15 |
| 8 | 0.9 |
| 10 | 1.0 |
| 12 | 1.0 |
| 14 | 1.0 |
| 16 | 1.0 |
| 18 | 1.0 |
| 20 | 1.0 |
</details>

Figure 5–58 Unit-step response curve.
