MATLAB Program 5–12   
```matlab
% ---- Ramp Response ----
num = [2 1];
den = [1 1 1];
t = 0:0.1:10;
r = t;
y = lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid
title('Unit-Ramp Response Obtained by Use of Command "lsim")'
xlabel('t Sec')
ylabel('Unit-Ramp Input and System Output')
text(6.3,4.6,'Unit-Ramp Input')
text(4.75,9.0,'Output') 
```

Unit-Ramp Response Obtained by use of Command “Isim”   
![](image/276a21ee3f0938423a9aa78f8c51a4a338b103501c7435616c9ea82448d96d57.jpg)

<details>
<summary>line</summary>

| t Sec | Unit-Ramp Input | Unit-Ramp Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | 10 | 10 |
</details>

Figure 5–28

Unit-ramp response.

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0. 5 \\ - 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u \\ y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \\ \end{array}
$$

Using MATLAB, obtain the response curves y(t) when the input u is given by

1. u=unit-step input   
2. u=e–t

Assume that the initial state is x(0)=0.

A possible MATLAB program to produce the responses of this system to the unit-step input Cu=1(t)D and the exponential input Cu=e–tD is shown in MATLAB Program 5–13. The resulting response curves are shown in Figures 5–29(a) and (b), respectively.

MATLAB Program 5–13   
t = 0:0.1:12;
A = [-1 0.5;-1 0];
B = [0;1];
C = [1 0];
D = [0];

% For the unit-step input u = 1(t), use the command "y = step(A,B,C,D,1,t)". 
y = step(A,B,C,D,1,t);
plot(t,y)
grid
title('Unit-Step Response')
xlabel('t Sec')
ylabel('Output')

% For the response to exponential input u = exp(-t), use the command
% "z = lsim(A,B,C,D,u,t)". 
u = exp(-t);
z = lsim(A,B,C,D,u,t);
plot(t,u,'-',t,z,'o')
grid
title('Response to Exponential Input u = exp(-t)')
xlabel('t Sec')
ylabel('Exponential Input and System Output')
text(2.3,0.49,'Exponential input')
text(6.4,0.28,'Output')

![](image/a14d7c8eed9258d003c4a4ac5be817c4b3a3963d49d60315467c753b0595e32e.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0 | 0.0 |
| 2 | 0.4 |
| 4 | 0.9 |
| 6 | 1.05 |
| 8 | 1.02 |
| 10 | 1.01 |
| 12 | 1.0 |
</details>
