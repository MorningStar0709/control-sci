# 8.5 习题

1. 设随机系统为

$$\boldsymbol {x} (k) = \boldsymbol {x} (k - 1) + 2 \boldsymbol {u} (k - 1) + \boldsymbol {w} (k - 1)\boldsymbol {z} (k) = \boldsymbol {x} (k) + \boldsymbol {v} (k)$$

其中 $w(k)$ 和 $v(k)$ 为互不相关的零均值正态白噪声序列, $w(k) \sim$

$N(0,25), \pmb{v}(k) \sim N(0,15)$ , 它们均与 $N(\mu_0, 100)$ 的初始状态 $x(0)$ 不相关, 试根据量测值 $z(1), z(2)$ , 求使得目标泛函

$$J = E \left\{x ^ {2} (3) + \sum_ {k = 0} ^ {2} u ^ {2} (k) \right\}$$

达到最小值的最优控制,并计算 min J。

2. 设随机系统的状态方程和量测方程分别为

$$
\boldsymbol {X} (k) = \left[ \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right] \boldsymbol {X} (k - 1) + \left[ \begin{array}{c c} k - 1 & 1 \\ 1 & k - 1 \end{array} \right] \boldsymbol {U} (k - 1) + \boldsymbol {w} (k - 1)
z (k) = [ 1 \quad 0 ] X (k) + v (k), \quad k = 1, 2, \dots
$$

其中 $\{w(k)\}$ 和 $\{v(k)\}$ 为两个互不相关的零均值正态平稳白噪声序列，方差为 $Q(k)=\begin{bmatrix}1&0\\ 0&2\end{bmatrix},R(k)=1$ 。又设初始状态 $X(0)$ 为正态随机向量，均值 $\mu_{0}=\begin{bmatrix}\mu_{01}\\ \mu_{02}\end{bmatrix}$ ，方差矩阵 $P_{0}=I=\begin{bmatrix}1&0\\ 0&1\end{bmatrix},X(0)$ 与 $w(k)$ 和 $v(k)$ 均不相关，若以 $z(1),z(2),\cdots$ 表示测量值，试求使目标泛函

$$J = E \left\{x _ {2} ^ {2} (3) + \sum_ {k = 0} ^ {2} \left[ x _ {1} ^ {2} (k) + u _ {1} ^ {2} (k) + u _ {2} ^ {2} (k) \right] \right\}$$

达到最小值的最优控制,并求出 min J。

3. 设随机系统方程为

$$\boldsymbol {X} (k) = \boldsymbol {\Phi} (k, k - 1) \boldsymbol {X} (k - 1) + \boldsymbol {B} (k - 1) \boldsymbol {u} (k - 1)\boldsymbol {z} (k) = \boldsymbol {X} (k) + \boldsymbol {v} (k)$$

其中 $X(k)$ 为 n 维状态向量， $u(k)$ 为 n 维控制向量， $B(k)$ 为 n 阶非奇异方阵 $(k=0,1,2,\cdots,N)$ ， $X(0)=N(0,P_{0})$ ， $\{v(k)\}$ 为与 $X(0)$ 不相关的正态白噪声序列， $E[v(k)]=0$ ， $E[v(k)v^{T}(k)]=R(k)>0$ ，目标泛函为 $J=E\left\{\sum_{k=1}^{N}[X^{T}(k)A(k)X(k)]\right\}$ ，其中 $A(k)>0$

(1) 试求最小化 J 的最优控制及 min J。

（2）证明系统按最优控制方案运行时，滤波值为增益矩阵与量测值之积，即 $\hat{\boldsymbol{X}}(k)=\boldsymbol{K}(k)\boldsymbol{z}(k)$ 。

（3）当系统进行最优运行时，证明对状态一步预测的误差等于系统（距原点）的误差，即 $\widetilde{X}(k+1|k)=X(k+1)$ 。

4. 利用上题结果,对一阶随机系统

$$
\begin{array}{l} \boldsymbol {x} (k + 1) = 2 \boldsymbol {x} (k) + \boldsymbol {u} (k) \\ \boldsymbol {z} (k) = \boldsymbol {x} (k) + \boldsymbol {v} (k) \\ \end{array}
$$

其中 $\boldsymbol{v}(k)$ 为 $N(0,5)$ 的白噪声序列， $\boldsymbol{x}(0)\sim N(0,5)$ ，且 $\boldsymbol{x}(0)$ 与 $\boldsymbol{v}(k)$ $(k=0,1,2,\cdots)$ 不相关，求使 $J=E[x(2)]^{2}$ 为最小的最优控制以及有关的卡尔曼滤波值和 min J。
