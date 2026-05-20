# 『仿真程序』

(1) 初始化程序: chap2\_12int.m

```matlab
clear all;
close all;
kp=1;ki=0.10;kd=10;
a2=43;
a1=3;
```

(2) Simulink 主程序: chap2\_12sim.mdl

![](image/e798234f4ac7dfa0766fa32d35da8f05fcbc2ab0062eb31641682543dd2c32f1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Step"] --> B["+"]
    B --> C["PID Controller"]
    C --> D["Rate Limiter"]
    D --> E["Saturation"]
    E --> F["Transfer Fcn"]
    F --> G["Scope"]
    F --> H["NCD Outport 1"]
    H --> I["NCD Outport"]
    I --> B
```
</details>

![](image/48fc566abdc118a0093bbf430e31fb6025870e7eb6746acd0ca35325b725d56f.jpg)
