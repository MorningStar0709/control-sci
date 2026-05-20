$$
\begin{array}{l} \mathbf {0} = \left[ \dot {\boldsymbol {K}} (t) + \boldsymbol {K} (t) \boldsymbol {A} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \right. \\ \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {C} (t) ] \boldsymbol {X} (t) + [ \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) ] \boldsymbol {g} (t) - \\ \dot {\boldsymbol {g}} (t) - \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {Z} (t) \tag {5-98} \\ \end{array}
$$

上式对任意的 $X(t), Z(t)$ 均应成立，于是可得

$$
\begin{array}{l} \dot {\boldsymbol {K}} (t) = - \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) + \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \\ \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {C} (t) \tag {5-99} \\ \end{array}
\dot {\boldsymbol {g}} (t) = \left[ \boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \right] \boldsymbol {g} (t) - \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {Z} (t) \tag {5-100}
$$

上面的微分方程组的边界条件可推导如下:由式(5-93)得

$$\boldsymbol {\lambda} (t _ {f}) = \boldsymbol {K} (t _ {f}) \boldsymbol {X} (t _ {f}) - \boldsymbol {g} (t _ {f})$$

而由式(5-92)得

$$\boldsymbol {\lambda} \left(t _ {f}\right) = \boldsymbol {C} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {P C} \left(t _ {f}\right) \boldsymbol {X} \left(t _ {f}\right) - \boldsymbol {C} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {P Z} \left(t _ {f}\right)$$

比较上面两式,可得

$$\boldsymbol {K} \left(t _ {\mathrm{f}}\right) = \boldsymbol {C} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P C} \left(t _ {\mathrm{f}}\right) \tag {5-101}\boldsymbol {g} \left(t _ {\mathrm{f}}\right) = \boldsymbol {C} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P Z} \left(t _ {\mathrm{f}}\right) \tag {5-102}$$

由上面的 $t_{f}$ 时的边界条件出发，逆时间积分式(5-99)和式(5-100)即可求出 $K(t)$ 、 $g(t)$ 。于是，最优控制可根据式(5-90)和式(5-93)求得为
