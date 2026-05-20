| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.1 | -100 | 50 |
| 1 | -120 | 25 |
| 10 | -140 | 0 |
| 100 | -180 | -50 |
| 1000 | -200 | -100 |
</details>

From MATLAB Program 7–27 and Figure 7–148 it is clearly seen that the phase margin is approximately $5 0 ^ { \circ }$ and the gain margin is ± q dB. Since the static velocity error constant $K _ { v }$ is 20 $\sec ^ { - 1 }$ , all the specifications are met. Before we conclude this problem, we need to check the transient-response characteristics.

Unit-Step Response: We shall compare the unit-step response of the compensated system with that of the original uncompensated system.

The closed-loop transfer function of the original uncompensated system is

$$\frac {C (s)}{R (s)} = \frac {1 0}{s ^ {2} + s + 1 0}$$

The closed-loop transfer function of the compensated system is

$$\frac {C (s)}{R (s)} = \frac {9 5 . 2 3 8 s + 2 8 6 . 6 7 5 9}{s ^ {3} + 1 5 . 3 3 3 9 s ^ {2} + 1 1 0 . 5 7 1 9 s + 2 8 6 . 6 7 5 9}$$

MATLAB Program 7–28 produces the unit-step responses of the uncompensated and compensated systems. The resulting response curves are shown in Figure 7–149. Clearly, the compensated system exhibits a satisfactory response. Note that the closed-loop zero and poles are located as follows:

$$\text { Zero at } s = - 3. 0 1 0 1\text { Poles at } s = - 5. 2 8 8 0 \pm j 5. 6 8 2 4, \quad s = - 4. 7 5 7 9$$

Unit-Ramp Response: It is worthwhile to check the unit-ramp response of the compensated system. Since $\bar { K } _ { v } = 2 0 \sec ^ { - 1 }$ , the steady-state error following the unit-ramp input will be

$1 / K _ { v } = 0 . 0 5$ . The static velocity error constant of the uncompensated system is $1 0 \ \mathrm { s e c } ^ { - 1 }$ . Hence, the original uncompensated system will have twice as large a steady-state error in following the unit-ramp input.

MATLAB Program 7–28   
```matlab
%*****Unit-step responses*****
num1 = [10];
den1 = [1 1 10];
num2 = [95.238 286.6759];
den2 = [1 15.3339 110.5719 286.6759];
t = 0:0.01:6;
[c1,x1,t] = step(num1,den1,t);
[c2,x2,t] = step(num2,den2,t);
plot(t,c1,'.',t,c2,'-')
grid;
title('Unit-Step Responses of Uncompensated System and Compensated System')
xlabel('t Sec');
ylabel('Outputs')
text(1.70,1.45,'Uncompensated System')
text(1.1,0.5,'Compensated System') 
```

Unit-Step Responses of Uncompensated System and Compensated System   
![](image/8cb01e30749c5a6d0d5f5ed245f9c3064e55b187522f97c531e095d48195c60d.jpg)

<details>
<summary>line</summary>
