%Linear model
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;

M=2;
if M==1 %Using simple PID
    yd(k)=R;
    error(k)=yd(k)-y(k);
end
if M==2 %Using Gradual approaching input value
if ydi<R-0.25
    ydi=ydi+k*ts*rate;
elseif ydi>R+0.25
    ydi=ydi-k*ts*rate;
else
    ydi=R;
end
    yd(k)=ydi;
    error(k)=yd(k)-y(k);
end

%PID with I separation
if abs(error(k))<=0.8
    ei=ei+error(k)*ts;
else 
```

```matlab
ei=0;
end
u(k)=kp*error(k)+ki*ei;

%----Return of PID parameters----
yd_1=yd(k);
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

error_2=error_1;
error_1=error(k);
end
figure(1);
subplot(211);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(212);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input');
figure(2);
plot(time,yd,'r','linewidth',2);
xlabel('time(s)');ylabel('ideal position value'); 
```

![](image/7f6eeb7ae5dc20ec1850bac14b258ef949611b7f4744d25bacc5ec51d2fe2cfe.jpg)
