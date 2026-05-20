不难验证 $\Theta_{22}^{-1}(s)$ 的状态空间实现的系统阵是 $A + (B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}})X$ 。所以 $\Theta_{22}^{-1}(s) \in RH_{\infty}^{r \times r}$ 。

因此根据引理6.4.1, 由 $\Theta(s), M(s)$ 以及 $K(s)$ 构成的闭环系统是内部稳定的并且满足

$$\| T _ {z w} (s) \| _ {\infty} < 1, \tag {6.6.14}$$

当且仅当由 $M(s)$ 和 $K(s)$ 构成的系统是内部稳定的并且满足

$$\| T _ {v r} (s) \| _ {\infty} < 1. \tag {6.6.15}$$

这个结论表明，如果我们将 $M(s)$ 看做受控对象，那么此时的反馈控制器 $K(s)$ 是相应的输出反馈 $H_{\infty}$ 设计问题的解。可以验证， $M(s)$ 满足引理6.6.1的条件。所以，根据引理6.6.1, Riccati方程

$$(A + B _ {1} B _ {1} ^ {\mathrm{T}} X) \Pi + \Pi (A + B _ {1} B _ {1} ^ {\mathrm{T}} X) ^ {\mathrm{T}} + \Pi (F ^ {\mathrm{T}} F - C _ {2} ^ {\mathrm{T}} C _ {2}) \Pi + B _ {1} B _ {1} ^ {\mathrm{T}} = 0 \tag {6.6.16}$$

具有半正定解 $\Pi$ ，且

$$A _ {\Pi} = A ^ {\mathrm{T}} + X B _ {1} B _ {1} ^ {\mathrm{T}} + (F ^ {\mathrm{T}} F - C _ {2} ^ {\mathrm{T}} C _ {2}) \Pi \tag {6.6.17}$$

是稳定阵．分别定义与 Riccati 方程 (6.6.4)，(6.6.16) 对应的 Hamilton 矩阵如下：

$$
H _ {Y} = \left[ \begin{array}{c c} A ^ {\mathrm{T}} & C _ {1} C _ {1} ^ {\mathrm{T}} - C _ {2} C _ {2} ^ {\mathrm{T}} \\ - B _ {1} ^ {\mathrm{T}} B _ {1} & - A \end{array} \right],

H _ {\Pi} = \left[ \begin{array}{c c} (A + B _ {1} B _ {1} ^ {\mathrm{T}} X) ^ {\mathrm{T}} & F ^ {\mathrm{T}} F - C _ {2} ^ {\mathrm{T}} C _ {2} \\ - B _ {1} B _ {1} ^ {\mathrm{T}} & - (A + B _ {1} B _ {1} ^ {\mathrm{T}} X) \end{array} \right],
$$

则有

$$
T ^ {- 1} H _ {\Pi} T = H _ {Y}, \quad T = \left[ \begin{array}{c c} - I & X \\ 0 & I \end{array} \right]. \tag {6.6.18}
$$

因此，若 Riccati 方程 (6.6.4) 有半正定解 $Y$ ，使得 $A_{Y} = A^{\mathrm{T}} + (C_{1}^{\mathrm{T}}C_{1} - C_{2}^{\mathrm{T}}C_{2})Y$ 是稳定阵，那么由

$$
H _ {Y} \left[ \begin{array}{l} I \\ Y \end{array} \right] = \left[ \begin{array}{l} I \\ Y \end{array} \right] A _ {Y} \tag {6.6.19}
$$

得

$$
H _ {\Pi} T \left[ \begin{array}{c} I \\ Y \end{array} \right] = H _ {\Pi} \left[ \begin{array}{c} I - X Y \\ Y \end{array} \right] = \left[ \begin{array}{c} I - X Y \\ Y \end{array} \right] A _ {Y}.
$$

根据定理假设可知， $I - XY$ 是非奇异阵，于是由上式得

$$
H _ {\Pi} \left[ \begin{array}{l} I \\ \Pi \end{array} \right] = \left[ \begin{array}{l} I \\ \Pi \end{array} \right] (I - X Y) A _ {Y} (I - X Y) ^ {- 1},
$$

即 Riccati 方程 (6.6.16) 有半正定解

$$\Pi = Y (I - X Y) ^ {- 1},$$

且 $A_{\Pi} = (I - XY)A_{Y}(I - XY)^{-1}$ 是稳定阵.

因此根据引理 6.6.1，广义受控对象 (6.6.1) 所对应的 $H_{\infty}$ 标准设计问题有解，且理想的控制器可以根据引理 6.6.1 求得，如式 (6.6.9).

必要性. 设受控对象 (6.6.1) 对应的 $H_{\infty}$ 设计问题有解, 且 $u = K(s)y$ 是一个解. 由于

$$
u = K (s) y = K _ {F I} (s) \left[ \begin{array}{l} x \\ w \end{array} \right], \tag {6.6.20}
$$

所以该闭环系统可以表示为
