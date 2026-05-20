所以，该项的幅值图是一条斜率为 $n \times (20\mathrm{dB} / 10$ 倍频)的直线。 $n$ 取不同的值，如图6.6所示。 $K_{\circ}(j\omega)^{n}$ 是唯一一类影响最低频率处的斜率的项，这是因为所有其他类的项在此区域均为常数。绘制这条曲线的最简单的方法就是定位频率 $\omega = 1$ 且在该频率处画出 $\lg K_{\circ}$ 。之后通过该点画斜率为 $n$ 的直线 $\ominus$ 。 $(j\omega)^{n}$ 的相位是 $\varphi = n \times 90^{\circ}$ ；它与斜率无关，因此相位曲线是一条水平直线：当 $n = -1$ 时，相位为 $-90^{\circ}$ ；当 $n = -2$ 时，相位为 $-180^{\circ}$ ；当 $n = +1$ 时，相位为 $+90^{\circ}$ 等等。

![](image/72c8503d59c23d8518ebc3b8ad771d2ccb742dc22f73b601ec644af8886d2dd3.jpg)  
图 6.6 $(j\omega)^{n}$ 的幅值

（2）对于 $(\mathrm{j}\omega t+1)$ ，该项的幅值在频率很低处趋近于一条渐近线且在频率很高处趋近于另一条渐近线。

(a) 对于 $\omega\tau\ll1,\quad j\omega\tau+1\approx1$ 。  
(b) 对于 $\omega\tau\gg1,\quad j\omega\tau+1\approx j\omega\tau$ 。

如果我们称 $\omega = 1 / \tau$ 为分离点，则我们知道分离点以下的幅值曲线近似为常数（=1），

而分离点以上的幅值曲线表现为与第一类的 $K_{0}(j\omega)^{n}$ 项相似。 $G(s)=10s+1$ 的例子画在图6.7中，该图说明了两条渐近线在分离点处是如何相交的，以及分离点处的实际的幅值曲线落在渐近线上方1.4倍（或+3dB）处。（若该项在分母上，实际曲线将在分离处的渐近线下方0.707或-3dB处）。注意，该项对分离点下方的复合幅值曲线仅有微小的影响，这是因为在该区域，它的值等于1(=0dB)。该项的幅值曲线在高频处的斜率为+1（或+20dB/10倍频）。相位曲线也可利用跟随低频和高频渐近线简单画出：

![](image/e387acdb4056f869439f6eca473b1c341a9074bc2622fe323215d69dce9064e7.jpg)  
图6.7 $\mathrm{j}\omega t + 1$ 的幅值图； $\tau = 10$

(a) 对于 $\omega\tau\ll1,\quad\angle1=0^{\circ}$   
(b) 对于 $\omega\tau\gg1,\quad\angle j\omega\tau=90^{\circ}$   
(c) 对于 $\omega\tau\approx1,\quad\angle(j\omega\tau+1)\approx45^{\circ}$

在 $\omega\tau\approx1$ 处， $\angle(j\omega+1)$ 曲线与一条渐近线相切，该渐近线从 $\omega\tau=0.2$ 处取值为 $0^{\circ}$ 运动到 $\omega\tau=5$ 处取值为 $90^{\circ}$ ，如图 6.8 所示。图中也展示了相位图的三条渐近线（虚线）并说明了实际曲线在它们的交点处偏离渐近线 $11^{\circ}$ 。这类项在低于分离点的频率处，对于复合相位与幅值曲线的影响都没有超过 10 倍，这是因为在低频段，该项的幅值是 1（或 0dB）且相位小于 $5^{\circ}$ 。

![](image/8538e2432c0b4740392a27a571b3092174434724c71ee497c27d3cef1958bd01.jpg)

<details>
<summary>line</summary>

| ω (rad/s) | ∠(ω10+1) |
| --- | --- |
| 0.02 | 0 |
| 0.1 | 50 |
| 0.4 | 90 |
</details>

图 6.8 $j\omega t+1$ 的相位图； $\tau=10$
