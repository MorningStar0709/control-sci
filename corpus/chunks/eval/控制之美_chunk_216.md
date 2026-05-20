# 非线性系统的线性化

本书中所研究的动态系统都是线性时不变系统,但在实际生活中,很多系统都是非线性的。若要使用线性系统的理论处理非线性系统,则需要将非线性系统线性化。这要用到泰勒级数展开,即一个无穷可微的函数可以展开为

$$f (x) = f \left(x _ {0}\right) + \frac {\left. \frac {\mathrm{d} f (x)}{\mathrm{d} x} \right| _ {x = x _ {0}}}{1 !} \left(x - x _ {0}\right) + \frac {\left. \frac {\mathrm{d} ^ {2} f (x)}{\mathrm{d} x ^ {2}} \right| _ {x = x _ {0}}}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots +\frac {\left. \frac {\mathrm{d} ^ {n} f (x)}{\mathrm{d} x ^ {n}} \right| _ {x = x _ {0}}}{n !} \left(x - x _ {0}\right) ^ {n} + \dots \tag {A.1}$$

当 $x$ 在 $x_0$ 附近时， $(x - x_0)$ 很小，所以高阶项的 $(x - x_0)^n \to 0 (n \geqslant 2$ 时。此时式(A.1)变为：

$$
\begin{array}{l} f (x) = f \left(x _ {0}\right) + \frac {\mathrm{d} f (x)}{\mathrm{d} x} \Bigg | _ {x = x _ {0}} \left(x - x _ {0}\right) \\ = \frac {\mathrm{d} f (x)}{\mathrm{d} x} \bigg | _ {x = x _ {0}} x + f (x _ {0}) - \frac {\mathrm{d} f (x)}{\mathrm{d} x} \bigg | _ {x = x _ {0}} x _ {0} \tag {A.2} \\ \end{array}
$$

式(A.2)是一个线性(直线)方程,其斜率为 $\frac{\mathrm{d}f(x)}{\mathrm{d}x}\bigg|_{x=x_0}$ ,截距为 $f(x_0)-\frac{\mathrm{d}f(x)}{\mathrm{d}x}\bigg|_{x=x_0}x_0$ 。式(A.2)说明使用泰勒级数展开的线性化运算省略了高阶项,这意味着 $x$ 偏离 $x_0$ 越大,线性化估计的误差就越大。例如,非线性函数 $f(x)=\sin x$ 在 $x_0=0$ 附近线性化可得

$$f (x) = f (0) + \frac {\mathrm{d} f (x)}{\mathrm{d} x} \Bigg | _ {x = 0} (x - 0) = \sin 0 + \cos 0 (x) = x \tag {A.3}$$

图A.1是 $f(x) = \sin x$ 与 $f(x) = x$ 的示意图，通过对比可以发现，在 $x$ 接近0点的时候这两条曲线非常相似。而一旦远离0点，就会产生较大的偏差。例如当 $x = \frac{\pi}{6}$ 时， $f(x) = \sin \frac{\pi}{6} = 0.5$ 。其线性化的结果是 $f(x) = x = \frac{\pi}{6}$ ，与实际结果之间的误差为 $\frac{\frac{\pi}{6} - 0.5}{0.5} \times 100\% = 4\%$ 。而当 $x = \frac{\pi}{4}$ 时，线性化后的估计结果与实际结果之间的误差为 $\frac{\frac{\pi}{4} - \sin \frac{\pi}{4}}{\sin \frac{\pi}{4}} \times 100\% = 11\%$ 。

![](image/29f2e3519e7f09332e4366ab5463d3986f2884e5fa44b3d7f82d7f429788eaaf.jpg)

<details>
<summary>text_image</summary>

f(x)
x
sinx
O
x
</details>

图A.1 $f(x) = \sin x$ 与 $f(x) = x$ 在0点附近的对比图

对于非线性的动态系统,一般要求在平衡点附近对其进行线性化,考虑一个非线性系统的微分方程:

$$\frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + \frac {\mathrm{d} x (t)}{\mathrm{d} t} + \frac {1}{x (t)} = 1 \tag {A.4}$$

首先求其平衡点, 令 $\frac{\mathrm{d}^2 x(t)}{\mathrm{d} t^2} = \frac{\mathrm{d} x(t)}{\mathrm{d} t} = 0$ , 得到 $x_{\mathrm{f}} = 1$ , 在平衡点附近时 $x(t)$ 可以表达为: $x(t) = x_{\mathrm{f}} + x_{\delta}(t)$ 。将非线性项 $f(x(t)) = \frac{1}{x(t)}$ 用泰勒级数在 $x_{\mathrm{f}}$ 附近展开可得
