Note that the Nyquist plot for the positive-feedback case is a mirror image about the imaginary axis of the Nyquist plot for the negative-feedback case.This may be seen from Figure 7–131, which was obtained by use of MATLAB Program 7–21. (Note that the positive-feedback case is unstable, but the negative-feedback case is stable.)

MATLAB Program 7–21   
```matlab
num1 = [1 4 6];
den1 = [1 5 4];
num2 = [-1 -4 -6];
den2 = [1 5 4];
nyquist(num1, den1);
hold on
nyquist(num2, den2);
v = [-2 2 -1 1];
axis(v);
grid
title('Nyquist Plots of G(s) and -G(s)')
text(1.0, 0.5, 'G(s)')
text(0.57, -0.48, 'Use this Nyquist')
text(0.57, -0.61, 'plot for negative')
text(0.57, -0.73, 'feedback system')
text(-1.3, 0.5, '-G(s)')
text(-1.7, -0.48, 'Use this Nyquist')
text(-1.7, -0.61, 'plot for positive')
text(-1.7, -0.73, 'feedback system') 
```

Figure 7–131 Nyquist plots for positive-feedback system and negativefeedback system.   
![](image/07ca1311ffdfa70f98d19d7b9bef4405666c80846068d55463e6d9aac27a6c07.jpg)

<details>
<summary>scatter</summary>

| System | Real Axis | Imag Axis |
| --- | --- | --- |
| Use this Nyquist plot for positive feedback system | -1.0 | 0.0 |
| Use this Nyquist plot for negative feedback system | 1.0 | 0.0 |
</details>

A–7–15. Consider the control system shown in Figure 7–60. (Refer to Example 7–19.) Using the inverse polar plot, determine the range of gain K for stability.

Solution. Since

$$G _ {2} (s) = \frac {1}{s ^ {3} + s ^ {2} + 1}$$

we have

$$G (s) = G _ {1} (s) G _ {2} (s) = \frac {K (s + 0 . 5)}{s ^ {3} + s ^ {2} + 1}$$

Hence, the inverse of the feedforward transfer function is

$$\frac {1}{G (s)} = \frac {s ^ {3} + s ^ {2} + 1}{K (s + 0 . 5)}$$

Notice that $1 / G ( s )$ has a pole at $s = - 0 . 5 .$ . It does not have any pole in the right-half s plane. Therefore, the Nyquist stability equation

$$Z = N + P$$

reduces to $Z = N$ since P=0. The reduced equation states that the number Z of the zeros of $1 + \left[ 1 / G ( s ) \right]$ D in the right-half s plane is equal to N, the number of clockwise encirclements of the $- 1 + j 0$ point. For stability, N must be equal to zero, or there should be no encirclement. Figure 7–132 shows the Nyquist plot or polar plot of $K / G ( j \omega )$ .

Notice that since
