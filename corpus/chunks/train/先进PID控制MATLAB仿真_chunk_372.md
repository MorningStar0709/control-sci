（4）作图程序：chap7\_4plot.m  
```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('step response');
legend('ideal position signal','position tracking');
subplot(212);
plot(t,y(:,1)-y(:,2),'r','linewidth',2);
xlabel('time(s)');ylabel('position tracking error');
figure(2);
plot(t,ut(:,1),'r',t,ut(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('control input');
legend('before saturation','after saturation'); 
```

![](image/aef04d84217412bb4f9455474446c48d28f22952498f2b27e9e1a3e3a23a5bd7.jpg)
