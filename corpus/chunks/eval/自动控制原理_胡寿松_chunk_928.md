# (2) 最优调节器设计

MATLAB 的控制工具箱提供了专门的最优状态调节器设计命令 lqr 和最优输出调节器设计命令 lqry，可以大大减小设计过程中的计算量。

命令格式： $[K,P,e] = lqr(A,B,Q,R)$

$$[ \mathrm{K}, \mathrm{P}, \mathrm{e} ] = \mathrm{lqry} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{Q}, \mathrm{R})$$

其中，K 表示状态反馈矩阵；P 表示里卡蒂方程的解；e 表示最优闭环系统的特征根。

下面结合具体实例说明上述命令的具体应用。

(3) 综合运用(无限时间最优调节器设计)

例 B-11 设系统状态方程

$$\dot {x} _ {1} (t) = u (t), x _ {1} (0) = 0\dot {x} _ {2} (t) = x _ {1} (t), x _ {2} (0) = 1$$

性能指标

$$J = \frac {1}{2} \int_ {0} ^ {\infty} \left[ x _ {2} ^ {2} (t) + \frac {1}{4} u ^ {2} (t) \right] \mathrm{d} t$$

试求最优控制 $u^{*}(t)$ 和最优指标 $J^{*}$ 。

解 本例为无限时间最优调节器问题。由题意

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \boldsymbol {Q} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 1 \end{array} \right], r = \frac {1}{4}
$$

令 $D^{T}D=Q$ ，得 $D^{T}=[0\quad1]$ 。

下面进行如下步骤计算：

1) 检验 $\{\pmb{A},\pmb{b}\}$ 的可控性和 $\{\pmb{A},\pmb{D}\}$ 的可观测性。若系统完全可控可观测，则最优控制 $u^{*}(t)$ 存在且最优闭环系统渐近稳定。

2) 求解里卡蒂方程

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} - \boldsymbol {P b r} ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {P} + Q = 0$$

得到对称矩阵 P。

3）由矩阵 P 确定最优控制 $u^{*}(t)$ ，其中

$$u ^ {*} (t) = - \frac {1}{r} \boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {P x} (t)$$

4) 计算最优指标 $J^{*}$ ，其中

$$J ^ {*} = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} (0) \boldsymbol {P x} (0)$$

MATLAB 程序: example11.m$[\mathrm{P},\mathrm{l},\mathrm{g}] = \mathrm{care}(\mathrm{A},\mathrm{b},\mathrm{Q},\mathrm{r})$ ； %求解里卡蒂方程，得矩阵 $P$

```matlab
A=[0 0;1 0];b=[1;0];Q=[0 0;0 1];r=1/4;
x0=[0;1];D=[0 1];
N=size(A);n=N(1);
control_matrix=ctrb(A,b); %求{A,b}可控性矩阵的秩
f=rank(control_matrix); %判断系统的可控性
if f==n
    disp('system is controlled')
else
    disp('system is no controlled')
end
obsver_matrix=obsv(A,D); %求{A,D}可观测性矩阵的秩
m=rank(obsver_matrix); %判断{A,D}的可观测性
```

```txt
if m==n
    disp('system is observable')
else
    disp('system is no observable')
end 
```

$K=(1/r)*b' * P$ ; %计算状态反馈矩阵

$J=(1/2)*(\mathbf{x}0)'*\mathbf{P}*\mathbf{x}0$ %计算最优指标 $J^{*}$

在 MATLAB 中运行 M 文件 example11 后, 得 $P=\begin{bmatrix}0.5 & 0.5 \\ 0.5 & 1\end{bmatrix}$ ，最优控制为 $u^{*}(t)=-2x_{1}(t)-2x_{2}(t)$ ，最优指标 $J^{*}=0.5$ 。最优闭环系统的特征根 $\lambda_{1}=-1+j, \lambda_{2}=-1-j$ ，由特征值判据可知，闭环系统渐近稳定。

当然 M 文件 example11 中的倒数第 2、3 行完全可以利用 lqr 命令替换为

$$[ \mathrm{K}, \mathrm{P}, \mathrm{e} ] = \mathrm{lqr} (\mathrm{A}, \mathrm{b}, \mathrm{Q}, \mathrm{r})$$

结果完全一致，读者不妨一试。
