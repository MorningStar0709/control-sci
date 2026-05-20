# 【仿真实例】

设被控对象为一延迟对象

$$G (s) = \frac {\mathrm{e} ^ {- 8 0 s}}{6 0 s + 1}$$

采样时间为 20s，延迟时间为 4 个采样时间，即 80s。采用 PID 控制器进行阶跃响应。输入信号为带有高频干扰的方波信号： $y_{\mathrm{d}}(t)=1.0\mathrm{sgn}(\sin(0.0005\pi t)+0.05\sin(0.03\pi t)$ 。

取 M=1，采有微分先行 PID 控制方法，其方波响应结果如图 1-43 所示。取 M=2，采用普通 PID 方法，其方波响应控制结果如图 1-44 所示。由仿真结果可以看出，对于给定值 $y_{\mathrm{d}}(k)$ 频繁升降的场合，引入微分先行后，可以避免给定值升降时所引起的系统振荡，明显地改善了系统的动态特性。

![](image/545072a248cb63fda4cb3ac3aadfb051d8a99b38c54e3834d754a9a492f01d64.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 2000 | 1.0 | 1.0 |
| 4000 | 1.0 | -1.0 |
| 6000 | 1.0 | -1.0 |
| 8000 | 1.0 | -1.0 |
</details>

图 1-43 微分先行 PID 控制方波响应（M=1）

![](image/a7e38e3ee98646da8cd6ce49ca2f9bc51d260a275533ae32b3867a2b8e289812.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 2000 | -1.0 | -1.0 |
| 4000 | -1.0 | -1.0 |
| 6000 | 1.0 | 1.0 |
| 8000 | -1.0 | -1.0 |
</details>

图 1-44 普通 PID 控制方波响应 (M=2)

〖仿真程序〗 chap1\_21.m  
```matlab
%PID Controller with differential in advance
clear all;
close all;

ts=20;
sys=tf([1],[60,1],'inputdelay',80);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
ud_1=0;
y_1=0;y_2=0;y_3=0;
error_1=0;error_2=0;
ei=0;
for k=1:1:400
time(k)=k*ts;

%Linear model
y(k)=-den(2)*y_1+num(2)*u_5;

kp=0.36;kd=14;ki=0.0021;

yd(k)=1.0*sign(sin(0.00025*2*pi*k*ts));
yd(k)=yd(k)+0.05*sin(0.03*pi*k*ts);

error(k)=yd(k)-y(k);
ei=ei+error(k)*ts;

gama=0.50;
Td=kd/kp;
Ti=0.5; 
```

```matlab
c1=gama*Td/(gama*Td+ts);
c2=(Td+ts)/(gama*Td+ts);
c3=Td/(gama*Td+ts);

M=2;
if M==1 %PID Control with differential in advance
    ud(k)=c1*ud_1+c2*y(k)-c3*y_1;
    u(k)=kp*error(k)+ud(k)+ki*ei;
elseif M==2 %Simple PID Control
    u(k)=kp*error(k)+kd*(error(k)-error_1)/ts+ki*ei;
end

if u(k)>=110
    u(k)=110;
end

if u(k)<=-110
    u(k)=-110;
end

%Update parameters
u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

error_2=error_1;
error_1=error(k);
end

figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('u'); 
```

![](image/f5cf6ac2053dd665f4de6ef310f3b4527ab235b46c1aa375970d140e87fcc767.jpg)
