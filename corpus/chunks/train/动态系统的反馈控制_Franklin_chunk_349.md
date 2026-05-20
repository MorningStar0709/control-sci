# 6.7.2 超前补偿

为了减小 PD 补偿环节的高频放大作用，可将一个一阶极点加到分母上，使其频率充分大于 PD 补偿环节的分离点频率。这样虽然相位增大，但是高频率处的放大作用被限制。由此而生的超前补偿的传递函数为

$$D _ {\mathrm{c}} (s) = \frac {T _ {\mathrm{D}} s + 1}{\alpha T _ {\mathrm{D}} s + 1}, \quad \alpha < 1 \tag {6.38}$$

其中： $1/\alpha$ 是极点与零点的分离点频率之比。

图 6.52 所示的是该超前补偿的频率响应。值得注意的是，超前补偿仍可提供超前的相位，但在高频段的放大作用却更小了。超前补偿器通常都可以使用，即使系统阻尼比要求大幅度提高。

![](image/d66305b131cd95fcde67653b955f5298ec56e8d37787bf2063e618b20ec95524.jpg)

![](image/a75409616b6addaf762f497a29a801022f9ca9e625ab1843027a20babe193bbf.jpg)

<details>
<summary>line</summary>

| ωT_D | ∠D_c(s) |
| --- | --- |
| 0.1 | 0° |
| 1 | 30° |
| 10 | 60° |
| 100 | 0° |
</details>

图 6.52 $1/\alpha=10$ 时超前补偿环节频率响应

加入式 $(6.38)$ 的超前补偿环节后相位为

$$\phi = \arctan (T _ {\mathrm{D}} \omega) - \arctan (\alpha T _ {\mathrm{D}} \omega)$$

(见习题 6.44) 相位取最大值时的频率值为

$$\omega_ {\mathrm{max}} = \frac {1}{T _ {\mathrm{D}} \sqrt {\alpha}} \tag {6.39}$$

最大超前相位是图 6.52 中 $\angle D_{c}(s)$ 曲线的峰值，相对应，有

$$\sin \phi_ {\max} = \frac {1 - \alpha}{1 + \alpha} \tag {6.40}$$

或

$$\alpha = \frac {1 - \sin \phi_ {\max}}{1 + \sin \phi_ {\max}}$$

另一种方法如下：在对数坐标下，最大相位的频率位于两个分离点频率（有时称转角频率）的中点，即

$$\lg \omega_ {\max} = \lg \frac {1 / \sqrt {T _ {\mathrm{D}}}}{\sqrt {\alpha T _ {\mathrm{D}}}} = \lg \frac {1}{\sqrt {T _ {\mathrm{D}}}} + \lg \frac {1}{\sqrt {\alpha T _ {\mathrm{D}}}} = \frac {1}{2} \left[ \lg \left(\frac {1}{T _ {\mathrm{D}}}\right) + \lg \left(\frac {1}{\alpha T _ {\mathrm{D}}}\right) \right] \tag {6.41}$$

如图6.52所示。或者，我们可以根据零极点的位置来确定这些结果。改写 $D_{\mathrm{c}}(s)$ 为根轨迹形式用于分析，得到

$$D _ {\mathrm{c}} (s) = \frac {s + z}{s + p} \tag {6.42}$$

习题6.44表明：

$$\omega_ {\max} = \sqrt {| z | | p |} \tag {6.43}$$

且

$$\lg \omega_ {\max} = \frac {1}{2} (\lg | z | + \lg | p |) \tag {6.44}$$

如果在式(6.39)和式(6.41)中取 $z = -1 / T_{\mathrm{D}}$ 和 $p = -1 / (\alpha T_{\mathrm{D}})$ ，这些结果与前面的是一致的。

例如，某超前补偿器在 $s = -2(T_{\mathrm{D}} = 0.5)$ 处有一个零点，在 $s = -10\left(\alpha T_{\mathrm{D}} = 0.1, \text{即} \alpha = \frac{1}{5}\right)$ 处有一个极点，该补偿的最大超前相位位于：

$$\omega_ {\max} = \sqrt {2 \times 1 0} = 4. 4 7 \mathrm{rad/s}$$

位于中点的超前相位值只依赖于式(6.40)中的 $\alpha$ ，其绘制如图6.53所示。当 $\alpha = 0.2$ 如图6.53所示 $\phi_{\mathrm{max}} = 40^{\circ}$ 。注意由图，我们可以通过使用更大的超前比 $1 / \alpha$ 的值来增大超
