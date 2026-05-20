# 〖仿真程序〗

(1) 初始化程序: chap11\_4int.m  
```matlab
%Three Loop of Flight Simulator Servo System with Direct Current Motor
clear all;
close all;
%(1)Current loop
L=0.001; %L<<1 Inductance of motor armature
R=1; %Resistance of motor armature
ki=0.001; %Current feedback coefficient
%(2)Velocity loop
kd=6; %Velocity loop amplifier coefficient
kv=2; %Velocity loop feedback coefficient
J=2; %Equivalent moment of inertia of frame and motor
b=1; %Viscosity damp coefficient of frame and motor
km=1.0; %Motor moment coefficient
Ce=0.001; %Voltage feedback coefficient
%Friction model: Coulomb&Viscous Friction
Fc=100.0;bc=30.0; %Practical friction
%(3)Position loop: PID controller
ku=11; %Voltage amplifier coefficient of PWM
kpp=150;
kii=0.1;
kdd=1.5; 
```

```matlab
%Friction Model compensation
%Equivalent gain from feedforward to practical friction
Gain=ku*Kd*1/R*km*1.0;
Fc1=Fc/Gain; bc1=bc/Gain; %Feedforward compensat 
```

（2）Simulink 主程序：chap11\_4sim.mdl（包括伺服系统位置环模块和伺服系统速度环和电流环模块）

![](image/8713825a40c316243c6fb07e42b42316360633aa325ac2b9b9b141368ad63d10.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave"] --> B["error"]
    B --> C["PID Controller"]
    C --> D["u"]
    D --> E["+"]
    E --> F["÷"]
    F --> G["kd"]
    G --> H["ku"]
    H --> I["In1 Out1 In2"]
    I --> J["Subsystem"]
    J --> K["1/s"]
    K --> L["Mux"]
    L --> M["y"]
    L --> N["Mux"]
    N --> O["dy"]
    O --> P["To Workspace2"]
    P --> Q["Velocity Loop"]
    Q --> R["kv"]
    R --> S["kv"]
    S --> T["Position Loop"]
    T --> U["t"]
    U --> V["Clock"]
    V --> W["To Workspace"]
    W --> X["Error"]
    X --> Y["PID Controller"]
    Y --> Z["u"]
    Z --> E
    style A fill:#f9f,stroke:#333
    style P fill:#f9f,stroke:#333
```
</details>

伺服系统位置环模块

![](image/4860d3bfc94ac4985dd6968bb4f0583ce83e84f689626ff675db3293f08c3243.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    In1["1 In1"] --> adder["+ -"]
    In2["2 In2"] --> adder
    adder --> L1["L.s+R"]
    L1 --> i["i"]
    i --> km["km"]
    km --> adder
    f(u) --> FrictionModel["f(u)"]
    FrictionModel --> adder
    Scope["Scope"] --> adder
    Adder --> J["m"]
    J --> Out1["1 Out1"]
    Ce["Ce"] --> Adder
    Adder --> k["i"]
    k --> adder
```
</details>

伺服系统速度环和电流环模块

（3）作图程序：chap11\_4plot.m

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

![](image/7f4301c4845210f9db5cf47caafc9ebd0fc64d1f75997daea694405f9a7008cf.jpg)
