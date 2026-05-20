k1=0.1;k2=0.1; %Verify by design_K.m
z=[thp wp]';
%%
K=[k1 k2]';
dz=A*z+H*ut+K*(yp-C*z_tol);

for i=1:2
    sys(i)=dz(i);

end

function sys=mdlOutputs(t,x,u)
thp=x(1);wp=x(2);

sys(1)=thp;
sys(2)=wp;
```

④ 作图程序：chap5\_12plot.m  
```matlab
close all;

figure(1);
subplot(211);
plot(t,p(:,1),'k',t,p(:,3),'r:','linewidth',2);
xlabel('time(s)');ylabel('x1 and its estimate');
legend('ideal signal','estimation signal');
subplot(212);
plot(t,p(:,2),'k',t,p(:,4),'r:','linewidth',2);
xlabel('time(s)');ylabel('x2 and its estimate');
legend('ideal signal','estimation signal'); 
```

```matlab
figure(2);
subplot(211);
plot(t,p(:,1)-p(:,3),'r','linewidth',2);
xlabel('time(s)');ylabel('error of x1 and its estimate');
subplot(212);
plot(t,p(:,2)-p(:,4),'r','linewidth',2);
xlabel('time(s)');ylabel('error of x2 and its estimate');
figure(3);
plot(t,p1(:,1),'k',t,p1(:,2),'r:','linewidth',2);
xlabel('time(s)');ylabel('x1 and its delayed value');
legend('ideal signal','delayed signal'); 
```
