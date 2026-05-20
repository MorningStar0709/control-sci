# 〖仿真程序〗

(1) Simulink 仿真程序: chap1\_2.mdl

![](image/87924be7eb57aabc03a2bc533b6615f8e5295edc7f3d4d2026780ac5c87eb9f1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave"] --> B["Sum"]
    B --> C["PID Controller"]
    C --> D["Transfer Fcn"]
    D --> E["x' = Ax+Bu\ny = Cx+Du"]
    E --> F["Plant"]
    F --> G["133/(s²+25s)"]
    G --> H["To Workspace1"]
    G --> I["To Workspace2"]
    H --> J["yd"]
    I --> K["y"]
    J --> L["Mux"]
    K --> L
    L --> M["Scope1"]
    N["Clock"] --> O["t"]
    O --> P["To Workspace"]
```
</details>

程序中同时采用了传递函数 $\frac{133}{s^2 + 25s}$ 的另一种表达方式，即状态方程的形式，其中 $A = \begin{bmatrix} 0 & 1 \\ 0 & -25 \end{bmatrix}, B = \begin{bmatrix} 0 \\ 133 \end{bmatrix}, C = \begin{bmatrix} 1 & 0 \end{bmatrix}, D = 0$ 。

(2) 作图程序: chap1\_2plot.m

```matlab
close all;
plot(t,yd(:,1),'r',t,y(:,1),'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```
