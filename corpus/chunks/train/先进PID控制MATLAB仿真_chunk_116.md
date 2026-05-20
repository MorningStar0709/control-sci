if M==3 %Using low frequency filter
    filthy(k)=-den1(2)*f_1+num1(1)*(yn(k)+yn_1);
    error(k)=yd(k)-filty(k);
end

%I separation
if abs(error(k))<=0.8
    ei=ei+error(k)*ts;
else
    ei=0;
end
    u(k)=kp*error(k)+ki*ei;
%----Return of PID parameters----
yd_1=yd(k);
u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

f_1=filty(k);
yn_1=yn(k);

error_2=error_1;
error_1=error(k);
end
figure(1);
subplot(211);
plot(time,yd,'r',time,filty,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(212);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('u');
figure(2);
plot(time,n,'r','linewidth',2);
xlabel('time(s)');ylabel('Noisy signal'); 
```
