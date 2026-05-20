由于滑模控制器含有不连续的符号函数 $\operatorname{sgn}(s_i)$ ，因此在理论与实践中出现了一些问题。在理论上，如解的存在性和唯一性，以及李雅普诺夫分析的有效性等，都必须在一个框架中验证，该框架不要求状态方程的右边具有局部利普希茨性①。实践中的问题是由于切换设备的非理想性以及延迟造成的抖动，这在引例中已做了说明。为了消除抖动，我们采用符号函数的连续逼近②，这种方法也避免了与不连续控制器相关联的理论困难③。具体来说，就是用一个陡峭的饱和函数 $\operatorname{sat}(s_i / \varepsilon)$ 逼近符号函数 $\operatorname{sgn}(s_i)$ ④，即

$$v _ {i} = - \beta (x) \operatorname{sat} \left(\frac {s _ {i}}{\varepsilon}\right), \quad 1 \leqslant i \leqslant p \tag {14.13}$$

其中 $\beta(x)$ 满足式(14.12)。为了分析连续滑模控制器的性能，用李雅普诺夫函数 $V_{i}=(1/2)s_{i}^{2}$ 检验到达阶段的特性。 $V_{i}$ 的导数满足不等式

$$\dot {V} _ {i} \leqslant g _ {i} (x) \left[ - \beta (x) s _ {i} \mathrm{sat} \left(\frac {s _ {i}}{\varepsilon}\right) + \varrho (x) | s _ {i} | + \kappa_ {0} \beta (x) | s _ {i} | \right]$$

在区域 $|s_{i}|\geqslant\varepsilon$ 内,有

$$\dot {V} _ {i} \leqslant g _ {i} (x) [ - (1 - \kappa_ {0}) \beta (x) + \varrho (x) ] | s _ {i} | \leqslant - g _ {0} \beta_ {0} (1 - \kappa_ {0}) | s _ {i} |$$

这表明只要 $|s_{i}(0)|>\varepsilon,|s_{i}(t)|$ 就会减小，直到在有限时间内到达集合 $\{|s_{i}|\leqslant\varepsilon\}$ ，并保持在该集合内。集合 $\{|s_{i}|\leqslant\varepsilon,1\leqslant i\leqslant p\}$ 称为边界层，为研究 $\eta$ 的特性以及设计滑动流形 $\xi=\phi(\eta)$ ，假设存在一个（连续可微的）李雅普诺夫函数 $V(\eta)$ ，对于所有 $(\eta,\xi)\in T(D)$ ，满足不等式

$$\alpha_ {1} (\| \eta \|) \leqslant V (\eta) \leqslant \alpha_ {2} (\| \eta \|) \tag {14.14}\frac {\partial V}{\partial \eta} f _ {a} (\eta , \phi (\eta) + s) \leqslant - \alpha_ {3} (\| \eta \|), \quad \forall \| \eta \| \geqslant \gamma (\| s \|) \tag {14.15}$$

其中 $\alpha_{1},\alpha_{2},\alpha_{3}$ 和 $\gamma$ 是 K 类函数 $^{⑤}$ ，注意到对于某个正常数 $k_{1}^{⑥}$ ，有

$$\left| s _ {i} \right| \leqslant c, \quad 1 \leqslant i \leqslant p \Rightarrow \| s \| \leqslant k _ {1} c \Rightarrow \dot {V} \leqslant - \alpha_ {3} (\| \eta \|), \quad \| \eta \| \geqslant \gamma (k _ {1} c)$$

定义K类函数 $\alpha$ 为

$$\alpha (r) = \alpha_ {2} (\gamma (k _ {1} r))$$

则

$$
\begin{array}{l} V (\eta) \geqslant \alpha (c) \Rightarrow V (\eta) \geqslant \alpha_ {2} (\gamma (k _ {1} c)) \Rightarrow \alpha_ {2} (\| \eta \|) \geqslant \alpha_ {2} (\gamma (k _ {1} c)) \\ \Rightarrow \| \eta \| \geqslant \gamma (k _ {1} c) \Rightarrow \dot {V} \leqslant - \alpha_ {3} (\| \eta \|) \leqslant - \alpha_ {3} (\gamma (k _ {1} c)) \\ \end{array}
$$

由于 $\dot{V}$ 在边界 $V(\eta) = c_0$ 处为负，所以上式表明当 $c_{0} \geqslant \alpha(c)$ 时， $\{V(\eta) \leqslant c_{0}\}$ 是正不变集（见图14.12），故
