# 1. 控制器的设计

采用 RBF 网络逼近 f，则 RBF 神经网络的输出为

$$\hat {\boldsymbol {f}} (\boldsymbol {x}) = \hat {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {\varphi} (\boldsymbol {x}) \tag {9.69}$$

取

$$\tilde {W} = W ^ {*} - \hat {W}, \| W ^ {*} \| _ {F} \leqslant W _ {\max}$$

设计控制律为

$$\boldsymbol {\tau} = \hat {\boldsymbol {f}} (\boldsymbol {x}) + \mathbf {K} _ {\mathrm{v}} \boldsymbol {r} - \boldsymbol {v} \tag {9.70}$$

式中，v 为用于克服神经网络逼近误差 $\varepsilon$ 的鲁棒项。

将控制律式(9.70)代入式(9.66)，得

$$\boldsymbol {D} \dot {\boldsymbol {r}} = - (\boldsymbol {K} _ {\mathrm{v}} + \boldsymbol {C}) \boldsymbol {r} + \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {\varphi} (\boldsymbol {x}) + (\boldsymbol {\varepsilon} + \boldsymbol {\tau} _ {\mathrm{d}}) + \boldsymbol {v} = - (\boldsymbol {K} _ {\mathrm{v}} + \boldsymbol {C}) \boldsymbol {r} + \varsigma_ {1} \tag {9.71}$$

式中， $\varsigma_{1}=\tilde{W}^{\mathrm{T}}\varphi(x)+(\varepsilon+\tau_{\mathrm{d}})+v$ 。

将鲁棒项 v 设计为

$$\boldsymbol {v} = - \left(\varepsilon_ {\mathrm{N}} + b _ {\mathrm{d}}\right) \operatorname{sign} (\boldsymbol {r}) \tag {9.72}$$

式中， $\| \pmb {\varepsilon}\| \leqslant \varepsilon_{\mathrm{N}},\| \pmb{\tau}_{\mathrm{d}}\| \leqslant b_{\mathrm{d}}$ 。
