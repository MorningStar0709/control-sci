%Linear model
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;
n(k)=0.50*rands(1); %Noisy signal
yn(k)=y(k)+n(k);

%Low frequency filter 
```

```matlab
filty(k)=-den1(2)*f_1+num1(1)*(yn(k)+yn_1);
error(k)=yd(k)-filty(k);

if abs(error(k))<=0.20
    ei=ei+error(k)*ts;
else
    ei=0;
end

kp=0.50;ki=0.10;kd=0.020;
u(k)=kp*error(k)+ki*ei+kd*(error(k)-error_1)/ts;

M=2;
if M==1
    u(k)=u(k);
elseif M==2 %Using Dead zone control
    if abs(error(k))<=0.10
    u(k)=0;
    end
end

if u(k)>=10
    u(k)=10;
end

if u(k)<=-10
    u(k)=-10;
end

%----Return of PID parameters----
yd_1=yd(k);
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

f_1=filty(k);
yn_1=yn(k);

error_2=error_1;
error_1=error(k);
end

figure(1);
subplot(211);
plot(time,yd,'r',time,y,'k','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(212);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input');
figure(2);
plot(time,n,'r','linewidth',2);
xlabel('time(s)');ylabel('Noisy signal'); 
```

![](image/8c9e8541a09a681133265fe5da8178a3cc976b6e86593da3ee28ae0514bc9b02.jpg)
