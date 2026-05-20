A–5–14. Obtain the response of the system shown in Figure 5–62 when the input r(t) is given by

$$r (t) = \frac {1}{2} t ^ {2}$$

[The input r(t) is the unit-acceleration input.]

![](image/45a830c194ad1275d02f13cc55955dbd6595d62deca8f92839038095b6bfcb06.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["2/(s(s+1))"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

Figure 5–62

Control system.

Solution. The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {2}{s ^ {2} + s + 2}$$

MATLAB Program 5–24 produces the unit-acceleration response.The resulting response, together with the unit-acceleration input, is shown in Figure 5–63.

MATLAB Program 5–24   
```matlab
num = [2];
den = [1 1 2];
t = 0:0.2:10;
r = 0.5*t.^2;
y = lsim(num,den,r,t);
plot(t,r,'-',t,y,'o',t,y,'-')
grid
title('Unit-Acceleration Response')
xlabel('t Sec')
ylabel('Input and Output')
text(2.1,27.5,'Unit-Acceleration Input')
text(7.2,7.5,'Output') 
```

![](image/c73f2d79d094c795a35596daaf05444a126ed3b9e22d66278a6c75a49b08402b.jpg)

<details>
<summary>line</summary>

| t Sec | Unit-Acceleration Input | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | ~1 | ~1 |
| 2 | ~3 | ~3 |
| 3 | ~6 | ~6 |
| 4 | ~10 | ~10 |
| 5 | ~15 | ~15 |
| 6 | ~20 | ~20 |
| 7 | ~25 | ~25 |
| 8 | ~30 | ~30 |
| 9 | ~35 | ~35 |
| 10 | ~45 | ~45 |
</details>

Figure 5–63 Response to unitacceleration input.

A–5–15. Consider the system defined by

$$\frac {C (s)}{R (s)} = \frac {1}{s ^ {2} + 2 \zeta s + 1}$$

where z=0, 0.2, 0.4, 0.6, 0.8, and 1.0. Write a MATLAB program using a “for loop” to obtain the two-dimensional and three-dimensional plots of the system output. The input is the unit-step function.

Solution. MATLAB Program 5–25 is a possible program to obtain two-dimensional and threedimensional plots. Figure 5–64(a) is the two-dimensional plot of the unit-step response curves for various values of z. Figure 5–64(b) is the three-dimensional plot obtained by use of the command “mesh(y)” and Figure 5–64(c) is obtained by use of the command “mesh(y¿)”. (These two three-dimensional plots are basically the same.The only difference is that x axis and y axis are interchanged.)
