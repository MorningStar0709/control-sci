# 〖仿真程序〗

(1) Simulink 主程序: chap1\_7.mdl

![](image/e37c66cc71527c5cb60e0574399390994554b2d359de0905c20ca05bf0c4016f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Signal Generator"] --> B["Sum"]
    B --> C["+"]
    C --> D["Mux"]
    D --> E["MATLAB Function"]
    E --> F["Transfer Fcn 523500 / (s³+87.35s²+10470s)"]
    F --> G["Mux"]
    G --> H["y"]
    I["Clock1"] --> J["t"]
    J --> K["To Workspace"]
    L["Clock"] --> M["+"]
    M --> N["Mux"]
    N --> E
    style A fill:#f9f,stroke:#333
    style H fill:#ccf,stroke:#333
```
</details>

(2) 控制器子程序: chap1\_7ctrl.m

```matlab
function [u]=pidsimf(u1,u2)
persistent pidmat errori error_1
t=u1; 
```

```matlab
if t==0
    errori=0;
    error_1=0;
end

kp=2.5;
ki=0.020;
kd=0.50;

error=u2;
errord=error-error_1;
errori=errori+error;

u=kp*error+kd*errord+ki*errori;
error_1=error; 
```

(3) 作图程序: chap1\_7plot.m

```matlab
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```
