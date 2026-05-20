| t Sec | Compensated System (Method 1) | Uncompensated System |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.8 | 0.6 |
| 1.0 | 1.6 | 1.2 |
| 1.5 | 1.4 | 1.0 |
| 2.0 | 1.2 | 0.6 |
| 2.5 | 1.0 | 0.9 |
| 3.0 | 1.2 | 1.2 |
| 3.5 | 1.0 | 1.0 |
| 4.0 | 0.9 | 0.8 |
| 4.5 | 1.0 | 1.0 |
| 5.0 | 1.0 | 1.1 |
</details>

Figure 6–45   
Unit-step response curves of designed systems and original uncompensated system.

$$\mathrm{num1} = [ 1 2. 2 8 7 2 3. 8 7 6 ]\mathrm{den} 1 = [ 1 \quad 5. 6 4 6 \quad 1 6. 9 3 3 \quad 2 3. 8 7 6 \quad 0 ]\mathrm{num2} = [ 9 ]\mathrm{den2} = [ 1 \quad 3 \quad 9 \quad 0 ]$$

The resulting unit-ramp response curves are shown in Figure 6–46.

MATLAB Program 6–10   
```matlab
% ***** Unit-Ramp Responses of Compensated Systems *****
num1 = [12.287 23.876];
den1 = [1 5.646 16.933 23.876 0];
num2 = [9];
den2 = [1 3 9 0];
t = 0:0.05:5;
c1 = step(num1, den1, t);
c2 = step(num2, den2, t);
plot(t, c1, '-', t, c2, '.', t, t, '-'')
grid
title('Unit-Ramp Responses of Compensated Systems')
xlabel('t Sec')
ylabel('Unit-Ramp Input and Outputs c1 and c2')
text(2.55, 3.8, 'Input')
text(0.55, 2.8, 'Compensated System (Method 1)')
text(2.35, 1.75, 'Compensated System (Method 2)') 
```

Figure 6–46 Unit-ramp response curves of designed systems.   
![](image/f90d70a73a75b59d88dfc9822bd41c04511072e0ee4be85edd2ae95f8810a5dc.jpg)

<details>
<summary>line</summary>

| t Sec | Input | Compensated System (Method 1) | Compensated System (Method 2) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0.5 | ~0.5 | ~0.3 | ~0.2 |
| 1 | ~1 | ~0.8 | ~0.6 |
| 1.5 | ~1.5 | ~1.3 | ~1.0 |
| 2 | ~2 | ~1.8 | ~1.4 |
| 2.5 | ~2.5 | ~2.3 | ~1.8 |
| 3 | ~3 | ~2.8 | ~2.2 |
| 3.5 | ~3.5 | ~3.3 | ~2.6 |
| 4 | ~4 | ~3.8 | ~3.0 |
| 4.5 | ~4.5 | ~4.3 | ~3.4 |
| 5 | ~5 | ~4.8 | ~3.8 |
</details>
