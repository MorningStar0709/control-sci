# (1) 峰值抑制

① 主程序：chap5\_7.sim.mdl

![](image/80868aed05ba9e3e9d916c5486cdc3b14794363a261a1a22d54a4741b5fadd29.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["chap5_7peak"] --> B["y"]
    C["10"] --> D["t"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
```
</details>

② 峰值抑制 S 函数：chap5\_7peak.m

```matlab
function [sys,x0,str,ts]=s_function(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 3,
    sys=mdlOutputs(t,x,u);
case {1,2,4,9}
    sys = [];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 0;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
Lambda=50;
R=100*(1-exp(-Lambda*t))/(1+exp(-Lambda*t));
Epsilon=1/R;
sys(1)=R;
sys(2)=Epsilon; 
```

③ 作图程序：chap5\_7plot.m

```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r','linewidth',2);
xlabel('time(s)');ylabel('R change');
subplot(212); 
```

```matlab
plot(t,y(:,2),'r','linewidth',2);
xlabel('time(s)');ylabel('Epsilon change'); 
```

(2) 扩张观测器

① 连续系统仿真。

主程序：chap5\_8sim.mdl

![](image/15d3f88d84b21f6e77f7efd09cf88dd7727d71759dde47725a9e059b367bec23.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave"] --> B["chap5_8plant"]
    B --> C["S-Function2"]
    C --> D["Mux"]
    D --> E["chap5_8eso"]
    E --> F["Mux"]
    F --> G["x Position2"]
    H["30 Clock"] --> I["t To Workspace"] --> J["Mux"]
    J --> E
    K["Clock"] --> I
```
</details>

a. 扩张观测器 S 函数: chap5\_8eso.m

```matlab
function [sys,x0,str,ts]=s_function(t,x,u,flag)
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
    sys=mdlDerivatives(t,x,u);
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys = [];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 3;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 2;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0 0 0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
y=u(1);
ut=u(2);

J=10;
b=1/J; 
```
