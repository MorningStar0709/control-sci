# 本章附录(程序代码)

$f(x_{1},x_{2})$ 的三维图仿真程序：function\_plot.m  
```matlab
clear all;
close all;

x_min=-2.048;
x_max=2.048;

L=x_max-x_min;
N=101;
for i=1:1:N
    for j=1:1:N
    x1(i)=x_min+L/(N-1)*(i-1); % x1取100个点
    x2(j)=x_min+L/(N-1)*(j-1); % x2取100个点
    fx(i,j)=100*(x1(i)^2-x2(j))^2+(1-x1(i))^2;
    end
end

figure(1);
surf(x1,x2,fx);
title('f(x)');
display('Maximum value of fx');
disp(max(max(fx)));
```

遗传算法二进制编码求函数极大值程序: chap10\_1.m  
```matlab
% Generic Algorithm for function f(x1,x2) optimum
clear all;
close all;

% Parameters
Size=80;
G=100;
CodeL=10;

umax=2.048;
umin=-2.048;

E=round(rand(Size,2*CodeL)); % Initial Code

% Main Program
for k=1:1:G
time(k)=k;

for s=1:1:Size
m=E(s,:);
y1=0;y2=0;
```

```matlab
% Uncoding
ml=m(1:1:CodeL);
for i=1:1:CodeL
    y1=y1+m1(i)*2^(i-1);
end
x1=(umax-umin)*y1/1023+umin;
m2=m(CodeL+1:1:2*CodeL);
for i=1:1:CodeL
    y2=y2+m2(i)*2^(i-1);
end
x2=(umax-umin)*y2/1023+umin;

F(s)=100*(x1^2-x2)^2+(1-x1)^2;
end

Ji=1./F;
% **** Step 1 : Evaluate BestJ *****
BestJ(k)=min(Ji);

fi=F; % Fitness Function
[Oderfi,Indexfi]=sort(fi); % Arranging fi small to bigger
Bestfi=Oderfi(Size); % Let Bestfi=max(fi)
BestS=E(Indexfi(Size),:); % Let BestS=E(m), m is the Indexfi belong to max(fi)
bfi(k)=Bestfi;

% **** Step 2 : Select and Reproduct Operation*****
fi_sum=sum(fi);
fi_Size=(Oderfi/fi_sum)*Size;

fi_S=floor(fi_Size); % Selecting Bigger fi value
% sum(fi_S) % Before fill
r=Size-sum(fi_S);
Rest=fi_Size-fi_S;
[RestValue,Index]=sort(Rest);
for i=Size:-1:Size-r+1 % Adding rest to equal Size
fi_S(Index(i))=fi_S(Index(i))+1;
end
% sum(fi_S) % After fill
kk=1;
for i=1:1:Size
    for j=1:1:fi_S(i) % Select and Reproduce
    TempE(kk,:)=E(Indexfi(i),:);
    kk=kk+1; % kk is used to reproduce
    end
    end
    E=TempE;
% **** Step 3 : Crossover Operation *****
pc=0.60;
n=ceil(20*rand);
for i=1:2:(Size-1) 
```

```matlab
temp=rand;
if pc> temp % Crossover Condition
for j=n:1:20
    TempE(i,j)=E(i+1,j);
    TempE(i+1,j)=E(i,j);
end
end
end
TempE(Size, :)=BestS;
E=TempE;

% ￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
% pm=0.001;
% pm=0.001-[1:1:Size]*(0.001)/Size; % Bigger fi, smaller Pm
% pm=0.0;    % No mutation
pm=0.1;    % Big mutation

for i=1:1:Size
    for j=1:1:2*CodeL
    temp=rand;
    if pm> temp    % Mutation Condition
    if TempE(i,j)==0
    TempE(i,j)=1;
    else
    TempE(i,j)=0;
    end
    end
    end
end

% Guarantee TempPop(30, :) is the code belong to the best individual(max(fi))
TempE(Size, :)=BestS;
E=TempE;
end

Max_Value=Bestfi
BestS
x1
x2
figure(1);
plot(time,BestJ);
xlabel('time(s)');ylabel('Best J');
figure(2);
plot(time,bfi);
xlabel('time(s)');ylabel('Best F'); 
```
