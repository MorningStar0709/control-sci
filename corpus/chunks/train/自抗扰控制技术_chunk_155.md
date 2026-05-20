在一般情况下这个 $\omega$ 的适应范围很宽, 因此很容易调整出合适的 $\omega$ .

按这种方法确定了参数 $\beta_{01},\beta_{02},\beta_{03}$ 之后，跟踪系统

$$
\left\{ \begin{array}{l} x _ {1} = x _ {1} + h x _ {2} \\ x _ {2} = x _ {2} + h \gamma \mathrm{sign} (\sin (\omega t)) \\ y = x _ {1} \end{array} \right. \tag {4.4.8}
$$

的“总和扰动”—— $\gamma \mathrm{sign}(\sin (\omega t))$ ，几乎不受扰动幅度 $\gamma$ 的限制. 受如下形式

$$w (t) = \gamma \operatorname{sign} (\sin (\omega t)), \omega = 0. 0 0 1 / h \tag {4.4.9}$$

方波扰动的受扰对象

$$
\left\{ \begin{array}{l} f = \gamma \operatorname{sign} \left(\sin \frac {0 . 0 0 0 5 5}{h} t\right) \\ x _ {1} = x _ {1} + h x _ {2} \\ x _ {2} = x _ {2} + h f \\ y = x _ {1} \end{array} \right. \tag {4.4.10}
$$

用扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ z _ {1} = z _ {1} + h (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h (z _ {3} - \beta_ {0 2} e) \\ z _ {3} = z _ {3} + (- \beta_ {0 3} e) \end{array} \right. \tag {4.4.11}
$$

来进行跟踪时,跟踪好坏的指标定为

$$J = \frac {1}{T} \int_ {0} ^ {\tau} | f - z _ {3} | \mathrm{d} \tau \tag {4.4.12}$$

式中， $T = 20000\mathrm{h}$ 是整个计算时间. 不管采样间隔多大，只计算20000步.

对系统(4.4.10)进行仿真计算结果概括如下:步长在 h = 1000000 \~ 0.000001 范围内随便取定,扰动幅度 $\gamma$ 也在这个范围随便确定,用扩张状态观测器(4.4.11)来进行跟踪,其跟踪扰动的误差指标 J 均在 0.0013 \~ 0.0015 之间.跟踪一阶对象

$$
\left\{ \begin{array}{l} f = \gamma \text {sign} \left(\sin \left(\frac {0 . 0 0 0 5 5}{h} t\right)\right) \\ x _ {1} = x _ {1} + h f \\ y = x _ {1} \end{array} \right. \tag {4.4.13}
$$

的结果是在上述步长和扰动幅度范围内跟踪扰动的误差指标 J 均在 0.00025 \~ 0.00026 之间. 不管一阶, 二阶情形这些扩张状态观测器跟踪效果都是很好的.
