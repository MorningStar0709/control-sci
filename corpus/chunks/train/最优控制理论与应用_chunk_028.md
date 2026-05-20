# 2.1 无约束条件的函数极值问题

一元函数 $f(x)$ 在 $x = x^{*}$ 处取极值的必要条件为

$$f ^ {\prime} \left(x ^ {*}\right) = \frac {\mathrm{d} f (x)}{\mathrm{d} x} \mid_ {x = x ^ {*}} = 0 \tag {2-1}$$

当

$$f ^ {\prime \prime} \left(x ^ {*}\right) = \frac {\mathrm{d} ^ {2} f (x)}{\mathrm{d} x ^ {2}} \Bigg | _ {x = x ^ {*}} > 0 \tag {2-2}$$

时， $f(x^{*})$ 为极小。当

$$f ^ {\prime \prime} \left(x ^ {*}\right) = \frac {\mathrm{d} ^ {2} f (x)}{\mathrm{d} x ^ {2}} \Bigg | _ {x = x ^ {*}} < 0 \tag {2-3}$$

时， $f(x^{*})$ 为极大。

为简单起见,以下将只讨论极小,式(2-1)和(2-2)一起构成 $f(x^{*})$ 为极小值的充分条件。当 $f''(x^{*})=0$ 时,也可能有极小值,不过要检验高阶导数。上述情况可用图2-1来表示。R点是局部极小点,又是总体极小点,U只是局部极小点,T是局部极大点,S是拐点,不是极值点。

例2-1 求使

$$f (x) = \left(x - a _ {1}\right) ^ {2} + \left(x - a _ {2}\right) ^ {2} + \dots + \left(x - a _ {n}\right) ^ {2}$$

最小的 $x$ 。

![](image/692eb0ae3fceea85e3031354ba73582f6a7d89467ab49e5ee178e8f28d5046c8.jpg)

<details>
<summary>text_image</summary>

f(x)
S
R
T
U
O
x
</details>

图2-1 函数的极值点和拐点

解 $f^{\prime}(x) = 2(x - a_{1}) + 2(x - a_{2}) + \dots +2(x - a_{n}) = 0$

$$x = \frac {a _ {1} + a _ {2} + \cdots + a _ {n}}{n}f ^ {\prime \prime} (x ^ {*}) = 2 n > 0$$

故解 $x$ 使 $f(x)$ 达到极小。本例是著名的最小二乘问题。例如， $x$ 是某个未知的物理量， $a_i$ 是测量值。根据这些测量值可决定 $x$ ，使误差的平方和为最小。

下面考虑二元函数 $f(x_{1},x_{2})$ 的极值问题。设 $f(x_{1},x_{2})$ 在 $\pmb{X}^{*} = [x_{1}^{*}, x_{2}^{*}]^{\mathrm{T}}$ 处取得极小值，记 $f(x_{1},x_{2}) = f(X)$ ，这里 $\pmb{X} = [x_1,x_2]^{\mathrm{T}}$ （T表示转置， $\pmb{X}$ 是列向量）。 $f(\pmb{X})$ 在 $\pmb{X} = \pmb{X}^{*}$ 处取得极小值的必要条件和充分条件可如下求得。将 $f(\pmb{X})$ 在 $\pmb{X} = \pmb{X}^{*}$ 周围展开为泰勒级数

$$
\begin{array}{l} f (\boldsymbol {X}) = f \left(x _ {1}, x _ {2}\right) = f \left(x _ {1} ^ {*} + \Delta x _ {1}, x _ {2} ^ {*} + \Delta x _ {2}\right) \\ = f \left(\boldsymbol {X} ^ {*}\right) + f _ {x _ {1}} ^ {\prime} \left(\boldsymbol {X} ^ {*}\right) \Delta x _ {1} + f _ {x _ {2}} ^ {\prime} \left(\boldsymbol {X} ^ {*}\right) \Delta x _ {2} + f _ {x _ {1} x _ {1}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) \left(\Delta x _ {1}\right) ^ {2} + \\ 2 f _ {x _ {1} x _ {2}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) \Delta x _ {1} \Delta x _ {2} + f _ {x _ {2} x _ {2}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) \left(\Delta x _ {2}\right) ^ {2} + o \left[ \left(\Delta x _ {1}\right) ^ {2}, \left(\Delta x _ {2}\right) ^ {2} \right] \tag {2-4} \\ \end{array}
$$

式中
