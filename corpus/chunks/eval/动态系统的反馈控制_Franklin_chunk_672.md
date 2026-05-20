\mathbf {A} _ {\mathrm{con}} = \left[ \begin{array}{c c c c} 3. 5 5 9 9 \times 1 0 ^ {- 7} & - 1. 1 1 3 6 \times 1 0 ^ {- 7} & - 1. 1 9 7 6 \times 1 0 ^ {- 7} & - 4. 7 0 1 1 \times 1 0 ^ {- 8} \\ - 1. 1 1 3 6 \times 1 0 ^ {- 7} & 1. 1 6 0 2 \times 1 0 ^ {- 2} & - 2. 5 0 2 7 \times 1 0 ^ {- 3} & - 9. 0 9 9 2 \times 1 0 ^ {- 3} \\ - 1. 9 7 6 1 \times 1 0 ^ {- 7} & - 2. 5 0 2 7 \times 1 0 ^ {- 3} & 6. 3 7 3 6 \times 1 0 ^ {- 3} & - 3. 8 7 0 7 \times 1 0 ^ {- 3} \end{array} \right]

\boldsymbol {B} = \left[ \begin{array}{l l l} 3. 4 6 0 0 \times 1 0 ^ {- 1} & 1. 1 7 7 2 \times 1 0 ^ {- 1} & 2. 8 3 8 0 \times 1 0 ^ {- 2} \\ 3. 8 8 0 3 \times 1 0 ^ {- 1 1} & 8. 0 2 4 9 \times 1 0 ^ {- 2} & 1. 8 0 7 2 \times 1 0 ^ {- 2} \\ 8. 0 0 4 1 \times 1 0 ^ {- 9} & 2. 7 2 1 6 \times 1 0 ^ {- 3} & 3. 1 7 1 3 \times 1 0 ^ {- 2} \end{array} \right]
$$

导出系统的线性模型为

$$\dot {\boldsymbol {T}} = \boldsymbol {A} _ {3} \boldsymbol {T} + \boldsymbol {B} _ {3} \boldsymbol {u}\mathbf {y} = \mathbf {C} _ {3} \mathbf {T} + \mathbf {D} _ {3} \mathbf {u} \tag {10.43}$$

其中： $y=\left[T_{y1}\quad T_{y2}\quad T_{y3}\right]^{\mathrm{T}}$ ，且

$$
\boldsymbol {A} _ {3} = \left[ \begin{array}{c c c} - 0. 0 6 8 2 & 0. 0 1 4 9 & 0. 0 0 0 0 \\ 0. 0 4 5 8 & - 0. 1 1 8 1 & 0. 0 2 1 8 \\ 0. 0 0 0 0 & 0. 0 4 6 8 3 & - 0. 1 0 0 8 \end{array} \right], \quad \boldsymbol {B} _ {3} = \left[ \begin{array}{c c c} 0. 3 7 8 7 & 0. 1 1 0 5 & 0. 0 2 2 9 \\ 0. 0 0 0 0 & 0. 4 4 9 0 & 0. 0 7 3 5 \\ 0. 0 0 0 0 & 0. 0 0 0 7 & 0. 4 1 7 7 \end{array} \right]

\boldsymbol {C} _ {3} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right], \quad \boldsymbol {D} _ {3} = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right]
$$

通过 Matlab 得到 3 个开环极点，分别位于 -0.0527、-0.0863 和 -0.1482 处。

本例中，因为我们将 3 个灯管绑定为一个执行器，并且只将中央温度作为反馈信号，则系统线性模型为

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c} - 0. 0 6 8 2 & 0. 0 1 4 9 & 0. 0 0 0 0 \\ 0. 0 4 5 8 & - 0. 1 1 8 1 & 0. 0 2 1 8 \\ 0. 0 0 0 0 & 0. 0 4 6 8 3 & - 0. 1 0 0 8 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 0. 5 1 2 2 \\ 0. 5 2 2 6 \\ 0. 4 1 8 5 \end{array} \right] \\ \boldsymbol {C} = \left[ \begin{array}{l l l} 0 & 1 & 0 \end{array} \right], \quad D = [ 0 ] \\ \end{array}
$$

因此传递函数为

$$G (s) = \frac {T _ {\mathrm{y2}} (s)}{V _ {\mathrm{cmd}} (s)} = \frac {0 . 5 2 2 6 (s + 0 . 0 8 7 6) (s + 0 . 1 4 3 8)}{(s + 0 . 1 4 8 2) (s + 0 . 0 5 2 7) (s + 0 . 0 8 6 3)}$$

步骤 5 尝试超前滞后或 PID 控制器。使用如下形式的简单 PI 控制器：

$$D _ {\mathrm{c}} (s) = \frac {(s + 0 . 0 5 2 7)}{s}$$

以消除其中一个较慢极点的影响。线性闭环响应如图 10.67a 所示，而相关的控制效果如图 10.67b 所示。系统响应跟随着控制轨迹，伴有大约 2s 的延时并且没有超调。灯管直到 75s 时才有正常的响应，并且极性变负（虚线所示），以跟踪控制温度的突然下降。系统不会出现这种情况，因为没有实时冷却系统并且灯管处于低温饱和状态。注意，在这种方式下我们并没有详述的方法可以控制温度的不均匀性。
