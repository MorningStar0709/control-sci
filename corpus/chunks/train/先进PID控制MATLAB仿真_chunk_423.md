%Adjusting Weight Value by hebb learning algorithm
M=1;
if M==1 %No Supervised Heb learning algorithm
    wkp(k)=wkp_1+xiteP*u_1*x(1); %P
    wiki(k)=wiki_1+xiteI*u_1*x(2); %I
    wk(d(k)=wkd_1+xiteD*u_1*x(3); %D
    K=0.06;
elseif M==2 %Supervised Delta learning algorithm
    wkp(k)=wkp_1+xiteP*error(k)*u_1; %P
    wiki(k)=wiki_1+xiteI*error(k)*u_1; %I
    wk(d(k)=wkd_1+xiteD*error(k)*u_1; %D
    K=0.12;
elseif M==3 %Supervised Heb learning algorithm
    wkp(k)=wkp_1+xiteP*error(k)*u_1*x(1); %P
    wiki(k)=wiki_1+xiteI*error(k)*u_1*x(2); %I
    wk(d(k)=wkd_1+xiteD*error(k)*u_1*x(3); %D
    K=0.12;
elseif M==4 %Improved Heb learning algorithm
    wkp(k)=wkp_1+xiteP*error(k)*u_1*(2*error(k)-error_1);
    wiki(k)=wiki_1+xiteI*error(k)*u_1*(2*error(k)-error_1);
    wk(d(k)=wkd_1+xiteD*error(k)*u_1*(2*error(k)-error_1);
    K=0.12;
end

x(1)=error(k)-error_1; %P
x(2)=error(k); %I
x(3)=error(k)-2*error_1+error_2; %D 
```

```matlab
wadd(k)=abs(wkp(k))+abs(wki(k))+abs(wkd(k));
w11(k)=wkp(k)/wadd(k);
w22(k)=wki(k)/wadd(k);
w33(k)=wkd(k)/wadd(k);
w=[w11(k),w22(k),w33(k)];
u(k)=u_1+K*w*x; %Control law
error_2=error_1;
error_1=error(k);
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);
wkp_1=wkp(k);
wkd_1=wkd(k);
wiki_1=wki(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position','position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

![](image/f82afb5c102e15bc10c1ef0072b4c88e33a415f5db2daaba3f5741c7a1aa8052.jpg)
