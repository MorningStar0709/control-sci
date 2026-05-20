```matlab
sys(1)=x(2);
sys(2)=-Km*Ce/(J*R)*x(2)+Ku*Km*ut/(J*R)-Ff/J;
function sys=mdlOutputs(t,x,u)

%Servo system Parameters
J=0.6;Ce=1.2;Km=6;
Ku=11;R=7.77;
kv=2.0;

alfa=0.01;
a1=1.0; %Effect on the shape of friction curve
Fm=20;
Fc=15;
kv=2.0;

ut=u(1);
F=ut;
if abs(x(2))<=alfa
    if F>Fm
    Ff=Fm;
    elseif F<-Fm
    Ff=-Fm;
    else
    Ff=F;
    end
end

if x(2)>alfa
    Ff=Fc+(Fm-Fc)*exp(-a1*x(2))+kv*x(2);
elseif x(2)<-alfa
    Ff=-Fc-(Fm-Fc)*exp(a1*x(2))+kv*x(2);
end

sys(1)=x(1); %Angle
sys(2)=x(2); %Angle speed
sys(3)=Ff; %Friction force 
```

③ 作图程序：chap11\_3plot.mdl  
```matlab
close all;
figure(1);
subplot(211);
plot(t,y(:,1),'r',t,y(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('ideal position signal','position tracking');
subplot(212);
plot(t,dy(:,1),'r',t,dy(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('Speed tracking');
legend('ideal speed signal','speed tracking');
figure(2); 
```

```javascript
plot(Ff(:,1),Ff(:,2),'r','linewidth',2);
xlabel('Angle speed');ylabel('Friction force'); 
```

![](image/47eedd40fb56ef2c50780c3b7fb5d4a5f0b806c0f7cec82510848a20ec2e7892.jpg)
