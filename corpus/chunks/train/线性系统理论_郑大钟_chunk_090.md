$$
\mathcal {Z} [ G x (k) ] = G \sum_ {k = 0} ^ {\infty} x (k) z ^ {- k} = G \hat {x} (z) \tag {2.184}
\begin{array}{l} \mathcal {Z} [ x (k + 1) ] = \sum_ {k = 0} ^ {\infty} x (k + 1) z ^ {- k} = z \sum_ {k = 0} ^ {\infty} x (k + 1) z ^ {- (k + 1)} \\ = z \left[ \sum_ {k = - 1} ^ {\infty} x (k + 1) z ^ {- (k + 1)} - x (0) \right] \\ = z \left[ \sum_ {k = 0} ^ {\infty} x (k) z ^ {- k} - x (0) \right] \\ = z [ \hat {x} (z) - x (0) ] \tag {2.185} \\ \end{array}
$$

于是，对(2.182)取 $\pmb{x}$ 变换，并利用(2.183)—(2.185)，就得到

$$z \hat {x} (z) - z x _ {0} = G \hat {x} (z) + H \hat {u} (z) \tag {2.186}\hat {y} (z) = C \hat {x} (z) + D \hat {u} (z)$$

进而，由上式可导出

$$\hat {y} (z) = C (z I - G) ^ {- 1} z x _ {0} + [ C (z I - G) ^ {- 1} H + D ] \hat {u} (z) \tag {2.187}$$

现取初始状态 $x_{0} = 0$ ，则得到系统的输出-输入关系式为

$$\hat {y} (z) = [ C (z I - G) ^ {- 1} H + D ] \hat {u} (z) = G (z) \hat {u} (z) \tag {2.188}$$

其中

$$G (z) = C (z I - G) ^ {- 1} H + D \tag {2.189}$$

为线性离散定常系统（2.182）的传递函数矩阵，并按习惯称为脉冲传递函数矩阵。

$G(z)$ 为 $z$ 的有理分式矩阵，并且我们通常只讨论 $G(z)$ 为真的和严格真的情况。因为非真的 $G(z)$ 将不具有因果性，即会出现还没有加入输入作用而已产生输出响应的现象，而这是不符合一般的物理可实现性的。
