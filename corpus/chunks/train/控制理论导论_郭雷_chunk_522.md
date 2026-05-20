# 线性控制系统的快速控制

线性时变控制系统的快速控制的状态方程，初始条件，控制约束，目标集和性能指标分别是

$$
\left\{ \begin{array}{l} \dot {x} = A (t) x + B (t) u, \\ x \left(t _ {0}\right) = x _ {0}, \end{array} \right. \tag {7.2.11}
u \in \mathbb {U} _ {r} = \{u | | u _ {j} | \leqslant 1, j = 1, 2, \dots , r \}, \tag {7.2.12}\mathcal {S} \stackrel {\text { def }} {=} \{x (t _ {f}) \mid x (t _ {f}) = 0 \}, \tag {7.2.13}J [ u ] = \int_ {t _ {0}} ^ {t _ {f}} \mathrm{d} t = t _ {f} - t _ {0}, \tag {7.2.14}
$$

其中 $A(t)=[a_{ik}(t)]$ 和 $B=[b_{ij}(t)]=[b_{1}(t),b_{2}(t),\cdots,b_{r}(t)]$ 分别是 $n\times n,n\times r$ 矩阵值函数，它们的元都是 t 的连续（或分段连续）函数.

利用极大值原理来求上述快速控制函数. 易知式 (7.2.11) 和式 (7.2.14) 的 Hamilton 函数 $H(x, u, \psi, t)$ 为

$$H (x, u, \psi , t) \stackrel {\mathrm{def}} {=} - 1 + \psi^ {\mathrm{T}} A (t) x + \psi^ {\mathrm{T}} B (t) u,$$

相应的共轭方程和横截条件是

$$\dot {\psi} = - A ^ {T} (t) \psi , \quad \psi (t _ {f}) = \mu . \tag {7.2.15}$$

记 $\Phi(t, s)$ 为式 (7.2.11) 的基本解矩阵，则式 (7.2.15) 的解 $\psi(t)$ 为

$$\psi (t) = \Phi^ {\mathbf {T}} (t _ {f}, t) \mu ,$$

根据极大值原理，由 $H(x,u,\psi ,t)$ 的特殊形式可知，快速控制 $u^{*}(t)$ 由

$$\psi^ {\mathrm{T}} (t) B (t) u ^ {*} (t) = \max _ {u \in \mathbf {U} _ {\mathrm{r}}} \psi^ {\mathrm{T}} (t) B (t) u \tag {7.2.16}$$

确定，并且有

$$\mu^ {\mathrm{T}} B (t _ {f}) u ^ {*} (t _ {f}) = 1, \quad \mu \neq 0.$$

注意到求解 $\max_{u\in U_{r}}\mu^{T}\Phi(t_{f},t)B(t)u$ 等价于求解 $\sum_{j=1}^{r}\max_{|u_{j}|\leqslant1}\mu^{T}\Phi(t_{f},t)b_{j}(t)u_{j}$ . 因此, $\forall j=1,2,\cdots,r$ , 当 $\psi^{T}(t)b_{j}(t)$ 在任一长度不为零的有限时间区间上仅有有限多个零点时, 快速控制函数 $u_{j}^{*}(t)$ 可表示为

$$u _ {j} ^ {*} (t) = \operatorname{sign} (\psi^ {\mathrm{T}} (t) b _ {j} (t)) = \operatorname{sign} (\mu^ {\mathrm{T}} (t) \Phi (t _ {f}, t) b _ {j} (t)), \quad j = 1, \dots , r,$$

或

$$u ^ {*} (t) = \operatorname{sign} (B ^ {\mathrm{T}} (t) \Phi^ {\mathrm{T}} (t _ {f}, t) \mu).$$

定理 7.2.2 对于快速控制系统 (7.2.11)\~(7.2.14)，假定 $A(t)$ ， $B(t)$ (n-1) 次连续可微。如果 $\forall j=1,2,\cdots,r$ 和 $e_{j}=\underbrace{[0,0,\cdots,0}_{j-1},1,\underbrace{0,0,\cdots,0}_{n-j}^{T}$ ，在任意长度不为零的区间 $[t_{1},t_{2}]$ 上皆有

$$\operatorname{rank} \left[ B _ {1} (t) e _ {j}, B _ {2} (t) e _ {j}, \dots , B _ {n} (t) e _ {j} \right] = n, \tag {7.2.17}$$

则 $\forall j=1,2,\cdots,r,b_{j}^{\mathrm{T}}(t)\psi(t)=b_{j}^{\mathrm{T}}\Phi^{\mathrm{T}}(t_{f},t)\mu$ 在 $[t_{1},t_{2}]$ 上至多有有限多个零点，即式 (7.2.11)\~(7.2.14) 是正则快速控制系统。在式 (7.2.17) 中
