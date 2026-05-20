$$
\begin{array}{l} \dot {G} (t) = \int_ {\Gamma} \left(\langle h, \nabla y \rangle + \frac {N - 1}{2} y\right) \frac {\partial y}{\partial \nu} d \sigma - \int_ {\Omega} \langle \nabla y, \nabla \langle h, \nabla y \rangle \rangle d x \\ + \frac {1}{2} \int_ {\Omega} \langle h, \nabla \dot {y} ^ {2} \rangle \mathrm{d} x + \frac {N - 1}{2} \int_ {\Omega} (\dot {y} ^ {2} - | \nabla y | ^ {2}) \mathrm{d} x \\ = \int_ {\Gamma} \left(\langle h, \nabla y \rangle + \frac {N - 1}{2} y\right) \frac {\partial y}{\partial \nu} d \sigma + \frac {1}{2} \int_ {\Omega} \left\langle h, \nabla \left(\dot {y} ^ {2} - | \nabla y | ^ {2}\right) \right\rangle d x \\ - \frac {1}{2} \int_ {\Omega} (\dot {y} ^ {2} + | \nabla y | ^ {2}) d x + \frac {N}{2} \int_ {\Omega} (\dot {y} ^ {2} - | \nabla y | ^ {2}) d x \\ = \int_ {\Gamma} \left(\langle h, \nabla y \rangle + \frac {N - 1}{2} y\right) \frac {\partial y}{\partial \nu} d \sigma - E (t) \\ + \frac {1}{2} \int_ {\Gamma} (\dot {y} ^ {2} - | \nabla y | ^ {2}) \langle h, \nu \rangle \mathrm{d} \sigma , \tag {10.5.10} \\ \end{array}
$$

这里我们已经利用了

$$
\begin{array}{l} \frac {1}{2} \int_ {\Omega} \langle h, \nabla (\dot {y} ^ {2} - | \nabla y | ^ {2}) \rangle \mathrm{d} x = \frac {1}{2} \int_ {\Omega} \left\langle \nabla \left(\frac {| h | ^ {2}}{2}\right), \nabla (\dot {y} ^ {2} - | \nabla y | ^ {2}) \right\rangle \mathrm{d} x \\ = \frac {1}{2} \int_ {\Gamma} \left(\dot {y} ^ {2} - | \nabla y | ^ {2}\right) \langle h, \nu \rangle \mathrm{d} \sigma - \frac {1}{2} \int_ {\Omega} \left(\dot {y} ^ {2} - | \nabla y | ^ {2}\right) \Delta \left(\frac {| h | ^ {2}}{2}\right) \mathrm{d} x \\ = \frac {1}{2} \int_ {\Gamma} (\dot {y} ^ {2} - | \nabla y | ^ {2}) \langle h, \nu \rangle \mathrm{d} \sigma - \frac {N}{2} \int_ {\Omega} (\dot {y} ^ {2} - | \nabla y | ^ {2}) \mathrm{d} x. \\ \end{array}
$$

注意到 $y|_{\Gamma_0} = 0$ ，可知 $\pmb{y}$ 在 $\Gamma_0$ 上的切向导数为0，从而在 $\Gamma_0$ 上有 $\nabla y = (\partial_\nu y)\nu$ 于是从式(10.5.10)得到

$$
\begin{array}{l} \dot {G} (t) \leqslant - \int_ {\Gamma_ {1}} \langle h, \nabla y \rangle \ell \dot {y} d \sigma - \frac {N - 1}{2} \int_ {\Gamma_ {1}} \ell y \dot {y} d \sigma - E (t) \\ + \frac {1}{2} \int_ {\Gamma_ {1}} \dot {y} ^ {2} \langle h, \nu \rangle \mathrm{d} \sigma - \frac {1}{2} \int_ {\Gamma_ {1}} | \nabla y | ^ {2} \langle h, \nu \rangle \mathrm{d} \sigma . \tag {10.5.11} \\ \end{array}
$$

利用嵌入定理，迹定理和 Poincaré 不等式，存在常数 $M_{2} > 0$ 使得
