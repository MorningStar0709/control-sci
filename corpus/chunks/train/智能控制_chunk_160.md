# 本章附录（程序代码）

“年轻”的隶属函数仿真程序: chap3\_1.m   
```matlab
% Membership function for Young People
clear all;
close all;

for k=1:1:1001
    x(k)=(k-1)*0.10;
if x(k)>=0&x(k)<=25
    y(k)=1.0;
else
    y(k)=1/(1+((x(k)-25)/5)^2);
end
end
plot(x,y,'k');
xlabel('x Years');ylabel('Degree of membership'); 
```

典型隶属函数仿真程序: chap3\_2.m   
```matlab
% Membership function
clear all;
close all;

M=6;
if M==1 % Gaussian membership function
    x=0:0.1:10;
    y=gaussmf(x,[2 5]);
    plot(x,y,'k');
    xlabel('x');ylabel('y');
elseif M==2 % General Bell membership function
    x=0:0.1:10;
    y=gbellmf(x,[2 4 6]);
    plot(x,y,'k');
    xlabel('x');ylabel('y');
elseif M==3 % S membership function
    x=0:0.1:10;
    y=sigmf(x,[2 4]);
    plot(x,y,'k');
    xlabel('x');ylabel('y');
elseif M==4 % Trapezoid membership function
    x=0:0.1:10;
    y=trapmf(x,[1 5 7 8]);
    plot(x,y,'k');
    xlabel('x');ylabel('y');
elseif M==5 % Triangle membership function
    x=0:0.1:10;
    y=trimf(x,[3 6 8]);
    plot(x,y,'k');
    xlabel('x');ylabel('y');
elseif M==6 % Z membership function
    x=0:0.1:10; 
```

```matlab
y=zmf(x,[37]);
plot(x,y,'k');
xlabel('x');ylabel('y');
end 
```

模糊系统隶属函数设计程序: chap3\_3.m  
```matlab
% Define N+1 triangle membership function
clear all;
close all;
N=6;

x=-3:0.01:3;
for i=1:N+1
    f(i)=-3+6/N*(i-1);
end
u=trimf(x,[f(1),f(1),f(2)]);
figure(1);
plot(x,u);
for j=2:N
    u=trimf(x,[f(j-1),f(j),f(j+1)]);
    hold on;
    plot(x,u);
end
u=trimf(x,[f(N),f(N+1),f(N+1)]);
hold on;
plot(x,u);
xlabel('x');
ylabel('Degree of membership'); 
```

模糊矩阵合成仿真程序: chap3\_4.m  
```matlab
clear all;
close all;
A=[0.8,0.7;
    0.5,0.3];
B=[0.2,0.4;
    0.6,0.9];
% Compound of A and B
for i=1:2
    for j=1:2
    AB(i,j)=max(min(A(i,:),B(:,j)'))
    end
end

% Compound of B and A
for i=1:2
    for j=1:2
    BA(i,j)=max(min(B(i,:),A(:,j)'))
    end
end 
```

模糊推理仿真程序: chap3\_5.m  
```matlab
clear all;
close all;

A=[0.5;1;0.1];
B=[0.1,1,0.6];
C=[0.4,1];

% Compound of A and B
for i=1:3
    for j=1:3
    AB(i,j)=min(A(i),B(j));
    end
end

% Transfer to Column
T1=[];
for i=1:3
    T1=[T1;AB(i,:)'];
end

% Get fuzzy R
for i=1:9
    for j=1:2
    R(i,j)=min(T1(i),C(j));
    end
end

% % % % % % % % % % % % % % % % % % % % % % % % % % % % % %
A1=[1,0.5,0.1];
B1=[0.1,0.5,1];

for i=1:3
    for j=1:3
    AB1(i,j)=min(A1(i),B1(j));
    end
end

% Transfer to Row
T2=[];
for i=1:3
    T2=[T2,AB1(i,:)];
end

% Get output C1
for i=1:9
    for j=1:2
    D(i,j)=min(T2(i),R(i,j));
    C1(j)=max(D(:,j));
    end
end 
```
