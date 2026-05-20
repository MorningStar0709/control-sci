通过把增益 $F, G_1, G_2, L, M_1, M_2$ 和 $M_3$ 作为分配变量 $\rho$ 的函数, 即用 $\rho$ 代换 $\alpha$ , 就可由固定增益控制器 (12.33) \~ (12.35) 得到增益分配控制器。可以验证, 在该控制器下闭环系统将具有期望的平衡点, 且其线性化矩阵 $(A_s(\alpha, w), B_s(\alpha, w), C_s(\alpha, w))$ 有 $A_s = A_f = \mathcal{A}_c, C_s = C_f$ , 但一般情况下 $B_s \neq B_f$ , 这是由于分配增益对 $\rho$ 的偏微分造成的。 $\mathcal{A}_c(\alpha, w)$ 对于所有 $(\alpha, w) \in D_\rho \times D_w$ 是赫尔维茨矩阵的事实表明, 当 $\rho = \alpha$ 时, 增益分配控制器将产生一个零稳态跟踪误差的指数稳定平衡点, 但是从 $\rho_\delta$ 到 $y_\delta$ 的闭环传递函数不同于对应设计模型的传递函数。因此必须通过分析或仿真检验增益分配控制器的局部性能, 如果结果能够令人满意, 则继续进行下一步, 实现增益分配控制器。然而, 已经过证实, 这一步可以做得更好。在例 12.5 中, 通过对增益分配控制器的修正, 实现了闭环系统在固定增益控制器下的线性化模型与增益分配控制器下的模型等效。在该例子中, 直接交换了增益 $k_2$ 与积分器, 即把积分器从控制器的输入端一边移到输出端一边, 使 $k_1$ 和 $k_2$ 都是 $e$ 的倍数, 而在稳态时 $e$ 为零。以上就是我们想要对控制器 (12.33) \~ (12.35) 要做的主要工作。然而, 由于动力学方程 (12.34) 的出现, 因其具有两个驱动输入 $\sigma$ 和 $y_m$ , 所以情况较为复杂。 $\sigma$ 是积分器的输出, 它对讨论把积分器移到控制器输出端有意义, $y_m$ 不是积分器的输出, 但是如果可测出 $\dot{y}_m$ , 即 $y_m$ 的导数, 即可克服困难。这是因为控制器 (12.33) \~ (12.35) 可以表示为

$$\dot {\lambda} = \psi\dot {z} = F (\alpha) z + G (\alpha) \lambdau = L (\alpha) z + M (\alpha) \lambda + M _ {3} (\alpha) e$$

其中 $\psi = \left[ \begin{array}{c}e\\ \dot{y}_m \end{array} \right],\quad G = \left[ \begin{array}{ll}G_1 & G_2 \end{array} \right],\quad M = \left[ \begin{array}{ll}M_1 & M_2 \end{array} \right]$

从 $\psi$ 到 $u - M_{3}(\alpha)e$ 的传递函数

$$\{L (\alpha) [ s I - F (\alpha) ] ^ {- 1} G (\alpha) + M (\alpha) \} \frac {1}{s}$$

等价于 $\frac{1}{s}\{L(\alpha)[sI - F(\alpha)]^{-1}G(\alpha) + M(\alpha)\}$

因此控制器可以通过 $\dot{\varphi} = F(\alpha)\varphi +G(\alpha)\psi$

$$\dot {\eta} = L (\alpha) \varphi + M (\alpha) \psiu = \eta + M _ {3} (\alpha) e$$

实现。图 12.4 所示为固定增益控制器的原始模型和修正模型框图。把修正实现中的增益 F, G, L, M 和 $M_{3}$ 作为分配变量 $\rho$ 的函数，即可获得增益分配控制器

$$\dot {\varphi} = F (\rho) \varphi + G _ {1} (\rho) e + G _ {2} (\rho) \dot {y} _ {m} \tag {12.42}\dot {\eta} = L (\rho) \varphi + M _ {1} (\rho) e + M _ {2} (\rho) \dot {y} _ {m} \tag {12.43}u = \eta + M _ {3} (\rho) e \tag {12.44}$$

当该控制器应用于非线性系统(12.28)\~(12.30)时,可得闭环系统

$$\dot {\mathcal {X}} = g (\mathcal {X}, \rho , w) \tag {12.45}y = h (x, w) \tag {12.46}$$

其中
