如前面所指出的，在定义脉冲响应矩阵时，总是假定系统具有零初始状态。由此，令(2.75)中 $x_0 = 0$ ，并加以改写，可进而得到

$$y (t) = \int_ {t _ {0}} ^ {t} [ C e ^ {A (t - \tau)} B + D \delta (t - \tau) ] u (\tau) d \tau \tag {2.76}$$

再将(2.76)和脉冲响应矩阵的基本关系式(2.69)加以比较,即可导出:

$$G (t - \tau) = C e ^ {A (t - \tau)} B + D \delta (t - \tau) \tag {2.77}$$

将上式作自变量置换，又可把(2.77)改写为：

$$G (t) = C e ^ {A t} B + D \delta (t) \tag {2.78}$$

从而，证明完成。

结论2 注意到 $e^{A(t - \tau)} = \Phi (t - \tau)$ 和 $e^{At} = \Phi (t)$ ，所以脉冲响应矩阵的表达式(2.73)和(2.74)还可表为如下的形式：

$$G (t - \tau) = C \Phi (t - \tau) B + D \delta (t - \tau) \tag {2.79}$$

和

$$G (t) = C \Phi (t) B + D \delta (t) \tag {2.80}$$

其中 $\Phi(\cdot)$ 是线性定常系统(2.72)的状态转移矩阵。

结论 3 两个代数等价的线性定常系统具有相同的脉冲响应矩阵。

证 利用结论 1 知, 系统 $(A, B, C, D)$ 的脉冲响应矩阵为:

$$G (t - \tau) = C e ^ {A (t - \tau)} B + D \delta (t - \tau) \tag {2.81}$$

而系统 $(\overline{A},\overline{B},\overline{C},\overline{D})$ 的脉冲响应矩阵为：

$$\bar {G} (t - \tau) = \bar {C} e ^ {\mathcal {K} (t - \tau)} \bar {B} + \bar {D} \delta (t - \tau) \tag {2.82}$$

但已知两个系统是代数等价的,即成立:

$$\bar {A} = P A P ^ {- 1}, \bar {B} = P B, \bar {C} = C P ^ {- 1}, \bar {D} = D \tag {2.83}$$

和

$$e ^ {\mathcal {A} (t - \tau)} = P e ^ {\mathcal {A} (t - \tau)} p ^ {- 1} \tag {2.84}$$

于是，由此即可导出：

$$
\begin{array}{l} \bar {G} (t - \tau) = \bar {C} e ^ {\lambda (t - \tau)} \bar {B} + \bar {D} \delta (t - \tau) \\ = C P ^ {- 1} \cdot P e ^ {A (t - \tau)} P ^ {- 1} \cdot P B + D \delta (t - \tau) \\ = C e ^ {A (t - \tau)} B + D \delta (t - \tau) = G (t - \tau) \tag {2.85} \\ \end{array}
$$

从而，证明完成。

结论 4 两个代数等价的线性定常系统的输出的零状态响应和零输入响应相同。

证 两个代数等价的线性定常系统 $(A, B, C, D)$ 和 $(\bar{A}, \bar{B}, \bar{C}, \bar{D})$ 的输出的零状态响应为：

$$y _ {0 x} (t) = \int_ {t _ {0}} ^ {t} [ C e ^ {\mathcal {A} (t - \tau)} B + D \delta (t - \tau) ] u (\tau) d \tau \tag {2.86}$$

和

$$\bar {y} _ {0 z} (t) = \int_ {t _ {0}} ^ {t} [ \overline {{C}} e ^ {\mathcal {X} (t - \tau)} \overline {{B}} + \overline {{D}} \delta (t - \tau) ] u (\tau) d \tau \tag {2.87}$$

由此并利用(2.85)，就可得到：

$$\bar {y} _ {0 x} (t) = y _ {0 x} (t), \quad t \geqslant t _ {0} \tag {2.88}$$

再知，两者的输出的零输入响应分别为：

$$\mathcal {Y} _ {0 n} (t) = C e ^ {A \left(t - t _ {0}\right)} x _ {0} \tag {2.89}$$

和

$$\bar {y} _ {0 n} (t) = \bar {C} e ^ {\mathcal {X} (t - t _ {0})} \bar {x} _ {0} \tag {2.90}$$

由代数等价性知成立 $\bar{x}_0 = Px_0$ 和(2.83)，于是由此即可导出：

$$
\begin{array}{l} \mathcal {Y} _ {0 n} (t) = \bar {C} e ^ {\mathcal {K} (t - t _ {0})} \bar {x} _ {0} = C P ^ {- 1} \cdot P e ^ {\mathcal {A} (t - t _ {0})} P ^ {- 1} \cdot P x _ {0} \\ = C e ^ {A (t - t _ {0})} x _ {0} = y _ {0 n} (t), \quad t \geqslant t _ {0} \tag {2.91} \\ \end{array}
$$

从而，证明完成。
