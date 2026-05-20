# 基于不确定逼近的 RBF 网络自适应控制仿真实例程序

(1) Simulink 主程序: chap9\_6sim.mdl

![](image/c736aa8a3cdcedbbc5450153ec8fd9887faff7e2663c66247e13c382da33c4e5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["chap9_6input\nS-Function2"] --> B["Demux"]
    B --> C["Mux"]
    C --> D["chap9_6ctrl\nS-Function"]
    D --> E["chap9_6plant\nS-Function1"]
    E --> F["Demux"]
    F --> G["Mux"]
    G --> H["x1\nPosition"]
    I["Clock"] --> J["t\nTo Workspace"]
    J --> K["du/dt\nDerivative"]
    K --> L["emux"]
    L --> M["tol1\nPosition2"]
    L --> N["tol2\nPosition3"]
    L --> O["Mux"]
    O --> P["f1\nPosition4"]
    L --> Q["Mux"]
    Q --> R["f2\nPosition5"]
    F --> S["Mux"]
    S --> T["x2\nPositionl"]
```
</details>

(2) 位置指令子程序: chap9\_6input.m

function [sys,x0,str,ts] = spacemodel(t,x,u,flag)   
```matlab
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
    sys=mdlDerivatives(t,x,u);
case 3,
    sys=mdlOutputs(t,x,u);
case {2,4,9}
    sys=[];
otherwise
    error(['Unhandled flag = ',num2str(flag)]);
end

function [sys,x0,str,ts]=mdlInitializeSizes
sizes=simsizes;
sizes.NumContStates =0;
sizes.NumDiscStates =0;
sizes.NumOutputs =2;
sizes.NumInputs =0;
sizes.DirFeedthrough =0;
sizes.NumSampleTimes =1; 
```

```matlab
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
qd1=1+0.2*sin(0.5*pi*t);
qd2=1-0.2*cos(0.5*pi*t);
sys(1)=qd1;
sys(2)=qd2; 
```

(3) 控制器子程序: chap9\_6ctrl.m  
```txt
function [sys,x0,str,ts] = spacemodel(t,x,u,flag) 
```

```matlab
switch flag,
case 0,
    [sys,x0,str,ts]=mdlInitializeSizes;
case 1,
sys=mdlDerivatives(t,x,u);
case 3,
sys=mdlOutputs(t,x,u);
case {2,4,9}
sys=[];
otherwise
error(['Unhandled flag = ',num2str(flag)]);
end

function [sys,x0,str,ts]=mdlInitializeSizes
global c b kvkp
sizes=simsizes;
sizes.NumContStates=10;
sizes.NumDiscStates=0;
sizes.NumOutputs=6;
sizes.NumInputs=8;
sizes.DirFeedthrough=1;
sizes.NumSampleTimes=1;
sys=simsizes(sizes);
x0=0.1*ones(1,10);
str=[];
ts=[0 0];

% c=0.60*ones(4,5);
c=[-2 -1 0 1 2;
-2 -1 0 1 2;
-2 -1 0 1 2;
-2 -1 0 1 2]; 
```

```matlab
b=3.0*ones(5,1);
alfa=3;
kp=[alfa^2 0;
    0 alfa^2];
kv=[2*alfa 0;
    0 2*alfa];
function sys=mdlDerivatives(t,x,u)
global c b kvkp

A=[zeros(2) eye(2);
    -kp -kv];
B=[0 0;0 0;1 0;0 1];

Q=[50 0 0 0;
    0 50 0 0;
    0 0 50 0;
    0 0 0 50];
P=lyap(A',Q);
eig(P);
