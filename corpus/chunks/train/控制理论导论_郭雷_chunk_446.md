$$I - \left[ S _ {0} ^ {\mathrm{T}} (- \mathrm{j} \omega) \right] ^ {- 1} V ^ {\mathrm{T}} (- \mathrm{j} \omega) V (\mathrm{j} \omega) S _ {0} ^ {- 1} (\mathrm{j} \omega) > 0, \quad \forall \omega \in \mathbb {R},$$

即

$$\left\| V (s) S _ {0} ^ {- 1} (s) \right\| _ {\infty} < 1. \tag {6.4.36}$$

如果根据定理6.4.4求谱因子 $S_0(s)$ ，则其逆 $S_0^{-1}(s)$ 的状态空间实现为

$$\{A _ {\Pi}, Z B _ {1}, B _ {1} ^ {\mathrm{T}} (P + Z \Pi), I \},$$

其中 $A_{\Pi} = A_F + ZB_1B_1^{\mathrm{T}}(P + Z^{\mathrm{T}}\Pi)$ 是稳定阵，且 $\Pi$ 是如下Riccati方程的半正定解：

$$\Pi \left(A _ {F} + Z B _ {1} B _ {1} ^ {\mathrm{T}} P\right) + \left(A _ {F} + Z B _ {1} B _ {1} ^ {\mathrm{T}} P\right) ^ {\mathrm{T}} \Pi + \Pi Z B _ {1} B _ {1} ^ {\mathrm{T}} Z \Pi + P B _ {1} P B _ {1} ^ {\mathrm{T}} P = 0. \tag {6.4.37}$$

注意在虚轴上解析的有理函数阵

$$\hat {T} (s) = T _ {1 2} ^ {\mathrm{T}} (- s) T _ {1 1} (s) S _ {0} ^ {- 1}$$

可以分解为 $\hat{T}(s) = \hat{T}_{-}(s) + \hat{T}_{+}(s)$ ，其中 $\hat{T}_{-}(s)$ 和 $\hat{T}_{+}(s)$ 分别是在闭右半平面和左半平面上解析的有理函数阵，其状态空间实现分别为

$$\widehat {T} _ {-} := \left\{A _ {\Pi}, Z B _ {1}, B _ {2} ^ {\mathbf {T}} \Pi , 0 \right\},\widehat {T} _ {+} := \left\{- A _ {F}, - (P + \Pi Z) B _ {1}, B _ {2} ^ {\mathrm{T}}, 0 \right\}.$$

由于

$$V (s) S _ {0} ^ {- 1} (s) = \widehat {T} (s) - Q _ {d} (s) S _ {0} ^ {- 1} (s) = \widehat {T} _ {+} (s) - \widehat {Q} (s),$$

其中 $\hat{Q}(s) = \hat{T}_{-}(s) + Q_{d}(s)S_{0}^{-1}\in RH_{\infty}^{r\times q}$ ，故根据式(6.4.36）得

$$\sup _ {\omega \in \mathbf {R}} \{\widehat {T} _ {+} (\mathrm{j} \omega) - \widehat {Q} (\mathrm{j} \omega) \} < 1. \tag {6.4.38}$$

因此得到如下 Nehari 最佳逼近值：

$$J _ {\min} = \inf _ {\hat {Q}} \sup _ {\omega} \left\{\hat {T} _ {+} (\mathrm{j} \omega) - \hat {Q} (\mathrm{j} \omega) \right\} = \lambda_ {\min} \left\{L _ {C} L _ {O} \right\} < 1. \tag {6.4.39}$$

根据定理 6.4.3, 上式中 $L_{C}, L_{O}$ 分别是满足如下 Lyapunov 方程的半正定阵:

$$
\left\{ \begin{array}{l} L _ {C} (- A _ {F}) + (- A _ {F}) ^ {\mathrm{T}} L _ {C} = (P + \Pi Z) B _ {1} B _ {1} ^ {\mathrm{T}} (P + \Pi Z) ^ {\mathrm{T}}, \\ L _ {O} (- A _ {F}) ^ {\mathrm{T}} + (- A _ {F}) L _ {O} = B _ {2} B _ {2} ^ {\mathrm{T}}. \end{array} \right. \tag {6.4.40}
$$

令 $L_{C} = \Pi, L_{O} = Y$ ，则不难验证 Riccati 方程 (6.4.35)，(6.4.37) 与 Lyapunov 方程 (6.4.40) 是等价的。因此有

$$\lambda_ {\min} (\Pi Y) < 1. \tag {6.4.41}$$

现在我们利用此关系来证明 Riccati 方程 (6.4.3) 有满足定理条件的半正定解 $X$ . 根据 Ricaati 方程与 Hamilton 矩阵的关系, 若 Riccati 方程 (6.4.37) 有半正定解 $\Pi$ , 且 $A_{\Pi} = A_{F} + ZB_{1}B_{1}^{\mathrm{T}}(P + Z^{\mathrm{T}}\Pi)$ 是稳定阵, 那么其解 $\Pi$ 满足 (详见定理 6.2.1 的证明)
