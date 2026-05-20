其中 $k_{1}$ 到 $k_{4}$ 是正常数。证明当以指数稳定性代替渐近稳定性时，定理 11.3 的结论成立。

11.25 （见文献[191]）考虑奇异扰动系统

$$\dot {x} = f (x, y)\varepsilon \dot {y} = A y + \varepsilon g _ {1} (x, y)$$

其中，A 是赫尔维茨矩阵，f 和 $g_{1}$ 是足够光滑的函数，在原点为零。假设在所讨论的定义域内存在一个李雅普诺夫函数 $V(x)$ ，使得 $[\partial V/\partial x]f(x,0)\leqslant-\alpha_{1}\phi(x)$ ，其中 $\alpha_{1}>0$ ，且 $\phi(x)$ 是正定的。设 P 是李雅普诺夫方程 $PA+A^{T}P=-I$ 的解，并取 $W(y)=y^{T}Py$ 。

(a) 假设 $f$ 和 $g_{1}$ 在所讨论的定义域内满足不等式

$$\| g _ {1} (x, 0) \| _ {2} \leqslant k _ {1} \phi^ {1 / 2} (x), \quad k _ {1} \geqslant 0\frac {\partial V}{\partial x} [ f (x, y) - f (x, 0) ] \leqslant k _ {2} \phi^ {1 / 2} (x) \| y \| _ {2}, \quad k _ {2} \geqslant 0$$

用备选李雅普诺夫函数 $\nu(x,y)=(1-d)V(x)+dW(y)$ ，0<d<1 和分析定理 11.3 的方法，证明对于足够小的 $\varepsilon$ ，原点是渐近稳定的。

(b) 作为定理 11.3 的另一种形式, 假设 f 和 $g_{1}$ 在所讨论的定义域内满足不等式

$$\| g _ {1} (x, 0) \| _ {2} \leqslant k _ {3} \phi^ {a} (x), \quad k _ {3} \geqslant 0, \quad 0 < a \leqslant \frac {1}{2}\frac {\partial V}{\partial x} [ f (x, y) - f (x, 0) ] \leqslant k _ {4} \phi^ {b} (x) \| y \| _ {2} ^ {c}, \quad k _ {4} \geqslant 0, \quad 0 < b < 1, \quad c = \frac {1 - b}{a}$$

用备选李雅普诺夫函数 $\nu(x,y)=V(x)+(y^{\mathrm{T}}Py)^{\gamma}$ ，其中 $\gamma=1/2a$ ，证明对于足够小的 $\varepsilon$ ，原点是渐近稳定的。

提示:应用 Young 不等式

$$u w \leqslant \frac {1}{\mu} u ^ {p} + \mu^ {\frac {1}{p - 1}} w ^ {\frac {p}{p - 1}}, \forall u \geqslant 0, w \geqslant 0, \mu > 0, p > 1$$

证明 $\dot{\nu} \leqslant -c_{1}\phi - c_{2}\| y\|_{2}^{2\gamma}$ , 再证明对于充分小的 $\varepsilon$ , 系数 $c_{1}$ 和 $c_{2}$ 是正数。(c) 给出一个例子, 满足 (b) 的互联条件, 但不满足 (a) 的条件。

11.26 （见文献[99]）考虑多参数奇异扰动系统

$$
\begin{array}{l} \dot {x} = f (x, z _ {1}, \dots , z _ {m}) \\ \varepsilon_ {i} \dot {z} _ {i} = \eta_ {i} (x) + \sum_ {j = 1} ^ {m} a _ {i j} z _ {j}, \quad i = 1, \dots , m \\ \end{array}
$$

其中， $x$ 是 $n$ 维向量， $z_{i}$ 是标量变量， $\varepsilon_{i}$ 是小的正参数。设 $\varepsilon = \max_i\varepsilon_i$ ，则方程可重写为

$$\dot {x} = f (x, z)\varepsilon D \dot {z} = \eta (x) + A z$$

其中 z 和 $\eta$ 是 m 维向量，其元素分别是 $z_{i}$ 和 $\eta_{i}$ 。A 是 $m \times m$ 矩阵，其元素为 $a_{ij}$ ，D 是 $m \times m$ 对角矩阵，其第 i 个对角元素是 $\varepsilon_{i}/\varepsilon$ 。D 的对角元素是正数，且以 1 为界。假设降阶系统 $\dot{x} = f(x, -A^{-1}\eta(x))$ 的原点是渐近稳定的，且存在一个李雅普诺夫函数 $V(x)$ 满足定理 11.3 的条件。进一步假设存在元素为正的对角矩阵 P，使得

$$P A + A ^ {\mathrm{T}} P = - Q, \quad Q > 0$$

利用 $\nu (x,z) = (1 - d)V(x) + d(z + A^{-1}\eta (x))^{\mathrm{T}}PD(z + A^{-1}\eta (x)),0 <   d <   1$

作为备选李雅普诺夫函数,分析原点的稳定性。对于多参数系统,叙述并证明与定理11.3相似的定理。所给出的结论应该允许参数 $\varepsilon_{i}$ 是任意的,仅要求 $\varepsilon_{i}$ 足够小。

11.27 (见文献[105])奇异扰动系
