# 习题 9.2

9.2.1 设 $\{w_{t},\mathcal{F}_{t}\}$ 是鞅差序列且满足本节条件 (A1), $\{f_t,\mathcal{F}_t\}$ 是任意随机适应序列, 利用本节定理证明下列估计式成立:

$$\sum_ {k = 1} ^ {t} f _ {k} w _ {k + 1} = O \left(\sqrt {s _ {t} \log s _ {t}}\right), \quad \text { a.s. },$$

其中 $s_t \stackrel{\text{def}}{=} \sum_{k=1}^{t} f_k^2$ .

9.2.2 设 $\{\phi_t\}$ 是有界序列，证明对由式 (9.2.5) 所定义的序列 $\{P_t\}$ ，当 $t \to \infty$ 时有 $\phi_t^{\mathrm{T}} P_t \phi_t \to 0$ 。进一步，对怎样的无界序列 $\{\phi_t\}$ ，此结果也成立？

9.2.3 考虑由式 (9.2.4)\~(9.2.6) 所定义的递推最小二乘算法，证明对任何初值 $(\theta_0, P_0)$ ，LS 的可能增长有上界

$$\| \theta_ {t + 1} \| = O (1) + o (\sqrt {\log r _ {t}}) \quad \text { a.s. }$$

其中 $r_t$ 由式 (9.2.9) 所定义 (注意, 该结论并不能直接从推论 9.2.1 得出, 因为我们没有假定 $\lambda_{\min}(P_{t+1}^{-1}) \to \infty$ ).

9.2.4 在什么条件下，递推 LS 估计是线性回归模型 (9.2.1) 的最小方差估计？对怎样的线性回归模型，加权最小二乘 (WLS) 估计也是最小方差估计？（提示：可利用 Kalman 滤波理论。）

9.2.5 LS 算法是否也具有自收敛性？(提示：可参考文献 [38],[40]).

9.2.6 设回归向量 $\phi_{t}$ 有下列表达式

$$\phi_ {t} ^ {\mathrm{T}} = [ F (z), \dots , z ^ {m} F (z), G (z), \dots , z ^ {n} G (z) ] \xi_ {t},$$

其中 $F(z)$ 和 $G(z)$ 是两个互质的多项式，其次数分别记为 $\partial F$ 和 $\partial G, m \geqslant 0$ 及 $n \geqslant 0$ 为两个整数， $z$ 表示后移算子（即 $z^k\xi_t \stackrel{\mathrm{def}}{=} \xi_{t-k}, k \geqslant 0$ ）。若 $m < \partial G$ 或 $n < \partial F$ ，证明一定存在常数 $c > 0$ ，使

$$\lambda_ {\min} \left(\sum_ {i = 0} ^ {t} \phi_ {i} \phi_ {i} ^ {\mathrm{T}}\right) \geqslant c \lambda_ {\min} \left(\sum_ {i = 0} ^ {t} \psi_ {i} \psi_ {i} ^ {\mathrm{T}}\right)$$

其中 $\psi_{t}^{T}\stackrel{\operatorname{def}}{=}[\xi_{t},\xi_{t-1},\cdots,\xi_{t-s}], s=\max\{m+\partial F,n+\partial G\}$ .

9.2.7 若一个实系数的有理分式 $H(z)$ 在单位圆 $|z| \leqslant 1$ 内没有极点，且满足

$$H \left(\mathrm{e} ^ {i \lambda}\right) + H \left(\mathrm{e} ^ {- i \lambda}\right) > 0, \quad \forall \lambda \in [ 0, 2 \pi ],$$

则 $H(z)$ 称为是严格正实 (SPR) 的. 设 $H(z)$ 是 SPR 的, 证明下列两个结论成立:

a) $H^{-1}(z)$ 也是SPR的；

b) 存在 $\epsilon > 0$ 使对任何 $t \geqslant 0$ 都有

$$\sum_ {i = 0} ^ {t} u _ {i} y _ {i} \geqslant \epsilon \sum_ {i = 0} ^ {t} (u _ {i} ^ {2} + y _ {i} ^ {2}),$$

其中 $\{y_i\}$ 和 $\{u_i\}$ 以 $H(z)$ 为传递函数 $y_t = H(z)u_t$ ，其中 $z$ 为后移算子，且假定 $u_t = y_t = 0$ ， $\forall t < 0$ .

9.2.8 考虑下列具有相关噪声的线性模型

$$\boldsymbol {y} _ {t + 1} = \boldsymbol {\beta} ^ {\mathbf {T}} \boldsymbol {\psi} _ {t} + \epsilon_ {t + 1},\epsilon_ {t + 1} = w _ {t + 1} + c _ {1} w _ {t} + \dots + c _ {r} w _ {t - r + 1},$$

其中 $\beta^{\mathrm{T}}$ 和 $c_{i}(1\leqslant i\leqslant r)$ 为未知参数， $\{w_t,\mathcal{F}_t\}$ 是鞅差噪声序列并满足本节的条件(A1)， $\{\psi_t,\mathcal{F}_t\}$ 是适应的随机回归向量序列．对未知参数向量
