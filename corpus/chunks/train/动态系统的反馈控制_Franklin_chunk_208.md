# 4.1.4 灵敏度

假定被控对象在运行过程中某一特定频率的增益在运行中由设定值 G 变成 $G + \delta G$ 。这个变化率用一个分数或百分数表示为 $\delta G / G$ 。为了分析，我们设定频率为 0，并让开环控制器增益设定值为 $D_{\mathrm{ol}}(0)$ 。因此，在开环情况下，系统标称总增益是 $T_{ol} = GD_{ol}$ ，加上被控对象的摄动增益，整个增益为

$$T _ {\mathrm{ol}} + \delta T _ {\mathrm{ol}} = D _ {\mathrm{ol}} (G + \delta G) = D _ {\mathrm{ol}} G + D _ {\mathrm{ol}} \delta G = T _ {\mathrm{ol}} + D _ {\mathrm{ol}} \delta G$$

因此，增益的变化是 $\delta T_{\mathrm{ol}} = D_{\mathrm{ol}}\delta G$ 。传递函数 $T_{\mathrm{ol}}$ 相对于对象增益 $G$ 的灵敏度 $S_{\mathrm{G}}^{\mathrm{T}}$ 定义为 $T_{\mathrm{ol}}$ 的变化率，即 $\frac{\delta T_{\mathrm{ol}}}{T_{\mathrm{ol}}}$ 相对于 $G$ 的变化率的比值。形式表示为

$$\mathcal {S} _ {G} ^ {T} = \frac {\frac {\delta T _ {\mathrm{ol}}}{T _ {\mathrm{ol}}}}{\frac {\delta G}{G}} \tag {4.18}= \frac {G}{T _ {\mathrm{ol}}} \frac {\delta T _ {\mathrm{ol}}}{\delta G} \tag {4.19}$$

以方程的形式代入后，我们得到

$$\frac {\delta T _ {\mathrm{ol}}}{T _ {\mathrm{ol}}} = \frac {D _ {\mathrm{ol}} \delta G}{D _ {\mathrm{ol}} G} = \frac {\delta G}{G} \tag {4.20}$$

这意味着如果 G 产生 10% 的误差，则相应的 $T_{cl}$ 也产生 10% 的误差。因此，在开环情况下，有 S=1。

由式(4.5)，在反馈情况下，G 同样地变化，则新的稳态反馈增益为

$$T _ {\mathrm{cl}} + \delta T _ {\mathrm{cl}} = \frac {(G + \delta G) D _ {\mathrm{cl}}}{1 + (G + \delta G) D _ {\mathrm{cl}}}$$

其中： $T_{cl}$ 是闭环增益。

我们直接采用微分法计算闭环增益的灵敏度。闭环稳态增益为

$$T _ {\mathrm{cl}} = \frac {G D _ {\mathrm{cl}}}{1 + G D _ {\mathrm{cl}}}$$

一阶变化正比于该方程的导数，即

$$\delta T _ {\mathrm{cl}} = \frac {\mathrm{d} T _ {\mathrm{cl}}}{\mathrm{d} G} \delta G$$

式 $(4.18)$ 中灵敏度的一般表达式为

$S_{G}^{T_{cl}} \stackrel{\mathrm{def}}{=} T_{cl}$ 相对于 G 的灵敏度

$$\mathcal {S} _ {G ^ {\mathrm{cl}}} \stackrel {\text {def}} {=} \frac {G}{T _ {\mathrm{cl}}} \frac {\mathrm{d} T _ {\mathrm{cl}}}{\mathrm{d} G} \tag {4.21}$$

于是

$$\mathcal {S} _ {G ^ {\mathrm{cl}}} ^ {T} = \frac {G}{G D _ {\mathrm{cl}} / (1 + G D _ {\mathrm{cl}})} \frac {(1 + G D _ {\mathrm{cl}}) D _ {\mathrm{cl}} - D _ {\mathrm{cl}} (G D _ {\mathrm{cl}})}{(1 + G D _ {\mathrm{cl}}) ^ {2}} = \frac {1}{1 + G D _ {\mathrm{cl}}} \tag {4.22}$$

这一结果显示出反馈的主要优势 $^{①}$ ：

在反馈控制中，与开环控制增益的误差相比，闭环传递函数增益的误差对于对象增益的变化并不敏感，是开环的 $S=\frac{1}{1+GD_{cl}}$ 倍。

如果增益满足 $1 + GD_{\mathrm{cl}} = 100$ ，且被控对象增益 $G$ 变化 $10\%$ ，则仅导致稳态增益变化 $0.1\%$ 。当闭环回路增益为100时，开环控制器对于增益变化的灵敏度是它的100倍。具有单位反馈情况的例子很常见，我们可以参照式(4.22)的结果，简记灵敏度为不带上标和下标的 $S$ 。因此，定义反馈系统的灵敏度函数为

$$\mathcal {S} \stackrel {\text { def }} {=} \frac {1}{1 + G D _ {\mathrm{cl}}} \tag {4.23}$$
