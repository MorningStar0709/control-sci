$$[ \dot {\boldsymbol {K}} (t) + \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) +\boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \boldsymbol {Q} (t) ] \boldsymbol {X} (t) = \boldsymbol {0}$$

上式对任意 $X(t)$ 都应成立，故方括号内的项应为0，这就得出

$$\dot {\boldsymbol {K}} (t) = - \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) +\boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \boldsymbol {Q} (t) \tag {5-14}$$

上式是 $K(t)$ 的非线性矩阵微分方程，称为黎卡提矩阵微分方程。一般来说得不出 $K(t)$ 的解析表达式，但可用计算机程序算出 $K(t)$ 的数值解。

为了求解 $K(t)$ ，要知道它的边界条件。比较式(5-11)和(5-10)可知

$$\boldsymbol {K} \left(t _ {\mathrm{f}}\right) = \boldsymbol {P} \tag {5-15}$$

因此可从 $t_{\mathrm{f}}$ 到 $t_0$ 逆时间积分黎卡提微分方程，求出 $\pmb {K}(t)$ 。由式(5-9)和(5-11)就可构成最优反馈控制

$$\boldsymbol {U} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \boldsymbol {X} (t) = - \boldsymbol {G} (t) \boldsymbol {X} (t) \quad (5 - 1 6)$$

$G(t) = R^{-1}(t)B^{\mathrm{T}}(t)K(t)$ 又称为最优反馈增益矩阵。最优反馈系统的结构图如图5-2所示。

![](image/d090a955b04ede2a8b7f2419ab11cdd1d3c38501c06cc4d0a45b9e88d3a8d5ad.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["-R⁻¹(t)Bᵀ(t)"] -->|U(t)| B["ẋ(t)=A(t)X(t)+B(t)U(t)"]
    B -->|X(t)| C
    C --> D["K(t)"]
    D --> A
```
</details>

图5-2 最优反馈系统的结构图

注意到 $K(t)$ 与状态 $X(t)$ 无关，故可在系统未运行前将 $\pmb{R}^{-1}(t)\pmb{B}^{\mathrm{T}}(t)\pmb{K}(t)$ 先计算出来（称为离线计算），把它存储在计算机中。在系统运行时，将 $-\pmb{R}^{-1}(t)\pmb{B}^{\mathrm{T}}(t)\pmb{K}(t)$ 从计算机存储元件中取出，与同一时刻测量到的 $X(t)$ 相乘，就可构成最优控制 $U(t)$ 。由此可见，系统运行时的计算量（称为在线计算量）只是一个乘法计算，故可用简单的微计算机来完成。
