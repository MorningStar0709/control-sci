由方程 (2.5.6) 得出：对于 $\lambda < 0$ ，当 $t \to +\infty$ 时， $y(t; y_0) \to 0$ ，并且对于任意 $y_0 \neq 0$ ，微分方程 (2.5.4) 以 $y_0$ 为初态的轨线是过 $y_0$ 的半射线；对于 $\lambda > 0$ 及 $y_0 \neq 0$ ，微分方程 (2.5.4) 以 $y_0$ 为初态的轨线同样是过 $y_0$ 的半射线，但当 $t \to +\infty$ 时，轨线离开原点而趋于无穷，但当 $t \to -\infty$ 时，微分方程 (2.5.4) 以任意 $y_0 \neq 0$ 为初态的轨线趋于原点。当 $\lambda$ 为矩阵 $A$ 的几何二重实特征值时， $y = 0$ 称为微分方程 (2.5.4) 的临界结点型奇点。 $\lambda < 0$ 时， $y = 0$ 称为微分方程 (2.5.4) 的稳定临界结点，而 $\lambda > 0$ 时，则称 $y = 0$ 为微分方程 (2.5.4) 的不稳定临界结点。这时其轨线的分布分别称为稳定临界结点型和不稳定临界结点型（图 2.5.7）。

![](image/0594eb4ee4cd7b5cc7564b0ba40c5af2b95421134ac42fdd18894fd092e4964e.jpg)

<details>
<summary>text_image</summary>

y₂
y₁
λ>0的情况
</details>

![](image/3d0c16f27b0c785f37de5dad9041d5d7de27cb01fa270b6e8c0d02d9bcc5c376.jpg)

<details>
<summary>text_image</summary>

y₂
y₁
λ<0 的情况
</details>

图2.5.7

(3) $A = \begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$ , $\lambda$ 为矩阵 $A$ 的代数二重特征值.

微分方程 (2.5.4) 的以 $y_0$ 为初值的解为

$$
y (t; y _ {0}) = \left[ \begin{array}{c c} \mathrm{e} ^ {\lambda t} & t \mathrm{e} ^ {\lambda t} \\ 0 & \mathrm{e} ^ {\lambda t} \end{array} \right] y _ {0}. \tag {2.5.7}
$$

由方程 (2.5.7) 不难看出，对于 $\lambda < 0$ ，当 $t \to +\infty$ 时，有 $y(t; y_0) \to 0$ ；当初值 $y_0$ 不在 $y_1$ 轴时，则当 $t \to \infty$ 时， $y(t; y_0)$ 按与 $y_1$ 轴相切的方式趋于 $y = 0$ ； $y_1$ 轴也是方程 (2.5.4) 的轨线。 $y = 0$ 称为微分方程 (2.5.4) 的稳定的退化结点型奇点。同样，其轨线的分布称为稳定退化结点型的（图 2.5.8）。

同理，对于 $\lambda > 0$ ，当 $t \to -\infty$ 时，有 $y(t; y_0) \to 0$ ；而对于不在 $y_1$ 轴上的 $y_0$ 点，当 $t \to -\infty$ 时， $y(t; y_0)$ 按与 $y_1$ 轴相切的方式趋于 $y = 0$ ； $y_1$ 轴也是微分方程 (2.5.4) 的轨线。这时微分方程 (2.5.4) 的相图如图 2.5.9 所示。 $y = 0$ 称为微分方程 (2.5.4) 的不稳定退化结点型奇点，相应的轨线分布称为不稳定退化结点型的 (图 2.5.9)。

![](image/383f5102adcb0cedf55ff857e0d3d5f3ebcaa926daad60e5d605f9c55c581865.jpg)

<details>
<summary>text_image</summary>

y₂
y₂
y₁
y₁
</details>

图2.5.8  
图2.5.91

(4) $\Lambda=\left[\begin{matrix}\alpha-\beta\\1-\beta\alpha\end{matrix}\right],\beta\neq0,\alpha\pm\beta$ 是 A 的一对复共轭特征值.

为了更容易画出微分方程(2.5.4)的相平面图，下面引入极坐标

$$
\begin{array}{l} y _ {1} = \rho \cos \theta , \\ y _ {2} = \rho \sin \theta . \tag {2.5.8} \\ \end{array}
$$

这时微分方程(2.5.4)变换为

$$\dot {\rho} = \alpha \rho , \quad \dot {\theta} = - \beta . \tag {2.5.9}$$

微分方程 (2.5.9) 的轨线的参数表达式 (时间视为参数) 为

$$
\left\{ \begin{array}{l} \rho (t; \rho_ {0}, \theta_ {0}) = - \rho_ {0} e ^ {\alpha t}, \\ \vdots \\ \theta (t; \rho_ {0}, \theta_ {0}) = - \beta t + \theta_ {0}. \end{array} \right. \tag {2.5.10}
$$
