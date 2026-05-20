# 〖仿真程序〗

（1）初始化程序：chap11\_6int.m

```matlab
%Flight Simulator Servo System
clear all;
close all;
J=2;
b=0.5;
kv=2;
```

```javascript
kp=15;
kd=6;
f1=(b+kd*kv);
f2=J; 
```

(2) Simulink 主程序: chap11\_6sim.mdl

![](image/abdeb80d0dfcc9fc606d2a36b3a7eff400aa326b368658ebcffe24dbdaa2c088.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["chap11_6Input"] --> B["S-Function"]
    C["Clock"] --> D["t"]
    D --> E["To Workspace"]
    F["0"] --> E
    E --> G["error"]
    G --> H["kp"]
    H --> I["+"]
    I --> J["kd"]
    J --> K["u"]
    K --> L["1/(J.s+b)"]
    L --> M["Integrator"]
    M --> N["Mux"]
    N --> O["y"]
    N --> P["Mux"]
    P --> Q["dy"]
    Q --> R["To Workspace2"]
    S["Forward Control"] --> T["f1"]
    T --> U["f2"]
    U --> V["1"]
    V --> W["+"]
    W --> X["u"]
    X --> Y["1/s"]
    Y --> Z["Velocity Loop"]
    Z --> AA["kv"]
    AA --> AB["1"]
    AB --> AC["Position Loop"]
```
</details>

(3) 作图程序: chap11\_6plot.m

```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
subplot(212);
plot(t,dy(:,1),'r',t,dy(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Speed tracking');
legend('ideal speed signal','speed tracking'); 
```
