$$u = - K _ {1} x - K _ {2} \sigma\dot {\sigma} = e = y - r$$

其中 $K=\left[K_{1}K_{2}\right]$ 设计为使A-BK是赫尔维茨矩阵。

例12.4 考虑单摆方程为

$$\ddot {\theta} = - a \sin \theta - b \dot {\theta} + c T$$

其中 $a = g / l > 0, b = k / m \geqslant 0, c = 1 / ml^2 > 0, \theta$ 是摆线与纵轴之间的夹角， $T$ 是作用于单摆的力矩。把 $T$ 看成控制输入，并假设要把 $\theta$ 调节到 $\delta$ 。取 $x_1 = \theta - \delta, x_2 = \dot{\theta}, u = T, y = x_1$

则状态方程为

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - a \sin (x _ {1} + \delta) - b x _ {2} + c uy = x _ {1}$$

容易看出期望的平衡点为 $x_{ss}=\left[\begin{array}{c}0\\0\end{array}\right]$ ， $u_{ss}=\frac{a}{c}\sin\delta$

$A, B$ 和 $C$ 分别为 $A = \left[ \begin{array}{cc}0 & 1\\ -a\cos \delta & -b \end{array} \right];\quad B = \left[ \begin{array}{c}0\\ c \end{array} \right];\quad C = \left[ \begin{array}{ll}1 & 0 \end{array} \right]$

注意到 c>0，容易验证 $(A,B)$ 是可控的，且满足秩条件 (12.23)。取 $K_{1}=\left[k_{1}\ k_{2}\right]$ ， $K_{2}=k_{3}$ ，利用劳斯-赫尔维茨准则可验证，如果

$$b + k _ {2} c > 0, \quad (b + k _ {2} c) (a \cos \delta + k _ {1} c) - k _ {3} c > 0, \quad k _ {3} c > 0$$

成立,则 $A-BK$ 是赫尔维茨矩阵。假设参数a>0, $b\geqslant0,c>0$ ,其准确值未知,但知道a/c的上界为 $\rho_{1},1/c$ 的上界为 $\rho_{2}$ ,选择

$$k _ {2} > 0, \quad k _ {3} > 0, \quad k _ {1} > \rho_ {1} + \frac {k _ {3}}{k _ {2}} \rho_ {2} \tag {12.24}$$

以保证A-BK是赫尔维茨矩阵。反馈控制律为

$$u = - k _ {1} (\theta - \delta) - k _ {2} \dot {\theta} - k _ {3} \sigma\dot {\sigma} = \theta - \delta$$

这是经典的PID控制器。将这个反馈控制律与例12.2中的结果比较，会发现不再需要计算为保持平衡位置所要求的稳态力矩。对于所有满足 $(b + k_2c)(a\cos \delta +k_1c) - k_3c > 0$ 的参数扰动，都能实现调节。图12.2所示为有积分作用（见例12.4）和没有积分作用（见例12.2）的情况下，把单摆调节到 $\delta = \pi /4$ 时的仿真结果。在前一种情况下，反馈增益为 $k_{1} = 8,k_{2} = 2,k_{3} = 10$ ，赋予的特征值为-15.93，-2.93和-2.14。在后一种情况下，反馈增益为 $k_{1} = 3,k_{2} = 0.7$ ，赋予的特征值为 $-4\pm j4.59$ 。两种情况下的标称参数都是 $a = c =$ $10,b = 1$ 。在扰动情况下， $b$ 和 $c$ 分别减小到0.5和5，对应于质量的2倍。仿真结果表明积分作用可改善稳态响应，其代价是在过渡周期中增加稳定时间和增大力矩。

在更为一般的输出反馈中,积分控制器可取为

$$\dot {\sigma} = e = y - r \tag {12.25}\dot {z} = F z + G _ {1} \sigma + G _ {2} y _ {m} \tag {12.26}u = L z + M _ {1} \sigma + M _ {2} y _ {m} + M _ {3} e \tag {12.27}$$

其中所涉及的 $F, G_{1}, G_{2}, L, M_{1}, M_{2}$ 和 $M_{3}$ 均与 $w$ 无关，并使得

$$
\mathcal {A} _ {c} = \left[ \begin{array}{c c c} A + B M _ {2} C _ {m} + B M _ {3} C & B M _ {1} & B L \\ C & 0 & 0 \\ G _ {2} C _ {m} & G _ {1} & F \end{array} \right]
$$

对于所有 $v \in D_v$ 为赫尔维茨矩阵, 其中 $C_m = [\partial h_m / \partial x](x_{\mathrm{ss}}, w)$ 。这将保证

$$
\left[ \begin{array}{l l} M _ {1} & L \\ G _ {1} & F \end{array} \right]
$$
