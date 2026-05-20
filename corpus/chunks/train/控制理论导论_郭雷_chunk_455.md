$$
[ W - I ] T ^ {- 1} H _ {\infty} T \left[ \begin{array}{l} I \\ W \end{array} \right] = - M ^ {T} [ M ^ {- T} X _ {0} - I ] H _ {\infty} \left[ \begin{array}{c} I \\ X _ {0} M ^ {- 1} \end{array} \right] M = 0, \tag {6.5.33}
$$

其中 $M = I - X_0^{-1}W$ 是非奇异阵， $M^{-T} = (M^{\mathrm{T}})^{-1}$ . 所以

$$
[ X - I ] H _ {\infty} \left[ \begin{array}{l} I \\ X \end{array} \right] = 0, \tag {6.5.34}
$$

即 $X = M^{-1}X_0 = X_0(X_0 - W)^{-1}X_0$ 是Riccati方程(6.4.3)的解.

另外，由于 $A_W = A_F + X_0^{-1}C_1^{\mathrm{T}}C_1X_0^{-1}W$ 是稳定阵，且

$$
\begin{array}{l} A _ {W} = A _ {F} + X _ {0} ^ {- 1} C _ {1} ^ {\mathrm{T}} C _ {1} X _ {0} ^ {- 1} W \\ = \bar {A} + X _ {0} ^ {- 1} C _ {1} ^ {T} C _ {1} X _ {0} ^ {- 1} W \\ = - X _ {0} ^ {- 1} \left\{A ^ {\mathrm{T}} + C _ {1} ^ {\mathrm{T}} C _ {1} \left(I - X _ {0} ^ {- 1} W\right) X _ {0} ^ {- 1} \right\} X _ {0}, \\ \end{array}
$$

所以 $A_{C} = -(A^{\mathrm{T}} + C_{1}^{\mathrm{T}}C_{1}(I - X_{0}^{-1}W)X_{0}^{-1}) = -(A^{\mathrm{T}}X + C_{1}^{\mathrm{T}}C_{1})X^{-1}$ 也是稳定阵. 又因为根据 Riccati 方程 (6.4.3) 有

$$A _ {C} = - (A ^ {\mathrm{T}} X + C _ {1} ^ {\mathrm{T}} C _ {1}) X ^ {- 1} = X \{A + (B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}}) X \} X ^ {- 1}, \tag {6.5.35}$$

即 $A_{C}$ 与 $A + (B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}})X$ 具有相同的特征值，所以 $A + (B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}})X$ 也是稳定阵.

注6.5.1 以上我们给出了定理6.4.1的必要性的证明。充分性证明与前一节的证明方法类似，在此不再赘述。另外，这里所讨论的证明方法还可以推广到广义受控对象 $D_{11} \neq 0$ 的情况，即评价信号 $z$ 含有广义干扰项的情况（详细可参阅文献[7]).
