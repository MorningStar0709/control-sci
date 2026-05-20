# 实例 2: 离散系统

仿真程序: chap7\_6.m

% RBF identification

clear all;

close all;

alfa=0.05;

xite=0.15;

$x=\left[0,1\right]'$ ;

b=3\*ones(5,1);

c=[-1 -0.5 0 0.5 1;

-1 -0.5 0 0.5 1];

w=rands(5,1);

w\_1=w; w\_2=w\_1;

```matlab
d_w=0*w;
y_1=0;

ts=0.001;
for k=1:1:10000

time(k)=k*ts;
u(k)=sin(k*ts);

y(k)=u(k)^3+y_1/(1+y_1^2);

x(1)=u(k);
x(2)=y_1;

for j=1:1:5
    h(j)=exp(-norm(x-c(:,j))^2/(2*b(j)*b(j)));
end
ym(k)=w'*h';
em(k)=y(k)-ym(k);

d_w(j)=xite*em(k)*h(j);
w=w_1+d_w+alfa*(w_1-w_2);

y_1=y(k);

w_2=w_1;
w_1=w;
end
figure(1);
subplot(211);
plot(time,y,'r',time,ym,'k:','linewidth',2);
xlabel('time(s)');ylabel('y and ym');
legend('ideal signal','signal approximation');
subplot(212);
plot(time,y-ym,'k','linewidth',2);
xlabel('time(s)');ylabel('error'); 
```

5 个 RBF 网络高斯基函数仿真程序: chap7\_7.m  
```matlab
% RBF function
clear all;
close all;

c=[-3 -1.5 0 1.5 3];

M=1;
if M==1
    b=0.50*ones(5,1);
elseif M==2
    b=1.50*ones(5,1);
end 
```

```matlab
h=[0,0,0,0,0]';
ts=0.001;
for k=1:1:2000
time(k)=k*ts;
% RBF function
x(1)=3*sin(2*pi*k*ts);
for j=1:1:5
    h(j)=exp(-norm(x-c(:,j))^2/(2*b(j)*b(j)));
end

x1(k)=x(1);
% First Redial Basis Function
h1(k)=h(1);
% Second Redial Basis Function
h2(k)=h(2);
% Third Redial Basis Function
h3(k)=h(3);
% Fourth Redial Basis Function
h4(k)=h(4);
% Fifth Redial Basis Function
h5(k)=h(5);
end
figure(1);
plot(x1,h1,'b');
figure(2);
plot(x1,h2,'g');
figure(3);
plot(x1,h3,'r');
figure(4);
plot(x1,h4,'c');
figure(5);
plot(x1,h5,'m');
figure(6);
plot(x1,h1,'b');
hold on;plot(x1,h2,'g');
hold on;plot(x1,h3,'r');
hold on;plot(x1,h4,'c');
hold on;plot(x1,h5,'m');
xlabel('Input value of Redial Basis Function');ylabel('Membership function degree'); 
```
