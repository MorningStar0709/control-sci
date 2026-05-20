```matlab
if M==1
    figure(1);
    plot(time,v,'r',time,v1,'k:',time,y,'b-','linewidth',2);
    xlabel('time(s)'),ylabel('position signal');
    legend('ideal position signal', 'transient position signal', 'position tracking signal');
    figure(2);
    subplot(311);
    plot(time,z1,'r',time,y,'k:','linewidth',2);
    xlabel('time(s)'),ylabel('z1,y');
    legend('practical position signal', 'position signal estimation');
    subplot(312);
    plot(time,z2,'r',time,dy,'k:','linewidth',2);
    xlabel('time(s)'),ylabel('z2,dy');
    legend('practical speed signal', 'speed signal estimation');
    subplot(313);
    plot(time,z3,'r',time,x3,'k:','linewidth',2);
    xlabel('time(s)'),ylabel('z3,x3');
    legend('practical uncertain part', 'uncertain part estimation');
elseif M==2
    figure(1);
    plot(time,v,'r',time,y,'k:','linewidth',2);
    xlabel('time(s)'),ylabel('position signal');
    legend('ideal position signal', 'position tracking');
end 
```

② 被控对象程序：chap6\_12plant.m

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
