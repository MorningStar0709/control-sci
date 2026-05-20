$$\boldsymbol {u} ^ {*} (t) = \frac {3 \langle \tilde {\boldsymbol {x}} , \tilde {\boldsymbol {v}} \rangle}{\left(1 - \frac {c _ {\mathrm{p}}}{c _ {\mathrm{e}}}\right) \langle \tilde {\boldsymbol {x}} , \tilde {\boldsymbol {x}} \rangle} \dot {\boldsymbol {q}} \times \tilde {\boldsymbol {x}} \tag {10-125}$$

上式是一种比例导引律, 它表示最优控制 $\boldsymbol{u}^{*}(t)=\boldsymbol{a}_{\mathrm{p}}(t)$ 其大小正比于视线角速度 $\dot{\pmb{q}}$ , 其方向与视线 $\tilde{x}$ 垂直, 且位于 $\tilde{x},\tilde{v}$ 所在平面内。这是因为由式 (10-125) 中

$$\dot {\boldsymbol {q}} \times \tilde {\boldsymbol {x}} = \frac {(\tilde {\boldsymbol {x}} \times \tilde {\boldsymbol {v}}) \times \tilde {\boldsymbol {x}}}{\langle \tilde {\boldsymbol {x}} , \tilde {\boldsymbol {x}} \rangle}$$

利用三维向量的多重积公式(10-122)，可见上式的分子是 $\tilde{\pmb{x}}$ 和 $\tilde{\pmb{v}}$ 的线性组合，即 $\dot{\pmb{q}} \times \tilde{\pmb{x}}$ 在 $\tilde{\pmb{v}}, \tilde{\pmb{x}}$ 所在的平面内。

$u^{*}(t)$ 的模可计算如下

$$\left| \boldsymbol {u} ^ {*} \right| = \frac {3 \left| \tilde {\boldsymbol {x}} \right| \left| \tilde {\boldsymbol {v}} \right| \cos \delta}{\left| 1 - \frac {c _ {\mathrm{p}}}{c _ {\mathrm{e}}} \right| \left| \tilde {\boldsymbol {x}} \right| ^ {2}} | \dot {\boldsymbol {q}} | | \tilde {\boldsymbol {x}} | = \frac {3 \cos \delta}{\left| 1 - \frac {c _ {\mathrm{p}}}{c _ {\mathrm{e}}} \right|} | \tilde {\boldsymbol {v}} | | \dot {\boldsymbol {q}} | \tag {10-126}$$

式中， $\delta$ 为 $\tilde{\pmb{x}}$ 和 $\tilde{\pmb{v}}$ 间的夹角，而由式(10-124)可见， $\dot{\pmb{q}}$ 与 $\tilde{\pmb{x}}$ 间的夹角为 $90^{\circ}$ ，故 $|\dot{\pmb{q}} \times \tilde{\pmb{x}}| = |\dot{\pmb{q}}||\tilde{\pmb{x}}|\sin 90^{\circ} = |\dot{\pmb{q}}||\tilde{\pmb{x}}|$ 。

式(10-126)可写成

$$\left| \boldsymbol {u} ^ {*} \right| = K \left| \tilde {\boldsymbol {v}} \right| \left| \dot {\boldsymbol {q}} \right|$$

式中， $K$ 为比例导航的有效导航常数

$$K = \frac {3 \cos \delta}{\left| 1 - \frac {c _ {\mathrm{p}}}{c _ {\mathrm{e}}} \right|}$$

当 $\delta = 0^{\circ}, c_{\mathrm{e}} = \infty$ 时， $K = 3$ ，这是经典的比例导航常数。由(10-111)可见 $c_{\mathrm{e}} = \infty$ 对应 $a_{\mathrm{e}} \rightarrow 0$ ，即目标不作机动。
