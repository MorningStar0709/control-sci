对于给定的 $x_0 \in \mathbb{R}^N$ . 记 $h(x) = x - x_0$ . 假定 $\Gamma_0$ 和 $\Gamma_1$ 满足

$$\sup _ {\Gamma_ {0}} \langle h, \nu \rangle \leqslant 0. \quad \inf _ {\Gamma_ {1}} \langle h, \nu \rangle \geqslant C _ {1} > 0. \tag {10.5.7}$$

我们的目的是证明上述波动反馈系统是指数稳定的.

首先我们把上述系统 (10.5.3)\~(10.5.6) 化成抽象空间中的方程。取状态空间为 Hilbert 空间 $\mathcal{H} = H_{\Gamma_0}^1 (\Omega)\times L^2 (\Omega),H_{\Gamma_0}^1 (\Omega)$ 的定义见5.4节。 $\mathcal{H}$ 中内积为

$$(Y _ {1}, Y _ {2}) _ {\mathcal {H}} = \int_ {\Omega} (\langle \nabla f _ {1}, \nabla f _ {2} \rangle + g _ {1} g _ {2}) \mathrm{d} x,$$

其中 $Y_{k} = [f_{k},g_{k}]^{\mathrm{T}}\in \mathcal{H},k = 1,2.$ 在 $\mathcal{H}$ 中定义线性算子 $\mathcal{A}$

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , \Delta \varphi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}),\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \mid \varphi \in H ^ {2} (\Omega) \cap H _ {\Gamma_ {0}} ^ {1} (\Omega), \psi \in H _ {\Gamma_ {0}} ^ {1} (\Omega), \partial_ {\nu} \varphi | _ {\Gamma_ {1}} = - \ell \psi | _ {\Gamma_ {1}} \right\},$$

于是系统 (10.5.3)\~(10.5.6) 可以写成 $\mathcal{H}$ 中线性发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t), \tag {10.5.8}$$

其中 $Y(t) = [y(\cdot, t), \dot{y}(\cdot, t)]^{\mathrm{T}}$ . 可以证明 $\mathcal{A}$ 生成 $\mathcal{H}$ 中 $C_0$ 压缩半群，从而相应的系统是适定的。特别当初值 $Y(0) \in \mathcal{D}(\mathcal{A})$ 时存在强解。

系统 (10.5.8) 的能量是

$$E (t) = \frac {1}{2} \int_ {\Omega} (| \dot {y} | ^ {2} + | \nabla y | ^ {2}) \mathrm{d} x.$$

对于 $Y(0) = [y_0, y_1]^{\mathrm{T}} \in \mathcal{D}(\mathcal{A})$ ，设 $Y(t) = [y(\cdot, t), \dot{y}(\cdot, t)]^{\mathrm{T}}$ 是系统 (10.5.8) 的强解，则通过计算，我们有

$$\dot {E} (t) = - \int_ {\Gamma_ {1}} \ell \dot {y} ^ {2} \mathrm{d} \sigma .$$

现在我们取能量摄动泛函为

$$E _ {\mu} (t) = (1 - \mu) t E (t) + G (t),$$

其中 $0 < \mu < 1$ ，而

$$G (t) = \int_ {\Omega} \dot {y} \langle h, \nabla y \rangle \mathrm{d} x + \frac {N - 1}{2} \int_ {\Omega} y \dot {y} \mathrm{d} x.$$

于是

$$\dot {E} _ {\mu} (t) = (1 - \mu) E (t) - (1 - \mu) t \int_ {\Gamma_ {1}} \ell \dot {y} ^ {2} \mathrm{d} \sigma + \dot {G} (t). \tag {10.5.9}$$

利用 Green 公式，我们有
