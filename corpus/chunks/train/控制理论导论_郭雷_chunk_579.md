$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial x} f (x) + \frac {1}{2 \gamma_ {0}} \left(\frac {\partial J}{\partial x}\right) G _ {1} (x) G _ {1} ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}}, \\ - \frac {1}{2} \left(\frac {\partial J}{\partial x}\right) G _ {2} (x) R _ {2} ^ {- 1} G _ {2} ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}} + \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x) = 0, \\ J (0) = 0 \end{array} \right. \tag {7.5.37}
$$

的正解.

不难证明，当系统(7.5.29)满足完全能检测性条件（即 $\lim_{t\to +\infty}h_1(x(t)) = 0\Longrightarrow$ $\lim_{t\to +\infty}x(t) = 0)$ 时，方程(7.5.36）中的 $u^{*}(x) = -R_{2}^{-1}G_{2}^{\mathrm{T}}(x)\left(\frac{\partial J^{*}(x)}{\partial x}\right)^{\mathrm{T}}$ 使系统(7.5.29）的 $H_{\infty}$ 次优问题可解（见文献[7]).

综上所述可得：

定理 7.5.3 对任意给定的 $\gamma_{0} > 0$ ，当受外干扰的仿射非线性控制系统 (7.5.29) 完全能检测时，状态反馈形式的控制规律

$$u ^ {*} (x) = - R _ {2} ^ {- 1} G _ {2} ^ {\mathrm{T}} (x) \left(\frac {\partial J ^ {*} (x)}{\partial x}\right) ^ {\mathrm{T}}$$

使系统 (7.5.29) 的 $H_{\infty}$ 控制次优问题可解，其中 $J^{*}(x)$ 是式 (7.5.37) 的正解.

推论7.5.3 当 $J^{*}(x)$ 是下列带终端点条件的偏微分不等式：

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial x} f (x) + \frac {1}{2 \gamma_ {0}} \left(\frac {\partial J}{\partial x}\right) G (x) G ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}} \\ - \frac {1}{2} \left(\frac {\partial J}{\partial x}\right) G _ {2} (x) R _ {2} ^ {- 1} G _ {2} ^ {\mathrm{T}} (x) \left(\frac {\partial J}{\partial x}\right) ^ {\mathrm{T}} + \frac {1}{2} h ^ {\mathrm{T}} (x) h (x) \leqslant 0 \\ J (0) = 0 \end{array} \right.
$$

的正定解时，定理7.5.3成立.

注7.5.5 定理7.5.3中，系统(7.5.29)的 $H_{\infty}$ 控制次优问题的解依赖偏微分方程(或偏微分不等式). 当 $J^{*}(x)$ 在 $x = 0$ 的某邻域 $\Omega$ 内或含内点 $x = 0$ 的区域 $\mathcal{D}$ 内存在时，相应的 $H_{\infty}$ 控制次优问题在 $\Omega$ 内或在 $\mathcal{D}$ 内可解．但一般难于得到 $H_{\infty}$ 控制的全局古典解.

注7.5.6 当系统(7.5.29)的状态不能全部被量测时，需要寻求量测输出反馈形式或动态输出反馈形式的控制规律，在一定假设下，能够得到这类控制规律存在的充分条件，但构造控制规律却不容易.
