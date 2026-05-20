\left[ \boldsymbol {Q} _ {1} ^ {\mathrm{T}} \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {Q} _ {1} ^ {\mathrm{T}} \right] = \left[ \begin{array}{c c} \sqrt {q} & 0 \\ 0 & \sqrt {q} \end{array} \right] \tag {5-83}
$$

(5-83)非奇异,故 $(A,Q_{1})$ 对可观测。于是满足稳态状态调节器问题的条件。由(5-78)令 $K=\begin{bmatrix}k_{11}&k_{12}\\ k_{12}&k_{22}\end{bmatrix}$ ，黎卡提方程可写成

$$
- \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] + \left[ \begin{array}{l l} q & 0 \\ 0 & 0 \end{array} \right] + \underbrace {\left[ \begin{array}{c c c} 0 & & 0 \\ 0 & k _ {1 1} + 2 k _ {1 2} + k _ {2 2} \end{array} \right]} _ {\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K A}} -

\underbrace {\left[ \begin{array}{c} 0 \\ k _ {1 2} + k _ {2 2} \end{array} \right]} _ {\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {K B}} \underbrace {\frac {1}{1 + k _ {2 2}}} _ {[ \boldsymbol {R} + \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K B} ] ^ {- 1}} \underbrace {\left[ \begin{array}{l l} 0 & k _ {1 2} + k _ {2 2} \end{array} \right]} _ {\boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K A}}

= \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right]
$$

由上式可解得

$$
\boldsymbol {K} = \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} q & 0 \\ 0 & \frac {1}{2} (q + \sqrt {q ^ {2} + 4 q}) \end{array} \right] \tag {5-84}
$$

由式(5-76)、(5-77)可得

$$
\begin{array}{l} \boldsymbol {U} (k) = - \boldsymbol {L X} (k) = \frac {- 1}{1 + k _ {2 2}} \left[ \begin{array}{l l} 0 & k _ {1 2} + k _ {2 2} \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] \\ = \frac {- \left(k _ {1 2} + k _ {2 2}\right)}{1 + k _ {2 2}} x _ {2} (k) = - \frac {q + \sqrt {q ^ {2} + 4 q}}{2 + q + \sqrt {q ^ {2} + 4 q}} x _ {2} (k) \\ \end{array}
$$

最优反馈增益阵

$$\boldsymbol {L} = \left[ 0 \quad \frac {k _ {1 2} + k _ {2 2}}{1 + k _ {2 2}} \right]$$

闭环系统的系统矩阵为

$$
\begin{array}{l} \boldsymbol {A} _ {\mathrm{CL}} = \boldsymbol {A} - \boldsymbol {B L} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 1 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \left[ \begin{array}{l l} 0 & \frac {k _ {1 2} + k _ {2 2}}{1 + k _ {2 2}} \end{array} \right] \\ = \left[ \begin{array}{c c} 0 & 1 \\ 0 & \frac {1}{1 + k _ {2 2}} \end{array} \right] \\ k _ {2 2} = \frac {1}{2} (q + \sqrt {q ^ {2} + 4 q}) \\ \end{array}
$$

闭环特征根为 $\lambda_{1} = 0, \lambda_{2} = \frac{1}{1 + k_{22}}$ 。显然，根的模都小于1，闭环系统稳定。由状态方程(5-80)可见，开环系统的根为 $\lambda_{1}' = 0, \lambda_{2}' = 1$ ，系统不是渐近稳定的。当 $q = 0$ ，于是 $k_{22} = 0, \lambda_{2} = 1$ ，闭环系统不是渐近稳定的，这是由于 $q = 0$ 不满足可观性条件，即式(5-83)为奇异阵，这时稳态状态调节器的最优控制解是不存在的。此外，当 $q \to \infty$ ，则有 $k_{22} \to \infty, \lambda_{2} \to 0$ 。
