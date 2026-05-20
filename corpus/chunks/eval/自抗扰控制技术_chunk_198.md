$$
\left\{ \begin{array}{l} r _ {0} ^ {\prime} = \rho r _ {0} \\ \beta_ {0 1} ^ {\prime} = \rho \beta_ {0 1}, \beta_ {0 2} ^ {\prime} = \rho^ {2} \beta_ {0 2}, \beta_ {0 3} ^ {\prime} = \rho^ {3} \beta_ {0 3} \\ \beta_ {1} ^ {\prime} = \rho^ {2} \beta_ {1}, \beta_ {2} ^ {\prime} = \rho \beta_ {2} \end{array} \right. \tag {5.6.4}
$$

那么上式进一步变成

$$
\left\{ \begin{array}{l} \mathrm{fh} ^ {\prime} = - r _ {0} ^ {\prime 2} \left(v _ {1} ^ {\prime} - v _ {0}\right) + 2 r _ {0} ^ {\prime} v _ {2} ^ {\prime} \\ v _ {1} ^ {\prime} = v _ {1} ^ {\prime} + h ^ {\prime} v _ {2} ^ {\prime} \\ v _ {2} ^ {\prime} = v _ {2} ^ {\prime} + h ^ {\prime} \mathrm{fh} ^ {\prime} \\ e ^ {\prime} = z _ {1} ^ {\prime} - y \\ z _ {1} ^ {\prime} = z _ {1} ^ {\prime} + h ^ {\prime} \left(z _ {2} ^ {\prime} - \beta_ {0 1} ^ {\prime} e ^ {\prime}\right) \\ z _ {2} ^ {\prime} = z _ {2} ^ {\prime} + h ^ {\prime} \left(z _ {3} ^ {\prime} - \beta_ {0 2} ^ {\prime} e ^ {\prime} + b _ {0} u ^ {\prime}\right) \\ z _ {3} ^ {\prime} = z _ {3} ^ {\prime} + h ^ {\prime} \left(- \beta_ {0 3} ^ {\prime} e ^ {\prime}\right) \\ e _ {1} ^ {\prime} = v _ {1} ^ {\prime} - z _ {1}, e _ {2} ^ {\prime} = v _ {2} - z _ {2} ^ {\prime} \\ u ^ {\prime} = \frac {\beta_ {1} ^ {\prime} e _ {1} ^ {\prime} + \beta_ {3} ^ {\prime} e _ {2} ^ {\prime} - z _ {3} ^ {\prime}}{b _ {0}} \end{array} \right. \tag {5.6.5}
$$

在式(5.6.5)中去掉每个变量的“ $\prime\prime$ ”就变成标准的算法(5.6.1)了．这说明采样步长 $h$ 所对应的自抗扰控制器参数组 $\{r_0,\beta_{01},\beta_{02},$ $\beta_{03},\beta_1,\beta_2,b_0\}$ 确定之后，对应于采样步长 $h^{\prime} = \frac{h}{\rho}$ 的自抗扰控制器参数组是由变换关系(5.6.4）来确定，即对应于采样步长 $h^{\prime}$ 的自抗扰控制器参数为 $\{\rho r_0,\rho \beta_{01},\rho^2\beta_{02},\rho^3\beta_{03},\rho^2\beta_1,\rho \beta_2\}$

线性自抗扰控制器的连续动态方程为

$$
\left\{ \begin{array}{l} \mathrm{fh} = - r _ {0} ^ {2} \left(v _ {1} - v _ {0}\right) + 2 r _ {0} v _ {2} \\ \dot {v} _ {1} = v _ {2} \\ \dot {v} _ {2} = \mathrm{fh} \\ e = z _ {1} - y \\ \dot {z} _ {1} = \left(z _ {2} - \beta_ {0 1} e\right) \\ \dot {z} _ {2} = \left(z _ {3} - \beta_ {0 2} e + b _ {0} u\right) \\ \dot {z} _ {3} = (- \beta_ {0 3} e) \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u = \frac {\beta_ {1} e _ {1} + \beta_ {2} e _ {2} - z _ {3}}{b _ {0}} \end{array} \right. \tag {5.6.6}
$$

在这里进行“时间尺度”变换

$$t = \rho \tau \tag {5.6.7}$$

那么由于 $\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{\mathrm{d}x}{\mathrm{d}\rho\tau} = \frac{1}{\rho}\frac{\mathrm{d}x}{\mathrm{d}\tau}$ (5.6.8)

就有
