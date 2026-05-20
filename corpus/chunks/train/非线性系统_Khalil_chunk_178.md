# 5.5 习题

5.1 证明两个L稳定(或有限增益L稳定)系统串联后仍是L稳定(或有限增益L稳定)系统。  
5.2 证明两个L稳定(或有限增益L稳定)系统并联后仍是L稳定(或有限增益L稳定)系统。  
5.3 考虑由无记忆函数 $y = u^{1/3}$ 定义的系统。

(a) 证明系统是零偏 $L_{\infty}$ 稳定的。  
(b) 对于任意正常数 a，证明系统为有限增益 $L_{\infty}$ 稳定的，且 $\gamma = a, \beta = (1/a)^{1/2}$ 。  
(c) 对上述两命题进行比较。

5.4 考虑由无记忆函数 $y = h(u)$ 定义的系统, 其中 $h: R^{m} \rightarrow R^{q}$ 为全局利普希茨的。当

(1) $h(0) = 0$

(2) $h(0)\neq 0$

时,对每个 $p\in[1,\infty]$ ,研究其 $L_{p}$ 稳定性。

5.5 试分析图 5.2 中各继电器特性的 $L_{\infty}$ 稳定性和 $L_{2}$ 稳定性。

![](image/930925d50abb3cc2c151bbdb3793b3f3c128aa7c881a90535c405bd977e0a90f.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(a) 具有迟滞的通断

![](image/0eeda75ac2f021ed4bdde7773786b6bdbf823e3f5213ce81aff38e294f8318ec.jpg)

<details>
<summary>text_image</summary>

Diagram showing a coordinate system with x and y axes, featuring directional arrows and labeled points on the u-axis.
</details>

(b) 具有死区和迟滞的通断

![](image/23749cd141bf42a54053fd8e107ae5341cd5467257762a270a22e34ad28fd9c1.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(c) 理想通断

![](image/a632e1ca5f49867f16a024e78a8461cafd44d6869f799746d9128e4eec5d8ec3.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(d) 具有死区的通断   
图 5.2 继电器特性

5.6 验证当 $V(t, x(t)) = 0$ 时， $D^{+}W(t)$ 满足式(5.12)。

提示: 利用习题 3.24 证明 $V(t+h, x(t+h)) \leqslant c_{4} h^{2} L^{2} \| u \|^{2}/2 + h o(h)$ ，其中当 h 趋于零时， $o(h)/h$ 趋于零。然后利用 $c_{4} \geqslant 2c_{1}$ 。

5.7 假设除将定理 5.1 的假设条件(5.10)改为

$$\| h (t, x, u) \| \leqslant \eta_ {1} \| x \| + \eta_ {2} \| u \| + \eta_ {3}, \quad \eta_ {3} > 0$$

外,其余假设条件都成立。证明系统是小信号有限增益 $L_{\infty}$ 稳定的(或当条件全局成立时,系统是 $L_{\infty}$ 稳定的),并求出式(5.11)中的 $\gamma$ 和 $\beta$ 。

5.8 假设定理 5.1 的假设条件除将式(5.10)改为式(5.20)外,其余假设条件都成立。证明系统是小信号 $L_{\infty}$ 稳定的(或当条件全局成立时,系统是 $L_{\infty}$ 稳定的)。

5.9 对于线性时变系统,试推导出与推论 5.2 类似的结论。

5.10 研究下列各系统的 $\mathcal{L}_{\infty}$ 稳定性和有限增益 $\mathcal{L}_{\infty}$ 稳定性：

(1) $\dot{x} = -(1 + u)x^3$ $y = x$

(2) $\begin{array}{rcl} \dot{x} & = & -(1 + u)x^3 - x^5 \\ y & = & x + u \end{array}$

(3) $\dot{x} = -x/(1 + x^{2}) + u$ $y = x/(1 + x^{2})$

(4) $\begin{array}{rcl}\dot{x} & = & -x - x^3 +x^2 u\\ y & = & x\sin u \end{array}$

5.11 研究下列各系统的 $L_{\infty}$ 稳定性和有限增益 $L_{\infty}$ 稳定性：

(1) $\dot{x}_1 = -x_1 + x_1^2 x_2,$

$\dot{x}_2 = -x_1^3 - x_2 + u, \quad y = x_1$

(2) $\dot{x}_{1} = -x_{1} + x_{2},$

$\dot{x}_2 = -x_1^3 - x_2 + u, \quad y = x_2$

(3) $\dot{x}_{1}=(x_{1}+u)(\|x\|_{2}^{2}-1),$
