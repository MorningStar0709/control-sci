# (3) 复合型性能指标

数学描述如式(10-3)所示。复合型性能指标是最一般的性能指标形式,表示对整个控制过程和末端状态都有要求。采用复合型性能指标的最优控制系统,主要有以下两种应用类型:

1) 状态调节器。

$$J = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {F x} \left(t _ {f}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R u} (t) \right] \mathrm{d} t \tag {10-9}$$

式中， $F=F^{T}\geqslant0,Q=Q^{T}\geqslant0,R=R^{T}>0$ ，称为加权矩阵。为了便于设计，权阵F,Q和R通常取为对角阵。性能指标(10-9)表示对于运行在某一平稳状态的线性控制系统，在系统受扰偏离原平衡状态时，控制律 $u^{*}(t)$ 使系统恢复到原平衡状态附近时所要求的性能。其中， $x^{\mathrm{T}}(t)Qx(t)$ 表示控制过程中的状态偏差； $u^{\mathrm{T}}(t)Ru(t)$ 表示控制过程中消耗的控制能量， $x^{\mathrm{T}}(t_{f})Fx(t_{f})$ 表示控制过程结束时的末态偏差，1/2是为便于进行二次型函数运算而加入的标量因子。采用式(10-9)作为性能指标的线性控制系统有许多种，例如导弹的横滚控制回路以及发电厂的电压调节系统，都属于状态调节器范畴。

2) 输出跟踪系统。

$$J = \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {F e} \left(t _ {f}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \boldsymbol {e} ^ {\mathrm{T}} (t) \boldsymbol {Q e} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R u} (t) \right] \mathrm{d} t \tag {10-10}$$

式中， $e(t)=z(t)-y(t)$ 为跟踪误差； $z(t)$ 为理想输出向量，与实际输出向量 $y(t)$ 同维；加权矩阵 F, Q 和 R 的要求同式(10-9)。式(10-10) 中各组成部分的物理意义与性能指标与式(10-9) 类似。许多实际控制系统，例如飞机、导弹及航天器的指令信号跟踪、模型跟踪控制系统中的状态或输出跟踪等，均采用式(10-10) 形式的性能指标。
