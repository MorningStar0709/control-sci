$$\dot {x} _ {1} = (a + x _ {2}) x _ {1} + 2 z, \quad \dot {x} _ {2} = b x _ {1} ^ {2}, \quad \varepsilon \dot {z} = - x _ {1} x _ {2} - z$$

其中 $a > 0, b > 0$ ，有一个平衡集 $\{x_1 = 0, z = 0\}$ 。对于较小的 $\varepsilon$ ，用 LaSalle 不变原理研究解的渐近特性。

提示:例4.10已经研究了降阶模型的渐近特性。运用复合李雅普诺夫函数并继续11.5节的讨论。但要注意定理11.3不适用于现在的问题。

11.28 证明系统

$$\dot {x} _ {1} = x _ {2} + e ^ {- t} z, \quad \dot {x} _ {2} = - x _ {2} + z, \quad \varepsilon \dot {z} = - (x _ {1} + z) - (x _ {1} + z) ^ {3}$$

的原点对于足够小的 $\varepsilon$ 是全局指数稳定的。

11.29 考虑奇异扰动系统

$$\dot {x} = - x + \arctan z, \quad \varepsilon \dot {z} = - x - z + u$$

(a) 求一个 $\varepsilon^{*}$ ，使得 $\forall \varepsilon < \varepsilon^{*}$ ，无激励系统的原点是全局渐近稳定的。

(b) 对于每个 $\varepsilon < \varepsilon^{*}$ ，证明系统是输入-状态稳定的。

11.30 考虑如图 7.1 所示的反馈连接, 其线性部件是一个奇异扰动系统, 表示为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} - 2 x _ {2} + z \\ \varepsilon \dot {z} = - z + u \\ y = 2 x _ {1} + x _ {2} \\ \end{array}
$$

且 $\psi$ 是光滑、无记忆、时不变非线性的，属于扇形区域 $[0,k]$ ，k>0。

(a) 把该闭环系统表示成奇异扰动系统, 并求其降阶模型和边界层模型。

(b) 证明对于每个 k > 0, 存在 $\varepsilon^{*} > 0$ , 使得对于所有 $0 < \varepsilon < \varepsilon^{*}$ , 系统是绝对稳定的。
