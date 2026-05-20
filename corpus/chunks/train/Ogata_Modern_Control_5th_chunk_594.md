```matlab
3.0000 1.0000 1.1469 2.7700
5.0000 0.8000 1.1485 2.2100
4.0000 0.9000 1.1497 2.3800
% Plot the response curve with the smallest overshoot shown in sortsolution table.
K = sortsolution(1,1), a = sortsolution(1,2)
K =
3.2000
a =
0.9000
num = [4*K 8*K*a 4*K*a^2];
den = [1 6 8+4*K 4+8*K*a 4*K*a^2];
num
num =
12.8000 23.0400 10.3680
den
den =
1.0000 6.0000 20.8000 27.0400 10.3680
y = step(num,den,t);
plot(t,y) % See Figure 8–24.
grid
title('Unit-Step Response')
xlabel('t sec')
ylabel('Output y(t)') 
```

Figure 8–24 Unit-step response curve of the system with K=3.2 and a=0.9.   
![](image/6f18a0b395a6a81a9b847c5836795baee38b7f7b9a9ce33cc817e05a4fcc39d0.jpg)

<details>
<summary>line</summary>

| t sec | Output y(t) |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.1 |
| 2 | 0.95 |
| 4 | 1.0 |
| 6 | 1.0 |
| 8 | 1.0 |
</details>

Consider the basic PID control system shown in Figure 8–25(a), where the system is subjected to disturbances and noises. Figure 8–25(b) is a modified block diagram of the same system. In the basic PID control system such as the one shown in Figure 8–25(b), if the reference input is a step function, then, because of the presence of the derivative term in the control action, the manipulated variable u(t) will involve an impulse function (delta function). In an actual PID controller, instead of the pure derivative term $T _ { d } s .$ , we employ

$$\frac {T _ {d} s}{1 + \gamma T _ {d} s}$$

where the value of g is somewhere around 0.1.Therefore, when the reference input is a step function, the manipulated variable u(t) will not involve an impulse function, but will involve a sharp pulse function. Such a phenomenon is called set-point kick.

PI-D Control. To avoid the set-point kick phenomenon, we may wish to operate the derivative action only in the feedback path so that differentiation occurs only on the feedback signal and not on the reference signal.The control scheme arranged in this way is called the PI-D control. Figure 8–26 shows a PI-D-controlled system.

From Figure 8–26, it can be seen that the manipulated signal U(s) is given by

$$U (s) = K _ {p} \left(1 + \frac {1}{T _ {i} s}\right) R (s) - K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) B (s)$$

![](image/0b85d3a9b15e4152bcd75c3da74b5fc734510601bad40cef8d42c11aa6672a25.jpg)

<details>
<summary>flowchart</summary>
