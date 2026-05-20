(2) 最大超调量(Maximum Overshoot) $M_{\mathrm{p}}$ ：系统输出的最大值(峰值)减去稳态值, 再乘以 $100\%$ ，即 $M_{\mathrm{p}} = \frac{x_{\max} - x(\infty)}{x(\infty)} \times 100\%$ ，这个指标说明了系统有多大的“矫枉过正”的倾向。  
(3) 稳定时间(Settling Time) $T_{s}$ : 又称调节时间, 是指系统进入稳态的误差范围内的时间。一般就是最终状态的 $2 \%$ 以内。

在实际工程中,以上三个指标都是可以通过实验测得的。如果系统的传递函数已知,就可以直接计算这三个指标。其中:

(1) 上升时间 $T_{r}$ 。

根据定义，当 $t = T_{\mathrm{r}}$ 时， $x(T_{\mathrm{r}}) = 1$ 。将其代入式(5.3.12)，可得

$$
\begin{array}{l} 1 = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} T _ {\mathrm{r}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin \left(\omega_ {\mathrm{d}} T _ {\mathrm{r}} + \varphi\right) \\ \Rightarrow 0 = \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} T _ {\mathrm{r}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin \left(\omega_ {\mathrm{d}} T _ {\mathrm{r}} + \varphi\right) \tag {5.4.1} \\ \end{array}
$$

式(5.4.1)等号右边的前面一项 $e^{-\zeta\omega_{n}T_{r}}\sqrt{\frac{1}{1-\zeta^{2}}}\neq0$ ，所以等式成立时， $\sin(\omega_{d}T_{r}+\varphi)=0$ ，
得到

$$\omega_ {\mathrm{d}} T _ {\mathrm{r}} + \varphi = k \pi , \quad k = 1, 2, 3, \dots \tag {5.4.2a}$$

可得

$$T _ {\mathrm{r}} = \frac {k \pi - \varphi}{\omega_ {\mathrm{d}}}, \quad k = 1, 2, 3, \dots \tag {5.4.2b}$$

因为上升时间是第一次到达稳定点的时间,所以取 k=1,即

$$T _ {\mathrm{r}} = \frac {\pi - \varphi}{\omega_ {\mathrm{d}}} = \frac {\pi - \varphi}{\omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}}} \tag {5.4.3}$$

式(5.4.3)说明固有频率 $\omega_{n}$ 越大, 则上升时间 $T_{r}$ 越小, 系统的响应就越快。同时, 阻尼比 $\zeta$ 越大, 上升时间 $T_{r}$ 越大。思考一下固有频率的物理定义, $\omega_{n} = \sqrt{\frac{k}{m}}$ 是弹簧系数与质量的比值。当 $\omega_{n}$ 增大时, 弹簧系数与质量的比值就增大, 此时相当于用一个强力弹簧去拉一个小质量的物体, 它的响应速度自然就会很快。而阻尼力则相反, 阻尼增大会减缓物体的移动速度,这是因为阻尼力与速度方向相反且大小与速度成正比。

(2) 最大超调量 $M_{p}$ 。

若求解最大超调量,首先要找到系统的峰值时间(Peak Time) $T_{p}$ 。即 $x(T_{p})=x_{\max}$ , 在此时刻,有

$$
\begin{array}{l} \left. \frac {\mathrm{d} x (t)}{\mathrm{d} t} \right| _ {t = T _ {\mathrm{p}}} = 0 \\ \begin{array}{l} \Rightarrow \zeta \omega_ {\mathrm{n}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \sin (\omega_ {\mathrm{d}} t + \varphi) - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \sqrt {\frac {1}{1 - \zeta^ {2}}} \omega_ {\mathrm{d}} \cos (\omega_ {\mathrm{d}} t + \varphi) \Bigg | _ {t = T _ {\mathrm{p}}} \\ = 0 \end{array} \tag {5.4.4a} \\ \end{array}
$$

可得
