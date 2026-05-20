```matlab
function e=pid_eq(K_pid)
assignin('base','kp',K_pid(1));
assignin('base','ki',K_pid(2));
assignin('base','kd',K_pid(3));
opt=simset('solver','ode5');
[tout,xout,y]=sim('chap2_13sim',[0 10],opt);
r=1.0;
e=r-y; 
```

(3) Simulink 子程序: chap2\_13sim.mdl

![](image/d60691a31726bcada95407f19257acb5c49e536dcc511e00c479feb6fbb3105c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Step"] --> B["+"]
    B --> C["PID Controller"]
    C --> D["Saturation"]
    D --> E["Transfer Fcn1"]
    E --> F["Transfer Fcn"]
    F --> G["Scope"]
    F --> H["NCD OutPort 1"]
    H --> I["NCD Outport"]
    I --> B
```
</details>

![](image/fe5effb36b1c69cb8bdb32627a841e5ef0a238ac5d2f04e36a2419109fb856e0.jpg)
