假定静态耦合矩阵 $\boldsymbol{B}(t), \boldsymbol{B}^{-1}(t)$ 均已知，而系统各通道的加速度和外扰作用分别为

$$
\left\{ \begin{array}{l} f _ {1} = x _ {1} ^ {2} + x _ {2} ^ {2} + \dot {x} _ {1} \dot {x} _ {2} + \operatorname{sign} (\cos (0. 9 t)) \\ f _ {2} = x _ {1} x _ {2} + \dot {x} _ {1} ^ {2} + \dot {x} _ {2} ^ {2} + \sin (0. 7 t) \end{array} \right. \tag {6.1.8}
$$

记虚拟控制量为

$$
\left[ \begin{array}{l} U _ {1} \\ U _ {2} \end{array} \right] = \boldsymbol {B} (t) \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] \tag {6.1.9}
$$

用虚拟控制量所作的整个自抗扰控制器算法为

$$
\left\{ \begin{array}{l} \mathrm{fh} = \text {fhan} \left(v _ {1 1} - y _ {1} ^ {\prime}, v _ {1 2}, r _ {0}, h\right) \\ v _ {1 1} = v _ {1 1} + h v _ {1 2} \\ v _ {1 2} = v _ {1 2} + h f _ {1} \\ e = z _ {1 1} - y _ {1}, \mathrm{fe} = \text {fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \text {fal} (e, 0. 2 5, h) \\ z _ {1 1} = z _ {1 1} + h \left(z _ {1 2} - \beta_ {0 1} e\right) \\ z _ {1 2} = z _ {1 2} + h \left(z _ {1 3} - \beta_ {0 2} \mathrm{fe} + U _ {1}\right) \\ z _ {1 3} = z _ {1 3} + h \left(- \beta_ {1 0} \mathrm{fe} _ {1}\right) \\ e _ {1} = v _ {1 1} - z _ {1 1}, e _ {2} = v _ {1 2} - z _ {1 2} \\ U _ {1} = - \text {fhan} \left(e _ {1}, c e _ {2}, r, h _ {1}\right) - z _ {1 3} \end{array} \right. \tag {6.1.10}

\left\{ \begin{array}{l} \mathrm{fh} = \text { fhan } (v _ {2 1} - y _ {2} ^ {*}, v _ {2 2}, r _ {0}, h) \\ v _ {2 1} = v _ {2 1} + h e _ {2 2} \\ v _ {2 2} = v _ {2 2} + h \mathrm{fh} \\ e = z _ {2 1} - y _ {2}, \mathrm{fe} = \text { fal } (e, 0. 5, h), \mathrm{fe} _ {1} = \text { fal } (e, 0. 2 5, h) \\ z _ {2 1} = z _ {2 1} + h (z _ {2 2} - \beta_ {0 1} e) \\ z _ {2 2} = z _ {2 2} + h (z _ {2 3} - \beta_ {0 0} \mathrm{fe} + U _ {2}) \\ z _ {2 3} = z _ {2 3} + h (- \beta_ {0 1} \mathrm{fe} _ {1}) \\ e _ {1} = v _ {2 1} - z _ {2 1}, e _ {2} = v _ {2 2} - z _ {2 2} \\ U _ {2} = - \text { fhan } (e _ {1}, c e _ {2}, r, h _ {1}) - z _ {2 3} \end{array} \right. \tag {6.1.11}
$$

确定出虚拟控制量 $U_{1}, U_{2}$ 以后, 所需的实际控制量为

$$
\left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] = \boldsymbol {B} ^ {- 1} (t) \left[ \begin{array}{l} U _ {1} \\ U _ {2} \end{array} \right] \tag {6.1.12}
$$

把这个控制量送入对象(6.1.5)中进行仿真的结果如图6.1.2所示.尽管开环系统很不稳定且受到时变强扰动作用,但是各通道的被控输出跟踪各自的设定值的效果很好,而且扩张状态观测器实时估计各自通道上的加速度和外扰总和作用也是很好的.

![](image/3a09c6bf1c6c9c70352d664e9c070378f60a13cf5cca0e4bf875351c0fa429dc.jpg)

<details>
<summary>line</summary>

| x | v₁₁v₁ | v₂₁v₂ | fᵣₙ₃₃ |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 5 | 2 | 1 | 1 |
| 10 | 3 | 2 | 2 |
| 15 | 4 | 3 | 3 |
| 20 | 3 | 2 | 2 |
| 5 | 1 | 1 | 1 |
| 10 | 0 | 0 | 0 |
| 15 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
h=0.01, r=100, β₁=0.1, c=1.0
</details>

图6.1.2

如果把各通道的设定值改成
