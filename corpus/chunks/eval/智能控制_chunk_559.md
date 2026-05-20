# 11.5.2 控制器设计及收敛性分析

定理 若由式(11.13)和式(11.14)描述的系统满足如下条件 $^{[24]}$

(1) $\| \mathbf{I} - \mathbf{C}(t)\mathbf{B}(t)\mathbf{\Gamma}(t)\| \leqslant \overline{\rho} < 1;$

(2) 每次迭代初始条件一致, 即 $x_{k}(0) = x_{0}(0)(k = 1, 2, 3, \cdots)$ , $y_{0}(0) = y_{d}(0)$ 。

则当 $k \to \infty$ 时，有 $\mathbf{y}_k(t) \to \mathbf{y}_{\mathrm{d}}(t), \forall t \in [0, T]$ 。

参考文献[27],下面给出定理1的收敛性详细证明。

证明 由式(11.13)及条件式(2)得 $y_{k+1}(0)=Cx_{k+1}(0)=Cx_{k}(0)=y_{k}(0)$ ，则 $y_{k}(0)=y_{0}(0), e_{k}(0)=y_{d}(0)-y_{k}(0)=0 (k=0,1,2,\cdots)$ ，即系统满足初始条件。

非齐次一阶线性微分方程 $\dot{\pmb{x}}(t) = \pmb {A}(t)\pmb {x}(t) + \pmb {B}(t)\pmb {u}(t)$ 的解为

$$
\begin{array}{l} \boldsymbol {x} (t) = \boldsymbol {C} \exp \left(\int_ {0} ^ {t} \boldsymbol {A} \mathrm{d} \tau\right) + \exp \left(\int_ {0} ^ {t} \boldsymbol {A} \mathrm{d} \tau\right) \int_ {0} ^ {t} \boldsymbol {B} (\tau) \boldsymbol {u} (\tau) \exp \left(\int_ {0} ^ {\tau} - \boldsymbol {A} \mathrm{d} \delta\right) \mathrm{d} \tau \\ = \mathbf {C} \exp (\mathbf {A} t) + \exp (\mathbf {A} t) \int_ {0} ^ {t} \mathbf {B} (\tau) \mathbf {u} (\tau) \exp (- \mathbf {A} \tau) d \tau \\ = \mathbf {C} \exp (\mathbf {A} t) + \int_ {0} ^ {t} \exp (\mathbf {A} (t - \tau)) \mathbf {B} (\tau) \mathbf {u} (\tau) d \tau \\ \end{array}
$$

取 $\boldsymbol{\Phi}(t,\tau)=\exp(\boldsymbol{A}(t-\tau))$ ，则

$$\boldsymbol {x} _ {k} (t) - \boldsymbol {x} _ {k + 1} (t) = \int_ {0} ^ {t} \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) (\boldsymbol {u} _ {k} (\tau) - \boldsymbol {u} _ {k + 1} (\tau)) \mathrm{d} \tau$$

由于 $e_k(t) = y_d(t) - y_k(t), e_{k+1}(t) = y_d(t) - y_{k+1}(t)$ ，则

$$
\begin{array}{l} \boldsymbol {e} _ {k + 1} (t) - \boldsymbol {e} _ {k} (t) = \mathbf {y} _ {k} (t) - \mathbf {y} _ {k + 1} (t) = \boldsymbol {C} (t) \left(\boldsymbol {x} _ {k} (t) - \boldsymbol {x} _ {k + 1} (t)\right) \\ = \int_ {0} ^ {t} \boldsymbol {C} (t) \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) \left(\boldsymbol {u} _ {k} (\tau) - \boldsymbol {u} _ {k + 1} (\tau)\right) d \tau \\ \end{array}
$$

即

$$\boldsymbol {e} _ {k + 1} (t) = \boldsymbol {e} _ {k} (t) - \int_ {0} ^ {t} \boldsymbol {C} (t) \boldsymbol {\Phi} (t, \tau) \boldsymbol {B} (\tau) (\boldsymbol {u} _ {k + 1} (\tau) - \boldsymbol {u} _ {k} (\tau)) \mathrm{d} \tau$$

将PID型控制律式(11.14)代入上式，则第 $k + 1$ 次输出的误差为
