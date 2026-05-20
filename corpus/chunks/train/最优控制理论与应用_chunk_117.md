$$
\dot {\boldsymbol {\lambda}} = \frac {\partial}{\partial \boldsymbol {X}} \left[ \frac {\partial V (\boldsymbol {X} , t)}{\partial t} \right] + \frac {\partial^ {2} V (\boldsymbol {X} , t)}{\partial \boldsymbol {X} \partial \boldsymbol {X} ^ {\mathrm{T}}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t)
\begin{array}{l} = - \frac {\partial}{\partial \boldsymbol {X}} \left[ F (\boldsymbol {X}, \boldsymbol {U}, t) + \left(\frac {\partial V}{\partial \boldsymbol {X}}\right) ^ {T} \cdot \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \right] + \frac {\partial^ {2} V (\boldsymbol {X} , t)}{\partial \boldsymbol {X} \partial \boldsymbol {X} ^ {T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \\ = - \left[ \frac {\partial F}{\partial X} + \left(\frac {\partial V}{\partial X}\right) ^ {T} \frac {\partial f}{\partial X} \right] \\ = - \frac {\partial}{\partial X} \left[ F + \left(\frac {\partial V}{\partial X}\right) ^ {T} f \right] \\ = - \frac {\partial H}{\partial X} \\ \end{array}
$$

即协态方程式(6-32)(因都是最优解条件。故省去\*号)。由式(6-22)和(6-27)再来推横截条件

$$
\begin{array}{l} \boldsymbol {\lambda} \left(t _ {f}\right) = \frac {\partial V \left[ \boldsymbol {X} \left(t _ {f}\right) , t _ {f} \right]}{\partial \boldsymbol {X} \left(t _ {f}\right)} \\ = \frac {\partial \phi [ X (t _ {f}) , t _ {f} ]}{\partial X (t _ {f})} \\ \end{array}
$$

即横截条件式(6-34)。其他条件如状态方程和初始条件都是给定的。故由动态规划推出了极小值原理的全部条件。应该强调，这不是说用动态规划可证明极小值原理。因为上面的推演要求 $V(X,t)$ 对 $X,t$ 二次连续可微，而极小值原理的证明本身不需要这一条件。
