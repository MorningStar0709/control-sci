# 本章附录（程序代码）

BP 网络逼近程序: chap7\_1.m  
```matlab
% BP identification
clear all;
close all;

xite=0.50;
alfa=0.05;

w2=rands(6,1);
w2_1=w2;w2_2=w2_1;

w1=rands(2,6);
w1_1=w1;w1_2=w1;

dw1=0* w1;

x=[0,0]';
u_1=0;
y_1=0;

I=[0,0,0,0,0,0]';
Iout=[0,0,0,0,0,0]';
FI=[0,0,0,0,0,0]';
ts=0.001;
for k=1:1:1000

time(k)=k*ts;
u(k)=0.50*sin(3*2*pi*k*ts);
y(k)=u_1^3+y_1/(1+y_1^2);

for j=1:1:6
    I(j)=x'*w1(:,j);
    Iout(j)=1/(1+exp(-I(j)));
end

yn(k)=w2'*Iout; % Output of NNI networks
e(k)=y(k)-yn(k); % Error calculation
w2=w2_1+(xite*e(k))*Iout+alfa*(w2_1-w2_2); 
```

```matlab
for j=1:1:6
    FI(j)=exp(-I(j))/(1+exp(-I(j)))^2;
end

for i=1:1:2
    for j=1:1:6
    dw1(i,j)=e(k)*xite*FI(j)*w2(j)*x(i);
    end
end

w1=w1_1+dw1+alfa*(w1_1-w1_2);

% % % % % % % % % % % % % Jacobian% % % % % % % % % % % % % % yu=0;
for j=1:1:6
    yu=yu+w2(j)*w1(1,j)*FI(j);
end

dyu(k)=yu;

x(1)=u(k);
x(2)=y(k);

w1_2=w1_1;w1_1=w1;
w2_2=w2_1;w2_1=w2;
u_1=u(k);
y_1=y(k);
end

figure(1);
plot(time,y,'r',time,yn,'b');
xlabel('time(s)');ylabel('y and yn');
figure(2);
plot(time,y-yn,'r');
xlabel('time(s)');ylabel('error');
figure(3);
plot(time,dyu);
xlabel('time(s)');ylabel('dy'); 
```

BP 网络模式识别程序: 包括网络训练程序 chap7\_2a.m 和网络测试程序 chap7\_2b.m。

(1) 网络训练程序: chap7\_2a.m

```matlab
% BP Training for MIMO and Multi-samples
clear all;
close all;
xite=0.50;
alfa=0.05; 
```

```matlab
w2=rands(6,2);
w2_1=w2;w2_2=w2_1;

w1=rands(3,6);
w1_1=w1;w1_2=w1;
dw1=0* w1;

I=[0,0,0,0,0,0]';
Iout=[0,0,0,0,0,0]';
FI=[0,0,0,0,0,0]';
OUT=2;
k=0;
E=1.0;
NS=3;

while E>=1e-020
    k=k+1;
    times(k)=k;

for s=1:1:NS % MIMO Samples
    xs=[1,0,0;
    0,1,0;
    0,0,1]; % Ideal Input
    ys=[1,0;
    0,0.5;
    0,1]; % Ideal Output

x=xs(s,: );
    for j=1:1:6
    I(j)=x*w1(:,j);
    Iout(j)=1/(1+exp(-I(j)));
    end

yl=w2'*Iout;
    yl=yl';

el=0;
    y=ys(s,: );
    for l=1:1:OUT
    el=el+0.5*(y(l)-yl(l))^2; % Output error
    end
    es(s)=el;

E=0;
    if s==NS
    for s=1:1:NS
    E=E+es(s);
    end 
```

```matlab
end
ey=y-yl;

w2=w2_1+xite*Iout*ey+alfa*(w2_1-w2_2);

for j=1:1:6
    S=1/(1+exp(-I(j)));
    FI(j)=S*(1-S);
end

for i=1:1:3
    for j=1:1:6
    dw1(i,j)=xite*FI(j)*x(i)*(ey(1)*w2(j,1)+ey(2)*w2(j,2));
    end
end

w1=w1_1+dw1+alfa*(w1_1-w1_2);

w1_2=w1_1;w1_1=w1;
w2_2=w2_1;w2_1=w2;
end % End of for
Ek(k)=E;
end % End of while
figure(1);
plot(times,Ek,'r');
xlabel('k');ylabel('E');

save wfile w1 w2; 
```

(2) 网络测试程序: chap7\_2b.m  
```matlab
% Test BP
clear all;
load wfile w1 w2;

% N Samples
x=[0.970,0.001,0.001;
    0.000,0.980,0.000;
    0.002,0.000,1.040;
    0.500,0.500,0.500;
    1.000,0.000,0.000;
    0.000,1.000,0.000;
    0.000,0.000,1.000];
for i=1:1:7
    for j=1:1:6
    I(i,j)=x(i,:) * w1(:,j);
    Iout(i,j)=1/(1+exp(-I(i,j)));
    end
end
y=w2'*Iout';
y=y' 
```
