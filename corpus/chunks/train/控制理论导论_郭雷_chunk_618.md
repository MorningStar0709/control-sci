$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{c} \mathrm{e} ^ {x _ {2}} (x _ {3} + 1) ^ {- 1} + \mathrm{e} ^ {x _ {4}} - x _ {1} \\ \mathrm{e} ^ {x _ {2}} (x _ {3} + 1) - 1 \\ \mathrm{e} ^ {x _ {2}} (x _ {3} + 1) ^ {2} \\ \mathrm{e} ^ {- x _ {4}} \end{array} \right] + \left[ \begin{array}{c} x _ {2} \mathrm{e} ^ {x _ {4}} + (\mathrm{e} ^ {x _ {4}} - 2) ^ {- 1} \\ x _ {1} \\ (x _ {3} + 1) ^ {3} (\mathrm{e} ^ {x _ {4}} - 2) ^ {- 1} \\ x _ {2} \end{array} \right] u \tag {8.4.15} \\ = f + g u, \\ \end{array}
$$

和分布

$$
\Delta = \text { span } \left\{\left[ \begin{array}{c} \mathrm{e} ^ {x _ {4}} \\ x _ {3} \\ 0 \\ 1 \end{array} \right], \quad \left[ \begin{array}{c} 1 \\ 1 \\ 0 \\ \mathrm{e} ^ {- x _ {4}} \end{array} \right] \right\}. \tag {8.4.16}
$$

容易验证 $\Delta$ 是对合的，且 $\Delta$ 和 $\Delta + G$ 在 $x = 0$ 的邻域内非奇异。此外， $\Delta$ 是弱 $(f, g)$ 不变的。我们将找一个合适的反馈律

$$u = \alpha + \beta v,$$

使得式 (8.4.2) 成立. 为得到平整坐标卡, 选择以下四个向量场

$$X _ {1} = \left[ e ^ {x _ {4}}, 0, 0, 1 \right] ^ {\mathrm{T}}, \quad X _ {2} = [ 0, 1, 0, 0 ] ^ {\mathrm{T}},X _ {3} = [ 0, 0, 0, 1 ]) ^ {\mathrm{T}}, \quad X _ {4} = [ 0, 0, 1, 0 ] ^ {\mathrm{T}}.$$

它们是线性无关的，令

$$\Delta = \operatorname{span} \left\{X _ {1}, X _ {2} \right\},$$

和

$$F (z) = \phi_ {z _ {1}} ^ {X _ {1}} \phi_ {z _ {2}} ^ {X _ {2}} \phi_ {z _ {3}} ^ {X _ {3}} \phi_ {z _ {4}} ^ {X _ {4}} (0). \tag {8.4.17}$$

于是 $z = F^{-1}(x)$ 定义了一个平整坐标卡。为得到 $F$ 可采用逐次积分方法。首先，由方程

$$
\frac {\mathrm{d}}{\mathrm{d} z _ {4}} \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] = X _ {4}, \quad \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \\ x _ {3} (0) \\ x _ {4} (0) \end{array} \right] = 0
$$

解出 $\phi_{z_4}^{X_4}(0)$ . 再由方程

$$
\frac {\mathrm{d}}{\mathrm{d} z _ {3}} \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] = X _ {3}, \quad \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \\ x _ {3} (0) \\ x _ {4} (0) \end{array} \right] = \phi_ {z _ {4}} ^ {X _ {4}} (0)
$$

解出 $\phi_{z_3}^{X_3}\phi_{z_4}^{X_4}(0)$ . 继续这个逐次积分过程，最后可得

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] = F (z) = \left[ \begin{array}{c} \mathrm{e} ^ {z _ {1} + z _ {3}} - \mathrm{e} ^ {z _ {3}} \\ z _ {2} \\ z _ {4} \\ z _ {1} + z _ {3} \end{array} \right].
$$

该映射的逆 $z = F^{-1}(x)$ 为

$$
\left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ z _ {3} \\ z _ {4} \end{array} \right] = F ^ {- 1} (z) = \left[ \begin{array}{c} x _ {4} - \ln (\mathrm{e} ^ {x _ {4}} - x _ {1}) \\ x _ {2} \\ \ln (\mathrm{e} ^ {x _ {4}} - x _ {1}) \\ x _ {3} \end{array} \right].
$$

由此得到
