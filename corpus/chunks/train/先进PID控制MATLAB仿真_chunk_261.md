![](image/c55a4139c4dd21aa14760b1d3b0175d63dca1139cee38f94a062b9c743084202.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave1"] --> B["+"]
    B --> C["PID Controller"]
    C --> D["+"]
    D --> E["chap5_2plant S-Function1"]
    E --> F["Mux"]
    F --> G["p To Workspace2"]
    H["100 Clock"] --> I["t To Workspace"]
    I --> J["Gain"]
    J --> K["0 Gain1"]
    K --> L["1/5 Gain"]
    L --> M["Mux"]
    M --> N["chap5_2obv S-Function2"]
    N --> O["To Workspace2"]
    P["PID Controller"] --> D
```
</details>

观测器闭环控制主程序

② 观测器 S 函数：chap5\_2obv.m

```txt
function [sys,x0,str,ts]=s_function(t,x,u,flag)
switch flag,
case 0,
[sys,x0,str,ts]=mdlInitializeSizes; 
```

```matlab
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
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 2;
sizes.NumInputs = 4;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);
dth=u(3);

k1=1000;
k2=200;

a=5;b=0.15;
sys(1)=k1*(x(2)-dth);
sys(2)=-x(1)+a*ut-k2*(x(2)-dth)-b*dth;
function sys=mdlOutputs(t,x,u)
sys(1)=x(1); %d estimate
sys(2)=x(2); %speed estimate 
```

③ 被控对象 S 函数：chap5\_2plant.m  
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
```

```matlab
function [sys,x0,str,ts]=mdlInitializeSizes
sizes = simsizes;
sizes.NumContStates = 2;
sizes.NumDiscStates = 0;
sizes.NumOutputs = 3;
sizes.NumInputs = 1;
sizes.DirFeedthrough = 0;
sizes.NumSampleTimes = 0;
sys=simsizes(sizes);
x0=[0;0];
str=[];
ts=[];
function sys=mdlDerivatives(t,x,u)
ut=u(1);
b=0.15;
a=5;
d=150*sign(sin(0.1*t));
ddth=-b*x(2)+a*ut-d;
sys(1)=x(2);
sys(2)=ddth;
function sys=mdlOutputs(t,x,u)
d=150*sign(sin(0.1*t));
sys(1)=x(1);
sys(2)=x(2);
sys(3)=d; 
```

④ 作图程序：chap5\_2plot.m

```matlab
close all;

figure(1);
plot(t,p(:,3),'r',t,p(:,4),'b:','linewidth',2);
xlabel('time(s)');ylabel('d and its estimate');
legend('d','Estimate d');

figure(2);
plot(t,sin(t),'r',t,p(:,1),'b:','linewidth',2);
xlabel('time(s)');ylabel('Ideal position signal and position tracking');
legend('Ideal position signal','position tracking'); 
```

![](image/1f30e6b01ab31433ec6ecd964c5ca185cf0156efdeeccf1da7d6a79bd74599be.jpg)
