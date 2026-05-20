# 12.3 基本的迭代学习控制算法

Arimoto 等首先给出了线性时变连续系统的 D 型迭代学习控制律 $^{[1]}$

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {\Gamma} \dot {\boldsymbol {e}} _ {k} (t) \tag {12.6}$$

式中， $\Gamma$ 为常数增益矩阵。在 D 型算法的基础上，相继出现了 P 型、PI 型、PD 型迭代学习控制律。从一般意义来看它们都是 PID 型迭代学习控制律的特殊形式，PID 迭代学习控制律表示为

$$\boldsymbol {u} _ {k + 1} (t) = \boldsymbol {u} _ {k} (t) + \boldsymbol {\Gamma} \dot {\boldsymbol {e}} _ {k} (t) + \boldsymbol {\Phi} \boldsymbol {e} _ {k} (t) + \boldsymbol {\Psi} \int_ {0} ^ {t} \boldsymbol {e} _ {k} (\tau) \mathrm{d} \tau \tag {12.7}$$

式中， $\Gamma$ 、 $\Phi$ 、 $\Psi$ 为学习增益矩阵。算法中的误差信息使用 $\pmb{e}_k(t)$ 称为开环迭代学习控制；如果使用 $\pmb{e}_{k+1}(t)$ ，则称为闭环迭代学习控制；如果同时使用 $\pmb{e}_k(t)$ 和 $\pmb{e}_{k+1}(t)$ ，则称为开闭环迭代学习控制。

此外，还有高阶迭代学习控制算法、最优迭代学习控制算法、遗忘因子迭代学习控制算法和反馈-前馈迭代学习控制算法等。

学习算法的收敛性分析是迭代学习控制的核心问题。基本的收敛性分析方法有压缩映射方法、谱半径条件法、基于2D理论的分析方法和基于Lyapunov直接法的设计方法等。

![](image/012e32dca469c929dcede0097141dd53bf829366521b5328e8023724db9127e7.jpg)
