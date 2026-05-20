# 9.8.2 模型不确定部分的RBF网络逼近

采用 RBF 网络对不确定项 f 进行自适应逼近。

RBF 网络输入、输出算法为

$$\phi_ {i} = g \left(\| \boldsymbol {x} - \boldsymbol {c} _ {i} \| ^ {2} / b _ {i} ^ {2}\right), i = 1, 2, \dots , ny = \boldsymbol {\theta} ^ {\mathrm{T}} \boldsymbol {\varphi} (\boldsymbol {x})$$

式中， $\| \cdot \|$ 为2-范数（见附录A）， $x$ 为网络的输入信号， $\varphi = [\phi_1, \phi_2, \dots, \phi_n]$ 为高斯基函数的输出， $\theta$ 为神经网络权值。

由已知证明可知 $^{[10.26]}$ ，在下述假设条件下，RBF网络针对连续函数在紧集范围内具有任意精度的逼近能力。

假设：

(1) 神经网络输出 $f(x,\theta)$ 为连续；  
(2) 存在理想的神经网络输出 $\hat{f}(x, \theta^{*})$ ，针对一个非常小的正实数 $\varepsilon_{0}$ ，有

$$\max \left\| \widehat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta} ^ {*}) - \boldsymbol {f} (\boldsymbol {x}) \right\| \leqslant \varepsilon_ {0}$$

误差状态方程式(9.45)可写为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \{\hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta} ^ {*}) + [ \boldsymbol {f} (\boldsymbol {x}) - \hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta} ^ {*}) ] \} \tag {9.47}$$

式中， $\pmb{\theta}^{*} = \arg \min_{\theta \in \beta (M_{\theta})}\{\sup_{x\in \varphi (M_x)}\| f(x) - \hat{f} (x,\pmb {\theta})\|\},\pmb{\theta}^{*}$ 为 $n\times n$ 阶矩阵，表示对 $f(x)$ 最佳逼近的神经网络权值。

取 $\| \pmb{\theta}^{*}\|_{\mathrm{F}}\leqslant \pmb{\theta}_{\max}$ ，由于 $f(x)$ 有界，则 $\pmb{\theta}^*$ 有界，即 $\pmb{\theta}_{\max}$ 有界。 $F-$ 范数定义见附录A。

式 $(9.47)$ 可写为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \{\hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta} ^ {*}) + \boldsymbol {\eta} \} \tag {9.48}$$

式中， $\eta$ 为神经网络理想逼近误差，即

$$\pmb {\eta} = \pmb {f} (\pmb {x}) - \hat {\pmb {f}} (\pmb {x}, \pmb {\theta} ^ {*}) \tag {9.49}$$

逼近误差 $\eta$ 为有界, 其界为 $\eta_{0}$ , 即

$$\pmb {\eta} _ {0} = \sup \| \pmb {f} (\pmb {x}) - \hat {\pmb {f}} (\pmb {x}, \pmb {\theta} ^ {*}) \| \tag {9.50}$$

神经网络输出 $f(\cdot)$ 的最佳估计值为

$$\hat {f} (x, \theta^ {*}) = \theta^ {* T} \varphi (x) \tag {9.51}$$

则式(9.48)可写为

$$\dot {\pmb {x}} = \pmb {A} \pmb {x} + \pmb {B} \{\pmb {\theta} ^ {* \mathrm{T}} \pmb {\varphi} (\pmb {x}) + \pmb {\eta} \} \tag {9.52}$$
