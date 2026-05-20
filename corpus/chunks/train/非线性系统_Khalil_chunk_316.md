$$
\begin{array}{l} \eta \| w (t, x, \eta) \| \leqslant k \eta t ^ {(1 - r)} e ^ {- \eta t} + k \eta^ {2} \int_ {0} ^ {t} e ^ {- \eta (t - \tau)} (t - \tau) ^ {(1 - r)} d \tau \\ \leqslant k \eta \left(\frac {1 - r}{\eta}\right) ^ {1 - r} e ^ {- (1 - r)} + k \eta^ {2} \int_ {0} ^ {\infty} e ^ {- \eta s} s ^ {(1 - r)} d s \\ \leqslant k \eta \left(\frac {1 - r}{\eta}\right) ^ {1 - r} e ^ {- (1 - r)} + k \eta^ {2} \frac {\Gamma (2 - r)}{\eta^ {(2 - r)}} \leqslant k k _ {1} \eta^ {r} \\ \end{array}
$$

其中， $\Gamma(\cdot)$ 表示标准 $\Gamma$ 函数。定义 $\alpha(\eta) = k_1 \eta^r$ ，有 $\eta \parallel w(t, x, \eta) \parallel \leqslant k \alpha(\eta)$ 。一般来说，可以证明（见习题10.19）存在一个 $\kappa$ 类函数 $\alpha$ ，使得

$$\eta \| w (t, x, \eta) \| \leqslant k \alpha (\eta), \forall (t, x) \in [ 0, \infty) \times D _ {0} \tag {10.44}$$

为不失一般性,可选择 $\alpha(\eta)$ , 使 $\alpha(\eta) \geqslant c\eta, \eta \in [0,1]$ , 其中 c 是正常数。偏导数 $[\partial w/\partial t]$ 和 $[\partial w/\partial x]$ 为

$$
\begin{array}{l} \frac {\partial w}{\partial t} = h (t, x) - \eta w (t, x, \eta) \\ \frac {\partial w}{\partial x} = \int_ {0} ^ {t} \frac {\partial h}{\partial x} (\tau , x) \exp [ - \eta (t - \tau) ] d \tau \\ \end{array}
$$

由于 $[\partial h / \partial x]$ 具有与 $h$ 相同的特性，其中的 $h$ 用于推出式(10.44)，显然可以重复上述推导，以证明

$$\eta \left\| \frac {\partial w}{\partial x} \right\| \leqslant k \alpha (\eta), \forall (t, x) \in [ 0, \infty) \times D _ {0} \tag {10.45}$$

在式(10.44)和式(10.45)中用同一个K类函数并不失一般性,因为估算仅对于非独立项 $\eta$ 的正系数不同,所以可采用两个常数中较大的一个定义 $\alpha$ 。

刚定义过的函数 $w(t,x,\eta)$ 具有10.4节给出的函数 $u(t,x)$ 的所有重要性质，唯一不同的是把函数 $w$ 用参数 $\eta$ 表示，使 $w$ 和 $[\partial w / \partial x]$ 的边界具有 $k\alpha (\eta) / \eta$ 的形式，其中 $\alpha$ 为K类函数，但 $u$ 不必用参数表示。事实上， $u(t,x)$ 只不过是函数 $w(t,x,\eta)$ 在 $\eta = 0$ 时的结果。毫无疑问，因为在周期函数情况下，收敛函数 $\sigma (t) = 1 / (t + 1)$ ，因此 $\alpha (\eta) / \eta = 1$ 。

从这一点往后的分析与10.4节的分析非常相似。定义变量代换

$$x = y + \varepsilon w (t, y, \varepsilon) \tag {10.46}$$

$\varepsilon w(t,y,\varepsilon)$ 一项具有 $O(\alpha (\varepsilon))$ 的数量级。因此，对于充分小的 $\varepsilon$ ，由于矩阵 $[I + \varepsilon \partial w / \partial y]$ 是非奇异的，故式(10.46)的变量代换是有严格定义的。具体地讲，有

$$\left[ I + \varepsilon \frac {\partial w}{\partial y} \right] ^ {- 1} = I + O (\alpha (\varepsilon))$$

和 10.4 节一样, 可证明 y 的状态方程为

$$\dot {y} = \varepsilon f _ {\mathrm{av}} (y) + \varepsilon \alpha (\varepsilon) q (t, y, \varepsilon) \tag {10.47}$$
