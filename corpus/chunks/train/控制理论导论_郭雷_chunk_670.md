注意到 $\theta$ 是常值，利用条件 (A1) 和 (A2) 从式 (9.2.1) 可得

$$E [ y _ {t + 1} | \mathcal {F} _ {t} ] = \theta^ {\mathrm{T}} \phi_ {t}.$$

因此，可以将下式称为对输出的条件期望的 LS 估计 (对输出本身的预报)

$$\hat {y} _ {t + 1} \stackrel {\text { def }} {=} \theta_ {t} ^ {\mathrm{T}} \phi_ {t}.$$

根据定理 9.2.1(ii) 可直接得到下列推论:

推论9.2.2 在定理9.2.1的条件下，

(i) 若 $\{\phi_t\}$ 满足条件

$$\phi_ {t} ^ {\mathrm{T}} P _ {t} \phi_ {t} = o \left(\frac {r _ {t}}{\log r _ {t}}\right) \quad \text { a.s., } \tag {9.2.20}$$

则当 $t \to \infty$ 时，对 $E[y_{t+1}|\mathcal{F}_t]$ 之 LS 估计的“平均”误差在下列意义下趋于零

$$\sum_ {i = 0} ^ {t} (E [ y _ {i + 1} | \mathcal {F} _ {i} ] - \hat {y} _ {i + 1}) ^ {2} = o (r _ {t}), \quad \text { a.s. } \quad \text { on } \quad [ r _ {t} \to \infty ]; \tag {9.2.21}$$

(ii) 若 $\{\phi_t\}$ 进一步满足条件

$$\phi_ {t} ^ {\mathrm{T}} P _ {t} \phi_ {t} = O (1) \quad \text { a.s., } \tag {9.2.22}$$

则

$$\sum_ {i = 0} ^ {t} (E [ y _ {i + 1} | \mathcal {F} _ {i} ] - \hat {y} _ {i + 1}) ^ {2} = O (\log r _ {t}), \quad \text { a.s. } \tag {9.2.23}$$

这说明“积累的”估计误差只有 $O(\log r_t)$ 的数量级，大大改进了式(9.2.21)中的结果.

然而，正如验证条件(9.2.19)一样，在一般自适应控制系统中，直接验证哪怕看起来较弱的条件(9.2.20)或条件(9.2.22)也往往不易。避开这一难点的办法之一是对LS算法进行适当的修正，使其不需要上述条件，也能得到类似于LS所具有的良好的渐近性质。

例如，考虑下列以序列 $\{\lambda_i\}$ 为加权的二次型指标：

$$J _ {t} (\theta) \stackrel {\text { def }} {=} \sum_ {i = 0} ^ {t} \lambda_ {i} (y _ {i + 1} - \theta^ {\mathrm{T}} \phi_ {i}) ^ {2}. \tag {9.2.24}$$

我们仍用 $\theta_{t + 1}$ 表示极小化上式的值（称为 $\theta$ 的加权最小二乘或WLS估计），则类似于前述LS情形，可得到如下WLS递推公式：

$$\theta_ {t + 1} = \theta_ {t} + a _ {t} P _ {t} \phi_ {t} (y _ {t + 1} - \phi_ {t} ^ {\mathrm{T}} \theta_ {t}), \tag {9.2.25}P _ {t + 1} = P _ {t} - a _ {t} P _ {t} \phi_ {t} \phi_ {t} ^ {\mathrm{T}} P _ {t}, \tag {9.2.26}a _ {t} = \left(\lambda_ {t} ^ {- 1} + \phi_ {t} ^ {\mathrm{T}} P _ {t} \phi_ {t}\right) ^ {- 1}. \tag {9.2.27}$$

为保证WLS具有良好的渐近性质，通常可简单取权函数为

$$\lambda_ {t} = \frac {1}{\log^ {1 + \delta} r _ {t}}, \quad \delta > 0, \tag {9.2.28}$$

其中 $r_t$ 仍如式 (9.2.9) 所定义。注意到 $\{\lambda_t\}$ 是非增序列，这说明 WLS 是一种“谨慎”的估计，因它的加权可用于对付一定的较大噪声方差的影响（见习题 9.2.4）。

类似于定理 9.2.1, 我们有下述结果 [3]:

定理 9.2.2 对随机回归模型 (9.2.1), 设条件 (A1) 和 (A2) 满足 (在条件 (A1) 中只需假定 $\beta = 2$ ), 那么当 $t \to \infty$ 时 WLS 算法 (9.2.25)\~算法 (9.2.28) 具有下列渐近性质:

(i) $\tilde{\theta}_{t + 1}^{\mathrm{T}}P_{t + 1}^{-1}\tilde{\theta}_{t + 1} = O(1)$ , a.s.

(ii) $\sum_{k=1}^{\infty} \frac{(\phi_k^T \tilde{\theta}_k)^2}{\lambda_k^{-1} + \phi_k^T P_k \phi_k} < \infty$ , a.s.

证明 记
