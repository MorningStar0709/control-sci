$$\boldsymbol {\lambda} \left(t _ {f}\right) = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {f}\right)} = \frac {\partial}{\partial \boldsymbol {X} \left(t _ {f}\right)} \left[ \frac {1}{2} \boldsymbol {e} ^ {T} \left(t _ {f}\right) \boldsymbol {P e} \left(t _ {f}\right) \right]= \boldsymbol {C} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P} \left[ \boldsymbol {C} \left(t _ {\mathrm{f}}\right) \boldsymbol {X} \left(t _ {\mathrm{f}}\right) - \boldsymbol {Z} \left(t _ {\mathrm{f}}\right) \right] \tag {5-92}$$

由上式可见 $\boldsymbol{\lambda}(t_{\mathrm{f}})$ 中有一项与 $\boldsymbol{X}(t_{\mathrm{f}})$ 成线性关系, 另一项与理想输出 $\boldsymbol{Z}(t_{\mathrm{f}})$ 成线性关系。根据扫描法的思想, 令

$$\boldsymbol {\lambda} (t) = \boldsymbol {K} (t) \boldsymbol {X} (t) - \boldsymbol {g} (t) \tag {5-93}$$

其中矩阵 $K(t)$ 和向量时间函数 $g(t)$ 待定。将式(5-93)对 $t$ 微分，得

$$\dot {\boldsymbol {\lambda}} (t) = \dot {\boldsymbol {K}} (t) \boldsymbol {X} (t) + \boldsymbol {K} (t) \dot {\boldsymbol {X}} (t) - \dot {\boldsymbol {g}} (t) \tag {5-94}$$

设法从上式中消去 $\dot{X}(t)$ , 为此把式(5-90)和式(5-93)代入状态方程(5-85), 可求出

$$\dot {\boldsymbol {X}} (t) = [ \boldsymbol {A} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) ] \boldsymbol {X} (t) +\boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {g} (t) \tag {5-95}$$

将式(5-95)代入式(5-94)，即得

$$\dot {\boldsymbol {\lambda}} (t) = \left[ \dot {\boldsymbol {K}} (t) + \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \right] \boldsymbol {X} (t) +\boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {g} (t) - \dot {\boldsymbol {g}} (t) \tag {5-96}$$

另外，式(5-93)代入式(5-91)可得

$$\dot {\boldsymbol {\lambda}} (t) = \left[ - \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {C} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \right] \boldsymbol {X} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {g} (t) +\boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {Z} (t) \tag {5-97}$$

式(5-96)减去式(5-97)可得
