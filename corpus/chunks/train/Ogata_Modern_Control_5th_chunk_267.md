A–5–16. Consider the system subjected to the initial condition as given below.

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 0 & - 1 7 & - 8 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right], \qquad \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \\ x _ {3} (0) \end{array} \right] = \left[ \begin{array}{c} 2 \\ 1 \\ 0. 5 \end{array} \right]

y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

(There is no input or forcing function in this system.) Obtain the response y(t) versus t to the given initial condition by use of Equations (5–58) and (5–60).

Solution. A possible MATLAB program based on Equations (5–58) and (5–60) is given by MAT-LAB program 5–26. The response curve obtained here is shown in Figure 5–65. (Notice that this problem was solved by use of the command “initial” in Example 5–16.The response curve obtained here is exactly the same as that shown in Figure 5–34.)

MATLAB Program 5–26   
```matlab
t = 0:0.05:10;
A = [0 1 0;0 0 1;-10 -17 -8];
B = [2;1;0.5];
C=[1 0 0];
[y,x,t] = step(A,B,C*A,C*B,1,t);
plot(t,y)
grid;
title('Response to Initial Condition')
xlabel('t (sec)')
ylabel('Output y') 
```

![](image/f9da1de06b449684daa997a28909142ad0e23d9ded1405993865c07c0a886977.jpg)

<details>
<summary>line</summary>

| t (sec) | Output y |
| --- | --- |
| 0 | 2.0 |
| 1 | 1.8 |
| 2 | 1.0 |
| 3 | 0.4 |
| 4 | 0.1 |
| 5 | 0.05 |
| 6 | 0.02 |
| 7 | 0.01 |
| 8 | 0.005 |
| 9 | 0.002 |
| 10 | 0.001 |
</details>

Figure 5–65 Response y(t) to the given initial condition.

A–5–17. Consider the following characteristic equation:

$$s ^ {4} + K s ^ {3} + s ^ {2} + s + 1 = 0$$

Determine the range of K for stability.

Solution. The Routh array of coefficients is

$$
\begin{array}{l} \begin{array}{c c c c c} s ^ {4} & & 1 & & 1 & 1 \\ s ^ {3} & & K & & 1 & 0 \end{array} \\ s ^ {2} \quad \frac {K - 1}{K} \quad 1 \\ s ^ {1} \quad 1 - \frac {K ^ {2}}{K - 1} \\ s ^ {0} \quad 1 \\ \end{array}
$$

For stability, we require that

$$K > 0\frac {K - 1}{K} > 01 - \frac {K ^ {2}}{K - 1} > 0$$

From the first and second conditions, K must be greater than 1. For $K > 1$ , notice that the term $1 - \left[ K ^ { 2 } / ( K - 1 ) \right]$ is always negative, since

$$\frac {K - 1 - K ^ {2}}{K - 1} = \frac {- 1 + K (1 - K)}{K - 1} < 0$$
