# 5.7 设计线性二次型最优控制的若干问题

线性二次型最优控制的设计步骤可大致归结为：

（1）给出系统的数学模型，通常以 $\dot{X} = AX + BU, Y = CX$ 的形式给出（本章只讨论了 C 为单位阵的情况）。  
（2）给定二次型性能指标中的加权矩阵 P、Q、R。通常选用常数对角阵。  
(3) 解黎卡提方程。对定常系统, 终端时间 $t_{\mathrm{f}}$ 无穷的稳态问题可解矩阵黎卡提代数方程, 其他情况一般要解矩阵黎卡提微分方程, 或矩阵黎卡提差分方程。对连续系统得到 $\pmb{K}(t)$ 或 $\pmb{K}$ 以后, 可求得反馈增益阵 $\pmb{G}(t)$ 或 $\pmb{G}$ 。对离散系统则是求得反馈增益矩阵 $\pmb{L}(k)$ 或 $\pmb{L}$ , 若 $\pmb{L}$ 或 $\pmb{G}$ 阵各元素的值太大, 不易在系统中实现, 则要更换 $\pmb{Q}, \pmb{R}, \pmb{P}$ 阵, 并返回到步骤 (2), 若 $\pmb{L}$ 或 $\pmb{G}$ 阵各元素的值合理, 则进行步骤 (4)。  
（4）构成闭环系统，求解在典型输入或初始条件下各状态变量的动态响应，若响应不满足要求，则要进一步改变 Q、R、P 阵，并返回步骤（2），若满足要求，则停止计算。一般来说，把 Q 中某个加权系数增大，则对应的状态变量会收敛得更快些，R 中某个加权系数增大则对应的控制量会小些。

从上面的设计步骤可看出,这是一个试凑的过程。若 Q、R 阵选择得合理,就可以减少试凑次数。若 Q、R 选择不合理,设计出来的系统是不满意的。因此所谓“最优”控制只是使 J 取最小值,并不一定保证系统的特性在实用中“最优”。另外,采用合理的计算方法可以使黎卡提方程的求解快速和精确。下面对这两个问题作一些简单的讨论。

1. 加权阵的选择。若已知各状态变量和控制变量允许的最大值为 $x_{1\max}, x_{2\max}, \cdots, x_{n\max}$ 和 $u_{1\max}, u_{2\max}, \cdots, u_{m\max}$ 则作为初始选择，可令

$$
Q = \left[ \begin{array}{c c c c} \frac {1}{x _ {1 \max}} & & & \\ & \frac {1}{x _ {2 \max}} & & \\ & & \ddots & \\ & & & \frac {1}{x _ {n \max}} \end{array} \right] \tag {5-108}

\boldsymbol {R} = \left[ \begin{array}{c c c c} \frac {1}{u _ {1 \max}} & & & \\ & \frac {1}{u _ {2 \max}} & & \\ & & \ddots & \\ & & & \frac {1}{u _ {m \max}} \end{array} \right]
$$

然后,再根据情况进行调整,直至设计结果满意为止。

2. 对黎卡提矩阵微分方程的求解, 建议采用变步长的四阶龙格-库塔法。不推荐用欧拉法, 因为它的数值特性不好。龙格-库塔法的计算机程序在一般的计算机数学库中都可找到。黎卡提矩阵代数方程的数值求解也不是一件容易的事, 它的解法有很多种。这里介绍一种迭代法 (称为牛顿方法)。在式(5-31)所示的黎卡提代数方程中, 加上一项 $KBR^{-1}B^{T}K$ 再减去 $KBR^{-1}B^{T}K$ 可得

$$- \boldsymbol {K} \boldsymbol {A} - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} + \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} - \boldsymbol {Q} + \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} - \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} = \mathbf {0} \tag {5-109}$$

因为

$$\left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K}\right) ^ {\mathrm{T}} \boldsymbol {K} = \left(\boldsymbol {A} ^ {\mathrm{T}} - \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}}\right) \boldsymbol {K} = \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K} - \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K}$$

故式 $(5-109)$ 可写成
