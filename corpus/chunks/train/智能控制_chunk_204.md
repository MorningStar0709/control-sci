# (3) 加权平均法

工业控制中广泛使用的反模糊方法为加权平均法,输出值由下式决定

$$v _ {\mathrm{o}} = \frac {\sum_ {i = 1} ^ {m} v _ {i} k _ {i}}{\sum_ {i = 1} ^ {m} k _ {i}} \tag {4.8}$$

式中，系数 $k_{i}$ 的选择根据实际情况而定。不同的系数决定系统具有不同的响应特性。当系数 $k_{i}$ 取隶属度 $\mu_v(v_i)$ 时，就转化为重心法。

反模糊化方法的选择与隶属度函数形状的选择、推理方法的选择相关。Matlab 提供 5 种反模糊化方法: ①centroid, 面积重心法; ②bisector, 面积等分法; ③mom, 最大隶属度平均法; ④som, 最大隶属度取小法; ⑤lom, 最大隶属度取大法。在 Matlab 中, 可通过 setfis() 设置反模糊化方法, 通过 defuzz() 执行反模糊化运算。

例如，重心法通过下例程序来实现：

$$
\begin{array}{l} \mathrm{x=-10:1:10;} \\ \mathrm{mf=trapmf(x,-10,-8,-4,7]}); \\ \mathrm{xx=defuzz(x,mf,'centroid')}; \end{array}
$$

在模糊控制中,重心法可通过下例语句来设定:

$$a 1 = \text { setfis } (a, ^ {\prime} D e f u z z M e t h o d ^ {\prime}, ^ {\prime} c e n t r o i d ^ {\prime})$$

其中，a 为模糊规则库。
