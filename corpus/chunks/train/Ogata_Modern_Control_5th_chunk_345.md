numc = [1.0235 0.0512];
denc = [1 3.005 2.015 1.0335 0.0512];
num = [1.06];
den = [1 3 2 1.06];

% ***** Specify the time range (such as t = 0:0.1:40) and enter
% step command and plot command. ****

t = 0:0.1:40;
c1 = step(numc,denc,t);
c2 = step(num,den,t);
plot(t,c1,'-',t,c2,':')
grid
text(13,1.12,'Compensated system')
text(13.6,0.88,'Uncompensated system')
title('Unit-Step Responses of Compensated and Uncompensated Systems')
xlabel('t Sec')
ylabel('Outputs c1 and c2')

Figure 6–52 Unit-step responses of compensated and uncompensated systems. [The compensator is given by Equation (6–20).]   
![](image/4b9ed251ccfeaa6f139454f4c30d318077445221930d8d1b79e9051a565ec282.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | 1.25 | 1.15 |
| 10 | 1.0 | 0.95 |
| 15 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 |
| 30 | 1.0 | 1.0 |
| 35 | 1.0 | 1.0 |
| 40 | 1.0 | 1.0 |
</details>

Comments. It is noted that under certain circumstances, however, both lead compensator and lag compensator may satisfy the given specifications (both transientresponse specifications and steady-state specifications.) Then either compensation may be used.
