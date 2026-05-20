# 定义6.1 对于系统 $y = h(t,u)$

- 如果 $u^{\mathrm{T}}y \geqslant 0$ ，则系统是无源的。  
- 如果 $u^{\mathrm{T}}y = 0$ ，则系统是无损耗的。  
- 如果对于某个函数 $\varphi$ ，满足 $u^{\mathrm{T}}y \geqslant u^{\mathrm{T}}\varphi(u)$ ，则系统是输入前馈无源的。  
- 如果 $\forall u \neq 0$ ，使 $u^{\mathrm{T}}y \geqslant u^{\mathrm{T}}\varphi(u)$ ，且 $u^{\mathrm{T}}\varphi(u) > 0$ ，则系统是严格输入无源的。  
- 如果对于某个函数 $\rho$ ，满足 $u^{\mathrm{T}}y \geqslant y^{\mathrm{T}}\rho(y)$ ，则系统是输出反馈无源的。

\- 如果 $\forall y \neq 0$ ，使 $u^{\mathrm{T}}y \geqslant y^{\mathrm{T}}\rho(y)$ ，且 $y^{\mathrm{T}}\rho(y) > 0$ ，则系统是严格输出无源的。

在各种情况下,不等式对所有 $(t,u)$ 均成立。

下面考虑标量函数 $y = h(t, u)$ ，对所有 $(t, u)$ 满足不等式

$$\alpha u ^ {2} \leqslant u h (t, u) \leqslant \beta u ^ {2} \tag {6.2}$$

其中 $\alpha$ 与 $\beta$ 是实数，且 $\beta \geqslant \alpha$ 。该函数的曲线属于一个扇形区域，其边界为直线 $y = \alpha u$ 和 $y = \beta u$ ，我们说 $h$ 属于扇形区域 $[\alpha, \beta]$ 。图6.6所示为当 $\beta > 0, \alpha$ 符号不同时的扇形区域 $[\alpha, \beta]$ 。如果满足严格不等式(6.2)的任何一边，我们说 $h$ 明显属于扇形区域 $(\alpha, \beta], [\alpha, \beta)$ 或 $(\alpha, \beta)$ 。将图6.6与图6.4和图6.5的扇形区域比较，说明扇形区域 $[\alpha, \beta]$ 内的函数是输入前馈无源性与严格输出无源性的结合，因为 $[\alpha, \beta]$ 是 $[\alpha, \infty]$ 和 $[0, \beta]$ 的交集。事实上可以证明，通过输入前馈和输出反馈序列运算，可以将这样的函数转换为属于扇形区域 $[0, \infty]$ 的函数。在证明之前，我们将扇形区域的定义拓展到向量情况，为此，注意到式(6.2)等价于对于所有 $(t, u)$ ，有

$$[ h (t, u) - \alpha u ] [ h (t, u) - \beta u ] \leqslant 0 \tag {6.3}$$

在向量情况下,我们首先考虑解耦为式(6.1)函数 $h(u,t)$ , 假设每个分量 $h_{i}$ 满足扇形区域条件式(6.2), 式中 $\alpha_{i}$ 和 $\beta_{i}$ 为常数, 且 $\beta_{i} > \alpha_{i}$ 。取

$$K _ {1} = \operatorname{diag} \left(\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {p}\right), \quad K _ {2} = \operatorname{diag} \left(\beta_ {1}, \beta_ {2}, \dots , \beta_ {p}\right)$$

容易看出,对于所有 $(t,u)$ ,有

$$[ h (t, u) - K _ {1} u ] ^ {\mathrm{T}} [ h (t, u) - K _ {2} u ] \leqslant 0 \tag {6.4}$$

注意 $K = K_{2} - K_{1}$ 是正定对称(对角)阵。不等式(6.4)对于更一般的向量函数也成立。例如，假设 $h(t,u)$ 对于所有 $(t,u)$ 满足不等式

$$\| h (t, u) - L u \| _ {2} \leqslant \gamma \| u \| _ {2}$$

取 $K_{1} = L - \gamma I, K_{2} = L + \gamma I$ ，可写出

$$[ h (t, u) - K _ {1} u ] ^ {\mathrm{T}} [ h (t, u) - K _ {2} u ] = \| h (t, u) - L u \| _ {2} ^ {2} - \gamma^ {2} \| u \| _ {2} ^ {2} \leqslant 0$$

同样, $K=K_{2}-K_{1}$ 是正定对称(对角)阵,因此可利用不等式(6.4)作为向量情况中扇形区域 $\left[K_{1},K_{2}\right]$ 的定义,其中 $K=K_{2}-K_{1}$ 为正定对称矩阵。下一定义对扇形区域一词做了总结。

![](image/fe86d3fdfc7b58c6c241264606d3f70b5d41aa44405b0eec49a368365c5295d6.jpg)

<details>
<summary>text_image</summary>

y
y=βu
y=αu
u
</details>

(a) $\alpha > 0$
