这里选步长因子 $\alpha^{K}=1$ 。如此继续下去，直至指标函数随迭代变化很小为止。

图 7-1 和图 7-2 表示了控制和状态的初始值和第一次迭代值, 可以看到第一次迭代 $x(t)$ 就几乎收敛到最优值, $u^{1}(t)$ 与最优值还有差异, 而且一般说来愈接近最优值收敛愈慢。

![](image/7251fc84871b28d23d515f052233f7d0a95dbf1d624a95a748a90b8a76ac5f4e.jpg)

<details>
<summary>text_image</summary>

u
最优值
u¹(t)
u⁰(t)
O
1 t
</details>

图7-1 用梯度法寻找最优控制  
![](image/7df2bd80ac514964ecddf57c5eb543b36f6e7742aa483f6251e7b79b2aad2bca.jpg)

<details>
<summary>text_image</summary>

x
0
x⁰(t)
x¹(t)和最优值
O
t
</details>

图7-2 最优状态的求解

梯度法应用得比较多,它的优点是:(1)简单,编制程序容易;(2)计算稳定可靠。缺点是:(1)在接近最优解时,迭代收敛很慢,为改善收敛性可用共轭梯度法和二阶变分法等;(2)不能区分局部极小和全局极小;(3)对控制变量受约束,终端状态受约束的情况不能直接处理。对于这种有约束的情况可用约束梯度法或惩罚函数法(代价函数法)加以处理。

约束梯度法可处理如下的不等式约束：

$$a _ {i} \leqslant u _ {i} (t) \leqslant b _ {i} \quad i = 1, 2, \dots , m \tag {7-15}$$

首先,对于任何控制 $\alpha$ ,定义约束算子 $C_{u}$

$$
u _ {i} (t) = C _ {u} \hat {u} _ {i} (t) = \left\{ \begin{array}{c c} a _ {i} & \hat {u} _ {i} (t) \leqslant a _ {i} \\ \hat {u} _ {i} (t) & a _ {i} <   \hat {u} _ {i} (t) <   b _ {i} \\ b _ {i} & \hat {u} _ {i} (t) \geqslant b _ {i} \end{array} \right. \tag {7-16}
$$

显然 $u_{i}(t), i=1,2,\cdots,m$ 满足约束，即

$$\boldsymbol {u} = C _ {u} \hat {\boldsymbol {u}} \tag {7-17}$$

满足约束, 其中 $\boldsymbol{u} = \left[u_{1} \cdots u_{m}\right]^{\mathrm{T}}, \hat{\boldsymbol{u}} = \left[\hat{u}_{1} \cdots \hat{u}_{m}\right]^{\mathrm{T}}$ 。再由 $\hat{u}$ 用无约束的梯度法求解, 在每一次迭代中得出 $\hat{u}$ , 然后用 $u = C_{u} \hat{u}$ 代替, 再进行下一次迭代。

惩罚函数法可处理如下形式的约束：

$$g _ {i} (X, u, t) \leqslant 0 \quad i = 1, 2, \dots , q \tag {7-18}h _ {i} \left(\boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}}\right) = 0 \quad i = 1, 2, \dots , l \tag {7-19}$$

这时，将性能指标 $J(u)$ 增广为 $\overline{J}(u)$ 。

$$\bar {J} (\boldsymbol {u}) = J (\boldsymbol {u}) + \mu \int_ {t _ {0}} ^ {t _ {f}} \sum_ {i = 1} ^ {q} \left[ g _ {i} (\boldsymbol {X}, \boldsymbol {U}, t) \right] ^ {2} \delta \left(g _ {i}\right) d t +\sum_ {i = 1} ^ {l} N _ {i} \left[ h _ {i} \left(\boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}}\right) \right] ^ {2} \tag {7-20}$$

其中， $\mu>0,N_{i}>0,$

$$
\delta \left(g _ {i}\right) = \left\{ \begin{array}{l l} 0 & g _ {i} \leqslant 0 \\ 1 & g _ {i} > 0 \end{array} \right. \tag {7-21}
$$

显然，当满足约束时， $\overline{J}(\boldsymbol{u})$ 中后两项为0。当不满足约束时，后两项将使 $\overline{J}(\boldsymbol{u})$ 增大，故称为惩罚函数。在迭代过程中，逐次增大 $\mu$ 和 $N_{i}$ 。显然当 $\mu$ 和 $N_{i}$ 很大时，所求得的 $\overline{J}(\boldsymbol{u})$ 的无约束最优控制近似于 $J(\boldsymbol{u})$ 的有约束最优控制。

（二）共轭梯度法 用共轭梯度法寻找最优控制时是沿着所谓共轭梯度向量的方向进行的。为了说明共轭梯度的意义，先从求函数极值问题的共轭梯度法开始，再推广到求泛函极值问题。
