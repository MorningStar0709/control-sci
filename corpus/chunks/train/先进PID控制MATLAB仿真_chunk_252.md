if M==1 %By Difference
figure(1);
plot(time,yd,'k',time,p,'r:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
elseif M==2 %By TD
figure(1);
subplot(211);
plot(time,p,'k',time,yp,'r:',time,y,'b:','linewidth',2);
xlabel('time(s)');ylabel('position signal');
legend('ideal position signal','position signal with noise','position signal by TD');
subplot(212);
plot(time,dy,'k','linewidth',2);
xlabel('time(s)');ylabel('speed signal');
legend('speed signal by TD');
figure(2);
plot(time,yd,'r',time,p,'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
end 
```
