$$
\left. \frac {\partial f}{\partial x} \right| _ {x = 0} = \left[ \begin{array}{c c} 1 - 3 x _ {1} ^ {2} - x _ {2} ^ {2} & 1 - 2 x _ {1} x _ {2} \\ - 2 - 2 x _ {1} x _ {2} & 1 - x _ {1} ^ {2} - 3 x _ {2} ^ {2} \end{array} \right] _ {x = 0} = \left[ \begin{array}{c c} 1 & 1 \\ - 2 & 1 \end{array} \right]
$$

的特征值为 $1 \pm j\sqrt{2}$ 。设 $M = \{V(x) \leqslant c\}$ ，其中 $V(x) = x_1^2 + x_2^2$ ，且 $c > 0$ 。很明显 $M$ 是有界闭集，且只包含一个平衡点，在平衡点处雅可比矩阵的特征值实部为正。在 $V(x) = c$ 的表面，有

$$
\begin{array}{l} \frac {\partial V}{\partial x _ {1}} f _ {1} + \frac {\partial V}{\partial x _ {2}} f _ {2} = 2 x _ {1} \left[ x _ {1} + x _ {2} - x _ {1} \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) \right] + 2 x _ {2} \left[ - 2 x _ {1} + x _ {2} - x _ {2} \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) \right] \\ = 2 \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) - 2 \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) ^ {2} - 2 x _ {1} x _ {2} \\ \leqslant 2 \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) - 2 \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) ^ {2} + \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) \\ = 3 c - 2 c ^ {2} \\ \end{array}
$$

其中用到不等式 $|2x_{1}x_{2}| \leqslant x_{1}^{2} + x_{2}^{2}$ 。选择 $c \geqslant 1.5$ 就可以保证所有轨线都包含在 $M$ 内，因此，由Poincaré-Bendixson准则可知在 $M$ 内有一个周期轨道。

例2.9 1.2.4节的负阻振荡器根据二阶微分方程

$$\ddot {v} + \varepsilon h ^ {\prime} (v) \dot {v} + v = 0$$

建立模型,其中 $\varepsilon$ 是正常数,h 满足条件

$$h (0) = 0, \quad h ^ {\prime} (0) < 0, \quad \lim _ {v \rightarrow \infty} h (v) = \infty , \quad \lim _ {v \rightarrow - \infty} h (v) = - \infty$$

为简化分析,对上述条件加以限制

$$h (v) = - h (- v), \quad h (v) < 0 \text {当} 0 < v < a, \quad h (v) > 0 \text {当} v > a$$

图 1.6(b) 的典型函数以及范德波尔振荡器的函数 $h(v) = -v + (1/3)v^{3}$ 满足这些条件。

选择状态变量 $x_{1} = v, \quad x_{2} = \dot{v} + \varepsilon h(v)$

可得状态模型 $\begin{array}{rcl}\dot{x}_1 & = & x_2 - \varepsilon h(x_1)\\ \dot{x}_2 & = & -x_1 \end{array}$ (2.8)

该模型在原点有唯一的平衡点。我们从证明每个以顺时针方向围绕平衡点旋转的非平衡解开始分析,最后把状态平面分成四个区域,这四个区域由两条曲线

$$x _ {2} - \varepsilon h (x _ {1}) = 0, \quad x _ {1} = 0$$

交叉确定,如图2.23所示。该图也显示出式(2.8)的向量场 $f(x)$ 在四个区域以及各区域交界处的方向。不难看出,从 $x_{2}$ 轴上半部分的点 $A=(0,p)$ 开始的解描述了图2.24所示的圆弧轨道的一般特性,圆弧与 $x_{2}$ 轴下半部分在E点相交,交点与起始点A有关。用 $(0,-\alpha(p))$ 表示E,我们将证明,如果p选得足够大,那么 $\alpha(p)<p$ 。考虑函数

$$V (x) = \frac {1}{2} (x _ {1} ^ {2} + x _ {2} ^ {2})$$

为证明 $\alpha(p)<p$ ，只要证明 $V(E)-V(A)<0$ 即可，因为

$$V (E) - V (A) = \frac {1}{2} [ \alpha^ {2} (p) - p ^ {2} ] \stackrel {\mathrm{def}} {=} \delta (p)$$

$V(x)$ 的导数为

$$\dot {V} (x) = x _ {1} \dot {x} _ {1} + x _ {2} \dot {x} _ {2} = x _ {1} x _ {2} - \varepsilon x _ {1} h (x _ {1}) - x _ {1} x _ {2} = - \varepsilon x _ {1} h (x _ {1})$$
