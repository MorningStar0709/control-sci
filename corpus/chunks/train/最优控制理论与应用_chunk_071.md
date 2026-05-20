$$u = - 1: \quad x _ {2} (t _ {1}) = - t _ {1} + x _ {2 0} \tag {4-71}x _ {1} \left(t _ {1}\right) = - \frac {1}{2} t _ {1} ^ {2} + x _ {2 0} t _ {1} + x _ {1 0} \tag {4-72}u = 0; \quad x _ {2} (t _ {2}) = x _ {2} (t _ {1}) \tag {4-73}x _ {1} \left(t _ {2}\right) = x _ {1} \left(t _ {1}\right) + x _ {2} \left(t _ {1}\right) \left(t _ {2} - t _ {1}\right) \tag {4-74}u = 1: \quad 0 = x _ {2} (t _ {2}) + (t _ {\mathrm{f}} - t _ {2}) \tag {4-75}0 = x _ {1} \left(t _ {2}\right) + x _ {2} \left(t _ {2}\right) \left(t _ {\mathrm{f}} - t _ {2}\right) + \frac {1}{2} \left(t _ {\mathrm{f}} - t _ {2}\right) ^ {2} (4 - 7 6)$$

由上面六个方程来解六个未知数： $t_1, t_2, x_1(t_1), x_2(t_1), x_1(t_2), x_2(t_2)$ 。由式(4-75)、(4-76)两式消去 $(t_f - t_2)$ ，再考虑式(4-73)可得

$$x _ {1} \left(t _ {2}\right) = \frac {1}{2} x _ {2} ^ {2} \left(t _ {2}\right) = \frac {1}{2} x _ {2} ^ {2} \left(t _ {1}\right) \tag {4-77}t _ {2} = t _ {\mathrm{f}} + x _ {2} \left(t _ {2}\right) = t _ {\mathrm{f}} + x _ {2} \left(t _ {1}\right) \tag {4-78}$$

由式 $(4-71)$ 、 $(4-72)$ 两式得

$$t _ {1} = x _ {2 0} - x _ {2} \left(t _ {1}\right) \tag {4-79}x _ {1} \left(t _ {1}\right) = x _ {1 0} - \frac {1}{2} x _ {2} ^ {2} \left(t _ {1}\right) + \frac {1}{2} x _ {2 0} ^ {2} \tag {4-80}$$

由式 $(4-78)$ 、 $(4-79)$ 两式得

$$t _ {2} - t _ {1} = 2 x _ {2} \left(t _ {1}\right) + t _ {\mathrm{f}} - x _ {2 0} \tag {4-81}$$

将式(4-81)代入式(4-74)得

$$2 x _ {2} ^ {2} \left(t _ {1}\right) + \left(t _ {\mathrm{f}} - x _ {2 0}\right) x _ {2} \left(t _ {1}\right) + x _ {1} \left(t _ {1}\right) - x _ {1} \left(t _ {2}\right) = 0$$

再利用式(4-77)和(4-80)，即得

$$x _ {2} ^ {2} \left(t _ {1}\right) + \left(t _ {\mathrm{f}} - x _ {2 0}\right) x _ {2} \left(t _ {1}\right) + x _ {1 0} + \frac {1}{2} x _ {2 0} ^ {2} = 0$$

由上式解出

$$x _ {2} \left(t _ {1}\right) = - \frac {t _ {\mathrm{f}} - x _ {2 0}}{2} \pm \frac {1}{2} \left[ \left(t _ {\mathrm{f}} - x _ {2 0}\right) ^ {2} - 4 x _ {1 0} - 2 x _ {2 0} ^ {2} \right] ^ {\frac {1}{2}} (4 - 8 2)$$

这里必须保证 $x_{2}(t_{1})$ 为实数，并在上式中选择正确的加减号。为了使 $x_{2}(t_{1})$ 为实数，必须有

$$\left(t _ {\mathrm{f}} - x _ {2 0}\right) ^ {2} - 4 x _ {1 0} - 2 x _ {2 0} ^ {2} \geqslant 0$$

这说明, 若 $t_{f}$ 规定小于最短时间(使上式等于 0 的 $t_{f}$ 值), 最少燃料控制是无解的。为了选择正确的加、减号, 应注意有下面的关系:

$$0 < t _ {1} < t _ {2} < t _ {\mathrm{f}}$$

即 $t_2 - t_1 > 0$ ，由式(4-81)可得

$$x _ {2} \left(t _ {1}\right) > - \frac {1}{2} \left(t _ {\mathrm{f}} - x _ {2 0}\right)$$

于是从式(4-82)可知,应选择加号,即

$$x _ {2} \left(t _ {1}\right) = - \frac {1}{2} \left\{t _ {\mathrm{f}} - x _ {2 0} - \left[ \left(t _ {\mathrm{f}} - x _ {2 0}\right) ^ {2} - 4 x _ {1 0} - 2 x _ {2 0} ^ {2} \right] ^ {\frac {1}{2}} \right\} \tag {4-83}$$
