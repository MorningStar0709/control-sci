# 习题

11.1 对于按顺序 $g_{1}(s) - g_{2}(s)$ 的串联系统，其中传递函数分别为：

$$g _ {1} (s) = \frac {s + 3}{s ^ {2} + 3 s + 2}, g _ {2} (s) = \frac {s + 2}{s + 4}$$

(i) 串联系统是否为能控；

(ii) 串联系统是否为能观测；

(iii) 串联系统是否可由传递函数 $g_{1}(s)g_{2}(s)$ 所完全表征。

11.2 对于按顺序 $G_{1}(s)-G_{2}(s)$ 的串联系统, 其中传递函数矩阵分别为:

$$
G _ {1} (s) = \left[ \begin{array}{c c} \frac {s + 1}{s + 2} & 0 \\ & \frac {s + 2}{s + 1} \\ 0 & \end{array} \right], G _ {2} (s) = \left[ \begin{array}{c c} \frac {1}{s - 1} & \frac {s + 2}{s + 1} \\ & \frac {1}{s + 1} \\ 0 & \end{array} \right]
$$

(i) 串联系统是否为能控；  
(ii) 串联系统是否为能观测；  
(iii) 串联系统是否可由传递函数矩阵 $G_{2}(s)G_{1}(s)$ 所完全表征。

11.3 考察图 P11.1 所示的两个反馈系统, 其中传递函数矩阵分别为

$$
G _ {1} (s) = \left[ \begin{array}{c c} \frac {1}{s + 1} & 1 \\ \frac {1}{s ^ {2} - 1} & \frac {1}{s - 1} \end{array} \right], G _ {2} (s) = \left[ \begin{array}{c c} \frac {1}{s + 3} & \frac {1}{s + 1} \\ \frac {1}{s + 3} & \frac {1}{s + 2} \end{array} \right]
$$

(i) 判断它们是否为 BIBO 稳定的；  
(ii) 判断它们是否为渐近稳定的。

11.4 判断下列各有理分式矩阵是否为循环的:

(i) $G_{1}(s)=\left[\begin{array}{cc}\frac{1}{(s-1)^{2}}&\frac{s+1}{s-2}\\ \frac{1}{s+3}&\frac{1}{s}\end{array}\right]$

(ii) $G_{2}(s)=\left[\begin{array}{cc}\frac{1}{s-1}&\frac{2}{s-1}\\ \frac{1}{(s-1)(s+1)}&\frac{2s}{(s-1)(s+1)}\end{array}\right]$

(iii) $G_{3}(s)=\left[\begin{array}{ccc} \frac{1}{s+1}&0&0\\ 0&\frac{1}{s+1}&0\\ 0&0&\frac{1}{s+1}\end{array}\right]$

11.5 设有理分式矩阵 $C(s)$ 为循环，试证明：对任意的同维实常阵 $K$ ， $\widetilde{C}(s) = C(s) + K$ 也是循环的。

11.6 给定系统的传递函数矩阵为:

$$
G _ {o} (s) = \left[ \begin{array}{c c} s ^ {2} + s + 1 & s + 1 \\ s ^ {2} + 2 s & 2 \end{array} \right] \left[ \begin{array}{c c} s ^ {3} + 2 s ^ {2} + 1 & 0 \\ 2 s ^ {2} + s + 1 & 4 s ^ {2} + 2 s + 1 \end{array} \right] ^ {- 1}
$$

试设计一个状态反馈阵 K，使得状态反馈系统的极点为： $\lambda_{1}^{*} = -2 \quad \lambda_{2,3}^{*} = -1 \pm j1$ ， $\lambda_{4,5}^{*} = -4 \pm j2$ 。

11.7 对于上题给出的受控系统和期望闭环极点组，确定实现极点配置的一个观测器一控制器型的补偿器，并画出闭环控制系统的结构图。

11.8 给定图 $P$ 11.2 所示的单位输出反馈系统, 其中受控系统的传递函数 $G_{o}(s) = (s^{2} - 1) / (s^{2} - 3s + 1)$ , 试确定一个次数为 2 的严格真的补偿器 $C(s)$ , 使得此单位输出反馈系统的极点为 $-4, -3, -2$ 和 $-1$ 。

![](image/4eff2c92b4f7d1ea10d75220302e52b82fb7dfd8ebf4c91556f4b12d989a8edf.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    v -->|+| sum((+))
    sum --> G1["G₁(s)"] --> G2["G₂(s)"] --> y
    y -->|-| feedback
```
</details>

(a)

![](image/d348dd4f0cc5cf95475f6ff5c6f49b101c2a1993d916f9aa3637acb0b784b3c0.jpg)  
(b)   
图 P11.1
