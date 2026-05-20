# 2.5.1 基本原理

相位裕度是衡量系统稳定度的一个重要指标。它是指频率的回路增益等 0dB（单位增益）时，反馈信号总的相位偏移与 $-180^{\circ}$ 的差。

相位裕度可以看作系统进入不稳定状态之前可以增加的相位变化，相位裕度越大，系统更加稳定，但同时时间响应速度减慢了，因此必须要有一个比较合适的相位裕度。经研究发现，相位裕度至少要 $45^{\circ}$ ，最好是 $60^{\circ}$ [7]。

针对具有一阶加积分形式的被控对象：

$$G (s) = \frac {K _ {\mathrm{g}}}{s \left(T _ {\mathrm{g}} s + 1\right)} = \frac {K _ {\mathrm{g}} \omega_ {\mathrm{g}}}{s \left(s + \omega_ {\mathrm{g}}\right)} \tag {2.14}$$

式中， $\omega_{g}=\frac{1}{T_{g}}$ 。

PI 控制器表示为

$$K (s) = K _ {\mathrm{p}} \left(1 + \frac {1}{T _ {\mathrm{i}} s}\right) = K _ {\mathrm{p}} \left(1 + \frac {\omega_ {\mathrm{i}}}{s}\right) \tag {2.15}$$

针对具有一阶加积分形式的被控对象具有如下频率特性：当转折频率是对称分布时，闭环系统 $K(s)G(s)$ 的相位裕度有最大值，如图2-17所示 $^{[7]}$ 。

根据图 2-17，有如下关系

$$2 \lg \omega_ {\mathrm{c}} = \lg \omega_ {\mathrm{i}} + \lg \omega_ {\mathrm{g}}$$

即

$$\frac {\omega_ {\mathrm{g}}}{\omega_ {\mathrm{c}}} = \frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{i}}} \tag {2.16}$$

令 $\alpha=\frac{\omega_{g}}{\omega_{i}}$ ，则有

$$\omega_ {\mathrm{c}} ^ {2} = \omega_ {\mathrm{g}} \omega_ {\mathrm{i}} = \omega_ {\mathrm{g}} \frac {\omega_ {\mathrm{g}}}{\alpha}, \text {即} \omega_ {\mathrm{c}} = \omega_ {\mathrm{g}} / \sqrt {\alpha} \tag {2.17}\omega_ {\mathrm{i}} = \omega_ {\mathrm{g}} / \alpha \tag {2.18}\frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{i}}} = \frac {\omega_ {\mathrm{g}} / \sqrt {\alpha}}{\omega_ {\mathrm{g}} / \alpha} = \sqrt {\alpha} \tag {2.19}$$

通过文献[7]，下面给出 $K_{\mathrm{p}}$ 的设计方法。
