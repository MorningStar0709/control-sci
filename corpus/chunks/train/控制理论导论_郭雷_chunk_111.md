$$\dot {\hat {x}} _ {L} = \boldsymbol {A} _ {L} \hat {x} _ {L} (t). \tag {1.8.7}$$

由于 $\sigma(A_L) \subset \mathbb{C}^-$ , 因此由方程 (1.8.7) 可知, 对任意 $\hat{x}_L(t_0)$ 都有

$$\lim _ {t \rightarrow \infty} \widehat {x} _ {L} (t) = 0. \tag {1.8.8}$$

又由式 (1.8.6), (1.8.4) 的第三式知

$$
\begin{array}{l} 0 = \lim _ {t \rightarrow \infty} z (t) = \lim _ {t \rightarrow \infty} \left(\boldsymbol {D} _ {L} x _ {L} (t) + \boldsymbol {D} _ {2} x _ {2} (t)\right) \\ = \lim _ {t \rightarrow \infty} \left(\boldsymbol {D} _ {L} \widehat {\boldsymbol {x}} _ {L} (t) + \left(\boldsymbol {D} _ {2} - \boldsymbol {D} _ {L} \boldsymbol {V}\right) \boldsymbol {x} _ {2} (t)\right) \\ = \lim _ {t \rightarrow \infty} (D _ {2} - D _ {L} V) x _ {2} (t). \\ \end{array}
$$

注意当 $x_{20} \neq 0$ 时，或者 $\lim_{t \to \infty} x_2(t)$ 不存在，或者 $\lim_{t \to \infty} |x_2(t)| = \infty$ 。所以有

$$\boldsymbol {D} _ {L} \boldsymbol {V} = \boldsymbol {D} _ {2}.$$

必要性得证.

推论1.8.1 已知闭环系统是内部稳定的。那么它是输出调节的充分必要条件是，存在 $n_1 \times n_2$ 和 $l \times n_2$ 常值矩阵 $V_1$ 和 $V_2$ ，使得等式

$$
\left\{ \begin{array}{l} (A _ {1} + B _ {1} F C _ {1}) V _ {1} - V _ {1} A _ {2} + B _ {1} F _ {c} V _ {2} = A _ {3} + B _ {1} F C _ {2} \\ B _ {c} C _ {1} V _ {1} + A _ {c} V _ {2} - V _ {2} A _ {2} = B _ {c} C _ {2} \\ D _ {1} V _ {1} = D _ {2} \end{array} \right. \tag {1.8.9}
$$

成立.

前面说过，调节器理论中的基本问题是动态补偿器的设计。为便于理解，暂时不考虑干扰信号对系统的影响，同时认为量测输出就是被调节输出。于是在这些假设下，对系统(1.8.1)作如下假设：

$$\boldsymbol {A} _ {3} = 0, \quad \boldsymbol {C} _ {1} = \boldsymbol {D} _ {1}, \quad \boldsymbol {C} _ {2} = \boldsymbol {D} _ {2} = 0,$$

这时 $y(t) = z(t)$ . 为书写简单，这一节把下标1都省略去，因此系统(1.8.1)就是在前几节研究的系统(1.6.1). 下面介绍三种关于系统(1.6.1)的动态补偿器的设计方法：
