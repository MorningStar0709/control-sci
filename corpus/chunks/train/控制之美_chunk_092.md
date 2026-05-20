# 5.1 二阶系统的一般形式——传递函数和状态空间方程

从一个典型的二阶系统例子入手,一个弹簧质量阻尼系统如图 5.1.1(a) 所示。其对应的微分方程为

$$m \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + b \frac {\mathrm{d} x (t)}{\mathrm{d} t} + k x (t) = f (t) \tag {5.1.1a}$$

调整可得

$$\frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + \frac {b}{m} \frac {\mathrm{d} x (t)}{\mathrm{d} t} + \frac {k}{m} x (t) = \frac {1}{m} f (t) \tag {5.1.1b}$$

定义：

固有频率或者自然频率(Natural Frequency): $\omega_{n}=\sqrt{\frac{k}{m}}$ 。

阻尼比(Damping Ratio): $\zeta=\frac{b}{2\sqrt{km}}$ 。

代入式(5.1.1b)，可得

$$\frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + 2 \zeta \omega_ {\mathrm{n}} \frac {\mathrm{d} x (t)}{\mathrm{d} t} + \omega_ {\mathrm{n}} ^ {2} x (t) = \frac {1}{m} f (t) \tag {5.1.1c}$$

为了简化计算,使系统单位化,定义系统的输入 $u(t)=\frac{f(t)}{m\omega_{n}^{2}}$ 。代入式(5.1.1c),可得

$$\frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + 2 \zeta \omega_ {\mathrm{n}} \frac {\mathrm{d} x (t)}{\mathrm{d} t} + \omega_ {\mathrm{n}} ^ {2} x (t) = \omega_ {\mathrm{n}} ^ {2} u (t) \tag {5.1.2}$$

在本章中只讨论 $m > 0, k > 0, b > 0$ 的情况，因此 $\omega_{\mathrm{n}} > 0$ 且 $\zeta > 0$ 。其他例外情况读者可以根据本章的方法去处理。

考虑零初始状态,对式(5.1.2)等号两边进行拉普拉斯变换并整理,可以得到一般形式二阶系统的传递函数,即

$$G (s) = \frac {X (s)}{U (s)} = \frac {\omega_ {\mathrm{n}} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \tag {5.1.3}$$

系统的框图如图 5.1.1(b) 所示。

![](image/2673ff98410b36e8b91aced82a788414164143d13c2465a8400339da691e8527.jpg)

<details>
<summary>text_image</summary>

k
x(t)
m
f(t)
b
</details>

(a) 弹簧质量阻尼系统

![](image/341cdb0b575c6653711743e2e3e0fc94eafb1187d4efa57fa57204c305f8c682.jpg)  
(b) 动态系统框图  
图5.1.1 弹簧质量阻尼系统与其传递函数

如果使用状态空间方程的表达形式,可以设系统的状态变量为 $z(t)=[z_{1}(t),z_{2}(t)]^{\mathrm{T}}=\left[x(t),\frac{\mathrm{d}x(t)}{\mathrm{d}t}\right]^{\mathrm{T}}$ 。得到

$$\frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = z _ {2} (t) \tag {5.1.4a}\frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = \frac {\mathrm{d} ^ {2} z _ {1} (t)}{\mathrm{d} t ^ {2}} = - 2 \zeta \omega_ {\mathrm{n}} z _ {2} (t) - \omega_ {\mathrm{n}} ^ {2} z _ {1} (t) + \omega_ {\mathrm{n}} ^ {2} u (t) \tag {5.1.4b}$$

将其写成紧凑的矩阵形式,得到

$$\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t) + B u (t)$$

其中

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ - \omega_ {\mathrm{n}} ^ {2} & - 2 \zeta \omega_ {\mathrm{n}} \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ \omega_ {\mathrm{n}} ^ {2} \end{array} \right] \tag {5.1.5}
$$
