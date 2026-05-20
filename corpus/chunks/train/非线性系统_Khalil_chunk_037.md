# 1.2.5 人工神经网络

人工神经网络利用分布式信息处理及其固有的并行计算能力模拟生物结构。图1.8所示为实现神经网络模型的一个电路，称为霍普菲尔德(Hopfield)模型。该电路基于一个与一些放大器连接的RC网络，放大器的输入-输出特性由 $v_{i}=g_{i}(u_{i})$ 给出，其中 $u_{i}$ 和 $v_{i}$ 是第i个放大器的输入电压和输出电压，函数 $g_{i}(\cdot):R\rightarrow(-V_{M},V_{M})$ 是一个以 $-V_{M}$ 和 $V_{M}$ 为渐近线的S状函数，如图1.9所示，是连续可微的单调递增函数，当且仅当 $u_{i}=0$ 时， $g_{i}(u_{i})=0$ 。 $g_{i}(\cdot)$ 可能的情况有

$$g _ {i} (u _ {i}) = \frac {2 V _ {M}}{\pi} \arctan \left(\frac {\lambda \pi u _ {i}}{2 V _ {M}}\right), \lambda > 0$$

和 $g_{i}(u_{i}) = V_{M}\frac{e^{\lambda u_{i}} - e^{-\lambda u_{i}}}{e^{\lambda u_{i}} + e^{-\lambda u_{i}}} = V_{M}\tanh (\lambda u_{i}),\lambda >0$

其中， $\lambda$ 决定 $g_{i}(u_{i})$ 在 $u_{i} = 0$ 点的斜率。这种 $S$ 状输入-输出特性可用运算放大器实现。电路中每个放大器都包含一个输出为 $-v_{i}$ 的反相放大器，这就允许选择与给定输入所连接的放大器输出的符号。输出 $v_{i}$ 和 $-v_{i}$ 通常由同一运算放大器电路的两个输出端提供，这一对非线性放大器称为“神经元”。电路中每个放大器的输入还有一个 $RC$ 节。电容 $C_{i} > 0$ 和电阻 $\rho_{i} > 0$ 表示第 $i$ 个放大器输入端的所有并联电容和并联电阻。由基尔霍夫电流定律，在第 $i$ 个放大器输入结点，有

$$C _ {i} \frac {d u _ {i}}{d t} = \sum_ {j} \frac {1}{R _ {i j}} (\pm v _ {j} - u _ {i}) - \frac {1}{\rho_ {i}} u _ {i} + I _ {i} = \sum_ {j} T _ {i j} v _ {j} - \frac {1}{R _ {i}} u _ {i} + I _ {i}$$

其中

$$\frac {1}{R _ {i}} = \frac {1}{\rho_ {i}} + \sum_ {j} \frac {1}{R _ {i j}}$$

$T_{ij}$ 表示带符号的电导, 其大小为 $1/R_{ij}$ , 其符号通过选择第 j 个放大器的正负输出决定, $I_{i}$ 是一个恒定的输入电流。对于含有 n 个放大器的电路, 可由 n 个一阶微分方程描述其运动。为写出状态方程, 选择状态变量为 $x_{i}=v_{i}, i=1,2,\cdots,n$ , 则有

$$\dot {x} _ {i} = \frac {d g _ {i}}{d u _ {i}} (u _ {i}) \times \dot {u} _ {i} = \frac {d g _ {i}}{d u _ {i}} (u _ {i}) \times \frac {1}{C _ {i}} \left(\sum_ {j} T _ {i j} x _ {j} - \frac {1}{R _ {i}} u _ {i} + I _ {i}\right)$$

定义 $h_i(x_i) = \frac{dg_i}{du_i}(u_i)\bigg|_{u_i = g_i^{-1}(x_i)}$

可把状态方程写为 $\dot{x}_{i}=\frac{1}{C_{i}}h_{i}(x_{i})\left[\sum_{j}T_{ij}x_{j}-\frac{1}{R_{i}}g_{i}^{-1}(x_{i})+I_{i}\right]$ (1.22)

$i=1,2,\cdots,n$ 。注意，由于 $g_{i}(\cdot)$ 的S状特性，函数 $h_{i}(\cdot)$ 满足

$$h _ {i} (x _ {i}) > 0, \forall x _ {i} \in (- V _ {M}, V _ {M})$$

系统的平衡点就是 $n$ 个联立方程

$$0 = \sum_ {j} T _ {i j} x _ {j} - \frac {1}{R _ {i}} g _ {i} ^ {- 1} (x _ {i}) + I _ {i}, \quad 1 \leqslant i \leqslant n$$

的根,它们由 S 状特性、线性电阻连接和输入电流决定。用 $u_{i}, i=1,2,\cdots,n$ 作为状态变量,可得到同样的状态模型。

![](image/28ec2a4a80b4b1764299cf81ac87b8353ab1bdcd2da24ec8db42e2a5ed1c1d45.jpg)

<details>
<summary>text_image</summary>

±v₁○─Rᵢ₁
±v₂○─Rᵢ₂
±v₃○─Rᵢ₃
⋮
±vₙ○─Rᵢₙ
Σ
uᵢ
Iᵢ Cᵢ ρᵢ
vᵢ
−vᵢ
</details>

图 1.8 霍普菲尔德人工神经网络

![](image/3bc8304003b43217d7d69de3d82612e032fbb5b1a8db9d246de26aef96949a7d.jpg)

<details>
<summary>text_image</summary>

g(u)
VM
u
-VM
</details>

图 1.9 霍普菲尔德网络中的典型放大器输入-输出特性

神经网络的稳定性分析严格取决于是否满足对称条件 $T_{ij} = T_{ji}$ ，4.2 节将给出一个当 $T_{ij} = T_{ji}$ 时的分析示例，而 9.5 节将给出一个 $T_{ij} \neq T_{ji}$ 的分析示例。
