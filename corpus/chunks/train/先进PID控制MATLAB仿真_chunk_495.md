```mermaid
graph TD
    A["1 In1"] --> B["+"]
    C["2 In3"] --> B
    B --> D["1/(L.s+R)"]
    D --> E["i"]
    E --> F["km"]
    F --> G["+"]
    H["1 Jm.s+bm"] --> G
    G --> I["Out1"]
    I --> J["Ce"]
    J --> B
    K["ki"] --> D
```
</details>

Direct Current Motor model

（3）作图程序：chap11\_5plot.m

```matlab
close all;
figure(1);
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
subplot(212);
plot(t,dy(:,1),'r',t,dy(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Speed tracking');
legend('ideal speed signal','speed tracking'); 
```

![](image/3e5790d09410fe5bd6db56f19545a5897760a87622cd7ab543566efbc8a6d6f7.jpg)
