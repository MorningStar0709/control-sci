![](image/a1e153d6f00f4b0c78d3c67b05ff0e84b3ceee1f57c9309782e96ce99811df5b.jpg)

<details>
<summary>text_image</summary>

x₁(t)
k(x₁(t)-x₂(t))
m₁
F(t)
</details>

图 10.2.3 两辆小车的受力分析图

将 $m_{1}=m_{2}=1kg, k=100N/m$ ，以及状态变量和系统输入代入其中，可得

$$
\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t) + B u (t) \tag {10.2.5}
$$

其中， $A=\begin{bmatrix}0&1&0&0\\-100&0&100&0\\0&0&0&1\\100&0&-100&0\end{bmatrix},B=\begin{bmatrix}0\\1\\0\\0\end{bmatrix}$ 。这是一个四维系统，n=4。它的能控矩阵为：

$$
\boldsymbol {C} _ {\circ} = \left[ \begin{array}{l l l l} \boldsymbol {B} & \boldsymbol {A B} & \boldsymbol {A} ^ {2} \boldsymbol {B} & \boldsymbol {A} ^ {3} \boldsymbol {B} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & - 1 0 0 \\ 1 & 0 & - 1 0 0 & 0 \\ 0 & 0 & 0 & 1 0 0 \\ 0 & 0 & 1 0 0 & 0 \end{array} \right], \operatorname{Rank} (\boldsymbol {C} _ {\circ}) = 4 \tag {10.2.6}
$$

所以系统能控。说明在一辆小车上面作用的力可以通过弹簧传递到另一辆小车上，选择合适的输入，可以令这两辆小车同时达到目标位置与速度。有两点需要说明：第一，能控性是指理论上能控，但具体到实际问题中，要考虑系统的物理限制。例如在本例中，弹簧超过一定长度之后就会发生不可逆的形变。第二，能控性表明系统的状态可以被控制到任意的终端状态，但是不代表系统可以稳定在任意的终端状态。10.3.2节会有详细的说明。

线性状态反馈控制器—可控性内容请扫描此二维码观看。
