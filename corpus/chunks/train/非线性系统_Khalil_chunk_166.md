这样,对于所有 a<1, 当 $c_{1}=\lambda_{\min}(P)$ , $c_{2}=\lambda_{\max}(P)$ , $c_{3}=1-a$ , $c_{4}=2\|P\|_{2}=2\lambda_{\max}(P)$ 时, V 全局满足式(5.6)到式(5.8)。当 $L=\eta_{1}=1$ , $\eta_{2}=0$ 时, 函数 f 和 h 全局满足式(5.9)和式(5.10)。因此, 对于每个 $x_{0}\in R^{2}$ 和 $p\in[1,\infty]$ , 系统是有限增益 $L_{p}$ 稳定的。

更一般的情况是系统(5.5)的原点一致渐近稳定的,这就需要研究 $L_{\infty}$ 稳定性。下面的两个定理分别给出了小信号 $L_{\infty}$ 稳定性和 $L_{\infty}$ 稳定性的条件。

定理 5.2 考虑系统(5.3)\~(5.4)，取 r>0，使得 $\{\|x\|\leqslant r\}\subset D$ 。假设

\- $x = 0$ 是系统(5.5)的一致渐近稳定平衡点, 且存在李雅普诺夫函数 $V(t,x)$ , 对于所有 $(t,x) \in [0,\infty) \times D$ 和 $\kappa$ 类函数 $\alpha_{1}$ 到 $\alpha_{4}$ , 满足

$$\alpha_ {1} (\| x \|) \leqslant V (t, x) \leqslant \alpha_ {2} (\| x \|) \tag {5.16}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, 0) \leqslant - \alpha_ {3} (\| x \|) \tag {5.17}\left\| \frac {\partial V}{\partial x} \right\| \leqslant \alpha_ {4} (\| x \|) \tag {5.18}$$

\- 对于所有 $(t, x, u) \in [0, \infty) \times D \times D_u, \mathcal{K}$ 类函数 $\alpha_5$ 到 $\alpha_7$ 和非负常数 $\eta, f$ 和 $h$ 满足不等式

$$\left\| f (t, x, u) - f (t, x, 0) \right\| \leqslant \alpha_ {5} (\| u \|) \tag {5.19}\left\| h (t, x, u) \right\| \leqslant \alpha_ {6} (\| x \|) + \alpha_ {7} (\| u \|) + \eta \tag {5.20}$$

则对于每个满足 $\| x_0\| \leqslant \alpha_2^{-1}(\alpha_1(r))$ 的 $x_0$ ，系统(5.3)\~(5.4)是小信号 $\mathcal{L}_{\infty}$ 稳定的。证明： $V$ 沿系统(5.3)轨线的导数满足

$$
\begin{array}{l} \dot {V} (t, x, u) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x, 0) + \frac {\partial V}{\partial x} [ f (t, x, u) - f (t, x, 0) ] \\ \leqslant - \alpha_ {3} (\| x \|) + \alpha_ {4} (\| x \|) \alpha_ {5} (\| u \|) \\ \leqslant - (1 - \theta) \alpha_ {3} (\| x \|) - \theta \alpha_ {3} (\| x \|) + \alpha_ {4} (r) \alpha_ {5} \left(\sup _ {0 \leqslant t \leqslant \tau} \| u (t) \|\right) \\ \end{array}
$$

其中 $0 < \theta < 1$ 。设定 $\mu = \alpha_{3}^{-1} \left( \frac{\alpha_{4}(r)\alpha_{5}\left(\sup_{0 \leqslant t \leqslant \tau} \|u(t)\|\right)}{\theta} \right)$

并选取足够小的 $r_u > 0$ ，使得当 $\sup_{0 \leqslant t \leqslant \tau} \| u(t) \| \leqslant r_u$ 时，满足 $\{\| u \| \leqslant r_u\} \subset D$ 和 $\mu \leqslant \alpha_2^{-1}(\alpha_1(r))$ 。于是，

$$\dot {V} \leqslant - (1 - \theta) \alpha_ {3} (\| x \|), \quad \forall \| x \| \geqslant \mu$$

应用定理 4.18, 由式(4.42)和式(4.43)可推得对所有 $0 \leqslant t \leqslant \tau$ , $\|x(t)\|$ 满足不等式
