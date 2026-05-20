# 〖仿真程序〗

（1）初始化程序：chap11\_5int.m  
```matlab
%Three Loop of Flight Simulator Servo System with two-mass of Direct Current Motor
clear all;
close all;

%(1)Current loop
L=0.001;    %L<<1,Inductance of motor armature
R=1.0;    %Resistance of motor armature
ki=0.001;    %Current feedback coefficient

%(2)Velocity loop
kd=6;    %Velocity loop amplifier coefficient
kv=2;    %Velocity loop feedback coefficient

Jm=0.005;    %Equivalent moment of inertia of motor
bm=0.010;    %Viscosity damp coefficient of motor

km=10;    %Motor moment coefficient
Ce=0.001;    %Voltage feedback coefficient

Jl=0.15;    %Equivalent moment of inertia of frame
bl=8.0;    %Viscosity damp coefficient of frame

kl=5.0;    %Motor moment coefficient between frame and motor

%Friction model: Coulomb&Viscous Friction
Fc=10;bc=3;    %Practical friction 
```

```matlab
%(3)Position loop: PID controller
ku=11; %Voltage amplifier coefficient of PWM
kpp=100;
kii=1.0;
kdd=50; 
```

（2）Simulink 主程序：chap11\_5sim.mdl（包括闭环 PID 控制 Simulink 主模型、二质量伺服系统 Simulink 模型和电机 Simulink 模型）

闭环 PID 控制 Simulink 主模型

![](image/4870d68569f07272f5ea4989c6b8a9d01cae87156621e187836611bb514963ed.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave"] --> B["+"]
    C["Clock"] --> D["t"]
    D --> E["Derivative"]
    B --> F["PID Controller"]
    F --> G["Out1 In1 Out2"]
    G --> H["Mux"]
    H --> I["y"]
    I --> J["To Workspace1"]
    B --> K["du/dt"]
    K --> L["General Plant"]
    L --> H
    M["Mux"] --> N["dy"]
    N --> O["To Workspace2"]
```
</details>

二质量伺服系统 Simulink 模型

![](image/17404bb89cf1fab5096fc9927010defa3673206de4afdc618b4e608f980a1ce2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 In1"] --> B["+"]
    B --> C["kd 2"]
    C --> D["ku 5"]
    D --> E["In1 Out1"]
    E --> F["1/s Integrator"]
    F --> G["+"]
    G --> H["kd"]
    H --> I["+"]
    I --> J["1/Jl s+bl"]
    J --> K["1/s Integrator1"]
    K --> L["Position Loop"]
    L --> M["f(u)"]
    M --> N["0 4"]
    N --> O["Kv"]
    O --> P["+"]
    P --> Q["In3 Motor Model"]
    Q --> R["In1 In3"]
    R --> S["Motor Model"]
    S --> T["Velocity Loop"]
    T --> U["1 In1"]
    U --> V["Out1"]
    V --> W["Out2"]
    W --> X["1 Out1"]
```
</details>

电机 Simulink 模型

![](image/317bba5a1339c619289d0d062fb29daa1892c36d24f6654989376b76871f6b03.jpg)

<details>
<summary>flowchart</summary>
