# 〖仿真程序〗

(1) Simulink 仿真主程序: chap1\_4.mdl

![](image/51785b7377fa9c9d272ee23e680e9dbde0add13001b67b44ff50164c98ba376d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Sine Wave1"] --> B["+"]
    C["Clock"] --> D["t"]
    D --> B
    B --> E["PID Controller"]
    E --> F["Transfer Fcn"]
    F --> G["In1 Out1 Subsystem"]
    G --> H["Mux"]
    H --> I["y"]
    I --> J["To Workspace1"]
    J --> B
    style A fill:#f9f,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#cfc,stroke:#333
    style B fill:#ffc,stroke:#333
    style E fill:#fcc,stroke:#333
    style F fill:#cff,stroke:#333
    style G fill:#ffc,stroke:#333
    style H fill:#fcc,stroke:#333
    style I fill:#ffc,stroke:#333
```
</details>

其中被控对象封装模块如下:

![](image/c21cd9abc4f2cf19352e752dd150e3dcbc9180e8584347642516386da8966135.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["0"] --> B["Clock1"]
    B --> C["300*sin(1*2*pi*u)"]
    C --> D["+"]
    D --> E["Product"]
    E --> F["1"]
    F --> G["Out1"]
    H["1"] --> I["+"]
    I --> J["1/s"]
    J --> K["1/s"]
    K --> L["1"]
    L --> M["Product1"]
    M --> N["Gain"]
    N --> O["×"]
    O --> P["+"]
    P --> Q["10*sin(3*2*pi*u)"]
    Q --> R["Fcn2"]
    R --> S["0"]
    S --> T["Clock2"]
    U["20"] --> V["+"]
    V --> W["Product1"]
    X["Constant1"] --> Y["+"]
    Y --> Z["Gain"]
    Z --> AA["×"]
    AA --> AB["+"]
    AB --> AC["10*sin(3*2*pi*u)"]
    AC --> AD["Fcn2"]
    AD --> AE["0"]
```
</details>

(2) 作图程序: chap1\_4plot.m

```txt
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```
