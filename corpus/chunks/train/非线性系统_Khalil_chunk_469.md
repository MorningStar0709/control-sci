14.42 考虑线性系统 $\dot{x} = Ax + Bu$ ，并假设存在一个正定对称矩阵 $P$ ，满足 $PA + A^{\mathrm{T}}P \leqslant 0$ ，并使矩阵对 $(A, B^{\mathrm{T}}P)$ 是可观测的。设计一个全局稳定状态反馈控制律 $u = -\psi(x)$ ，使得对于所有 $x$ ，有 $\| \psi(x) \| \leqslant k, k$ 为给定的正常数。

14.43 考虑系统 $\dot{x}_{1}=x_{2},\quad\dot{x}_{2}=-x_{1}^{3}+\psi(u)$

其中 $\psi$ 是局部利普希茨函数, 满足 $\psi(0)=0$ , 且对于所有 $u\neq0$ , 有 $u\psi(u)>0$ 。设计一个全局稳定状态反馈控制器。

14.44 考虑一个相对阶为 1 的单输入-单输出系统, 具有全局定义的标准形

$$\dot {\eta} = f _ {0} (\eta , y), \quad \dot {y} = b (\eta , y) + a (\eta , y) u$$

其中 $f_{0}(0,0) = 0, a(\eta, y) \geqslant a_{0} > 0$ 。假设存在一个（已知的）径向无界的李雅普诺夫函数 $W(\eta), [\partial W / \partial \eta](0) = 0$ ，使得对于所有 $\eta \neq 0$ ，有 $[\partial W / \partial \eta] f_{0}(\eta, 0) < 0$ 。设计一个全局稳定状态反馈控制器。

14.45 对例 13.17 的系统, 设计一个基于无源的全局稳定状态反馈控制器。

14.46 对系统 $\dot{x}_{1}=-(1+x_{3})x_{1}^{3},\quad\dot{x}_{2}=x_{3},\quad\dot{x}_{3}=x_{2}^{2}-1+u$

设计一个全局稳定状态反馈控制律。

14.47 考虑一个相对阶为 1 的单输入-单输出系统,该系统在某个包含原点的定义域内可表示为标准形 $\dot{\eta}=f_{0}(\eta,y),\quad\dot{y}=b(\eta,y)+a(\eta,y)u$

其中 $f_{0}, a$ 和 $b$ 充分光滑， $a(\eta, y) \geqslant a_{0} > 0, f_{0}(0, 0) = 0, b(0, 0) = 0$ 。假设 $\dot{\eta} = f_{0}(\eta, 0)$ 的原点是渐近稳定的，且存在一个李雅普诺夫函数 $V(\eta)$ ，使得对 $\mathcal{K}$ 类函数 $\alpha_{1}, \alpha_{2}, \alpha_{3}$ 和 $\gamma$ ，满足

$$\alpha_ {1} (\| \eta \|) \leqslant V (\eta) \leqslant \alpha_ {2} (\| \eta \|) \quad \text {和} \quad {\frac {\partial V}{\partial \eta}} f _ {0} (\eta , y) \leqslant - \alpha_ {3} (\| \eta \|), \quad \forall \| \eta \| \geqslant \gamma (| y |)$$

设 $\hat{a}(y)$ 和 $\hat{b}(y)$ 分别是 $a(\eta,y)$ 和 $b(\eta,y)$ 的光滑标称模型，在所讨论的定义域上，满足 $\hat{a}(y) \geqslant \hat{a}_{0} > 0$ 和

$$\left| \frac {b (\eta , y)}{a (\eta , y)} - \frac {\hat {b} (y)}{\hat {a} (y)} \right| \leqslant \varrho (y) \tag {14.116}$$

$\varrho(y)$ 已知,可选择 $\hat{a}=1,\hat{b}=0$ 。

(a) 证明一个连续稳定滑模控制器可取为

$$u = - \frac {\hat {b} (y)}{\hat {a} (y)} - \beta (y) \mathrm{sat} \left(\frac {y}{\varepsilon}\right)$$

其中对于正常数 $\varepsilon$ 和 $\beta_0$ ，有 $\beta(y) \geqslant \varrho(y) + \beta_0$ ，特别证明对于某个 $\mathcal{K}$ 类函数 $\alpha$ ，存在正不变紧集 $\Omega$ 和 $\Omega_{\varepsilon} = \{V(\eta) \leqslant \alpha(\varepsilon), |y| \leqslant \varepsilon\} \subset \Omega$ ，使得始于 $\Omega$ 内的每条轨线都在有限时间内进入到 $\Omega_{\varepsilon}$ 。

(b) 证明如果 $\dot{\eta} = f_0(\eta, 0)$ 的原点是指数稳定的, 那么对于足够小的 $\varepsilon$ , 闭环系统的原点也是指数稳定的, 且 $\Omega$ 是其吸引区的子集。

(c) 证明在任何 $\varrho$ 为常数的紧集上,式(14.116)都成立。

(d) 在什么条件下,该控制器可达到半全局稳定?
