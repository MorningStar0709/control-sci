# 例3.6 频率响应

对于例 3.1 中的系统，求其正弦输入 $u = A \cos(\omega t)$ 的系统响应，即：

(1) 求频率响应，并画出 k=1 时的频率响应图。  
(2) 确定系统在 k=1 时，对于正弦输入 $u(t)=\sin(10t)$ 的全响应。

解答。在例 3.4 中，我们已得到系统的传递函数。为了求解频率响应，令 $s = j\omega$ ，那么

$$H (s) = \frac {1}{s + k} \Rightarrow H (\mathrm{j} \omega) = \frac {1}{\mathrm{j} \omega + k}$$

由此可得

$$M = \left| \frac {1}{\mathrm{j} \omega + k} \right| = \frac {1}{\sqrt {\omega^ {2} + k ^ {2}}}, \quad \varphi = - \arctan \left(\frac {\omega}{k}\right)$$

根据式 $(3.28)$ ，正弦输入信号的系统响应为

$$y (t) = A M \cos (\omega t + \varphi) \tag {3.29}$$

M 通常称为幅值比， $\varphi$ 称为相位，它们都是输入频率 $\omega$ 的函数。以下的 Matlab 程序可以用于计算 k=1 时的幅值比和相位，如图 3.4 所示。在 Matlab 中，logspace 命令用来设置频率范围(对数刻度)，bode命令用来计算频率响应。因为这种描述频率响应的方法(在对数坐标上)是由H.W.伯德提出的；所以该频率图也称为“伯德图” $^{①}$ （见6.1节）。

k = 1;
tf=('s'); % define Laplace variable
sysH = 1/(s+k); % define system by its transfer function
w = logspace(-2,2); % set frequency w to 50 values from $10^{-2}$ to $10^{+2}$ [mag,phase] = bode(sysH,w); % compute frequency response
loglog(w,squeeze(mag)); % log-log plot of magnitude
semilogx(w,squeeze(phase)); % semi-log plot of phase

![](image/fc27473c20e1d47653b55f0ba1ee22ac8877e3b9ffb24c33d2a1d4182093e9e2.jpg)

<details>
<summary>line</summary>

| ω (rad/s) | M |
| --- | --- |
| 10^-2 | 1.0 |
| 10^-1 | 1.0 |
| 10^0 | 0.5 |
| 10^1 | 0.1 |
| 10^2 | 0.01 |
</details>

![](image/f50d54eadf228ade9d647056bdcaefdd798e1a9e90e71de358f6fda86daecfbc.jpg)

<details>
<summary>line</summary>

| ω (rad/s) | φ (°) |
| --- | --- |
| 10⁻² | 0 |
| 10⁻¹ | -20 |
| 10⁰ | -60 |
| 10¹ | -85 |
| 10² | -90 |
</details>

图 3.4 k=1 时的频率响应

作为式(3.18)的推广，我们来研究信号 $f(t)$ 的拉普拉斯变换

$$F (s) = \int_ {- \infty} ^ {+ \infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {3.30}$$

从而推广频率响应。

如果将该定义用于 $u(t)$ 和 $y(t)$ ，并应用卷积积分，即式(3.13)，可得

$$Y (s) = H (s) U (s) \tag {3.31}$$

其中： $Y(s)$ 和 $U(s)$ 分别是 $y(t)$ 和 $u(t)$ 的拉普拉斯变换。

与傅里叶变换只关注系统的稳态响应相比，式(3.30)的拉普拉斯变换是用来研究反馈系统的全响应特性，包括暂态响应，即系统对初始条件或突然施加信号的时间响应。在控制领域，普遍遇到的问题是求系统对于输入 $u(t)$ 的输出响应 $y(t)$ ，以及系统模型。应用式(3.30)，我们就有了计算线性时不变系统输入的拉普拉斯变换和系统传递函数拉普拉斯变换的方法，而由式(3.31)可知，输出的拉普拉斯变换可为两者之积。如果想得到输出的时间函数，就需要对 $Y(s)$ 进行反变换得到拉普拉斯反变换式。这一步通常不进行明确说明。然而，明白由 $Y(s)$ 如何得到 $y(t)$ 非常重要，因为它能够使我们比较深入地了解一般线性系统的性能。因此，对于给定的线性系统，其传递函数为 $H(s)$ ，输入信号为 $u(t)$ ，应用拉普拉斯变换来确定 $y(t)$ 步骤如下。

步骤1)确定系统的传递函数： $H(s) = \mathcal{L}\{$ 系统脉冲响应}。用以下步骤计算 $H(s)$ 。

（a）对运动方程进行拉普拉斯变换。在这个过程中，拉普拉斯变换表格是经常用到的。
