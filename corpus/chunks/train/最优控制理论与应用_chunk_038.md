# 3.1 变分法基础

先来给出下面的一些定义。

1. 泛函: 如果对某一类函数 $\{X(t)\}$ 中的每一个函数 $X(t)$ ，有一个实数值 J 与之相对应，则 J 称为依赖于函数 $X(t)$ 的泛函，记为

$$J = J [ X (t) ]$$

粗略来说,泛函是以函数为自变量的函数。

2. 泛函的连续性: 若对任给的 $\varepsilon > 0$ , 存在 $\delta > 0$ , 当 $\| X(t) - \hat{X}(t) \| < \delta$ 时, 就有

$$\mid J (\boldsymbol {X}) - J (\hat {\boldsymbol {X}}) \mid < \varepsilon$$

则称 $J(X)$ 在 $\hat{X}$ 处是连续的。

3. 线性泛函：满足下面条件的泛函称为线性泛函

$$J [ \alpha X ] = \alpha J [ X ]J (\boldsymbol {X} + \boldsymbol {Y}) = J (\boldsymbol {X}) + J (\boldsymbol {Y})$$

这里 $\alpha$ 是实数, X 和 Y 是函数空间中的函数。

4. 自变量函数的变分: 自变量函数 $X(t)$ 的变分 $\delta X$ 是指同属于函数类 $\{X(t)\}$ 中两个函数 $X_{1}(t)$ 、 $X_{2}(t)$ 之差

$$\delta \boldsymbol {X} = \boldsymbol {X} _ {1} (t) - \boldsymbol {X} _ {2} (t)$$

这里， $t$ 看作为参数。当 $X(t)$ 为一维函数时， $\delta X$ 可用图3-1来表示。

5. 泛函的变分：当自变量函数 $X(t)$ 有变分 $\delta X$ 时，泛函的增量为

![](image/4b34089902e2146f72bdd7c7f093298f7f3de33c8d64930bdea5a7913b7015b1.jpg)

<details>
<summary>text_image</summary>

X(t)
X₁
X₂
δX
O
t
</details>

图3-1 自变量函数的变分

$$
\begin{array}{l} \Delta J = J [ X + \delta X ] - J [ X ] \\ = \delta J [ X, \delta X ] + \varepsilon \| \delta X \| \\ \end{array}
$$

这里， $\delta J[X, \delta X]$ 是 $\delta X$ 的线性泛函，若 $\| \delta X \| \to 0$ 时，有 $\varepsilon \to 0$ ，则称 $\delta J[X, \delta X]$ 是泛函 $J[X]$ 的变分。 $\delta J$ 是 $\Delta J$ 的线性主部。

6. 泛函的极值：若存在 $\varepsilon > 0$ ，对满足 $\|X - X^* \| < \varepsilon$ 的一切 $X, J(X) - J(X^*)$ 具有同一符号，则称 $J(X)$ 在 $X = X^*$ 处有极值。

定理 $J(X)$ 在 $X = X^{*}$ 处有极值的必要条件是对于所有容许的增量函数 $\delta X$ （自变量的变分），泛函 $J(X)$ 在 $X^{*}$ 处的变分为0：

$$\delta J (X ^ {*}, \delta X) = 0$$

为了判别是极大还是极小,要计算二阶变分 $\delta^{2}J$ 。但在实际问题中根据问题的性质容易判别是极大还是极小,故一般不计算 $\delta^{2}J$ 。
