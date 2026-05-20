对不允许有阻塞，即无阻塞的系统，建模需引入与控制有关的 $B$ 阵：把 $\hat{x}_0(j)$ 记为 $u(j)$ ，即把投入 $J_j$ 的时刻作为控制量。因为必须有 $u(j) \geqslant \hat{x}_1(j - 1)$ ，所以 $\hat{x}_0(j) = u(j) \oplus \hat{x}_1(j - 1)$ 。把它代入 $r = 1$ 的引理11.8.1证明中的递推式，即可导出 $B(j)$ 为

$$\boldsymbol {B} (j) = \left[ P _ {1} (j), P _ {1 2} (j), \dots , P _ {1 m} (j) \right] ^ {\mathrm{T}},$$

且可得状态方程

$$\boldsymbol {x} (j) = \boldsymbol {A} (j) \boldsymbol {x} (j - 1) \oplus \boldsymbol {B} (j) u (j). \tag {11.8.4}$$

这样建模得到的 $A(j), B(j)$ 阵比文献[10]中描写两批间关系的 $A, B$ 阵简单得多，这是因为复杂的批间关系已用式(11.8.2)中的乘法记号 $\prod$ 来简单表达，而不具体算出 $A_N$ 的每个元.

式 (11.8.4) 中的 $u(j)$ 如何取到最优控制？解决这问题的思路并不复杂。无阻塞的充要条件易知是： $m_{i}$ 完成 $J_{j}$ 的时刻大于或等于 $m_{i+1}$ 完成 $J_{j-1}$ 的时刻，这意味着

$$
\begin{array}{l} u (j) \geqslant \widehat {x} _ {1} (j - 1), \\ u (j) P _ {1 1} (j) \geqslant \widehat {x} _ {2} (j - 1), \\ u (j) P _ {1, m - 1} (j) \geqslant \widehat {x} _ {m} (j - 1), \\ \end{array}
$$

■
■
■

也就是

$$u (j) \geqslant \sum_ {r = 1} ^ {m - 1} p _ {1, r} (j) ^ {- 1} \widehat {x} _ {r + 1} (j - 1) \oplus 0 \cdot \widehat {x} _ {1} (j - 1).$$

为了使效率达到最高，要求 $u(j)$ 尽量小，因此上式中 $\geqslant$ 取成 $= 0$ ， $u(j)$ 是无阻塞最优控制，即 $u(j)$ 可以取成状态反馈 $u(j) = K(j)x(j - 1)$ ，其中

$$\boldsymbol {K} (j) = [ 0, P _ {1 1} (j) ^ {- 1}, P _ {1 2} (j) ^ {- 1}, \dots , P _ {1, m - 1} (j) ^ {- 1} ]. \tag {11.8.5}$$

综上所述，我们已证明了如下定理：

定理 11.8.1 无存储器时，系统 (11.8.4) 的无阻塞最优控制可由状态反馈 $u(j)=K(j)x(j-1)$ 来实现，其中 $K(j)$ 阵如式 (11.8.5) 所示。令

$$
\left\{ \begin{array}{l} \tilde {\boldsymbol {A}} (j) = \boldsymbol {A} (j) \oplus \boldsymbol {B} (j) \boldsymbol {K} (j), \\ \boldsymbol {A} _ {N} = \prod_ {j = 1} ^ {N} \tilde {\boldsymbol {A}} (j), \end{array} \right. \tag {11.8.6}
$$

则可得到式（11.8.1）形式的批量生产的状态方程，并实现无阻塞最优控制。这里 $j = 1$ 时 $J_{j - 1}$ 表示上一批最后一个工件。

现在来讨论最优调度。由于“单位时间的最大利润”中分母是系统周期，所以必须分析系统的周期。

先分析无阻塞最优控制下的系统周期与最优调度问题. 对式 (11.8.6) 定义的系统, 由 $u(j)$ 的定义与系统无阻塞易知

$$\boldsymbol {x} (j) = u (j) \boldsymbol {B} (j).$$

由于 $u(j + 1) = K(j + 1)x(j)$ ，所以有

$$u (j + 1) = u (j) K (j + 1) B (j),u (j + 1) u (j) ^ {- 1} = K (j + 1) B (j).$$

因为无阻塞，对同一个工件，进料时刻 $u$ 与完成加工时刻 $\hat{x}_m$ 差同一个常数 $p_{1m}$ ，所以 $u(j + N)u(j)^{-1}$ 等于批加工周期 $\lambda$ 。由上式得

$$\lambda = \prod_ {j = 1} ^ {N} K (j + 1) B (j).$$

上式说明 $\lambda$ 与 $A(j)$ 无关．通过计算也表明 $A(j) \oplus B(j)K(j) = B(j)K(j)$ ，所以也与 $A(j)$ 无关．综上所述，已证得以下定理：

定理 11.8.2 式 (11.8.1). (11.8.6) 描写的无阻塞最优控制系统有批生产周期

$$\lambda = \prod_ {j = 1} ^ {N} K (j + 1) B (j).$$

用普通运算表示，最优调度问题中的目标函数有以下形式：

$$f = \sum_ {i = 1} ^ {n} W _ {i} M _ {i} / \left(\sum_ {i = 1} ^ {n} \alpha_ {i} M _ {i} + \beta\right).$$
