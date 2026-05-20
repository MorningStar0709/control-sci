# ① 连续系统仿真。

a. 主程序：chap4\_3sim.mdl

![](image/472cfce8526126998164d69a086e8ead582b397f8f8f963f1ec232ec4377413d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave"] --> B["Capacitor"]
    B --> C["chap4_3ctrl"]
    C --> D["chap4_3plant"]
    D --> E["Mux"]
    E --> F["y Position"]
    B --> G["Manual Switch"]
    G --> H["Clock"]
    H --> I["t To Workspace"]
    I --> J["chap4_3std"]
    J --> K["chap4_3ctrl"]
    K --> L["S-Function3"]
    L --> M["chap4_3plant"]
    M --> N["S-Function1"]
    N --> O["Derivative1"]
    O --> P["mux"]
    P --> Q["s Position2"]
    Q --> R["maoci"]
    R --> S["S-Function4"]
    S --> T["n Position1"]
    T --> U["Output"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#ffc,stroke:#333
    style F fill:#fcc,stroke:#333
    style G fill:#fff,stroke:#333
    style H fill:#fff,stroke:#333
    style I fill:#fff,stroke:#333
    style J fill:#fff,stroke:#333
    style K fill:#fff,stroke:#333
    style L fill:#fff,stroke:#333
    style M fill:#fff,stroke:#333
    style N fill:#fff,stroke:#333
    style O fill:#fff,stroke:#333
    style P fill:#fff,stroke:#333
    style Q fill:#fff,stroke:#333
    style R fill:#fff,stroke:#333
    style S fill:#fff,stroke:#333
    style T fill:#fff,stroke:#333
```
</details>

b. 控制器 S 函数：chap4\_3ctrl.m

```matlab
function [sys,x0,str,ts] = Differentiator(t,x,u,flag)
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
sizes.NumOutputs = 1;
sizes.NumInputs = 3;
sizes.DirFeedthrough = 1;
sizes.NumSampleTimes = 1;
sys = simsizes(sizes);
x0 = [];
str = [];
ts = [0 0];
function sys=mdlOutputs(t,x,u)
yd=u(1);
dyd=cos(t);
y=u(2);
dy=u(3);
e=yd-y;
de=dyd-dy; 
```

```javascript
kp=10;kd=0.5;
ut=kp*e+kd*de;
sys(1)=ut; 
```
