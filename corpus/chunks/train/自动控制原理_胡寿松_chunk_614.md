$$\boldsymbol {x} (t) = \mathscr {L} ^ {- 1} [ (\boldsymbol {s I} - \boldsymbol {A}) ^ {- 1} ] \boldsymbol {x} (0) \tag {9-28}$$

与式(9-25)相比有

$$\mathrm{e} ^ {\boldsymbol {A} t} = \mathscr {L} ^ {- 1} [ (\boldsymbol {s I} - \boldsymbol {A}) ^ {- 1} ] \tag {9-29}$$

式(9-29)给出了 $e^{A'}$ 的闭合形式,说明了式(9-24)所示级数的收敛性。

从上述分析可看出,求解齐次状态方程的问题,就是计算状态转移矩阵 $\Phi(t)$ 的问题,因而有必要研究 $\Phi(t)$ 的运算性质。

(2) 状态转移矩阵的运算性质

重写状态转移矩阵 $\Phi(t)$ 的幂级数展开式

$$\boldsymbol {\Phi} (t) = \mathrm{e} ^ {\boldsymbol {A} t} = \boldsymbol {I} + \boldsymbol {A} t + \frac {1}{2} \boldsymbol {A} ^ {2} t ^ {2} + \dots + \frac {1}{k !} \boldsymbol {A} ^ {k} t ^ {k} + \dots \tag {9-30}$$

$\Phi(t)$ 具有如下运算性质：

1) $\Phi(0) = I$ (9-31)

2) $\dot{\Phi}(t) = A\Phi(t) = \Phi(t)A$ (9-32)

上述性质利用式(9-30)很容易进行证明。式(9-32)表明， $A\Phi(t)$ 与 $\Phi(t)A$ 可交换， $\dot{\Phi}(0)=A$ ，并且 $\Phi(t)$ 是微分方程

$$\dot {\boldsymbol {\Phi}} (t) = \boldsymbol {A} \boldsymbol {\Phi} (t), \quad \boldsymbol {\Phi} (0) = \boldsymbol {I} \tag {9-33}$$

的唯一解。

3) $\Phi(t_1 \pm t_2) = \Phi(t_1) \Phi(\pm t_2) = \Phi(\pm t_2) \Phi(t_1)$ (9-34)

令式(9-30)中 $t=t_{1}\pm t_{2}$ ，便可证明这一性质。 $\Phi(t_{1}),\Phi(t_{2}),\Phi(t_{1}\pm t_{2})$ 分别表示由状态x(0)转移至状态 $x(t_{1}),x(t_{2}),x(t_{1}\pm t_{2})$ 的状态转移矩阵。该性质表明 $\Phi(t_{1}\pm t_{2})$ 可分解为 $\Phi(t_{1})$ 与 $\Phi(\pm t_{2})$ 的乘积，且 $\Phi(t_{1})$ 与 $\Phi(\pm t_{2})$ 是可交换的。

4) $\Phi^{-1}(t) = \Phi(-t), \quad \Phi^{-1} \quad (-t) = \Phi(t)$ (9-35)

证明 由性质3)有

$$\boldsymbol {\Phi} (t - t) = \boldsymbol {\Phi} (t) \boldsymbol {\Phi} (- t) = \boldsymbol {\Phi} (- t) \boldsymbol {\Phi} (t) = \boldsymbol {I}$$

根据逆矩阵的定义可得式(9-35)。

根据 $\Phi(t)$ 的这一性质,对于线性定常系统,显然有

$$\boldsymbol {x} (t) = \boldsymbol {\Phi} (t) \boldsymbol {x} (0), \quad \boldsymbol {x} (0) = \boldsymbol {\Phi} ^ {- 1} \quad (t) \boldsymbol {x} (t) = \boldsymbol {\Phi} (- t) \boldsymbol {x} (t)$$

这说明状态转移具有可逆性, $x(t)$ 可由 $x(0)$ 转移而来, $x(0)$ 也可由 $x(t)$ 转移而来。

5) $x(t_{2}) = \Phi (t_{2} - t_{1})x(t_{1})$ (9-36)

证明 由于

$$\boldsymbol {x} \left(t _ {1}\right) = \boldsymbol {\Phi} \left(t _ {1}\right) \boldsymbol {x} (0), \quad \boldsymbol {x} (0) = \boldsymbol {\Phi} ^ {- 1} \quad \left(t _ {1}\right) \boldsymbol {x} \left(t _ {1}\right) = \boldsymbol {\Phi} \left(- t _ {1}\right) \boldsymbol {x} \left(t _ {1}\right)$$

则 $x(t_{2}) = \Phi (t_{2})x(0) = \Phi (t_{2})\Phi (-t_{1})x(t_{1}) = \Phi (t_{2} - t_{1})x(t_{1})$

即由 $x(t_{1})$ 转移至 $x(t_{2})$ 的状态转移矩阵为 $\Phi(t_{2}-t_{1})$ 。
