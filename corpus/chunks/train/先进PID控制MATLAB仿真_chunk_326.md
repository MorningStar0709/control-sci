M=1;
if M==1 %With ESO Compensation
    u(k)=kp*(yd(k)-y(k))+kd*(dyd(k)-dy(k))-z3(k)/b;
elseif M==2 %Without ESO Compensation
    u(k)=kp*(yd(k)-y(k))+kd*(dyd(k)-dy(k));
end
%z1_1=z1(k);z2_1=z2(k);z3_1=z3(k);
u_1=u(k);
end
figure(1);
subplot(211);
plot(time,yd,'k',time,y,'r:','linewidth',2);
xlabel('time(s)'),ylabel('position signal');
legend('ideal position signal','position tracking');
subplot(212);
plot(time,yd-y,'r','linewidth',2);
xlabel('time(s)'),ylabel('position tracking error');
legend('tracking signal error');
figure(2);
subplot(311);
plot(time,z1,'k',time,y,'r:','linewidth',2); 
```

```matlab
xlabel('time(s)'),ylabel('z1,y');
legend('practical position signal', 'position signal estimation');
subplot(312);
plot(time,z2,'k',time,dy,'r:','linewidth',2);
xlabel('time(s)'),ylabel('z2,dy');
legend('practical speed signal', 'speed signal estimation');
subplot(313);
plot(time,z3,'k',time,x3,'r:','linewidth',2);
xlabel('time(s)'),ylabel('z3,x3');
legend('practical uncertain part', 'uncertain part estimation'); 
```

② 被控对象 S 函数：chap6\_9plant.m

```matlab
function dy = PlantModel(t,y,flag,p1,p2)
ut=p1;
time=p2;
dy=zeros(2,1);
f=-25*y(2)+33*sin(pi*p2); %Unknown part
b=133;
dy(1)=y(2);
dy(2)=f+b*ut; 
```

![](image/473a06ca49c0ad3d3004a3d419ea689e1d0666055ea43f9d73aa010194c0649f.jpg)
