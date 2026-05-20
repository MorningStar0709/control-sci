$$
\Rightarrow K = - \frac {s ^ {2} + \omega_ {\mathrm{n}} ^ {2}}{2 \omega_ {\mathrm{n}} s} \tag {8.2.8}
$$

在式(8.2.8)中,可以认为 K 是以 s 为自变量的函数,其中, $s=\sigma+j\omega$ 是一个复数。当 s 位于实轴时 $(j\omega=0)$ ,K 就是以 $\sigma$ 为自变量的一个函数。式(8.2.8)可以写成

$$
K (\sigma) = - \frac {\sigma^ {2} + \omega_ {\mathrm{n}} ^ {2}}{2 \omega_ {\mathrm{n}} \sigma} \tag {8.2.9}
$$

求 $K(\sigma)$ 的极值，令

$$
\frac {\mathrm{d} K (\sigma)}{\mathrm{d} \sigma} = 0 \tag {8.2.10}
$$

满足式(8.2.10)的 $\sigma$ 就是汇合点, 这是因为此时 $\sigma$ 代表了 $s$ 在实轴上的极限位置。将式(8.2.9)代入式(8.2.10), 可得

$$
\begin{array}{l} \frac {\mathrm{d} \left(- \frac {\sigma^ {2} + \omega_ {\mathrm{n}} ^ {2}}{2 \omega_ {\mathrm{n}} \sigma}\right)}{\mathrm{d} \sigma} = 0 \\ \Rightarrow \frac {2 \sigma \left(2 \omega_ {\mathrm{n}} \sigma\right) - \left(\sigma^ {2} + \omega_ {\mathrm{n}} ^ {2}\right) 2 \omega_ {\mathrm{n}}}{\left(- 2 \omega_ {\mathrm{n}} \sigma\right) ^ {2}} = 0 \\ \Rightarrow \sigma = \pm \omega_ {\mathrm{n}} \tag {8.2.11a} \\ \end{array}
$$

根据图8.2.10，汇合点在虚轴的左边，所以取 $\sigma = -\omega_{\mathrm{n}}$ 。将其代入式(8.2.9)，可得

$$
K (\sigma = - \omega_ {\mathrm{n}}) = - \frac {(- \omega_ {\mathrm{n}}) ^ {2} + \omega_ {\mathrm{n}} ^ {2}}{2 \omega_ {\mathrm{n}} (- \omega_ {\mathrm{n}})} = 1 \tag {8.2.11b}
$$

式(8.2.11b)说明实轴上的汇合点位置在 $\sigma = -\omega_{\mathrm{n}}$ 上, 此时 $K = 1$ 。根据前面的定义, $K$ 就是二阶系统的阻尼比, 即 $K = \zeta$ 。如图8.2.10所示, 当 $K = \zeta = 0$ 时, 闭环传递函数有两个纯虚数根, 对应无阻尼二阶系统。当 $1 > K = \zeta > 0$ 时, 闭环传递函数有两个共轭的复数根, 对应于欠阻尼系统。当 $K = 1$ 时, 对应于临界阻尼系统。当 $K = \zeta > 1$ 时, 闭环传递函数有两个实根, 对应于过阻尼系统。

通过上述例子,我们将二阶系统的时域响应(第5章)、系统稳定性分析(第6章)及本章的根轨迹分析结合起来,请读者将上述分析与图6.2.2及图5.3.4进行比较思考。

分离点的计算方法和分析与汇合点一样, 故不再赘述。值得注意的是, 在分析分离/汇合点时, 关注的重点应该放在 $K$ 的取值上, 即 $K$ 等于多少的时候闭环传递函数的极点会进入(离开)实轴。当闭环传递函数的极点存在共轭复数根的时候, 系统将会产生振动。在掌握了分离/汇合点的信息后, 就可以调节增益避免或利用系统的振动。

根轨迹内容请扫描此二维码观看。
