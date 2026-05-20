其中 $S(s) \in RH_{\infty}^{m \times m}$ 和 $S^{-1}(s) \in RH_{\infty}^{m \times m}$ 分别为

$$
\begin{array}{l} S (s) = I + \left(C - B ^ {T} X\right) (s I - A) ^ {- 1} B. \\ S ^ {- 1} (s) = I - \left(C - B ^ {\mathrm{T}} X\right) \left(s I - A _ {X}\right) ^ {- 1} B. \tag {6.4.20} \\ \end{array}
$$

注6.4.2 显然，根据定义可知， $J(s)$ 的极点在复平面上关于原点对称分布。如果式(6.4.18)有满足上述定理条件的解，那么由定理可知 $J(s)$ 不但在虚轴上解析，而且还可以用 $RH_{\infty}^{m \times m}$ 的元 $S(s)$ 分解如式(6.4.19)。这种分解称为谱分解， $S(s)$ 称为 $J(s)$ 的谱因子。上述定理的证明可参阅文献[15]。

现在我们可以用上述基本结果来证明定理 6.4.1.

证明 定理 6.4.1 的充分性. 设 Riccati 方程 (6.4.3) 有满足定理条件的半正定解 X, 且令反馈控制器 $K(s)$ 由式 (6.4.4) 给定, 则闭环系统为

$$
\left\{ \begin{array}{l} \dot {x} = A _ {F} x + B _ {1} w + B _ {2} v, \\ z = C _ {F} x + D _ {1 2} v, \\ \widehat {y} = - F _ {1} x + w, \\ v = Q (s) \widehat {y}, \end{array} \right. \tag {6.4.21}
$$

其中 $A_{F} = A + B_{2}F_{2}, C_{F} = C_{1} + D_{12}F_{2}$ .

定义

$$
\left[ \begin{array}{l} z \\ \widehat {y} \end{array} \right] = T (s) \left[ \begin{array}{l} w \\ v \end{array} \right]. \tag {6.4.22}
$$

那么上述闭环系统可以表示为如图6.4.1所示的反馈结构，并且 $T(s)$ 的状态空间实现为 $\{A_F, \widetilde{B}, \widetilde{C}, \widetilde{D}\}$ ，其中

$$
\tilde {B} = [ B _ {1} B _ {2} ], \quad \tilde {C} = \left[ \begin{array}{l} C _ {F} \\ - F _ {1} \end{array} \right], \quad \tilde {D} = \left[ \begin{array}{l l} 0 & D _ {1 2} \\ I & 0 \end{array} \right].
$$

因此，根据引理6.4.1, 如果 $T(s)$ 是内函数阵且满足 $T_{21}^{-1}(s) \in RH_{\infty}^{q \times q}$ , 则该系统是内部稳定的，且有

$$\left\| T _ {z w} (\cdot) \right\| _ {\infty} < 1, \quad \forall Q (s) \in R H _ {\infty} ^ {q \times q}. \tag {6.4.23}$$

以下我们用引理6.4.2来验证 $T(s)$ 是内函数阵. 首先, 根据条件(A2), 有 $\tilde{D}^{\mathrm{T}}\tilde{D} = I$ . 又因为 $A_{F} + [0 - B_{1}]\tilde{C} = A - B_{2}B_{2}^{\mathrm{T}}X + B_{1}B_{1}^{\mathrm{T}}X$ 是稳定阵, 所以 $(\tilde{C}, A_{F})$ 是能检测的.

由于 Riccati 方程 (6.4.3) 又可以表示为

$$A _ {F} ^ {\mathrm{T}} X + X A _ {F} = - \widetilde {C} ^ {\mathrm{T}} \widetilde {C}, \tag {6.4.24}$$

且容易验证， $\tilde{D}^{\mathrm{T}}\tilde{C} + \tilde{B}^{\mathrm{T}}X = 0$ ，因此根据引理6.4.2， $A_{F}$ 是稳定阵，而且 $T(s)$ 是内函数阵。

另外，由于 $T_{21}(s) = I - F_1(sI - A_F)^{-1}B_1$ ，所以 $T_{21}^{-1}(s)$ 的最小实现为 $\{A_F + B_1F_1,B_1,F_1,I\}$ .可以验证

$$A _ {F} + B _ {1} F _ {1} = A - B _ {2} B _ {2} ^ {\mathrm{T}} X + B _ {1} B _ {1} ^ {\mathrm{T}} X$$

是稳定阵，故 $T_{21}^{-1}(s) \in RH_{\infty}^{q \times q}$ .

综上所述， $T(s)$ 满足引理6.4.1的条件，所以式(6.4.23)成立.
