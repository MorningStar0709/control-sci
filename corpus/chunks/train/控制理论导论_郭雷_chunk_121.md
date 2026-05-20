$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {1 e} \\ \dot {x} _ {2 e} \end{array} \right] = \left[ \begin{array}{c c c} A _ {1} & B _ {1} K _ {1} & - B _ {1} K _ {2} \\ G _ {1} C _ {1} & A _ {1} - G _ {1} C _ {1} + B _ {1} K _ {1} & 0 \\ G _ {2} C _ {1} & - G _ {2} C _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {1 e} \\ x _ {2 e} \end{array} \right] + \left[ \begin{array}{l} A _ {3} \\ 0 \\ 0 \end{array} \right] x _ {2}, \tag {1.8.37}
y (t) = C _ {1} x _ {1} (t). \tag {1.8.38}
$$

由于

$$
\begin{array}{l} \left[ \begin{array}{c c c} I _ {n _ {1}} & 0 & 0 \\ - I _ {n _ {1}} & I _ {n _ {1}} & 0 \\ 0 & 0 & I _ {n _ {2}} \end{array} \right] \left[ \begin{array}{c c c} A _ {1} & B _ {1} K _ {1} & - B _ {1} K _ {2} \\ G _ {1} C _ {1} & A _ {1} - G _ {1} C _ {1} + B _ {1} K _ {1} & 0 \\ G _ {2} C _ {1} & - G _ {2} C _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{c c c} I _ {n _ {1}} & 0 & 0 \\ I _ {n _ {1}} & I _ {n _ {1}} & 0 \\ 0 & 0 & I _ {n _ {2}} \end{array} \right] \\ = \left[ \begin{array}{c c c} A _ {1} + B _ {1} K _ {1} & B _ {1} K _ {1} & - B _ {1} K _ {2} \\ 0 & A _ {1} - G _ {1} C _ {1} & A _ {3} \\ 0 & - G _ {2} C _ {1} & A _ {2} \end{array} \right], \\ \end{array}
$$

所以闭环系统的特征值集合为

$$
\sigma (A _ {1} + B _ {1} K _ {1}) \cup \sigma \left(\left[ \begin{array}{c c} A _ {1} - G _ {1} C _ {1} & A _ {3} \\ - G _ {2} C _ {1} & A _ {2} \end{array} \right]\right) \subset \mathbb {C} ^ {-},
$$

故闭环系统 (1.8.37), (1.8.38) 是内部稳定的.

此外，如果取 $V_{1}=0, V_{2}=0, V_{3}=-I_{n_{2}}$ ，那么有

$$
\left[ \begin{array}{c c c} A _ {1} & B _ {1} K _ {1} & - B _ {1} K _ {2} \\ G _ {1} C _ {1} & A _ {1} - G _ {1} C _ {1} + B _ {1} K _ {1} & 0 \\ G _ {2} C _ {1} & - G _ {2} C _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{l} V _ {1} \\ V _ {2} \\ V _ {3} \end{array} \right] - \left[ \begin{array}{l} V _ {1} \\ V _ {2} \\ V _ {3} \end{array} \right] A _ {2} = \left[ \begin{array}{l} A _ {3} \\ 0 \\ 0 \end{array} \right],
\boldsymbol {C} _ {1} \boldsymbol {V} _ {1} = 0.
$$

根据引理1.8.1可知，闭环系统是输出调节的。可见按上述步骤设计的动态补偿器是合乎要求的。这就完成了定理的证明。

对带有干扰补偿的动态补偿器可作如下解释. 当把控制规律 (1.8.34) \~ (1.8.36) 代入系统 (1.8.29) 后, 有

$$\dot {x} _ {1} (t) = A _ {1} x _ {1} (t) + B _ {1} K _ {1} x _ {1 e} (t) + B _ {1} K _ {1} \left(x _ {2} - x _ {2 e}\right)$$

或者

$$\dot {x} _ {1} (t) = \left(A _ {1} + B _ {1} K _ {1}\right) x _ {1} (t) + B _ {1} K _ {1} \tilde {x} _ {1 e} (t) - B _ {1} K _ {1} \tilde {x} _ {2 e}$$

这里 $\tilde{x}_{1e}(t) = x_{1e}(t) - x_1(t)$ , $\tilde{x}_{2e}(t) = x_{2e}(t) - x_2(t)$ . 当估计误差为 0 时, 也就是说当系统达到稳态时, 外部干扰就被完全补偿了.
