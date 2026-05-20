在 $R^2$ 上连续可微, 因此在 $R^2$ 上是局部利普希茨的。但是, 它不是全局利普希茨的, 因为 $[\partial f / \partial x]$ 在 $R^2$ 上不是一致有界的。在 $R^2$ 的任何紧子集上, $f$ 是利普希茨的。假设只想计算在凸集 $W = \{x \in R^2 | |x_1| \leqslant a_1, |x_2| \leqslant a_2\}$ 上的一个利普希茨常数, 雅可比矩阵由下式给出:

$$
\left[ \frac {\partial f}{\partial x} \right] = \left[ \begin{array}{c c} - 1 + x _ {2} & x _ {1} \\ - x _ {2} & 1 - x _ {1} \end{array} \right]
$$

利用 $R^2$ 上对向量的范数 $\| \cdot \|_{\infty}$ 和矩阵的导出阵模，有

$$\left\| \frac {\partial f}{\partial x} \right\| _ {\infty} = \max \{| - 1 + x _ {2} | + | x _ {1} |, | x _ {2} | + | 1 - x _ {1} | \}$$

W 内的所有点都满足

$$\left| - 1 + x _ {2} \right| + \left| x _ {1} \right| \leqslant 1 + a _ {2} + a _ {1}, \quad \left| x _ {2} \right| + \left| 1 - x _ {1} \right| \leqslant a _ {2} + 1 + a _ {1}$$

因此 $\left\| \frac{\partial f}{\partial x} \right\|_{\infty} \leqslant 1 + a_1 + a_2$

利普希茨常数可取为 $L = 1 + a_{1} + a_{2}$

△

例3.2 函数 $f(x) = \left[ \begin{array}{c}x_{2}\\ -\mathrm{sat}(x_{1} + x_{2}) \end{array} \right]$

在 $R^2$ 上不是连续可微的，通过检验 $f(x) - f(y)$ 来检验函数的利普希茨性。利用 $R^2$ 上对向量的 $\| \cdot \|_2$ 和饱和函数 $\operatorname{sat}(\cdot)$ 满足

$$\left| \operatorname{sat} (\eta) - \operatorname{sat} (\xi) \right| \leqslant | \eta - \xi |$$

可得 $\| f(x) - f(y)\| _2^2\leqslant (x_2 - y_2)^2 +(x_1 + x_2 - y_1 - y_2)^2$ $= (x_{1} - y_{1})^{2} + 2(x_{1} - y_{1})(x_{2} - y_{2}) + 2(x_{2} - y_{2})^{2}$

利用不等式

$$
a ^ {2} + 2 a b + 2 b ^ {2} = \left[ \begin{array}{l} a \\ b \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{l l} 1 & 1 \\ 1 & 2 \end{array} \right] \left[ \begin{array}{l} a \\ b \end{array} \right] \leqslant \lambda_ {\max} \left\{\left[ \begin{array}{l l} 1 & 1 \\ 1 & 2 \end{array} \right] \right\} \times \left\| \left[ \begin{array}{l} a \\ b \end{array} \right] \right\| _ {2} ^ {2}
$$

可得 $\| f(x) - f(y)\| _2\leqslant \sqrt{2.618}\| x - y\| _2,\forall x,y\in R^2$

这里用到了半正定对称矩阵的性质,即对于所有 $x \in R^{n}, x^{T}Px \leqslant \lambda_{\max}(P)x^{T}x$ , 其中 $\lambda_{\max}(\cdot)$ 是矩阵的最大特征值。如果我们用更保守的不等式

$$a ^ {2} + 2 a b + 2 b ^ {2} \leqslant 2 a ^ {2} + 3 b ^ {2} \leqslant 3 (a ^ {2} + b ^ {2})$$

就会得到一个更为保守的(更大的)利普希茨常数,这样得到的利普希茨常数为 $L=\sqrt{3}$ 。

△

在上面的两个例子中,一个用到 $\|\cdot\|_{\infty}$ , 另一个用到 $\|\cdot\|_{2}$ 。由于范数是等价的, 所以在 $R^{n}$ 上选择哪种范数并不影响函数的利普希茨性, 只影响利普希茨常数的值(见习题3.5)。例3.2说明, 式(3.2)的利普希茨条件不能唯一地定义利普希茨常数 L。如果式(3.2)满足某一正常数 L, 那么它就满足任何大于 L 的常数。通过定义 L 是满足式(3.2)的最小常数, 即可消除这一非唯一性, 但一般不必这么做。
