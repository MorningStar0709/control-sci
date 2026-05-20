# (2) 定常连续动态方程的离散化

已知定常连续系统状态方程 $\dot{\pmb{x}} = \pmb {A}\pmb {x} + \pmb {B}\pmb{u}$ 在 $x(t_0)$ 及 $\pmb {u}(t)$ 作用下的解为

$$\boldsymbol {x} (t) = \boldsymbol {\Phi} (t - t _ {0}) \boldsymbol {x} (t _ {0}) + \int_ {t _ {0}} ^ {T} \boldsymbol {\Phi} (t - \tau) \boldsymbol {B u} (\tau) d \tau$$

令 $t_0 = kT$ ，则 $\pmb{x}(t_0) = \pmb{x}(kT) = \pmb{x}(k)$ ；令 $t = (k + 1)T$ ，则 $\pmb{x}(t) = \pmb{x}[(k + 1)T] = \pmb{x}(k + 1)$ ；在 $t\in [k,k + 1)$ 区间内， $\pmb {u}(t) = \pmb {u}(k) =$ 常数，于是其解化为

$$\boldsymbol {x} (k + 1) = \boldsymbol {\Phi} [ (k + 1) T - k T ] \boldsymbol {x} (k) + \int_ {k T} ^ {(k + 1) T} \boldsymbol {\Phi} [ (k + 1) T - \tau ] \boldsymbol {B} d \tau \cdot \boldsymbol {u} (k)$$

记 $\pmb {G}(T) = \int_{kT}^{(k + 1)T}\pmb {\Phi}[ (k + 1)T - \tau ]\pmb {B}\mathrm{d}\tau$

为了便于计算 $\mathbf{G}(T)$ ，引入变量置换，令 $(k + 1)T - \tau = \tau'$ ，则

$$\pmb {G} (T) = \int_ {0} ^ {T} \pmb {\Phi} (\tau^ {\prime}) \pmb {B} \mathrm{d} \tau^ {\prime} \tag {9-69}$$

故离散化状态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {\Phi} (T) \boldsymbol {x} (k) + \boldsymbol {G} (T) \boldsymbol {u} (k) \tag {9-70}$$

式中， $\Phi(T)$ 与连续系统状态转移矩阵 $\Phi(T)$ 的关系为

$$\boldsymbol {\Phi} (T) = \boldsymbol {\Phi} (t) \Big | _ {t = T} \tag {9-71}$$

离散化系统的输出方程仍为

$$\mathbf {y} (k) = \mathbf {C x} (k) + \mathbf {D u} (k)$$
