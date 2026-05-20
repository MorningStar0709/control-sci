# 4. PID 数字控制器的实现

在数字校正装置 $D(z)$ 的实现方法中，常采用PID数字控制器。PID控制器的传递函数为

$$D (s) = \frac {U (s)}{X (s)} = K _ {1} + \frac {K _ {2}}{s} + K _ {3} s$$

将其中的微分项和积分项进行离散化处理, 就可以确定 PID 控制器的数字实现。

对微分项,应用向后差分法,有

$$u (k T) = \frac {\mathrm{d} x}{\mathrm{d} t} \Big | _ {t = k T} = \frac {1}{T} \{x (k T) - x [ (k - 1) T ] \}$$

上式的 $z$ 变换为

$$U (z) = \frac {(1 - z ^ {- 1})}{T} X (z) = \frac {z - 1}{T z} X (z)$$

对积分项,同样有

$$u (k T) = u [ (k - 1) T ] + T x (k T)$$

上式的 $z$ 变换为

$$U (z) = z ^ {- 1} U (z) + T X (z)$$

整理得

$$U (z) = \frac {T z}{z - 1} X (z)$$

因此，PID控制器在 $z$ 域的传递函数为

$$D (z) = \frac {U (z)}{X (z)} = K _ {1} + K _ {2} \frac {T z}{z - 1} + K _ {3} \frac {z - 1}{T z}$$

若记 $x(kT) = x(k)$ ，则可得PID控制器的差分方程：

$$
\begin{array}{l} u (k) = K _ {1} x (k) + K _ {2} [ u (k - 1) + T x (k) ] + \frac {K _ {3}}{T} [ x (k) - x (k - 1) ] \\ = \left[ K _ {1} + K _ {2} T + \frac {K _ {3}}{T} \right] x (k) - \frac {K _ {3}}{T} x (k - 1) + K _ {2} u (k - 1) \\ \end{array}
$$

采用计算机软件,可以方便地实现上述 PID 数字控制器。显然,令 $K_{2}$ 或 $K_{3}$ 分别为零,可得 PD 或 PI 数字控制器。
