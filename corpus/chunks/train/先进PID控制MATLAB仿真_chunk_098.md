# (2) 作图程序: chap1\_11plot.m

```matlab
close all;
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```

![](image/4eccbd259c21f1487cf2632e0de2337c14c9b00b34108bf10154bea9f79bd233.jpg)
