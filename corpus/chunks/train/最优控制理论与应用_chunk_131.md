$$\frac {\partial \boldsymbol {\Psi}}{\partial \boldsymbol {\lambda} ^ {T} \left(t _ {0}\right)} = \left[ \frac {\partial \mathbf {Z} _ {i} \left(t _ {f}\right)}{\partial \boldsymbol {\lambda} _ {j} \left(t _ {0}\right)} \right] _ {\boldsymbol {\lambda} _ {j} \left(t _ {0}\right) = \hat {\boldsymbol {\lambda}} _ {j} \left(t _ {0}\right)} \tag {7-71}$$

式中， $\frac{\partial \mathbf{Z}_i(t_f)}{\partial \pmb{\lambda}_j(t_0)}$ 是 $\frac{\partial \Psi}{\partial \pmb{\lambda}}$ 的第 $i$ 行，第 $j$ 列元素。式(7-71)右端表示由第 $i$ 行第 $j$ 列元素构成的矩阵。

由式(7-69)和式(7-70)可得

$$\boldsymbol {\lambda} \left(t _ {0}\right) = \hat {\boldsymbol {\lambda}} \left(t _ {0}\right) + \left(\frac {\partial \boldsymbol {\Psi}}{\partial \boldsymbol {\lambda} ^ {\mathrm{T}} \left(t _ {0}\right)}\right) ^ {- 1} \left(\boldsymbol {Z} \left(t _ {\mathrm{f}}\right) - \hat {\boldsymbol {Z}} \left(t _ {\mathrm{f}}\right)\right) \tag {7-72}$$

因 $\pmb{\Psi}$ 一般是非线性函数，式(7-72)是一个近似式，为了求得正确的 $\pmb {\lambda}(t_0)$ ，要用迭代求解。令 $\hat{\pmb{\lambda}}^K (t_0)$ 是第 $K$ 步的估值，则根据式(7-72)可得到下面的迭代格式

$$\hat {\boldsymbol {\lambda}} ^ {K + 1} \left(t _ {0}\right) = \hat {\boldsymbol {\lambda}} ^ {K} \left(t _ {0}\right) + \beta \left(\frac {\partial \boldsymbol {\Psi}}{\partial \boldsymbol {\lambda} ^ {T} \left(t _ {0}\right)}\right) _ {K} ^ {- 1} \left(\boldsymbol {Z} \left(t _ {f}\right) - \hat {\boldsymbol {Z}} ^ {K} \left(t _ {f}\right)\right) (7 - 7 3)$$

其中， $K$ 是迭代次数， $\beta$ 是松弛因子， $0 \leqslant \beta \leqslant 1, \beta$ 可改善收敛性，收敛到最后时，将 $\beta$ 取为1。在第 $K$ 步，用 $\hat{\lambda}^K(t_0)$ 作为估值，积分正则方程，求得 $\hat{Z}^K(t_f)$ ，若

$$\left\| \mathbf {Z} (t _ {\mathrm{f}}) - \hat {\mathbf {Z}} ^ {K} (t _ {\mathrm{f}}) \right\| < \varepsilon \tag {7-74}$$

$\varepsilon$ 为指定的小值，则停止计算。否则用 $\hat{\pmb{\lambda}}^K (t_0)$ 代替 $\hat{\pmb{\lambda}}^{K + 1}(t_0)$ ，再积分正则方程，重复进行。

计算步骤如下：

(1) 由 $\frac{\partial H}{\partial u}=0$ 解出 $u=u(X,\lambda,t)$ ，代入状态和协态方程。

(2) 设已求出 $\pmb{\lambda}(t_0)$ 的第 $K$ 步估计值 $\hat{\pmb{\lambda}}^K(t_0)$ 和给定的 $\pmb{X}(t_0)$ 合在一起，从 $t_0$ 到 $t_f$ 积分正则方程，求出 $\pmb{X}^K(t), \pmb{\lambda}^K(t)$ 。抽出 $n$ 个要求的分量的终值 $\hat{\pmb{Z}}^K(t_f)$ ，若 $\| \pmb{Z}(t_f) - \hat{\pmb{Z}}^K(t_f) \| < \varepsilon$ ，停止计算，否则进行下一步。

(3) 求敏感矩阵 $\frac{\partial\Psi}{\partial\lambda^{T}}$ 。

(4) 按 $(7-73)$ 计算 $\hat{\lambda}^{K+1}(t_{0})$ 。

(5) 令 $K = K + 1$ 回到步骤(2)。
