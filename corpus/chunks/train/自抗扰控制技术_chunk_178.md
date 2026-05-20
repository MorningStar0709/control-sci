这类控制器是由三个部分结构组合而成的：①“安排过渡过程”的装置；②“提取输出量微分信号”的装置；③“误差及其微分、积分信号的合理组合”来生成误差反馈律的装置。这三个装置都有好几种可能的选择。比如“安排过渡过程”可以用跟踪微分器，也可以用适当的函数发生器。用跟踪微分器可以用线性的或非线性的，还有按经典的办法事先不安排过渡过程等。这样，“安排过渡过程”至少有四种可能的选择；“提取输出微分信号”可以用用跟踪微分器，也可以用状态观测器或扩张状态观测器。这两个装置也可以是线性的，也可以是非线性的，这样“提取输出微分信号”至少有六种可能的选择；“误差及其微分、积分信号的合理组合”形式也有线性的或两种非线性形式等至少三种不同的组合形式。这样，我们可以组合出至少 $4 \times 6 \times 3 = 72$ 种改进的线性的或非线性的PID控制器。

以下所采用的跟踪微分器是第二章中提出的离散形式的最速跟踪微分器

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (v _ {1} - v, v _ {2}, r, h _ {0}) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \end{array} \right. \tag {5.1.1}
$$

或线性跟踪微分器

$$
\left\{ \begin{array}{l} \mathrm{fh} = - r ^ {2} (v _ {1} - v) - 2 r v _ {2} \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \end{array} \right. \tag {5.1.2}
$$

也可以用如下状态观测器的形式

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \mathrm{fe} = \operatorname{fal} (e, \alpha , \delta), 0 <   \alpha <   1 \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(- \beta_ {0 2} \mathrm{fe}\right) \end{array} \right. \tag {5.1.3}
$$

或如下扩张状态观测器的形式

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \mathrm{fe} = \operatorname{fal} (e, 0. 5, h) \\ \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} + b _ {0} u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {5.1.4}
$$

来提取输出信号 y 的微分信号.
