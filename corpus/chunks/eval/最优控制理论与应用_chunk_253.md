$$
\begin{array}{l} \mathbf {A} = \left[ 0 1; - 5, - 3 \right]; \\ \mathbf {B} = [ 0; 1 ]; \\ \mathrm{Q} = [ 5 0 0 2 0 0; 2 0 0 1 0 0 ]; \\ \mathrm{R} = 1. 6 6 6 7; \\ [ \mathrm{P}, \mathrm{E}, \mathrm{K}, \mathrm{RR} ] = \operatorname{care} (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R}, \text {zeros} (\text {size} (\mathrm{B})) , \text {eye} (\text {size} (\mathrm{A})) \\ \end{array}
$$

运行结果：

$$
\begin{array}{l} \mathrm{P} = 6 7. 9 4 0 6 \quad 2 1. 7 1 3 1 \\ \begin{array}{l l} 2 1. 7 1 3 1 & 1 1. 2 4 9 5 \end{array} \\ \mathrm{E} = - 7. 2 6 9 8 \\ - 2. 4 7 9 8 \\ \mathrm{K} = 1 3. 0 2 7 6 \quad 6. 7 4 9 6 \\ \mathrm{RR} = 2. 8 4 5 8 \mathrm{e} - 0 1 5 \\ \end{array}
$$

以上的三种方法的运行结果相同。可以得到,最优控制变量与状态变量之间的关系:

$$\boldsymbol {u} ^ {*} (t) = - 1 3. 0 2 7 6 x _ {1} (t) - 6. 7 4 9 6 x _ {2} (t)$$

在以上程序的基础上,可以得到在最优控制的作用下的最优控制曲线与最优状态曲线,其程序如下:

% \* \* \* \* \* \* \* \* \* \* \* \* MATLAB 程序 \* \* \* \* \* \* \* \* \* \* \* %

figure('pos', [50, 50, 200, 150], 'color', 'w');

axes('pos', [0.15, 0.14, 0.72, 0.72])

$\mathbf{ap} = [\mathbf{A} - \mathbf{B} * \mathbf{K}]$ ;

bp = B ;

$C = [1,0]$ ;

D = 0 ;

[ap,bp,cp,dp] = augstate(ap,bp,C,D);

$\mathbf{cp} = [\mathbf{cp}; - \mathbf{K}]$

dp = [ dp;0];

$G = \mathrm{ss}(\mathrm{ap},\mathrm{bp},\mathrm{cp},\mathrm{dp})$

$\left[\mathbf{y},\mathbf{t},\mathbf{x}\right] = \operatorname {step}(\mathbf{G})$

plotyy(t,y(:,2:3),t,y(:,4))

[ax,h1,h2] = plotyy(t,y(:,2:3),t,y(:,4));

axis(ax(1), [0 2.5 0 0.1]), axis(ax(2), [0 2.5 -1 0])

运行结果：

![](image/8292c891034cd7ace77f9ee5144c198c4b5f64e5f4b7f14f9df1cb5dc14c5b25.jpg)

<details>
<summary>line</summary>

| x | x1 | x2 | u* |
| --- | --- | --- | --- |
| 0.0 | 0.0000 | 0.1000 | 0.0 |
| 0.5 | 0.0400 | 0.0800 | -0.6 |
| 1.0 | 0.0550 | 0.0400 | -0.7 |
| 1.5 | 0.0580 | 0.0200 | -0.75 |
| 2.0 | 0.0590 | 0.0100 | -0.8 |
| 2.5 | 0.0600 | 0.0050 | -0.85 |
</details>

图12-1 最优控制曲线与最优状态曲线

该程序采用 augstate 函数将状态变量作为输出变量,用于显示;输出项作为最优控制的输出。因此,阶跃响应输出 y 中,y(1)是系统输出,y(2)和 y(3)是状态变量输出,y(4)是系统控制变量输出。用 plotyy 函数进行双坐标显示,并设置相应的坐标范围。

以上三种方法中,第一种方法易于理解黎卡提方程的解法,其解法简单但是并不可靠。第二种方法比起另两种方法使用方便，不易出错，所以我们推荐使用这种方法。但是采用 $\mathrm{lqr}()$ 函数不能设置代数黎卡提方程的边界条件，所以，如果题目设置了 $P$ 的终值条件，只能使用第三种方法来求解，例如设置 $P$ 的终值条件为[0.2;0.2]。

程序如下：

% \* \* \* \* \* \* \* \* \* \* \* \* \* MATLAB 程序 \* \* \* \* \* \* \* \* \* \* \* \* %
