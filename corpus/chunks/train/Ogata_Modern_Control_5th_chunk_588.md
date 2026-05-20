Therefore, the designed system satisfies all the requirements. Thus, the designed system is acceptable. (Note that there exist infinitely many systems that satisfy all the requirements. The present system is just one of them.)

Next, we shall obtain the unit-step response and the unit-ramp response of the designed system. The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {5 s ^ {2} + 2 1 s + 4}{s ^ {3} + 5 s ^ {2} + 2 2 s + 4}$$

Note that the closed-loop zeros are located at

$$s = - 4, \quad s = - 0. 2$$

The closed-loop poles are located at

$$s = - 2. 4 0 5 2 + j 3. 9 1 1 9s = - 2. 4 0 5 2 - j 3. 9 1 1 9s = - 0. 1 8 9 7$$

Notice that the complex-conjugate closed-loop poles have the damping ratio of 0.5237. MATLAB Program 8–5 produces the unit-step response and the unit-ramp response.

```matlab
MATLAB Program 8–5

%***** Unit-step response ****
num = [5 21 4];
den = [1 5 22 4];
t = 0:0.01:14;
c = step(num,den,t);
plot(t,c)
grid
title('Unit-Step Response of Compensated System')
xlabel('t (sec)')
ylabel('Output c(t)')
%***** Unit-ramp response ****
num1 = [5 21 4];
den1 = [1 5 22 4 0];
t = 0:0.02:20;
c = step(num1,den1,t);
plot(t,c,'-',t,t,'--')
title('Unit-Ramp Response of Compensated System')
xlabel('t (sec)')
ylabel('Unit-Ramp Input and Output c(t)')
text(10.8,8,'Compensated System') 
```

Unit-Step Response of Compensated System   
![](image/0da1318f713ccf6b71a7b44f8072f661d0708239a88a7cf959a156d01ceaa7f0.jpg)

<details>
<summary>line</summary>

| t (sec) | Output c(t) |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.25 |
| 2 | 0.9 |
| 4 | 0.98 |
| 6 | 0.99 |
| 8 | 0.995 |
| 10 | 0.998 |
| 12 | 0.999 |
| 14 | 1.0 |
</details>

Figure 8–17 Unit-step response curve.

The resulting unit-step response curve is shown in Figure 8–17 and the unitramp response curve in Figure 8–18. Notice that the closed-loop pole at s = 0.1897 and the zero at $s = - 0 . 2$ produce a long tail of small amplitude in the unit-step response.

For an additional example of design of a PID controller based on the frequencyresponse approach, see Problem A–8–7.

![](image/6e621ebebb05e7f1a57f077dd607ebe904f9cbfd463713095080473121c70d41.jpg)

<details>
<summary>line</summary>

| t (sec) | Unit-Ramp Input and Output c(t) |
| --- | --- |
| 0 | 0 |
| 4 | 4 |
| 8 | 8 |
| 12 | 12 |
| 16 | 16 |
| 20 | 20 |
</details>

Figure 8–18 Unit-ramp input and the output curve.
