$$
\begin{array}{l} \boldsymbol {D} \dot {\boldsymbol {r}} = - \boldsymbol {C r} - \hat {\boldsymbol {f}} - \boldsymbol {K} _ {\mathrm{v}} \boldsymbol {r} + \boldsymbol {f} + \tau_ {\mathrm{d}} \\ = - \left(\mathbf {K} _ {\mathrm{v}} + \mathbf {C}\right) \mathbf {r} + \widetilde {\mathbf {f}} + \boldsymbol {\tau} _ {\mathrm{d}} = - \left(\mathbf {K} _ {\mathrm{v}} + \mathbf {C}\right) \mathbf {r} + \varsigma_ {0} \tag {9.68} \\ \end{array}
$$

式中， $\widetilde{f}=f-\widehat{f},\varsigma_{0}=\widetilde{f}+\tau_{d}$

定义 Lyapunov 函数

$$L = \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {D} \boldsymbol {r}$$

则

$$\dot {L} = \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {D} \dot {\boldsymbol {r}} + \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} \dot {\boldsymbol {D}} \boldsymbol {r} = - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{v}} \boldsymbol {r} + \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} (\dot {\boldsymbol {D}} - 2 \boldsymbol {C}) \boldsymbol {r} + \boldsymbol {r} ^ {\mathrm{T}} \varsigma_ {0}\dot {L} = \boldsymbol {r} ^ {\mathrm{T}} \varsigma_ {0} - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{v}} \boldsymbol {r}$$

可见，在 $K_{v}$ 固定条件下，控制系统的稳定依赖于 $S_{0}$ ，即f对f的逼近精度及干扰 $\tau_{d}$ 的大小。

采用 RBF 网络对不确定项 f 进行逼近。理想的 RBF 网络算法为

$$\phi_ {i} = g (\parallel \boldsymbol {x} - \boldsymbol {c} _ {i} \parallel^ {2} / b _ {i} ^ {2}), i = 1, 2, \dots , ny = W ^ {* T} \pmb {\varphi} (\pmb {x}), f (\pmb {x}) = w ^ {*} \pmb {\varphi} (\pmb {x}) + \varepsilon$$

式中，x 为网络的输入信号， $\varphi=\left[\phi_{1},\phi_{2},\cdots,\phi_{n}\right]^{T}$ ， $\varepsilon$ 为神经网络逼近误差， $w^{*}$ 为理想 RBF 网络的权值。
