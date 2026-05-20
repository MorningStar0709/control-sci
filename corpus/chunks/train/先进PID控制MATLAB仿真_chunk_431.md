# 1. 基本的神经网络系统

RBF 神经网络具有万能逼近的特性 $^{[5]}$ ，采用 RBF 网络可实现对不确定项 f 进行自适应逼近。RBF 网络算法为

$$h _ {j} = g \left(\left\| \boldsymbol {x} - \boldsymbol {c} \right\| ^ {2} / b _ {j} ^ {2}\right)f = \boldsymbol {W} ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) + \varepsilon$$

式中，x 为网络的输入信号； $c=[c_{ij}]$ ；i 为网络输入个数；j 为网络隐含层节点的个数； $h=\left[h_{1},h_{2},\cdots,h_{n}\right]^{T}$ 为高斯基函数的输出；W 为神经网络权值； $\varepsilon$ 为神经网络逼近误差， $\varepsilon\leqslant\varepsilon_{N}$ 。

采用 RBF 网络逼近 f，根据 f 的表达式，网络输入取 $x=\left[e\quad\dot{e}\right]^{T}$ ，RBF 神经网络的输出为

$$\hat {f} (\boldsymbol {x}) = \hat {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) \tag {9.16}$$
