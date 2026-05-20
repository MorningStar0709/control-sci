%*****Unit-step response*****
num = [1];
den = [0.5 1.5 1 1];
numc = [50 5];
denc = [50 150.5 101.5 51 5];
t = 0:0.1:40;
[c1,x1,t] = step(num,den,t);
[c2,x2,t] = step(numc,denc,t);
plot(t,c1,'.',t,c2,'-')
grid
title('Unit-Step Responses of Compensated and Uncompensated Systems')
xlabel('t Sec')
ylabel('Outputs')
text(12.7,1.27,'Compensated system')
text(12.2,0.7,'Uncompensated system')

%*****Unit-ramp response*****
num1 = [1];
den1 = [0.5 1.5 1 1 0];
num1c = [50 5];
den1c = [50 150.5 101.5 51 5 0];
t = 0:0.1:20;
[y1,z1,t] = step(num1,den1,t);
[y2,z2,t] = step(num1c,den1c,t);
plot(t,y1,'.',t,y2,'-',t,t,'--');
grid
title('Unit-Ramp Responses of Compensated and Uncompensated Systems')
xlabel('t Sec')
ylabel('Outputs')
text(8.3,3,'Compensated system')
text(8.3,5,'Uncompensated system') 
```

Figure 7–106 Unit-step response curves for the compensated and uncompensated systems (Example 7–27).   
![](image/2493b631494acb9f0d47ef6a6c30de2c404de5f1a7b80f3cc82e8cb00087aee1.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | 1.35 | 1.4 |
| 10 | 1.05 | 0.85 |
| 15 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 |
| 30 | 1.0 | 1.0 |
| 35 | 1.0 | 1.0 |
| 40 | 1.0 | 1.0 |
</details>

Figure 7–107 Unit-ramp response curves for the compensated and uncompensated systems (Example 7–27).   
![](image/82b1587353f16439856187e52a32845c0b5720683d400f4dd950159b222ce3ff.jpg)

<details>
<summary>line</summary>

| t Sec | Uncompensated system | Compensated system |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2 | ~1.5 | ~1.0 |
| 4 | ~3.5 | ~2.5 |
| 6 | ~5.5 | ~4.5 |
| 8 | ~7.5 | ~6.5 |
| 10 | ~9.5 | ~8.5 |
| 12 | ~11.5 | ~10.5 |
| 14 | ~13.5 | ~12.5 |
| 16 | ~15.5 | ~14.5 |
| 18 | ~17.5 | ~16.5 |
| 20 | ~19.5 | ~18.5 |
</details>

Note that the zero and poles of the designed closed-loop system are as follows:

$$
\begin{array}{l} \text { Zero   at } s = - 0. 1 \\ \text { Poles   at } s = - 0. 2 8 5 9 \pm j 0. 5 1 9 6, \quad s = - 0. 1 2 2 8, \quad s = - 2. 3 1 5 5 \end{array}
$$

The dominant closed-loop poles are very close to the jv axis with the result that the response is slow. Also, a pair of the closed-loop pole at s=–0.1228 and the zero at s=–0.1 produces a slowly decreasing tail of small amplitude.
