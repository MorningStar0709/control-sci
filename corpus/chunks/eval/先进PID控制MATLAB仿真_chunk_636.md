（4）作图程序：chap17\_1plot.m  
```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('Ideal position signal','Position signal tracking');
subplot(212);
plot(t,0.1*cos(t),'r',t,y(:,3),:','linewidth',2);
xlabel('time(s)');ylabel('Speed tracking');
legend('Ideal speed signal','Speed signal tracking');
figure(2);
plot(t,ut(:,1),'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

![](image/67b14090efc561e99df5512e69df74a17b861bf0c6acefcf9ddc675da039be4c.jpg)
