$$\nabla_ {h f} g = h \nabla_ {f} g, \quad \nabla_ {f} (h g) = L _ {f} (h) g + h \nabla_ {f} g, \quad h \in C ^ {\infty} (M), \tag {3.11.7}$$

则 $\nabla$ 称为一个联络.

在一个局部坐标 $x$ 下，联络对基底的作用记作

$$\nabla_ {\frac {\partial}{\partial x _ {i}}} \left(\frac {\partial}{\partial x _ {j}}\right) = \sum_ {k = 1} ^ {n} \gamma_ {i j} ^ {k} \frac {\partial}{\partial x _ {k}},$$

这里 $\gamma_{ij}^{k}$ 称为 Christoffel 符号. 我们定义 Christoffel 矩阵 $\Gamma$ 为

$$
\Gamma = \left[ \begin{array}{c c c c c c c} \gamma_ {1 1} ^ {1} & \dots & \gamma_ {1 n} ^ {1} & \dots & \gamma_ {n 1} ^ {1} & \dots & \gamma_ {n n} ^ {1} \\ \vdots & & \vdots & & \vdots & & \vdots \\ \gamma_ {1 1} ^ {n} & \dots & \gamma_ {1 n} ^ {n} & \dots & \gamma_ {n 1} ^ {n} & \dots & \gamma_ {n n} ^ {n} \end{array} \right].
$$

在下面的推导中，我们使用矩阵的半张量积 $\times$ 定义可参见文献[5].

两向量间的联络由以下矩阵表示：

命题3.11.1 设 $f = \sum_{i=1}^{n} f_i \frac{\partial}{\partial x_i}$ 及 $g = \sum_{j=1}^{n} g_j \frac{\partial}{\partial x_j}$ . 那么

$$\nabla_ {f} g = D g \ltimes f + \Gamma \ltimes f \ltimes g. \tag {3.11.8}$$

证明 由定义 (3.11.6)\~(3.11.7)，可算出

$$
\begin{array}{l} \nabla_ {f} g = \sum_ {i = 1} ^ {n} f _ {i} \left(\sum_ {j = 1} ^ {n} L _ {\frac {\partial}{\partial x _ {i}}} g _ {j} \frac {\partial}{\partial x _ {j}} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} g _ {j} \gamma_ {i j} ^ {k} \frac {\partial}{\partial x _ {k}}\right) \\ = D g \ltimes f + \Gamma \ltimes f \ltimes g. \tag {3.11.9} \\ \end{array}
$$

式(3.11.9)的最后式子是向量场的向量形式表示．一般地，向量场 $f=\sum_{i=1}^{n}f_{i}\frac{\partial}{\partial x_{i}}$ 简单表示为 $f = [f_{1}, f_{2}, \cdots, f_{n}]^{T}$ .

设 $y = y(x)$ 是另一个局部坐标。我们导出 $\Gamma$ 在新坐标下的表示。记作 $\tilde{\Gamma}$ 和 $\widetilde{\gamma}_{ij}^{k}$ 为新坐标下的相应元素，则有如下引理：

引理3.11.1 在新坐标 $y$ 下，
