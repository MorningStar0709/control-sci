sortsolution = sortrows(solution,3) % Print solution table sorted by
% column 3 
```

(continues on next page)

```matlab
sortsolution =
2.0000 0.5000 0.9002
2.2000 0.5000 0.9114
2.4000 0.5000 0.9207
2.6000 0.5000 0.9283
2.8000 0.5000 0.9348
3.0000 0.5000 0.9402
2.0000 0.7000 0.9807
2.2000 0.7000 0.9837
2.4000 0.7000 0.9859
2.6000 0.7000 0.9877
2.8000 0.7000 1.0024
3.0000 0.7000 1.0177
2.0000 0.9000 1.0614
2.2000 0.9000 1.0772
2.4000 0.9000 1.0923

% Plot the response with the largest overshoot that is less than 10%
K = sortsolution(k,1)
K =
2.4000
a = sortsolution(k,2)
a =
    0.9000
gc = tf(K*[1 2*a a^2], [1 0]);
G = gc*g/(1 + gc*g);
step(G,t)
grid % See Figure 8–20

% If you wish to plot the response with the smallest overshoot that is
% greater than 0%, then enter the following values of 'K' and 'a'
K = sortsolution(11,1)
K =
    2.8000
a = sortsolution(11,2)
a =
    0.7000
gc = tf(K*[1 2*a a^2], [1 0]);
G = gc*g/(1 + gc*g);
step(G,t)
grid % See Figure 8–21 
```

Figure 8–20 Unit-step response of the system with K=2.4 and a=0.9. (The maximum overshoot is 9.23%.)   
![](image/5631b7b03fd28e14a85e4c06f6bca245f670af6e429afd0a00ddaea17c8e0bf5.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.6 |
| 1.0 | 1.0 |
| 1.5 | 1.1 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

To plot the unit-step response curve of the last set of the K and a values in the sorted table, we enter the commands

$$K = \text { sortsolution } (k, 1)a = \text { sortsolution } (k, 2)$$

and use the step command. (The resulting unit-step response curve is shown in Figure 8–20.) To plot the unit-step response curve with the smallest overshoot that is greater than 0% found in the sorted table, enter the commands

$$K = \text { sortsolution } (1 1, 1)a = \text { sortsolution } (1 1, 2)$$

and use the step command. (The resulting unit-step response curve is shown in Figure 8–21.)

Figure 8–21 Unit-step response of the system with K=2.8 and a=0.7. (The maximum overshoot is 0.24%.)   
![](image/d0fdcc902cacbfcea69dd23baf206beccc55dc1b787d925b4b623f6ff2cee8df.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.6 |
| 1.0 | 1.0 |
| 1.5 | 0.98 |
| 2.0 | 0.95 |
| 2.5 | 0.96 |
| 3.0 | 0.97 |
| 3.5 | 0.98 |
| 4.0 | 0.99 |
| 4.5 | 0.995 |
| 5.0 | 1.0 |
</details>
