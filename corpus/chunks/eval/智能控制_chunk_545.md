# 2. 辨识程序

(1) 差分进化算法辨识程序: chap10\_8.m

```txt
clear all;
close all;
load del_file;
```

```javascript
MinX=[0 0 0 0]; % 参数搜索范围
MaxX=[5 5 5 5];
```

% 设计粒子群参数

Size=80; % 种群规模

CodeL=4; % 参数个数

```matlab
F=0.80; %变异因子:[1,2]  
cr=0.6; %交叉因子  
G=500; %最大迭代次数
```

% 初始化种群的个体

```matlab
for i=1:1:CodeL
    X(:,i)=MinX(i)+(MaxX(i)-MinX(i))*rand(Size,1);
end

BestS=X(1,:); % 全局最优个体
for i=2:Size
    if chap10_8obj(X(i,:),y,N)<chap10_8obj(BestS,y,N)
    BestS=X(i,:);
    end
end
Ji=chap10_8obj(BestS,y,N);
```

% 进入主要循环,直到满足精度要求  
```matlab
for kg=1:1:G
    time(kg)=kg;
%变异
    for i=1:Size
    r1=1;r2=1;r3=1;r4=1;
    while(r1==r2||r1==r3||r2==r3||r1==i||r2==i||r3==i||r4==i||r1==r4||r2==r4||r3==r4)
    r1=ceil(Size*rand(1));
    r2=ceil(Size*rand(1));
    r3=ceil(Size*rand(1));
    r4=ceil(Size*rand(1));
    end
    h(i,:)=BestS+F*(X(r1,:)-X(r2,:));
    %h(i,:)=X(r1,:)+F*(X(r2,:)-X(r3,:));

    for j=1:CodeL %检查值是否越界
    if h(i,j)<MinX(j)
    h(i,j)=MinX(j);
    elseif h(i,j)>MaxX(j)
    h(i,j)=MaxX(j);
    end
end
```  
% 交叉

```matlab
for j=1:1:CodeL
    tempr=rand(1);
    if (tempr<cr)
    v(i,j)=h(i,j);
    else
    v(i,j)=X(i,j);
    end
end
```  
% 选择

```matlab
if (chap10_8obj(v(i,:), y, N) < chap10_8obj(X(i,:), y, N))
    X(i,:) = v(i,:);
end 
```

% 判断和更新  
```matlab
if chap10_8obj(X(i,:), y, N) < Ji % 判断当此时的指标是否为最优的情况
    Ji = chap10_8obj(X(i,:), y, N);
    BestS = X(i,:);
    end
end
Best_J(kg) = chap10_8obj(BestS, y, N);
end
display('true value: g=1, h=2, k1=1, k2=0.5'); 
```

BestS % 最佳个体  
```txt
Best_J(kg)% 最佳目标函数值
```

figure(1);% 指标函数值变化曲线  
```javascript
plot(time,Best_J(time),'r','linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('Best J'); 
```

(2) 目标函数计算程序: chap10\_8obj.m  
function J=obj(X,y,N)% \*\*\*\*\*\*计算个体目标函数值  
```matlab
gp=X(1);
hp=X(2);
klp=X(3);
k2p=X(4);

xmin=-4;
xmax=4;

for i=1:1:N
    x(i)=xmin+(i-1)*0.10;
    x_abs=abs(x(i));
    if x_abs<=gp
    yp(i)=0;
    elseif x_abs> gp&&x_abs<=hp
    yp(i)=klp*(x(i)-gp*sign(x(i)));
    elseif x_abs>=hp
    yp(i)=k2p*(x(i)-hp*sign(x(i)))+klp*(hp-gp)*sign(x(i));
    end
end

E=yp-y;
J=0;
    for i=1:1:N
    J=J+0.5*E(i)*E(i);
    end
end 
```
