Notice that the system with k=0.4490 has a pair of dominant complex-conjugate closed-loop poles, while in the system with k=1.4130 the real closed-loop pole at $s = - 0 . 6 8 2 3$ is dominant, and the complex-conjugate closed-loop poles are not dominant. In this case, the response characteristic is primarily determined by the real closed-loop pole.

Let us compare the unit-step responses of both systems. MATLAB Program 6–14 may be used for plotting the unit-step response curves in one diagram. The resulting unit-step response curves $[ c _ { 1 } ( t )$ for $k = 0 . 4 4 9 0$ and $c _ { 2 } ( t )$ for $k = 1 . 4 1 3 0 ]$ are shown in Figure 6–63.

MATLAB Program 6–14   
% ---- Unit-step response ----
% ***** Enter numerators and denominators of systems with
% k = 0.4490 and k = 1.4130, respectively. *****
num1 = [20];
den1 = [1 5 12.98 20];
num2 = [20];
den2 = [1 5 32.26 20];
t = 0:0.1:10;
c1 = step(num1, den1, t);
c2 = step(num2, den2, t);
plot(t, c1, t, c2)
text(2.5, 1.12, 'k = 0.4490')
text(3.7, 0.85, 'k = 1.4130')
grid
title('Unit-step Responses of Two Systems')
xlabel('t Sec')
ylabel('Outputs c1 and c2')

Figure 6–63 Unit-step response curves for the system shown in Figure 6–61 when the damping ratio z of the dominant closedloop poles is set equal to 0.4. (Two possible values of k give the damping ratio z equal to 0.4.)   
![](image/df2f4c3b240f063fe8c8c4bc760d4a2ac3ffb4a2ed08f8a20a662ba9fce95f5e.jpg)

<details>
<summary>line</summary>

| t Sec | k = 0.4490 | k = 1.4130 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | ~1.1 | ~0.6 |
| 2 | ~1.15 | ~0.8 |
| 3 | ~0.95 | ~0.9 |
| 4 | ~1.0 | ~0.95 |
| 5 | ~1.0 | ~0.98 |
| 6 | ~1.0 | ~0.99 |
| 7 | ~1.0 | ~0.995 |
| 8 | ~1.0 | ~0.998 |
| 9 | ~1.0 | ~0.999 |
| 10 | ~1.0 | ~1.0 |
</details>

From Figure 6–63 we notice that the response of the system with $k = 0 . 4 4 9 0$ is oscillatory. (The effect of the closed-loop pole at $s = - 2 . 9 0 2 1$ on the unit-step response is small.) For the system with $k = 1 . 4 1 3 0$ , the oscillations due to the closed-loop poles at $s = - 2 . 1 5 8 9 \pm j 4 . 9 6 5 2$ damp out much faster than purely exponential response due to the closed-loop pole at $s = - 0 . 6 8 2 3$ .

The system with $k = 0 . 4 4 9 0$ (which exhibits a faster response with relatively small overshoot) has a much better response characteristic than the system with k=1.4130 (which exhibits a slow overdamped response). Therefore, we should choose $k = 0 . 4 4 9 0$ for the present system.
