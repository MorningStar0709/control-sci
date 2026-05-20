| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | 85 | 85 |
| 200 | 95 | 95 |
| 400 | 98 | 98 |
| 600 | 99 | 99 |
| 800 | 99.5 | 99.5 |
| 1000 | 99.8 | 99.8 |
| 1200 | 99.9 | 99.9 |
| 1400 | 99.95 | 99.95 |
| 1600 | 99.98 | 99.98 |
| 1800 | 99.99 | 99.99 |
| 2000 | 100 | 100 |
</details>

图 3-18 采用 Smith 补偿的阶跃响应

〖仿真程序〗 按图 3-14 设计 Smith 控制系统。

(1) Simulink 主程序: chap3\_5sim.md

![](image/a9b62ba73dc5037be98d0e6395ff77a33905d141ee718307f07719cce7c959ee.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Step"] --> B["+"]
    B --> C["PID Controller"]
    C --> D["Transfer Fcn"]
    D --> E["Transport Delay"]
    E --> F["Mux"]
    F --> G["y"]
    G --> H["To Workspace1"]
    H --> I["1/60s+1"]
    I --> J["Manual Switch"]
    J --> K["+"]
    K --> L["60s+1"]
    L --> M["1"]
    M --> N["Clock"]
    N --> O["To Workspace"]
```
</details>

(2) 作图程序: chap3\_5plot.m

```javascript
close all;
figure(1);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position signal','position tracking'); 
```

![](image/57feccae8bbabd926768443f8bea56a2927b98eb9b2f5f4b0eb6fe314853e95a.jpg)
