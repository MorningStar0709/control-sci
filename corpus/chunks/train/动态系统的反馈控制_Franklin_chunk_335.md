对于这个系统以及许多类似的系统，基于开环频率响应，用于判断稳定性的包围判据可简化为一个非常简单的判据：当 $G(j\omega)$ 相位为 $180^{\circ}$ 时，如果 $\left|KG(j\omega)\right|<1$ ，那么系统是稳定的。注意，这个关系与式(6.25)所给出的稳定准则是完全相同的；然而，若使用奈奎斯特稳定判据，我们就不需要得到根轨迹以确定 $\left|KG(j\omega)\right|<1$ 还是 $\left|KG(j\omega)\right|>1$ 。

![](image/0990e037ca0be5acb049dcc0f5a8e5cdb6a1111c5dd5f89f72ad135771ade574.jpg)

<details>
<summary>text_image</summary>

Im(s)
C₁
Re(s)
</details>

图 6.27 例 6.9 中系统的包围右半平面的闭合曲线 $C_{1}$

我们利用 Matlab 画奈奎斯特图。其语句如下。

$$
\begin{array}{l} s = t f \left(^ {\prime} s ^ {\prime}\right); \\ \mathrm{sysG} = 1 / \left(\mathrm{s} ^ {*} (\mathrm{s} + 1) ^ {\wedge} 2\right); \\ \text { nyquist(sysG) } \\ \text { axis } ([ - 3 3 - 3 3 ]) \\ \end{array}
$$

axis 命令确定了图的范围，使其仅包含实轴和虚轴上 -3 到 +3 之间的点。如果不人为规定范围，图就会基于 Matlab 计算出的最大值来确定范围，这样在 -1 点区域附近的最重要的特征就会丢失。

因为式(6.28)中的 $P \neq 0$ ，所以必须注意开环不稳定的系统。我们会看到，在此情况下需要修改 6.2 节中的简单的规则。
