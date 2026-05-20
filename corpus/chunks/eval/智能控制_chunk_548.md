# 11.2 基本迭代学习控制算法

Arimoto 等人首先给出了线性时变连续系统的 D 型迭代学习控制律 $^{[25]}$

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {\Gamma} \dot {\boldsymbol {e}} _ {k} (t) \tag {11.6}$$

式中， $\Gamma$ 为常数增益矩阵。在 D 型算法的基础上，相继出现了 P 型、PI 型、PD 型迭代学习控制律。从一般意义来看，它们都是 PID 型迭代学习控制律的特殊形式，PID 迭代学习控制律表示为

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {\Gamma} \dot {\boldsymbol {e}} _ {k} (t) + \boldsymbol {\Phi} \boldsymbol {e} _ {k} (t) + \boldsymbol {\Psi} \int_ {0} ^ {t} \boldsymbol {e} _ {k} (\tau) \mathrm{d} \tau \tag {11.7}$$

式中， $\Gamma, \Phi, \Psi$ 为学习增益矩阵。算法(11.7)中的误差信息使用 $e_k(t)$ ，称为开环迭代学习控制；如果使用 $e_{k+1}(t)$ ，则称为闭环迭代学习控制；如果同时使用 $e_k(t)$ 和 $e_{k+1}(t)$ ，则称为开闭环迭代学习控制。

此外，还有高阶迭代学习控制算法、最优迭代学习控制算法、遗忘因子迭代学习控制算法和反馈一前馈迭代学习控制算法等 $^{[26]}$ 。
