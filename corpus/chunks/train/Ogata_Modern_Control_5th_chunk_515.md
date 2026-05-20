MATLAB programs for obtaining the unit-step response and unit-ramp response curves are given in MATLAB Program 7–13. Figure 7–99 shows the unit-step response curves of the system before and after compensation. Also, Figure 7–100 depicts the unit-ramp response curves before and after compensation. These response curves indicate that the designed system is satisfactory.

```matlab
MATLAB Program 7-13

%*****Unit-step responses*****
num = [4];
den = [1 2 4];
numc = [166.8 735.588];
denc = [1 20.4 203.6 735.588];
t = 0:0.02:6;
[c1,x1,t] = step(num,den,t);
[c2,x2,t] = step(numc,denc,t);
plot (t,c1,'.',t,c2,'-')
grid
title('Unit-Step Responses of Compensated and Uncompensated Systems')
xlabel('t Sec')
ylabel('Outputs')
text(0.4,1.31,'Compensated system')
text(1.55,0.88,'Uncompensated system')

%*****Unit-ramp responses*****
num1 = [4];
den1 = [1 2 4 0];
num1c = [166.8 735.588];
den1c = [1 20.4 203.6 735.588 0];
t = 0:0.02:5;
[y1,z1,t] = step(num1,den1,t);
[y2,z2,t] = step(num1c,den1c,t);
plot(t,y1,'.',t,y2,'-',t,t,'--')
grid
title('Unit-Ramp Responses of Compensated and Uncompensated Systems')
xlabel('t Sec')
ylabel('Outputs')
text(0.89,3.7,'Compensated system')
text(2.25,1.1,'Uncompensated system') 
```

It is noted that the closed-loop poles for the compensated system are located as follows:

$$s = - 6. 9 5 4 1 \pm j 8. 0 5 9 2s = - 6. 4 9 1 8$$

Because the dominant closed-loop poles are located far from the jv axis, the response damps out quickly.

Figure 7–99 Unit-step response curves of the compensated and uncompensated systems.   
Figure 7–100 Unit-ramp response curves of the compensated and uncompensated systems.   
Unit-Step Responses of Compensated and Uncompensated Systems   
![](image/f9fb7f1855fd17559e0ba60bd8e51dd1299909ce65980bca14e3d4a522646472.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 0.5 | 1.2 | 0.2 |
| 1.0 | 1.0 | 0.8 |
| 1.5 | 1.1 | 1.0 |
| 2.0 | 1.15 | 1.0 |
| 2.5 | 1.1 | 1.0 |
| 3.0 | 1.0 | 1.0 |
| 3.5 | 1.0 | 1.0 |
| 4.0 | 1.0 | 1.0 |
| 4.5 | 1.0 | 1.0 |
| 5.0 | 1.0 | 1.0 |
| 5.5 | 1.0 | 1.0 |
| 6.0 | 1.0 | 1.0 |
</details>

Unit-Ramp Responses of Compensated and Uncompensated Systems   
![](image/ef1bd5de007efc272da26fce437aeb53349655de2eeec72d115007fda571cc0e.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0.5 | ~0.5 | ~0.2 |
| 1 | ~1 | ~0.5 |
| 1.5 | ~1.5 | ~1 |
| 2 | ~2 | ~1.5 |
| 2.5 | ~2.5 | ~2 |
| 3 | ~3 | ~2.5 |
| 3.5 | ~3.5 | ~3 |
| 4 | ~4 | ~3.5 |
| 4.5 | ~4.5 | ~4 |
| 5 | ~5 | ~4.5 |
</details>
