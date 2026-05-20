# 9.7.2 RBF 网络原理

由于 RBF 网络具有万能逼近特性 $^{[20]}$ ，因此采用 RBF 神经网络逼近 $f(x)$ ，网络算法为

$$h _ {j} = \exp \left(\frac {\| x - c _ {j} \| ^ {2}}{2 b _ {j} ^ {2}}\right) \tag {9.33}f = \boldsymbol {W} ^ {* \mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) + \varepsilon \tag {9.34}$$

式中，x 为网络的输入，j 为网络隐含层第 j 个节点， $h = [h_j]^T$ 为网络的高斯基函数输出， $W^*$ 为网络的理想权值， $\varepsilon$ 为网络的逼近误差， $\varepsilon \leqslant \varepsilon_N$ 。

网络输入取 $x = [x_{1} \quad x_{2}]^{T}$ ，则网络输出为

$$\hat {f} (x) = \hat {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {h} (x) \tag {9.35}$$
