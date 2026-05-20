# 3. 开环幅相曲线

根据系统开环频率特性的表达式,可以通过取点、计算和作图等方法绘制系统开环幅相曲线。这里着重介绍结合工程需要,绘制概略开环幅相曲线的方法。

概略开环幅相曲线应反映开环频率特性的三个重要因素：

1) 开环幅相曲线的起点 $(\omega=0_{+})$ 和终点 $(\omega=\infty)$ 。  
2）开环幅相曲线与实轴的交点。设 $\omega = \omega_{x}$ 时， $G(\mathrm{j}\omega_x)H(\mathrm{j}\omega_x)$ 的虚部为

$$\operatorname{Im} \left[ G \left(\mathrm{j} \omega_ {x}\right) H \left(\mathrm{j} \omega_ {x}\right) \right] = 0 \tag {5-48}$$

或

$$\varphi \left(\omega_ {x}\right) = \underline {{{G \left(j \omega_ {x}\right) H \left(j \omega_ {x}\right)}}} = k \pi ; \quad k = 0, \pm 1, \pm 2, \dots \tag {5-49}$$

称 $\omega_{x}$ 为穿越频率,而开环频率特性曲线与实轴交点的坐标值为

$$\operatorname{Re} \left[ G \left(\mathrm{j} \omega_ {x}\right) H \left(\mathrm{j} \omega_ {x}\right) \right] = G \left(\mathrm{j} \omega_ {x}\right) H \left(\mathrm{j} \omega_ {x}\right) \tag {5-50}$$

3) 开环幅相曲线的变化范围(象限、单调性)。开环系统典型环节分解和典型环节幅相曲线的特点是绘制概略开环幅相曲线的基础,下面结合具体的系统加以介绍。

例 5-1 某 0 型单位反馈系统

$$G (s) = \frac {K}{(T _ {1} s + 1) (T _ {2} s + 1)}; \quad K, T _ {1}, T _ {2} > 0$$

试概略绘制系统开环幅相曲线。

解 由于惯性环节的角度变化为 $0^{\circ} \sim -90^{\circ}$ , 故该系统开环幅相曲线

起点： $A(0) = K,\varphi (0) = 0^{\circ}$

终点： $A(\infty) = 0, \varphi (\infty) = 2 \times (-90^{\circ}) = -180^{\circ}$

系统开环频率特性

$$G (\mathrm{j} \omega) = \frac {K [ 1 - T _ {1} T _ {2} \omega^ {2} - \mathrm{j} (T _ {1} + T _ {2}) \omega ]}{(1 + T _ {1} ^ {2} \omega^ {2}) (1 + T _ {2} ^ {2} \omega^ {2})}$$

令 $\operatorname{Im} G(\mathrm{j}\omega_r) = 0$ ，得 $\omega_r = 0$ ，即系统开环幅相曲线除在 $\omega = 0$ 处外与实轴无交点。

由于惯性环节单调地从 $0^{\circ}$ 变化至 $-90^{\circ}$ ，故该系统幅相曲线的变化范围为第 IV 和第 III 象限，系统概略开环幅相曲线如图 5-18 实线所示。

若取 K<0，由于非最小相位比例环节的相角恒为 $-180^{\circ}$ ，故此时系统概略开环幅相曲线由原曲线绕原点顺时针旋转 $180^{\circ}$ 而得，如图 5-18 中虚线所示。

例 5-2 设系统开环传递函数为

$$G (s) H (s) = \frac {K}{s (T _ {1} s + 1) (T _ {2} s + 1)}; \quad K, T _ {1}, T _ {2} > 0$$

试绘制系统概略开环幅相曲线。

解 系统开环频率特性

$$
\begin{array}{l} G (\mathrm{j} \omega) H (\mathrm{j} \omega) = \frac {K (1 - \mathrm{j} T _ {1} \omega) (1 - \mathrm{j} T _ {2} \omega) (- \mathrm{j})}{\omega \left(1 + T _ {1} ^ {2} \omega^ {2}\right) \left(1 + T _ {2} ^ {2} \omega^ {2}\right)} \\ = \frac {K \left[ - \left(T _ {1} + T _ {2}\right) \omega + j \left(- 1 + T _ {1} T _ {2} \omega^ {2}\right) \right]}{\omega \left(1 + T _ {1} ^ {2} \omega^ {2}\right) \left(1 + T _ {2} ^ {2} \omega^ {2}\right)} \\ \end{array}
$$

![](image/c4546e8c7ec03839c218c1febf3d7c800e824cdad6711d601cde7f4093fcce0b.jpg)

<details>
<summary>other</summary>
