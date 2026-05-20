# 习题 1.9

1.9.1 对给定的开环系统

$$
\left\{ \begin{array}{l} \dot {x} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ - 1 & - 2 & - 3 \end{array} \right] x + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] u, \\ y = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] x, \end{array} \right.
$$

(i) 试求反馈控制律 $u = -Kx + Lv$ 使上述系统的闭环系统实现积分解耦控制；  
(ii) 试求反馈控制律 $u = -Kx + Lv$ ，使上述系统的闭环系统实现解耦控制，并有形如 $\mathrm{diag}\left(\frac{1}{s + 1},\frac{1}{s + 2}\right)$ 的传递函数.

1.9.2 对给定的开环系统

$$
\left\{ \begin{array}{l} \dot {x} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 1 \\ - 1 & - 2 & - 3 \end{array} \right] x + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] u, \\ y = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] x, \end{array} \right. \tag {1.9.12}
$$

(i) 问能否找到 $(K, L)$ 使在形如 $u = -Kx + Lv$ 的控制下，闭环系统实现输入输出解耦；  
(ii) 若能，找 $(K, L)$ ，使在形如 $u = -Kx + Lv$ 的控制下，闭环系统实现输入输出解耦，并使闭环传递函数有极点 -1 和 -2；  
(iii) 能否找到 $(K, L)$ 使在形如 $u = -Kx + Lv$ 的控制下，使闭环系统实现输入输出解耦，并使闭环传递函数有极点-2和-2，或者 $-1 \pm j$ ;  
(iv) 证明 (ii) 中实现的闭环系统不是能控能观的;  
(v) 对于开环系统 (1.9.12)，证明找不到 $(K, L)$ 使在形如 $u = -Kx + Lv$ 的控制下，闭环系统既实现输入输出解耦，又能控能观.

1.9.3 对开环系统 (1.9.1), $E, d_{i} (i = 1, \cdots, m)$ 如定理 1.9.1 中定义，并假定 $E$ 满秩.

(i) 证明: $d_{1} + d_{2} + \cdots + d_{m} \leqslant n - m$ ;   
(ii) 若 $d_{1} + d_{2} + \cdots + d_{m} = n - m,$ 问：  
(a) 能否在实现输入输出解耦的同时，对闭环传递函数任意配置 $n$ 个互异实极点；  
(b) 能否在实现输入输出解耦的同时，对闭环传递函数配置一个 $n$ 重极点；  
(c) 能否在实现输入输出解耦的同时，使闭环系统能控能观，且使闭环特征值全在左半平面.

1.9.4 对开环系统 (1.9.1), $E, d_{i} (i = 1, \cdots, m)$ 如定理 1.9.1 中定义，并假定 $\pmb{E}$ 满秩。证明：找不到 $(K, L)$ 使在形如 $u = -Kx + Lv$ 的控制下，闭环系统有如下形式的传递函数：

$$
\text {(i)} \left( \begin{array}{c c c} \frac {1}{s ^ {d _ {1} + 2} + \alpha_ {1 1} s ^ {d _ {1} + 1} + \cdots + \alpha_ {1 (d _ {1} + 2)}} & & \\ & \ddots & \\ & & \frac {1}{s ^ {d _ {m} + 2} + \alpha_ {m 1} s ^ {d _ {m} + 1} + \cdots + \alpha_ {m (d _ {m} + 2)}} \end{array} \right);

\text {(ii)} \left( \begin{array}{c c c} \frac {1}{s ^ {d _ {1}} + \alpha_ {1 1} s ^ {d _ {1} - 1} + \cdots + \alpha_ {1 d _ {1}}} & & \\ & \ddots & \\ & & \frac {1}{s ^ {d _ {m}} + \alpha_ {m 1} s ^ {d _ {m} - 1} + \cdots + \alpha_ {m d _ {m}}} \end{array} \right).
$$

1.9.5 对给定的开环系统

$$
\left\{ \begin{array}{l} \dot {x} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right] x + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \\ 1 & 0 \end{array} \right] u, \\ y = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right] x, \end{array} \right.
$$

试求反馈控制律 $u = -Kx + Lv$ ，使上述系统的闭环实现静态解耦。
