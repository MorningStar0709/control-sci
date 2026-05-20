# 10.2 基于差分进化算法的函数优化

利用差分进化算法求 Rosenbrock 函数的极大值:

$$
\left\{ \begin{array}{l} f (x _ {1}, x _ {2}) = 1 0 0 (x _ {1} ^ {2} - x _ {2}) ^ {2} + (1 - x _ {1}) ^ {2} \\ - 2. 0 4 8 \leqslant x _ {i} \leqslant 2. 0 4 8 \quad (i = 1, 2) \end{array} \right.
$$

该函数有两个局部极大点，分别是 $f(2.048,-2.048)=3897.7342$ 和 $f(-2.048,-2.048)=3905.9262$ ，其中后者为全局最大点。

函数 $f(x_{1},x_{2})$ 的三维图如图 10-2 所示，可以发现该函数在指定的定义域上有两个接近的极点，即一个全局极大值和一个局部极大值。因此，采用寻优算法求极大值时，需要避免陷入局部最优解。

![](image/be0957b47f503f6db3891fcc21b3e7651468904771db80d4d7707080bcd7a899.jpg)

<details>
<summary>surface_3d</summary>

| x | y |
| --- | --- |
| -2.5 | 0 |
| -2.0 | 500 |
| -1.5 | 1000 |
| -1.0 | 1500 |
| -0.5 | 2000 |
| 0.0 | 2500 |
| 0.5 | 3000 |
| 1.0 | 3500 |
| 1.5 | 4000 |
| 2.0 | 3500 |
| 2.5 | 3000 |
</details>

图10-2 $f(x_{1},x_{2})$ 的三维图

〖仿真程序〗 chap10\_1.m

```txt
clearall;
closeall;
```

```matlab
x_min=-2.048;
x_max=2.048;

L=x_max-x_min;
N=101;
fori=1:1:N
for j=1:1:N
x1(i)=x_min+L/(N-1)*(i-1); %ÔÚx1ÖáÉÏÈ¡100μã
x2(j)=x_min+L/(N-1)*(j-1); %ÔÚx2ÖáÉÏÈ¡100μã
fx(i,j)=100*(x1(i)^2-x2(j))^2+(1-x1(i))^2;
end
end
figure(1);
surf(x1,x2,fx);
title('f(x)');
display('Maximum value of fx');
disp(max(max(fx))); 
```

采用实数编码求函数极大值，用两个实数分别表示两个决策变量 $x_{1}, x_{2}$ ，分别将 $x_{1}, x_{2}$ 的定义域离散化为从离散点-2.048到离散点2.048的Size个实数。个体的适应度直接取为对应的目标函数值，越大越好，即取适应度函数为 $F(x) = f(x_{1}, x_{2})$ 。

在差分进化算法仿真中，取 F=1.2，CR=0.90，样本个数为 Size=50，即群体规模 M=50，最大迭代次数 G=30。按式（10.1）～式（10.5）设计差分进化算法，经过 30 步迭代，最佳样本为 BestS = [-2.048 -2.048]，即当 $x_{1}=-2.048$ ， $x_{2}=-2.048$ 时，Rosenbrock 函数具有极大值，极大值为 3905.9。

适应度函数 F 的变化过程如图 10-3 所示，通过适当增大 F 值及增加样本数量，有效地避免了陷入局部最优解，仿真结果表明正确率接近 100%。

![](image/dbad41914f7262fc90cd53482cfc8b38bc509f01dd3a67dbd7cb3e4023c17a48.jpg)

<details>
<summary>line</summary>

| Times | Best f |
| --- | --- |
| 0 | 3897.5 |
| 1 | 3897.5 |
| 2 | 3906 |
| 30 | 3906 |
</details>

图 10-3 适应度函数 F 的优化过程

〖仿真程序〗差分进化算法优化仿真程序包括以下两个部分：

(1) 主程序: chap10\_2.m  
```matlab
%To Get maximum value of function f(x1,x2) by Differential Evolution
clear all;
close all;

Size=30;
CodeL=2;

MinX(1)=-2.048;
MaxX(1)=2.048;
MinX(2)=-2.048;
MaxX(2)=2.048;

G=50;

F=1.2;    %变异因子[0,2]
cr=0.9;    %交叉因子[0.6,0.9]

%初始化种群
fori=1:1:CodeL
    P(:,i)=MinX(i)+(MaxX(i)-MinX(i))*rand(Size,1);
end

BestS=P(1,:);    %全局最优个体
fori=2:Size
    if(chap10_2obj(P(i,1),P(i,2))>chap10_2obj(BestS(1),BestS(2)))
BestS=P(i,:);
end
end

fi=chap10_2obj(BestS(1),BestS(2));
