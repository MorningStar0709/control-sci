# 〖仿真程序〗

(1) 初始化程序: chap1\_19int.m

```matlab
clear all;
close all;

ts=0.001;
%Low Filter
Q=tf([1],[0.04,1]);
Qz=c2d(Q,ts,'tustin');
[numQ,denQ]=tfdata(Qz,'v');

%Plant 
```

```matlab
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
kp=0.20;
ki=0.05;
```

(2) Simulink 主程序: chap1\_19.mdl

![](image/0f30b69e7e9139610bf8919d56cfc3354466128e729b8fb483c8f707295f2d5a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Step1"] --> B["+"]
    C["Clock"] --> D["t"]
    D --> E["To Workspace"]
    B --> F["Subsystem"]
    F --> G["In1 Out1"]
    G --> H["num/den"]
    H --> I["Discrete Transfer Fcn"]
    I --> J["+"]
    K["Random Number"] --> L["1 Gain"]
    L --> I
    J --> M["numQ/denQ"]
    M --> N["Discrete Filter1"]
    N --> O["Mux"]
    O --> P["y"]
    P --> Q["To Workspace1"]
```
</details>

PI 控制器子程序如下:

![](image/6b3cc74ca4e3a9f774bddb7dcee8ae2707f28121805d84d98efdd5d2d4e0417f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 In1"] --> B["0"]
    B --> C["abs(u)"]
    C --> D["ki"]
    D --> E["K Ts z / z-1"]
    E --> F["Discrete-Time Integrator1"]
    F --> G["Fcn"]
    G --> H["kp"]
    H --> I["Switch"]
    I --> J["Scope1"]
    I --> K["Scope2"]
    K --> L["Saturation"]
    L --> M["1 Out1"]
    L --> N["Scope3"]
    N --> O["Output"]
```
</details>

(3) 作图程序: chap1\_19plot.m

```txt
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```

![](image/45df64332bb31987a416788e17d7e2f5bb1334c20983e8b743a1f20f19a70cef.jpg)
