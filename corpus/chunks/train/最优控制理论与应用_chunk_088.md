$$u (t) = - \frac {1}{r} K x (t) \tag {5-36}$$

代入状态方程式(5-32)，得

$$\dot {x} (t) = \left[ a - \frac {1}{r} K \right] x (t) \tag {5-37}$$

闭环特征根变为

$$a - \frac {1}{r} K = - \sqrt {\frac {q}{r} + a ^ {2}} < 0$$

即最优反馈系统是稳定的。

若 $q = 0$ （相当于 $\pmb{Q}$ 为半正定），则指标蜕化为

$$J = \frac {1}{2} \int_ {0} ^ {\infty} r u ^ {2} (t) \mathrm{d} t$$

从 J 的形式立即可判断出 $u(t)=0$ 时 J 最小。这时无反馈控制作用，系统保持为开环不稳定。从黎卡提方程来看，这时有

$$K ^ {2} - 2 r a K = 0$$

有两个解: K=0 和 K=2ar>0 。只有 K=0 可使 u=0 ，从而性能指标为最小，但这时系统不稳定。

例5-3 考虑下面的不可控系统

$$\dot {x} _ {1} (t) = x _ {2} (t) + u (t) \tag {5-38}\dot {x} _ {2} (t) = a x _ {2} (t) \tag {5-39}$$

性能指标为

$$J = \int_ {0} ^ {\infty} \left[ x _ {1} ^ {2} (t) + u ^ {2} (t) \right] \mathrm{d} t \tag {5-40}$$

要求出最优控制使 J 为最小。

解 显然, 这个系统的 $x_{1}(t)$ 是可控的, 而 $x_{2}(t)$ 不可控, 性能指标中只包含了可控的状态变量 $x_{1}$ 。由状态方程和性能指标求得

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & a \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \quad \boldsymbol {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {R} = 1 \tag {5-41}
$$

显然 $\pmb{Q}$ 为半正定阵。可控性阵为

$$
[ \boldsymbol {B}, \boldsymbol {A} \boldsymbol {B} ] = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right] \tag {5-42}
$$

是奇异的,系统不可控。将 Q 阵作下面的分解

$$
\left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right] = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \left[ \begin{array}{l l} 1 & 0 \end{array} \right] = \boldsymbol {Q} _ {1} ^ {\mathrm{T}} \boldsymbol {Q} _ {1}
$$

由 $(Q_{1},A_{1})$ 对构成的可观性阵为

$$
\left[ \boldsymbol {Q} _ {1} ^ {\mathrm{T}}, \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {Q} _ {1} ^ {\mathrm{T}} \right] = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \tag {5-43}
$$

是非奇异阵，故 $(\pmb{A},\pmb{Q}_1)$ 为可观测对。令

$$
\boldsymbol {K} = \left[ \begin{array}{l l} k _ {1 1} & k _ {1 2} \\ k _ {1 2} & k _ {2 2} \end{array} \right]
$$

代入矩阵黎卡提代数方程式(5-31)可得

$$- 1 + k _ {1 1} ^ {2} = 0- k _ {1 1} + k _ {1 1} k _ {1 2} - a k _ {1 2} = 0 \tag {5-44}- 2 k _ {1 2} - 2 a k _ {2 2} + k _ {1 2} ^ {2} = 0$$

由上式可解得

$$k _ {1 1} = 1 \quad k _ {1 2} = \frac {1}{1 - a} \quad k _ {2 2} = \frac {2 a - 1}{2 a (1 - a) ^ {2}} \tag {5-45}$$

为保证 K 正定, 根据西尔维斯特判据, K 的各阶主子式应大于 0, 即

$$k _ {1 1} > 0 \quad k _ {2 2} > 0 \quad k _ {1 1} k _ {2 2} > k _ {1 2} ^ {2} \tag {5-46}$$

将求得的 $k_{11}, k_{12}, k_{22}$ 的值代入上面正定性条件，可得

$$\frac {2 a - 1}{2 a (1 - a) ^ {2}} > \frac {1}{(1 - a) ^ {2}} \quad \text {或} \quad \frac {2 a - 1}{2 a} > 1 \tag {5-47}$$
