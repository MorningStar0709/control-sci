F_1=F(j);
th_2=th_1;
th_1=th(j);
dth_1=dth(j);
end%End
%To view the curve, short the points
tshort=linspace(0,tmax,nt/100);
yshort=zeros(nx,nt/100);
dyshort=zeros(nx,nt/100);
for j=1:nt/100
fori=1:nx
yshort(i,j)=y(i,j*100); %Using true y(i,j)
dyshort(i,j)=dy(i,j*100); %Using true dy(i,j)
end
end
%%%%%%%%%%%%%%%%%%%%
figure(1);
subplot(211);
plot(t,thd,'r',t,th,'k','linewidth',2);
title('Joint angle tracking');
xlabel('time(s)');ylabel('angle tracking');
legend('thd','th');
subplot(212);
plot(t,dth,'k','linewidth',2);
xlabel('Time (s)');ylabel('Angle speed response (rad/s)');
legend('dth');

figure(2);
subplot(211); 
```

```matlab
surf(tshort,x,yshort);
title('Elastic deflection of the flexible arms');
xlabel('time(s)'); ylabel('x');zlabel('deflection,y(x,t)');
subplot(212);
surf(tshort,x,dyshort);
xlabel('Time (s)'); ylabel('x');zlabel('Deflection rate, dy(x,t) (m/s)');
figure(3);
subplot(211);
for j=1:nt/100
yshortL(j)=y(nx,j*100);
end
plot(tshort,yshortL,'r','linewidth',2);
xlabel('Time (s)');ylabel('y(L,t)');
subplot(212);
for j=1:nt/100
yshortl(j)=y(nx/2,j*100);
end
plot(tshort,yshortl,'r','linewidth',2);
xlabel('Time (s)');ylabel('y(x,t) at half of L');
figure(4);
subplot(211);
plot(t,tol,'r','linewidth',2);
xlabel('Time (s)');ylabel('control input,tol');
subplot(212);
plot(t,F,'r','linewidth',2);
xlabel('Time (s)');ylabel('control input,F'); 
```

![](image/40facf47b3c81823ca2e085ce7e515f2b0d99e41f8d1e4d6e8c692053fbd1815.jpg)
