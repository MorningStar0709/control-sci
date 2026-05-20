$$U _ {\varepsilon} = \{x \in R ^ {n} \mid \operatorname{dist} (x, M) < \varepsilon \}$$

其中 $\mathrm{dist}(x,M)$ 表示 x 到 M 内一点的最小距离, 即

$$\operatorname{dist} (x, M) = \inf _ {y \in M} \| x - y \|$$

定义8.1 方程(8.16)的闭不变集 $M$

\- 如果对于每个 $\varepsilon > 0$ ，存在 $\delta > 0$ ，满足

$$x (0) \in U _ {\delta} \Rightarrow x (t) \in U _ {\varepsilon}, \forall t \geqslant 0$$

则 M 是稳定的。

\- 如果 $M$ 是稳定的, 且可以选择 $\delta$ , 使得

$$x (0) \in U _ {\delta} \Rightarrow \lim _ {t \rightarrow \infty} \operatorname{dist} (x (t), M) = 0$$

则 M 是渐近稳定的。

当 $M$ 是一个平衡点时, 该定义即简化为定义4.1。第4章关于平衡点的李雅普诺夫稳定性理论可以扩展到不变集①。例如, 重复定理4.1的证明就不难看出, 如果存在一个函数 $V(x)$ , 在 $M$ 上为0, 而在 $M$ 的某个邻域 $D$ 内为正, 不包含 $M$ 本身, 而且如果在 $D$ 内导数 $\dot{V}(x) = [\partial V / \partial x]$ $f(x) \leqslant 0$ , 则 $M$ 是稳定的。如果 $\dot{V}(x)$ 在 $D$ 内为负, 不包含 $M$ 本身, 则 $M$ 是渐近稳定的。

不变集的稳定性和渐近稳定性对不变集本身是重要的概念,这里我们将应用这一概念把不变集 M 是闭轨道的特例与周期解联系在一起进行研究。设 $u(t)$ 是自治系统(8.16)的非平凡周期解,周期为 T 并设 $\gamma$ 是闭轨道,定义为

$$\gamma = \{x \in R ^ {n} \mid x = u (t), 0 \leqslant t \leqslant T \}$$

周期轨道 $\gamma$ 是 $u(t)$ 在状态空间的象, 它是稳定性由定义 8.1 描述的不变集。通常, 特别是对于二阶系统而言, 把渐近稳定的周期轨道称为稳定的极限环。

例8.14 谐振器

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - x _ {1}$$

有一个周期轨道的连续统,即一组以原点为圆心的同心圆,其中任意一个周期轨道 $\gamma_{c}$ 都是稳定的。例如,考虑由

$$\gamma_ {c} = \{x \in R ^ {2} \mid r = c > 0 \}, \text {其中} r = \sqrt {x _ {1} ^ {2} + x _ {2} ^ {2}}$$

定义的周期轨道 $\gamma_{c}$ ，其 $U_{\varepsilon}$ 邻域定义为环形区域

$$U _ {\varepsilon} = \{x \in R ^ {2} \mid c - \varepsilon < r < c + \varepsilon \}$$

该环形区域本身就是一个不变集。因此，给定 $\varepsilon > 0$ ，可取 $\delta = \varepsilon$ ，并看出在 $t = 0$ 时始于 $U_{\delta}$ 邻域内的任何解在所有 $t \geqslant 0$ 时都保持在 $U_{\varepsilon}$ 邻域内。所以周期轨道 $\gamma_{c}$ 是稳定的。但是它不是渐近稳定的，因为当 $t$ 趋于无穷时，始于 $\gamma_{c}$ 的一个 $U_{\delta}$ 邻域内的解不会趋于 $\gamma_{c}$ ，无论 $\delta$ 取多么小。周期轨道 $\{r = c\}$ 的稳定性还可由李雅普诺夫函数

$$V (x) = (r ^ {2} - c ^ {2}) ^ {2} = (x _ {1} ^ {2} + x _ {2} ^ {2} - c ^ {2}) ^ {2}$$

证明,该函数沿系统轨线的导数为

$$\dot {V} (x) = 4 (r ^ {2} - c ^ {2}) r \dot {r} = 0$$

例 8.15 考虑例 8.13 所示的系统, 它有一个孤立周期轨道

$$\gamma = \{x \in R ^ {2} \mid r = 1 \}, \quad \text {其中} r = \sqrt {x _ {1} ^ {2} + x _ {2} ^ {2}}$$

对于 $x \notin \gamma$ ，有

$$\operatorname{dist} (x, \gamma) = \inf _ {y \in \gamma} \| x - y \| _ {2} = \inf _ {y \in \gamma} \sqrt {(x _ {1} - y _ {1}) ^ {2} + (x _ {2} - y _ {2}) ^ {2}} = | r - 1 |$$

回顾 $r(t) = \left[1 - \frac{1 - r_0^2}{\sqrt{1 + 4t(1 - r_0^2)^2}}\right]^{1 / 2}$

容易看出满足稳定性的 $\varepsilon -\delta$ 要求，且

$$\mathrm{dist} (x (t), \gamma) \to 0, \text {当} t \to \infty$$

因此周期轨道是渐近稳定的。应用李雅普诺夫函数

$$V (x) = (r ^ {2} - 1) ^ {2} = (x _ {1} ^ {2} + x _ {2} ^ {2} - 1) ^ {2}$$

沿系统轨线的导数为

$$\dot {V} (x) = 4 (r ^ {2} - 1) r \dot {r} = - 4 (r ^ {2} - 1) ^ {4} < 0, \quad \text {当} r \neq 1$$

也可得到相同的结论。

△

定义了周期轨道的稳定性性质后,我们就可以定义周期解的稳定性性质了。

定义8.2 系统(8.16)的一个非平凡周期解为 $u(t)$ ，

\- 如果由 $u(t)$ 产生的闭轨道 $\gamma$ 是稳定的, 则 $u(t)$ 是轨道稳定的。

\- 如果由 $u(t)$ 产生的闭轨道 $\gamma$ 是渐近稳定的, 则 $u(t)$ 是渐近轨道稳定的。

注意到,当谈及周期解或者相应的周期轨道时,所用名词是不同的。在例8.15中,我们说单位圆是一个渐近稳定的周期轨道,但我们说周期解 $(\cos t,\sin t)$ 是轨道渐近稳定的。
