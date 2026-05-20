$$M _ {\mathrm{p}} = \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} = \mathrm{e} ^ {\frac {\frac {a}{2 \sqrt {a K _ {\mathrm{I}}} \pi}}{\sqrt {1 - \frac {a}{4 K _ {\mathrm{I}}}}}} = \mathrm{e} ^ {\frac {- a \pi}{\sqrt {4 a K _ {\mathrm{I}} - a ^ {2}}}} \tag {7.3.15b}$$

式(7.3.15b)说明随着 $K_{\mathrm{I}}$ 的增加, 超调量 $M_{\mathrm{p}}$ 也将增加。图 7.3.2 表示了不同的 $K_{\mathrm{I}}$ 对系统输出的影响 (在此实验中选取 $G(s) = \frac{1}{s + 1}$ , 参考值 $r(t) = 1$ ), 可见积分控制很好地消除了稳态误差。

同时，图7.3.2与式(7.3.15)的结果说明了积分控制器设计中调参时的矛盾：在使用积分控制时，提高积分增益 $K_{1}$ 可以加快系统的响应速度，但与此同时，超调量也会增加。

![](image/866c527dffcdaddfddcc77b0162c0c35862fb2b8410825dc0c3bdc566028ec05.jpg)

<details>
<summary>line</summary>
