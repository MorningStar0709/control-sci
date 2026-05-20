# 粒子群优化仿真程序

(1) 主程序: chap10\_3. m  
```txt
clear all;
close all;
```  
%(1) 初始化粒子群算法参数

```javascript
min=-2.048;max=2.048;% 粒子位置范围
```  
Vmax=1;Vmin=-1;% 粒子运动速度范围

```javascript
c1=1.3;c2=1.7;% 学习因子[0,4]
```

wmin=0.10; wmax=0.90; % 惯性权重  
```txt
G=100; % 最大迭代次数
```

```txt
Size=50; % 初始化群体个体数目
```

for i=1:G   
```matlab
w(i)=wmax-((wmax-wmin)/G)*i; %随着优化进行,应降低自身权重
end 
```

```matlab
for i=1:Size
for j=1:2
    x(i,j)=min+(max-min)*rand(1); % 随机初始化位置
    v(i,j)=Vmin+(Vmax-Vmin)*rand(1); % 随机初始化速度
end
end
```

%(2)计算各个粒子的适应度,并初始化 pi、plocal 和最优个体 BestS

```matlab
for i=1:Size
p(i)=chap10_3func(x(i,:));
y(i,:) = x(i,:);
if i == 1
plocal(i,:) = chap10_3lbest(x(Size,:), x(i,:), x(i+1,:));
elseif i == Size
plocal(i,:) = chap10_3lbest(x(i-1,:), x(i,:), x(1,:));
else
plocal(i,:) = chap10_3lbest(x(i-1,:), x(i,:), x(i+1,:));
end
end 
```

```julia
BestS=x(1,:); % 初始化最优个体 BestS
for i=2:Size
if chap10_3func(x(i,:)) > chap10_3func(BestS)
BestS=x(i,:);
end
end
```

% (3) 进入主循环

```txt
for kg=1:G
for i=1:Size 
```

```lisp
M=1;
if M==1
v(i,:) = w(kg) * v(i,:) + c1*rand*(y(i,:) - x(i,:)) + c2*rand*(plocal(i,:) - x(i,:)); 
```

% 局部寻优: 加权, 实现速度的更新

```txt
elseif M==2
    v(i,:) = w(kg) * v(i,:) + c1 * rand * (y(i,:) - x(i,:)) + c2 * rand * (BestS - x(i,:)); 
```

% 全局寻优:加权,实现速度的更新

```txt
end
for j=1:2 % 检查速度是否越界
```

```julia
if v(i,j) < Vmin
v(i,j) = Vmin;
elseif x(i,j) > Vmax
v(i,j) = Vmax;
end
end 
```

```matlab
x(i,:) = x(i,:) + v(i,:) * 1; % 实现位置的更新
for j = 1:2 % 检查位置是否越界
if x(i,j) < min
    x(i,j) = min;
elseif x(i,j) > max
    x(i,j) = max;
end
end
```  
% 自适应变异,避免粒子群算法陷入局部最优

```matlab
if rand>0.60
    k=ceil(2*rand);
x(i,k)=min+(max-min)*rand(1);
end

%(4)判断和更新
if i==1
plocal(i,:)=chap10_3lbest(x(Size,:),x(i,:),x(i+1,:));
elseif i==Size
plocal(i,:)=chap10_3lbest(x(i-1,:),x(i,:),x(1,:));
else
plocal(i,:)=chap10_3lbest(x(i-1,:),x(i,:),x(i+1,:));
end 
```

```matlab
if chap10_3func(x(i,:)) > p(i) % 判断此时的位置是否为最优的情况, 当不满足时继续更新
p(i) = chap10_3func(x(i,:));
y(i,:) = x(i,:);
end
if p(i) > chap10_3func(BestS)
BestS = y(i,:);
end
end
Best_value(kg) = chap10_3func(BestS);
end
figure(1);
kg = 1:G;
plot(kg, Best_value, 'r', 'linewidth', 2);
xlabel('generations'); ylabel('Fitness function');
display('Best Sample='); disp(BestS);
display('Biggest value='); disp(Best_value(G)); 
```

(2) 局部最优排序函数: chap10\_3lbest.m   
```matlab
function f = evaluate_localbest(x1, x2, x3) % 求解粒子环形邻域中的局部最优个体
K0 = [x1; x2; x3];
K1 = [chap10_3func(x1), chap10_3func(x2), chap10_3func(x3)];
[maxvalue index] = max(K1);
plocalbest = K0(index, :);
f = plocalbest; 
```

(3) 函数计算程序: chap10\_3func.m

function f = func(x)

$f=100*(x(1)^{2}-x(2))^{2}+(1-x(1))^{2};$
