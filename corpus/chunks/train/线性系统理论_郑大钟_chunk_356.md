# 习题

9.1 确定下列标量传递函数 $g(s)$ 的能控规范形实现和能观测规范形实现：

(i) $g(s) = \frac{4s^2 + 2s + 1}{3s^3 + 5s^2 + 2s + 3}$

(ii) $g(s) = \frac{(s + 1)(s + 3)}{(s + 2)(s + 4)(s + 6)}$

(iii) $g(s) = \frac{5s^3 + s^2 + 4s + 1}{2s^3 + 4s^2 + 6s + 3}$

9.2 确定下列传递函数矩阵 $G(s)$ 的能控形实现和能观测形实现：

(i) $G(s) = \left[\frac{1}{s + 1} \frac{1}{s^{2} + 3s + 2}\right]$

(ii) $G(s) = \begin{bmatrix} \frac{1}{s(s+1)} & \frac{2}{(s+2)} \\ \frac{2}{(s+1)} & \frac{1}{(s+1)} \end{bmatrix}$

9.3 定出下列传递函数矩阵 $G(s)$ 的任意两个最小实现：

$$
G (s) = \left[ \begin{array}{c c} \frac {2 s + 1}{s ^ {2} - 1} & \frac {s}{s ^ {2} + 5 s + 4} \\ \frac {1}{s + 3} & \frac {2 s + 5}{s ^ {2} + 7 s + 1 2} \end{array} \right]
$$

9.4 设有状态空间描述为:

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 2 & 1 \\ 0 & 1 & 0 \\ 0 & 3 & 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \\ 1 & 1 \end{array} \right] \boldsymbol {u} \\ \mathbf {y} = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 1 & 1 & 1 \end{array} \right] \mathbf {x} \\ \end{array}
$$

试判断：它是否为下列传递函数矩阵

$$
G (s) = \left[ \begin{array}{c c} 1 & 0 \\ 1 & - 2 (s - 1) \end{array} \right] \left[ \begin{array}{c c} 0 & - 2 (s - 1) ^ {2} \\ \frac {1}{2} (s - 2) & s ^ {2} + 4 s - 4 \end{array} \right] ^ {- 1}
$$

的一个实现和最小实现。

9.5 确定下列各右 MFD 的控制器形实现:

(i) $[s^2 - 1, s + 1]\begin{bmatrix} s^3 & s^2 - 1 \\ s + 1 & s^3 + s^2 + 1 \end{bmatrix}^{-1}$

(ii) $\left[ \begin{array}{ll}2s & 0\\ -s & s^2 \end{array} \right]\left[ \begin{array}{cc}0 & s^3 +4s^2 +5s + 2\\ (s + 2)^2 & s + 2 \end{array} \right]^{-1}$

9.6 求出下列传递函数矩阵 $G(s)$ 的任意两个维数不同的控制器形实现:

(i) $G(s) = \left[ \begin{array}{ll}\frac{1}{s^2 - 1} & \frac{s + 1}{s^2 + 5s + 4}\\ \frac{1}{s + 3} & \frac{s + 4}{s^2 + 7s + 12} \end{array} \right]$

(ii) $G(s)=\left[\begin{array}{ccc}\frac{2s^{2}+2s+1}{s^{2}-3}&\frac{s^{2}+4s+6}{s^{2}+s+1}\\ \frac{4s+5}{s+2}&\frac{3s^{2}+4s+1}{s^{2}+7s+12}\end{array}\right]$

9.7 确定下列各左 MFD 的观测器形实现:

(i) $\left[ \begin{array}{ccc} s^2 - 1 & 0 \\ 0 & s - 1 \end{array} \right]^{-1} \left[ \begin{array}{cc} 1 & s - 1 \\ 2 & s^2 \end{array} \right]$

(ii) $\left[ \begin{array}{ccc}0 & s^2 - 1\\ s - 1 & 0 \end{array} \right]^{-1}\left[ \begin{array}{ccc}s - 1 & 1 & s - 1\\ s + 1 & 0 & s + 1 \end{array} \right]$

9.8 给定传递函数矩阵 $G(s)$ 为:

$$
G (s) = \left[ \begin{array}{c c} \frac {1}{s + 1} & \frac {2}{s + 1} \\ \frac {1}{(s + 1) (s + 2)} & \frac {1}{s + 2} \end{array} \right]
$$

(i) 确定它的一个观测器形实现：

(ii) 确定它的一个能控性形实现。

9.9 证明：一个左 MFD $D_{L}^{-1}(s)N_{L}(s)$ 和其观测器形实现 $(A_{o}, B_{o}, C_{o})$ 之间成立如下的关系式：
