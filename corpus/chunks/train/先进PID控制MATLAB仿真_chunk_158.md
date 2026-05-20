# (1) 对象开环测试

① Simulink 主程序：chap2\_1sim.mdl

![](image/e4a67fa9221e4b345639ff2027cc4fc1b00c3fb620f04c31c72c709f8dd8b07c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Step"] --> B["Transfer Fcn"]
    C["0 Clock"] --> D["t To Workspace"]
    B --> E["Transport Delay"]
    D --> E
    E --> F["Scope"]
    E --> G["y To Workspace1"]
```
</details>

② 作图程序：chap2\_1plot.m

```matlab
close all;
figure (1);
plot(t,y(:,1),'k','linewidth',2);
xlabel('time(s)');ylabel('y'); 
```
