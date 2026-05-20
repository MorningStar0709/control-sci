# 5.1.6 不同误差组合方式所成的“非线性PID”

在公式(5.1.9)、式(5.1.11)、式(5.1.12)、式(5.1.16)中只改变各误差量的“非线性组合”形式就能得到各种不同形式的非线性PID调节器。我们推荐的可供选择的非线性组合方式为

$$
\begin{array}{l} \left\{ \begin{array}{l l} (1) u = \beta_ {0} \mathrm{fal} (e _ {0}, \alpha_ {0}, \delta) + \beta_ {1} \mathrm{fal} (e _ {1}, \alpha_ {1}, \delta) + \beta_ {2} \mathrm{fal} (e _ {2}, \alpha_ {2}, \delta) \\ \alpha_ {0} <   0 <   \alpha_ {1} <   1 <   \alpha_ {2}, \text {或} 0 <   \alpha_ {0} <   \alpha_ {1} <   1 <   \alpha_ {2} \end{array} \right. \\ u = \beta_ {0} e _ {0} - \text { fhan } (e _ {1}, e _ {2}, r _ {1}, h _ {1}) (2) \\ u = - \operatorname{fhan} \left(e _ {1}, c e _ {2}, r _ {2}, h _ {2}\right) (3) \\ \end{array}
$$

(5.1.17)

在(1)的组合方式中,参数 $\alpha_{i},\delta$ 事先可以确定,如:

$$\alpha_ {0} = - 0. 6, \alpha_ {1} = 0. 6, \alpha_ {2} = 1. 2 \text {或}\alpha_ {0} = 0. 2 5, \alpha_ {1} = 0. 7 5, \alpha_ {2} = 1. 5, \delta = h \text {或} \delta = k h$$

这样，可调参数只有各误差的反馈增益 $\beta_0, \beta_1, \beta_2$ 三个了；在(2)的组合方式中，可调参数也有三个： $\beta_0, r_1, h_1$ ；而(3)的组合方式中也是有三个可调参数 $r_2, h_2, c.$ 总而言之，在上述三种不同的非线性组合形式，就像经典PID一样，可调参数只有三个 $\beta_0, \beta_1, \beta_2$ ，或 $\beta_0, r_1, h_1$ ，或 $r_2, h_2, c.$

例 我们考察用上述方法控制系统(5.1.10)时的阶跃响应. 这里状态误差量的非线性组合分别采用前述三种方法之一.

(1) 采用非线性组合

$$u = \beta_ {0} \operatorname{fal} \left(e _ {0}, \alpha_ {0}, \delta\right) + \beta_ {1} \operatorname{fal} \left(e _ {1}, \alpha_ {1}, \delta\right) + \beta_ {2} \operatorname{fal} \left(e _ {2}, \alpha_ {2}, \delta\right)$$

时，先确定 $\alpha_{0}=\frac{1}{4},\alpha_{1}=\frac{3}{4},\alpha_{2}=\frac{3}{2},\delta=2h,h=0.01$ ，然后调整出 $\beta_{0},\beta_{1},\beta_{2}$ ，得

$$\beta_ {0} = 1 0, \beta_ {1} = 5, \beta_ {2} = 1 0 0$$

用这组参数所作的仿真结果如图 5.1.8 所示.

![](image/cbcdc5591c081c6ecae176013c3055920e22755a2134e44bcb098787f0ecb3ef.jpg)

<details>
<summary>line</summary>

| x | v₁,v |
| --- | --- |
| 0 | 0.0 |
| 2 | 0.5 |
| 4 | 0.8 |
| 6 | 0.9 |
| 8 | 0.95 |
| 10 | 0.98 |
| 12 | 0.97 |
| 14 | 0.96 |
| 16 | 0.95 |
| 18 | 0.94 |
| 20 | 0.93 |
</details>

图5.1.8

(2) 采用非线性组合

$$u = \beta_ {0} e _ {0} - \operatorname{fhan} \left(e _ {1}, e _ {2}, r _ {1}, h _ {1}\right)$$

时，调整出参数 $\beta_{0},r_{1},h_{1}$ ，得

$$\beta_ {0} = 5 0 0, r _ {2} = 2 0, h _ {2} = 0. 0 8$$

对应的仿真结果如图 5.1.9 所示.

![](image/fa46087ba9b0b3b431f01fa8f0189759f4c05c81981c1f2e08e55f3363b78d9a.jpg)

<details>
<summary>line</summary>
