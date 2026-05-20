if M==1 %No Precise Model: PI+Smith
    e1(k)=yd(k)-y(k);
    e2(k)=e1(k)-xm(k)+ym(k);
    ei=ei+Ts*e2(k);
    u(k)=0.50*e2(k)+0.010*ei;
    e1_1=e1(k); 
```

```matlab
elseif M==2 %Precise Model: PI+Smith
    e2(k)=yd(k)-xm(k);
    ei=ei+Ts*e2(k);
    u(k)=0.50*e2(k)+0.010*ei;
    e2_1=e2(k);
elseif M==3 %Only PI
    e1(k)=yd(k)-y(k);
    ei=ei+Ts*e1(k);
    u(k)=0.50*e1(k)+0.010*ei;
    e1_1=e1(k);
end

%----Return of smith parameters----
xm_1=xm(k);
ym_1=ym(k);

u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_1=y(k);
end

figure(1);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position signal','position tracking'); 
```
