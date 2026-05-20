wm=imag(pole(2));
kp=0.6*km
kd=kp*pi/(4*wm)
ki=kp*wm/pi

figure(2);
grid on;
bode(sys,'r');

sys_pid=tf([kd,kp,ki],[1,0])
sysc=series(sys,sys_pid)
hold on;
bode(sysc,'b')

figure(3);
rlocus(sysc); 
```

(2) Simulink 主程序: chap2\_4sim.mdl

![](image/5410e6c8ce86dda63194a9d3b6b69b61eb1c0d3a89a325ac17f814684b5e7fc7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Sine Wave"] --> B["Sum"]
    B --> C["PID Controller"]
    C --> D["Manual Switch1"]
    D --> E["Transfer Fcn 400/(s³+30s²+200s)"]
    E --> F["Mux Mux"]
    F --> G["y To Workspace1"]
    H["Clock"] --> I["t To Workspace"]
    I --> B
```
</details>

（3）作图程序：chap2\_4plot.m

```javascript
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('position signal');
legend('ideal position signal','position tracking'); 
```

![](image/aa856df7ecf1236c77fd69f17f933f7a88834833c49fc69b15eaeb80417de92a.jpg)
