式中 $b_{1} = -\sum_{j = 1}^{m}z_{j},\qquad a_{1} = -\sum_{i = 1}^{n}p_{i}$

当 $s$ 值很大时，式(4-12)可近似为

$$G (s) H (s) = \frac {K ^ {*}}{s ^ {n - m} + (a _ {1} - b _ {1}) s ^ {n - m - 1}}$$

由 $G(s)H(s) = -1$ 得渐近线方程

$$s ^ {n - m} \left(1 + \frac {a _ {1} - b _ {1}}{s}\right) = - K ^ {*}$$

或

$$s \left(1 + \frac {a _ {1} - b _ {1}}{s}\right) ^ {\frac {1}{n - m}} = (- K ^ {*}) ^ {\frac {1}{n - m}} \tag {4-13}$$

根据二项式定理

$$\left(1 + \frac {a _ {1} - b _ {1}}{s}\right) ^ {\frac {1}{n - m}} = 1 + \frac {a _ {1} - b _ {1}}{(n - m) s} + \frac {1}{2 !} \times \frac {1}{n - m} \left(\frac {1}{n - m} - 1\right) \left(\frac {a _ {1} - b _ {1}}{s}\right) ^ {2} + \dots$$

在 $s$ 值很大时，近似有

$$\left(1 + \frac {a _ {1} - b _ {1}}{s}\right) ^ {\frac {1}{n - m}} = 1 + \frac {a _ {1} - b _ {1}}{(n - m) s} \tag {4-14}$$

将式(4-14)代入式(4-13)，渐近线方程可表示为

$$s \Big [ 1 + \frac {a _ {1} - b _ {1}}{(n - m) s} \Big ] = (- K ^ {*}) ^ {\frac {1}{n - m}} \tag {4-15}$$

现在以 $s = \sigma +\mathrm{j}\omega$ 代入式(4-15)，得

$$\left(\sigma + \frac {a _ {1} - b _ {1}}{n - m}\right) + j \omega = \sqrt [ n - m ]{K ^ {*}} \left[ \cos \frac {(2 k + 1) \pi}{n - m} + j \sin \frac {(2 k + 1) \pi}{n - m} \right]k = 0, 1, \dots , n - m - 1$$

令实部和虚部分别相等，有

$$\sigma + \frac {a _ {1} - b _ {1}}{n - m} = \sqrt [ n - m ]{K ^ {*}} \cos \frac {(2 k + 1) \pi}{n - m}\omega = \sqrt [ n - m ]{K ^ {*}} \sin \frac {(2 k + 1) \pi}{n - m}$$

从最后两个方程中解出

$$\sqrt [ n - m ]{K ^ {*}} = \frac {\omega}{\sin \varphi_ {a}} = \frac {\sigma - \sigma_ {a}}{\cos \varphi_ {a}} \tag {4-16}\omega = (\sigma - \sigma_ {a}) \tan \varphi_ {a} \tag {4-17}$$

式中

$$\varphi_ {a} = \frac {(2 k + 1) \pi}{n - m}; \qquad k = 0, 1, \dots , n - m - 1 \tag {4-18}\sigma_ {a} = - \left(\frac {a _ {1} - b _ {1}}{n - m}\right) = \frac {\sum_ {i = 1} ^ {n} p _ {i} - \sum_ {j = 1} ^ {m} z _ {j}}{n - m} \tag {4-19}$$

在 s 平面上, 式(4-17)代表直线方程, 它与实轴的交角为 $\varphi_{a}$ , 交点为 $\sigma_{a}$ 。当 k 取不同值时, 可得 n-m 个 $\varphi_{a}$ 角, 而 $\sigma_{a}$ 不变, 因此根轨迹渐近线是 n-m 条与实轴交点为 $\sigma_{a}$ , 交角为 $\varphi_{a}$ 的一组射线, 如图 4-4 所示(图中只画了一条渐近线)。

下面举例说明根轨迹渐近线的做法。设控制系统如图4-5(a)所示，其开环传递函数

$$G (s) = \frac {K ^ {*} (s + 1)}{s (s + 4) (s ^ {2} + 2 s + 2)}$$

试根据已知的三个基本法则，确定绘制根轨迹的有关数据。

首先将开环零、极点标注在 s 平面的直角坐标系上，以“×”表示开环极点，以“○”表示开环零点，如图 4-5(b) 所示。

![](image/47a4547ea0fbbf7936f9b580a3c6704c848f456d444f3c4d0ed76ee07676e97d.jpg)

<details>
<summary>text_image</summary>

j
ωₐ = -σₐ tanφₐ
φₐ
σₐ
0
</details>

图 4-4 根轨迹渐近线

注意,在根轨迹绘制过程中,由于需要对相角和模值进行图解测量,所以横坐标与纵坐标必须采用相同的坐标比例尺。

![](image/861ae8381ea3b69e1fb7ec7b934c2a3231f7f175fee14577739182be38e7446b.jpg)
