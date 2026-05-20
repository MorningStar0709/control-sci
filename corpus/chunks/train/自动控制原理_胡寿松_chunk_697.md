# (2) 全维状态观测器分析设计

由图 9-26 可列出全维状态观测器动态方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} - \boldsymbol {H} (\boldsymbol {y} - \boldsymbol {y}), \quad \boldsymbol {y} = \boldsymbol {C} \boldsymbol {x} \tag {9-231}$$

故有

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} - \boldsymbol {H C} (\boldsymbol {x} - \boldsymbol {x}) = (\boldsymbol {A} - \boldsymbol {H C}) \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} + \boldsymbol {H y} \tag {9-232}$$

式中， $(A - HC)$ 称为观测器系统矩阵。观测器分析设计的关键问题是能否在任何初始条件下，即尽管 $\hat{x}(t_0)$ 与 $x(t_0)$ 不同，但总能保证

$$\lim _ {t \rightarrow \infty} (\hat {\mathbf {x}} (t) - \mathbf {x} (t)) = \mathbf {0} \tag {9-233}$$

成立。只有满足式(9-233)，状态反馈系统才能正常工作，式(9-231)所示系统才能作为实际的状态观测器，故式(9-233)称为观测器存在条件。

由式(9-232)与式(9-229)可得

$$\dot {\boldsymbol {x}} - \dot {\boldsymbol {x}} = (\boldsymbol {A} - \boldsymbol {H C}) (\boldsymbol {x} - \boldsymbol {x}) \tag {9-234}$$

其解为

$$\boldsymbol {x} (t) - \hat {\boldsymbol {x}} (t) = \mathrm{e} ^ {(\boldsymbol {A} - \boldsymbol {H C}) (t - t _ {0})} [ \boldsymbol {x} (t _ {0}) - \hat {\boldsymbol {x}} (t _ {0}) ] \tag {9-235}$$

显见当 $\hat{x}(t_0) = x(t_0)$ 时，恒有 $x(t) = \hat{x}(t)$ ，所引入的输出反馈并不起作用。当 $\hat{x}(t_0) \neq x(t_0)$ 时，有 $\hat{x}(t) \neq x(t)$ ，输出反馈便起作用了，这时只要 $(A - HC)$ 的全部特征值具有负实部，初始状态向量误差总会按指数衰减规律满足式(9-233)，其衰减速率取决于观测器的极点配置。由前面的输出反馈定理可知，若被控对象可观测，则 $(A - HC)$ 的极点可任意配置，以满足 $\hat{x}$ 逼近 $x$ 的速率要求，因而保证了状态观测器的存在性。

定理 9-7 若被控系统 $(A,B,C)$ 可观测,则其状态可用形如

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} - \boldsymbol {H C} (\boldsymbol {x} - \boldsymbol {x}) = (\boldsymbol {A} - \boldsymbol {H C}) \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} + \boldsymbol {H y} \tag {9-236}$$

的全维状态观测器给出估值,其中矩阵 H 按任意配置观测器极点的需要来选择,以决定状态误差衰减的速率。

选择 H 阵参数时,应注意防止数值过大带来的实现困难,如饱和效应、噪声加剧等,通常希望观测器响应速度比状态反馈系统的响应速度要快些。

例 9-22 设被控对象传递函数为

$$\frac {Y (s)}{U (s)} = \frac {2}{(s + 1) (s + 2)}$$

试设计全维状态观测器，将极点配置在-10,-10。

解 被控对象的传递函数为

$$\frac {Y (s)}{U (s)} = \frac {2}{(s + 1) (s + 2)} = \frac {2}{s ^ {2} + 3 s + 2}$$

根据传递函数可直接写出系统的可控标准型

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {c} \boldsymbol {x}$$
