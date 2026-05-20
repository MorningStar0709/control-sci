我们对这个弹簧系统感兴趣是因为如果没有与 $\varepsilon$ 相关的尺度，它就不能转换为标准奇异扰动模型。当 $\varepsilon$ 趋于零时，轮胎的刚度 $k_{t} = O(1 / \varepsilon^{2})$ 趋于无穷。由于轮胎势能 $k_{t}(d_{u} - d_{r})^{2} / 2$ 保持有界，故位移 $d_{u} - d_{r}$ 一定是 $O(\varepsilon)$ ，即有尺度的位移 $(d_{u} - d_{r}) / \varepsilon$ 一定保持有限。除该尺度以外，还要将所有变量归一化为无量纲的量，距离除以 $\ell$ ，速度除以 $\ell \sqrt{k_s / m_s}$ ，力除以 $\ell k_{s}$ ，时间除以 $\sqrt{m_s / k_s}$ 。这样，为了用标准奇异扰动形式表示系统，引入慢变量和快变量

$$
x = \left[ \begin{array}{c} (d _ {s} - d _ {u}) / \ell \\ (\dot {d} _ {s} / \ell) \sqrt {m _ {s} / k _ {s}} \end{array} \right], \quad z = \left[ \begin{array}{c} (d _ {u} - d _ {r}) / (\varepsilon \ell) \\ (\dot {d} _ {u} / \ell) \sqrt {m _ {s} / k _ {s}} \end{array} \right]
$$

并取 $u = F / (k_{s} \ell)$ 作为控制输入， $w = (d_{r} / \ell) \sqrt{m_{s} / k_{s}}$ 作为扰动输入， $t_{r} = t \sqrt{k_{s} / m_{s}}$ 为无量纲的时间，所得奇异受扰动模型为

$$
\begin{array}{l} \frac {d x _ {1}}{d t _ {r}} = x _ {2} - z _ {2} \\ \frac {d x _ {2}}{d t _ {r}} = - x _ {1} - \beta (x _ {2} - z _ {2}) + u \\ \varepsilon \frac {d z _ {1}}{d t _ {r}} = z _ {2} - w \\ \varepsilon \frac {d z _ {2}}{d t _ {r}} = \alpha x _ {1} - \alpha \beta (z _ {2} - x _ {2}) - z _ {1} - \alpha u \\ \end{array}
$$

其中 $\alpha = \sqrt{\frac{k_s m_s}{k_t m_u}},\quad \beta = \frac{b_s}{\sqrt{k_s m_s}}$

对于被动悬挂的典型汽车,参数 $\alpha,\beta$ 和 $\varepsilon$ 的取值范围分别是 [0.6,1.2], [0.5,0.8] 和 [0.08,0.135]。对于主动/半主动悬挂,阻尼常数会随强制驱动装置提供的额外阻尼而减小。令 $\varepsilon=0$ , 得降阶模型

$$
\begin{array}{l} \frac {d x _ {1}}{d t _ {r}} = x _ {2} - w \\ \frac {d x _ {2}}{d t _ {r}} = - x _ {1} - \beta (x _ {2} - w) + u \\ \end{array}
$$

这与图 11.4 所示的简化一阶自由度(one-degree-of-freedom)模型相一致。

△

![](image/1f060bf728fc3b00d4aeea388e610a24497e9e5540c8b974d602e1ef038fc894.jpg)

<details>
<summary>text_image</summary>

Quarter-Car 模型
ds
du
dr
参考点
mS
F
ks
bs
F
mu
kT
轮胎
路面
车体
简化模型
ms
ks
bs
F
mS
ks
bs
</details>

图 11.4 汽车悬挂的 Quarter-Car 模型
