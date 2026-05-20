$$U _ {2 1} (s) D (s) + U _ {2 2} (s) N (s) = 0 \tag {6.51}$$

现令 $B(s) = -U_{21}(s)$ 和 $A(s) = U_{22}(s)$ ，即得(6.48)。

(2) 证明 $\deg \det A(s) = \deg \det V_{11}(s)$

令 $U^{-1}(s) = V(s)$ ，则可将(6.50)改写为

$$
\left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.52}
$$

并可由此导出

$$D (s) = V _ {1 1} (s) R (s) \tag {6.53}$$

现知 $D(s)$ 为非奇异，故 $R(s)$ 也为非奇异，从而可知 $V_{11}(s)$ 为非奇异。于是，可构成如下的恒等式：

$$
\begin{array}{l} \left[ \begin{array}{c c} I & \mathbf {0} \\ - V _ {2 1} (s) V _ {1 1} ^ {- 1} (s) & I \end{array} \right] \left[ \begin{array}{c c} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \\ = \left[ \begin{array}{c c} V _ {1 1} (s) & V _ {1 2} (s) \\ 0 & A \end{array} \right] \tag {6.54} \\ \end{array}
$$

其中 $\Delta = V_{21}(s) - V_{21}(s)V_{11}^{-1}(s)V_{11}(s)$ 。再对(6.54)取行列式，那么考虑到 $V(s)$ 为单模阵的同时，有

$$\det V (s) = \det V _ {1 1} (s) \det \Delta \neq 0, \forall s \in \mathcal {C} \tag {6.55}$$

表明 $\Delta$ 为非奇异，故 $\Delta^{-1}$ 存在。这样，对式(6.54)进行求逆，可得

$$
\left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} I & \mathbf {0} \\ - V _ {2 1} (s) V _ {1 1} ^ {- 1} (s) & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} V _ {1 1} ^ {- 1} (s) & - V _ {1 1} ^ {- 1} (s) V _ {1 2} (s) \Delta^ {- 1} \\ \mathbf {0} & \Delta^ {- 1} \end{array} \right] \tag {6.56}
$$

因此，进一步可导出

$$
\begin{array}{l} \left[ \begin{array}{c c} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] = V ^ {- 1} (s) = \left[ \begin{array}{c c} V _ {1 1} ^ {- 1} (s) & - V _ {1 1} ^ {- 1} (s) V _ {1 2} (s) \Delta^ {- 1} \\ \mathbf {0} & \Delta^ {- 1} \end{array} \right] \\ \times \left[ \begin{array}{c c} I & 0 \\ V _ {2 1} (s) V _ {1 1} ^ {- 1} (s) & I \end{array} \right] = \left[ \begin{array}{c c} * & * \\ * & A ^ {- 1} \end{array} \right] \tag {6.57} \\ \end{array}
$$

其中“\*”表示不必确知的多项式元。于是，由式(6.57)可得

$$U _ {2 i} (s) = \Delta^ {- 1} \text {或} U _ {2 i} (s) \Delta = I \tag {6.58}$$

对(6.58)取行列式,进而有

$$\det \Delta = 1 / \det U _ {2 2} (s) \tag {6.59}$$

而把(6.59)代入(6.55)则又有

$$\det V (s) = \det V _ {1 1} (s) / \det U _ {2 1} (s) \tag {6.60}$$

但已知 $U_{23}(s) = A(s)$ ，而由 $V(s)$ 为单模阵可导出 $\deg \det V(s) = 0$ ，从而由 (6.60) 即得

$$\deg \det A (s) = \deg \det V _ {1 1} (s) \tag {6.61}$$

(3) 已知 $D(s)$ 和 $N(s)$ 非右互质，欲证式(6.49)成立。
