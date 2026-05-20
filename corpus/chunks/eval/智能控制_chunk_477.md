# 离散系统的 RBF 网络控制仿真程序

(1) $f(x(k-1))$ 为已知的仿真程序: chap9\_9.m  
```matlab
% Discrete controller
clear all;
close all;
ts=0.001;
```

```matlab
c1=-0.01;
u_1=0;y_1=0;
fx_1=0;
for k=1:1:20000
time(k)=k*ts; 
```

```matlab
yd(k)=sin(k*ts);
yd1=sin((k+1)*ts);
% Nonlinear plant
fx(k)=0.5*y_1*(1-y_1)/(1+exp(-0.25*y_1));
y(k)=fx_1+u_1;
e(k)=y(k)-yd(k);
u(k)=yd1-fx(k)-c1*e(k);
y_1=y(k);
u_1=u(k);
fx_1=fx(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

(2) $f(x(k-1))$ 为未知的仿真程序: chap9\_10.m  
```matlab
% Discrete RBF controller
clear all;
close all;
ts=0.001;

c1=-0.01;
beta=0.001;
epcf=0.003;
gama=0.001;
G=50000;

b=15;
c=[-2 -1.5 -1 -0.5 0 0.5 1 1.5 2];
w=rands(9,1);
w_1=w;

u_1=0;
y_1=0;
e1_1=0;
e_1=0;
fx_1=0;
for k=1:1:10000
time(k)=k*ts;

yd(k)=sin(k*ts);
yd1(k)=sin((k+1)*ts);
% Nonlinear plant 
```

```matlab
fx(k)=0.5*y_1*(1-y_1)/(1+exp(-0.25*y_1));  
y(k)=fx_1+u_1;  
e(k)=y(k)-yd(k);  
x(1)=y_1;  
for j=1:1:9  
    h(j)=exp(-norm(x-c(:,j))^2/(2*b^2));  
end  
v1_bar(k)=beta/(2*gama*c1^2)*h*h';  
e1(k)=(-c1*e1_1+beta*(e(k)+c1*e_1))/(1+beta*(v1_bar(k)+G)); 
```

```matlab
if abs(e1(k)) > epcf/G
    w = w_1 + beta / (gama * c1^2) * h' * e1(k);
elseif abs(e1(k)) <= epcf/G
    w = w_1;
end

fnn(k) = w' * h';

u(k) = ydl(k) - fnn(k) - c1 * e(k);
% u(k) = ydl(k) - fx(k) - c1 * e(k); % With precise fx

fx_1 = fx(k);
y_1 = y(k); 
```

```matlab
w_1=w;
u_1=u(k);
e1_1=e1(k);
e_1=e(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input');
figure(3);
plot(time,fx,'r',time,fnn,'k:','linewidth',2);
xlabel('time(s)');ylabel('fx and fx estimation');
legend('Ideal fx','fx estimation'); 
```
