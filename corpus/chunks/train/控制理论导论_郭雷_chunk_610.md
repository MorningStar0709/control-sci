同样的讨论可知 $c_{1}^{k_{s}-2}=\cdots=c_{m_{s}}^{k_{s}-2}=0$ 。继续这个过程可以证明所有的 $c_{j}^{i}=0$ ，即 $dL_{f}^{i}z_{j}$ 线性无关， $i=1,\cdots,k_{s}-1,j=1,\cdots,m_{s}$ 。

事实上，以上讨论也说明了

$$L _ {f} ^ {i} z _ {j} \in \Delta_ {k _ {s} - 1 - i} ^ {\perp}, \quad j = 1, \dots , m _ {s}. \tag {8.3.19}$$

其次，可以找到 $m_{s-1}-m_{s}$ 个函数 $z_{m_{s}+1},\cdots,z_{m_{s-1}}$ ，使得

$$\mathrm{d} z _ {1}, \dots , \mathrm{d} L _ {f} ^ {d _ {s}} z _ {1}, \dots , \mathrm{d} z _ {m _ {s}}, \dots , \mathrm{d} L _ {f} ^ {d _ {s}} z _ {m _ {s}}, \mathrm{d} z _ {m _ {s} + 1}, \dots , \mathrm{d} z _ {m _ {s - 1}}$$

线性无关，且它们形成余分布

$$\Omega_ {1} ^ {2} = \left(\Delta_ {d _ {s - 1} - 1} ^ {s - 1}\right) ^ {\perp}$$

的基底．继续这个过程，最后我们可找到 m 个函数 $z_{1}, \cdots, z_{m}$ 使得下面的 n 个 1-形式 $\omega_{j}^{i} = dL_{f}^{i}z_{j}$ 线性无关：

$$
\left[ \begin{array}{c c c c c c c c c} \omega_ {1} ^ {0} & \dots & \omega_ {1} ^ {d _ {s}} & \omega_ {1} ^ {d _ {s} + 1} & \dots & \omega_ {1} ^ {d _ {s} + d _ {s - 1}} & \dots & \omega_ {1} ^ {d _ {s} + \dots + d _ {2} + 1} & \dots & \omega_ {1} ^ {d _ {s} + \dots + d _ {1}} \\ \vdots & & & \vdots & & & & \vdots & & \\ \omega_ {m _ {s}} ^ {0} & \dots & \omega_ {m _ {s}} ^ {d _ {s}} & \omega_ {m _ {s}} ^ {d _ {s} + 1} & \dots & \omega_ {m _ {s}} ^ {d _ {s} + d _ {s - 1}} & \dots & \omega_ {m _ {s}} ^ {d _ {s} + \dots + d _ {2} + 1} & \dots & \omega_ {m _ {s}} ^ {d _ {s} + \dots + d _ {1}} \\ & & & \vdots & & & & \vdots & & \\ & & & \omega_ {m _ {s - 1}} ^ {0} & \dots & \omega_ {m _ {s - 1}} ^ {d _ {s - 1}} & & \omega_ {m _ {s - 1}} ^ {d _ {s - 1} + \dots + d _ {2} + 1} & \dots & \omega_ {m _ {s - 1}} ^ {d _ {s - 1} + \dots + d _ {1}} \\ & & & & & & \vdots & & \\ & & & & & & \omega_ {m _ {1}} ^ {0} & \dots & \omega_ {m _ {1}} ^ {d _ {1}} \end{array} \right], (8. 3. 2 0)
$$

而且式 (8.3.20) 的前 $t$ 列余向量场张成余分布 $\Omega_t, t = 1, \dots, k_m$ .

令 $r_{1}=d_{1}+\cdots+d_{s}, r_{2}=d_{1}+\cdots+d_{s-1}, \cdots, r_{s}=d_{1}$ ，我们可得到 n 个线性无关函数，将其分组成

$$
\begin{array}{l} z _ {1} ^ {1} = \left[ \begin{array}{c} z _ {1} \\ \vdots \\ z _ {m _ {s}} \end{array} \right], \quad z _ {2} ^ {1} = L _ {f} z _ {1} ^ {1}, \dots , z _ {r _ {1}} ^ {1} = L _ {f} ^ {r _ {1} - 1} z _ {1} ^ {1}, \\ \begin{array}{c} z _ {1} ^ {2} = \left[ \begin{array}{c} z _ {m _ {s} + 1} \\ \vdots \\ z _ {m _ {s - 1}} \end{array} \right], \qquad z _ {2} ^ {2} = L _ {f} z _ {1} ^ {2}, \dots , z _ {r _ {2}} ^ {2} = L _ {f} ^ {r _ {2} - 1} z _ {1} ^ {2}, \\ \vdots \end{array} \\ z _ {1} ^ {s} = \left[ \begin{array}{c} z _ {m _ {2} + 1} \\ \vdots \\ z _ {m _ {1}} \end{array} \right], \quad z _ {2} ^ {s} = L _ {f} z _ {1} ^ {s}, \dots , z _ {r _ {s}} ^ {s} = L _ {f} ^ {r _ {s} - 1} z _ {1} ^ {s}. \\ \end{array}
$$

利用这组函数作为局部坐标，可得到
