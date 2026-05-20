# 『仿真程序』

(1) Simulink 主程序: chap3\_2sim.mdl

![](image/9ac0fbc37de61a391609ec0e763fed3654b7e7fd20de4e76adca95dc933e7238.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Step"] --> B["+"]
    B --> C["PID Controller"]
    C --> D["+"]
    D --> E["Gain2"]
    E --> F["+"]
    F --> G["Manual Switch"]
    G --> H["Transfer Fcn1"]
    H --> I["Transfer Fcn2"]
    I --> J["Mux"]
    J --> K["Scope"]
    K --> B
    L["Sine Wave"] --> M["Gain1"]
    M --> N["+"]
    N --> D
```
</details>

(2) 作图程序: chap3\_2plot.m

```matlab
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:',linewidth',2);
xlabel('time(s)');ylabel('r and y');
legend('ideal position signal','position tracking'); 
```

![](image/ee5b3558ec386ee7a9718b589e4c5a2da1c790a29ccfe9e9a3ab59cd58d1de65.jpg)
