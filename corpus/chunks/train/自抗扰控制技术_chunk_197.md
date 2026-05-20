# 5.6 系统的时间尺度与自抗扰控制器

本节就对线性自抗扰控制器的各参数与系统“时间尺度”之间关系进行探讨.

二阶线性自抗扰控制器的标准算法为

$$
\left\{ \begin{array}{l} \mathrm{fh} = - r _ {0} ^ {2} \left(v _ {1} - v _ {0}\right) + 2 r _ {0} v _ {2} \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \\ e = z _ {1} - y \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} e + b _ {0} u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} e\right) \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u = \frac {\beta_ {1} e _ {1} + \beta_ {2} e _ {2} - z _ {3}}{b _ {0}} \end{array} \right. \tag {5.6.1}
$$

对这个算法进行“时间尺度”变换

$$h = \rho h ^ {\prime} \tag {5.6.2}$$

那么有

$$
\left\{ \begin{array}{l} \mathrm{fh} = - r _ {0} ^ {2} (v _ {1} - v _ {0}) + 2 r _ {0} v _ {2} \\ v _ {1} = v _ {1} + h ^ {\prime} \rho v _ {2} \\ v _ {2} = v _ {2} + h ^ {\prime} \rho \mathrm{fh} \\ e = z _ {1} - y \\ z _ {1} = z _ {1} + h ^ {\prime} \rho (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h ^ {\prime} \rho (z _ {3} - \beta_ {0 2} e + b _ {0} u) \\ z _ {3} = z _ {3} + h ^ {\prime} \rho (- \beta_ {0 3} e) \\ e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u = \frac {\beta_ {1} e _ {1} + \beta_ {2} e _ {2} - z _ {3}}{b _ {0}} \end{array} \right.
$$

再令

$$
\left\{ \begin{array}{l} v _ {1} ^ {\prime} = v _ {1}, v _ {2} ^ {\prime} = \rho v _ {2} \\ z _ {1} ^ {\prime} = z _ {1}, z _ {2} ^ {\prime} = \rho z _ {2}, z _ {3} ^ {\prime} = \rho^ {2} z _ {3}, u ^ {\prime} = \rho^ {2} u \\ e _ {1} ^ {\prime} = e _ {1}, e _ {2} ^ {\prime} = \rho e _ {2} \end{array} \right. \tag {5.6.3}
$$

就得

$$
\left\{ \begin{array}{l} \mathrm{fh} ^ {\prime} = - \rho^ {2} z _ {0} ^ {2} \left(v _ {1} ^ {\prime} - v _ {0}\right) + 2 r _ {0} \rho v _ {2} ^ {\prime} \\ v _ {1} ^ {\prime} = v _ {1} ^ {\prime} + h ^ {\prime} v _ {2} ^ {\prime} \\ v _ {2} ^ {\prime} = v _ {2} ^ {\prime} + h ^ {\prime} \mathrm{fh} ^ {\prime} \\ e = z _ {1} ^ {\prime} - y \\ z _ {1} ^ {\prime} = z _ {1} ^ {\prime} + h ^ {\prime} \left(z _ {2} ^ {\prime} - \beta_ {0 1} \rho e\right) \\ z _ {2} ^ {\prime} = z _ {2} ^ {\prime} + h ^ {\prime} \left(z _ {3} ^ {\prime} - \beta_ {0 2} \rho^ {2} e + b _ {0} u ^ {\prime}\right) \\ z _ {3} ^ {\prime} = z _ {3} ^ {\prime} + h ^ {\prime} \left(- \beta_ {0 3} \rho^ {3} e\right) \\ e _ {1} ^ {\prime} = v _ {1} ^ {\prime} - z _ {1} ^ {\prime}, e _ {2} ^ {\prime} = v _ {2} ^ {\prime} - z _ {2} ^ {\prime} \\ u ^ {\prime} = \frac {\rho^ {2} \beta_ {1} e _ {1} ^ {\prime} + \rho \beta_ {2} e _ {2} ^ {\prime} - z _ {3} ^ {\prime}}{b _ {0}} \end{array} \right.
$$

于是再记
