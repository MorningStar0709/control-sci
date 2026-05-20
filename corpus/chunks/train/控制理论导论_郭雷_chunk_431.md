根据上式可知 $A + BB^{\mathrm{T}}X = T_{1}JT_{1}^{-1}$ ，即 $A + BB^{\mathrm{T}}X$ 与 $J$ 相似.所以 $A + BB^{\mathrm{T}}X$ 也是稳定阵．此外上式两端乘 $[-X,I]$ ，有

$$
[ - X I ] H \left[ \begin{array}{l} I \\ X \end{array} \right] = A ^ {\mathrm{T}} X + X A + X B B ^ {\mathrm{T}} X + C ^ {\mathrm{T}} C = 0. \tag {6.2.5}
$$

因此我们只需证明 $T_{1}$ 可逆并且 $X = T_{2}T_{1}^{-1}$ 是半正定阵。为此我们用反证法。

假设 $T_{1}$ 为奇异阵，且 $\operatorname{rank}(T_1) = n - q$ ( $1 \leqslant q \leqslant n$ ), 则存在 $q$ 个线性独立的 $n$ 维向量 $b_{1}, b_{2}, \cdots, b_{q}$ , 使得满足

$$T _ {1} b = 0 \tag {6.2.6}$$

的任意向量 $b$ 均可以表示为其线性组合，即

$$b = \sum_ {i = 1} ^ {q} c _ {i} b _ {i} = M _ {b} k,$$

其中 $M_{b} = [b_{1} b_{2} \cdots b_{q}]$ ，且 $k = [c_{1} c_{2} \cdots c_{q}]^{T}$ 为线性组合系数向量.

根据式 (6.2.4) 有

$$A T _ {1} b + B B ^ {\mathrm{T}} T _ {2} b = T _ {1} J b.$$

容易证明 $T_{2}^{*}T_{1} = T_{1}^{*}T_{2}$ (请读者自行证明), 所以利用式 (6.2.6) 得

$$b ^ {*} T _ {2} ^ {*} (A T _ {1} b + B B ^ {\mathrm{T}} T _ {2} b) = b ^ {*} T _ {2} ^ {*} B B ^ {\mathrm{T}} T _ {2} b = b ^ {*} T _ {2} ^ {*} T _ {1} J b = b ^ {*} T _ {1} ^ {*} T _ {2} J b = 0,$$

即 $B^{\mathrm{T}}T_{2}b = 0$ 因此有

$$T _ {1} J b = 0. \tag {6.2.7}$$

这表明，若 $b$ 满足 $T_{1}b = 0$ ，那么向量 $\widetilde{b} = Jb$ 同样满足 $T_{1}\widetilde{b} = 0.$ 所以 $\widetilde{b}_i = Jb_i$ 均可以表示为 $b_{1}, b_{2}, \dots, b_{q}$ 的线性组合．于是存在向量 $k_{1}, k_{2}, \dots, k_{q}$ 使得

$$[ \widetilde {b} _ {1} \widetilde {b} _ {2} \dots \widetilde {b} _ {q} ] = J M _ {b} = M _ {b} K,$$

其中 $K = [k_{1}, k_{2}, \cdots, k_{q}] \in R^{q \times q}$ . 令 A 为 K 的 Jordan 标准型，即存在 Y 满足 $K = Y^{-1} \Lambda Y$ . 因此

$$J \widetilde {Y} = \widetilde {Y} \Lambda , \quad \widetilde {Y} = M _ {b} Y = [ \widetilde {y} _ {1} \widetilde {y} _ {2} \dots \widetilde {y} _ {q} ],$$

即存在 $y_0 \in \mathbb{R}^n, \lambda_0 \in \mathbb{C}$ , 使得 $T_1y_0 = 0$ , 且

$$J y _ {0} = \lambda_ {0} y _ {0}, \operatorname{Re} \{\lambda_ {0} \} < 0. \tag {6.2.8}$$

又根据式 (6.2.4) 有

$$- C ^ {\mathrm{T}} C T _ {1} - A ^ {\mathrm{T}} T _ {2} = T _ {2} J,$$

故

$$- C ^ {\mathrm{T}} C T _ {1} y _ {0} - A ^ {\mathrm{T}} T _ {2} y _ {0} = - A ^ {\mathrm{T}} T _ {2} y _ {0} = T _ {2} J y _ {0} = \lambda_ {0} T _ {2} y _ {0},$$

即

$$A ^ {\mathrm{T}} u _ {0} = - \lambda_ {0} u _ {0}, \qquad u _ {0} = T _ {2} y _ {0}. \tag {6.2.9}$$

上式意味着， $A$ 在右半平面有特征值 $-\lambda_0$ ，这与 $A$ 是稳定阵的假设矛盾．因此 $T_{1}$ 可逆.

(2) $\Longrightarrow$ (1). 对于由式 (6.2.3) 定义的 $T(s)$ 的状态空间实现 $\{H, B_h, C_h, I\}$ 作如下相似变换：

$$
\bar {A} = U ^ {- 1} H U, \quad \ddot {B} = U ^ {- 1} B _ {h}, \quad \bar {C} = C _ {h} U, \quad U = \left[ \begin{array}{l l} I & 0 \\ X & I \end{array} \right],
$$

其中 $X$ 为式 (6.2.1) 的半正定解，则得
