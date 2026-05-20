$$\int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \dot {\boldsymbol {x}} d t = \left[ \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \boldsymbol {x} \right] \Bigg | _ {t _ {0}} ^ {t _ {f}} - \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {d}{d t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \boldsymbol {x} d t \tag {10-33}$$

将式(10-33)代入式(10-32)，所得结果代入式(10-30)，同时将式(10-31)也代入式(10-30)，然后对式(10-30)表示的泛函增量取线性主部，即得泛函变分

$$\delta J = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial L}{\partial \boldsymbol {x}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} \mathrm{d} t + \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} \Bigg | _ {t _ {0}} ^ {t _ {f}} + L (\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t) \mid_ {t _ {f}} \delta t _ {f} \tag {10-34}$$

令式(10-34)表示的 $\delta J = 0$ ，同时考虑到 $\delta x(t_0) = 0$ ，立即得到 $t_f$ 自由、末端变动时泛函极值的必

要条件:欧拉方程

$$\frac {\partial L}{\partial \boldsymbol {x}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} = \mathbf {0} \tag {10-35}$$

横截条件及边界条件

$$\left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \Big | _ {t _ {f}} \delta \boldsymbol {x} (t _ {f}) + L (\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t) \mid_ {t _ {f}} \delta t _ {f} = 0, \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0} \tag {10-36}$$

由式(10-35)和式(10-36)的推导过程和推导结果可见：

1) $t_f$ 自由、末端变动时的欧拉方程(10-35)的形式，与 $t_f$ 固定、末端固定时的欧拉方程(10-22)完全相同，这一结论同样适用于有等式约束的泛函极值问题。  
2) $t_f$ 自由、末端变动时的横截条件及边界条件通式(10-36)，包含了 $t_f$ 固定、末端固定时的横截条件及边界条件通式(10-24)，因为在 $t_f$ 固定的情况下必有 $\delta t_f = 0$ 。

(3) 末端时刻自由、末端状态变动时的横截条件

1) 末端自由时的横截条件。当末端 $x(t_f)$ 自由时，关系式(10-26)成立：

$$\delta \boldsymbol {x} (t _ {f}) = \delta \boldsymbol {x} _ {f} - \dot {\boldsymbol {x}} (t _ {f}) \delta t _ {f}$$

将上式代入式(10-36)，整理得
