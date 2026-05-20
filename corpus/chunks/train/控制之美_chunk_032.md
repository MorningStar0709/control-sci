![](image/25844fb5f7d11bd551a0fe7a551cc8daa25f22810ea90dc86ae6412e3e0eca22.jpg)

<details>
<summary>line</summary>

| t | u(t) |
| --- | --- |
| ΔT | 1/ΔT |
</details>

(a)

![](image/8c2266762a3c7757e08f48aa324c8fcd384b82d1b42de8e7b5fde922ef4cd9bd.jpg)

<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 0 |
| Peak | hΔ(t) |
| End | ~0 |
</details>

(b)   
图 2.1.4 单位脉冲方波及其响应

当 $\delta_{\Delta}(t)$ 作用在上述弹簧系统上时, 系统对其响应如图 2.1.4(b) 所示, 定义为 $h_{\Delta}(t)$ 。根据线性时不变系统的性质, 如果系统的输入是 $A\delta_{\Delta}(t-T)$ (它代表 A 倍单位面积的 $\delta_{\Delta}(t)$ 在延迟了 T 之后作用到系统中), 则系统的输出是 $Ah_{\Delta}(t-T)$ 。

如图2.1.5所示， $u_{0}(t), u_{1}(t)$ 和 $u_{2}(t)$ 中分别包含的面积为 $A_{0}, A_{1}$ 和 $A_{2}$ 。以 $A_{2}$ 为例，它的高是连续函数 $u(t)$ 在 $2\Delta T$ 时刻的值 $u(2\Delta T)$ ，宽是 $\Delta T$ ，可得

$$A _ {2} = u (2 \Delta T) \Delta T \tag {2.1.3}$$

同时， $u_{2}(t)$ 作用在系统的时间延迟了 $2\Delta T$ ，因此

$$u _ {2} (t) = u (2 \Delta T) \Delta T \delta_ {\Delta} (t - 2 \Delta T) \tag {2.1.4}$$

![](image/7836f264b36b208040426d7a3d8690745ff292b09982baef1ea2c8b29ac1d5ac.jpg)

<details>
<summary>text_image</summary>

u(t)
u(2ΔT)
A₂
A₁
δₐ(t),面积为1
O
ΔT
t
</details>

图 2.1.5 单位冲激函数和冲激响应

动态系统对于式(2.1.4)的响应为

$$x _ {2} (t) = u (2 \Delta T) \Delta T h _ {\Delta} (t - 2 \Delta T) \tag {2.1.5}$$

式(2.1.5)说明 $x_{2}(t)$ 是扩大了 $A_{2}=u(2\Delta T)\Delta T$ 倍且延迟了 $2\Delta T$ 的响应 $h_{\Delta}(t)$ 。

同理,可以得到 $u_{0}(t)$ 和 $u_{1}(t)$ 及其对应的输出,分别为

$$
\left\{ \begin{array}{l} u _ {0} (t) = u (0) \Delta T \delta_ {\Delta} (t) \\ u _ {1} (t) = u (\Delta T) \Delta T \delta_ {\Delta} (t - \Delta T) \end{array} \right. \tag {2.1.6}

\left\{ \begin{array}{l} x _ {0} (t) = u (0) \Delta T h _ {\Delta} (t) \\ x _ {1} (t) = u (\Delta T) \Delta T h _ {\Delta} (t - \Delta T) \end{array} \right. \tag {2.1.7}
$$

将式 $(2.1.5)$ 和式 $(2.1.7)$ 代入式 $(2.1.1)$ ，得到

$$x (t) = u (0) \Delta T h _ {\Delta} (t) + u (\Delta T) \Delta T h _ {\Delta} (t - \Delta T) + u (2 \Delta T) \Delta T h _ {\Delta} (t - 2 \Delta T)$$

即

$$x (t) = \sum_ {i = 0} ^ {2} u (i \Delta T) \Delta T h _ {\Delta} (t - i \Delta T) \tag {2.1.8}$$

现在将图 2.1.2(a) 中的划分间隔 $\Delta T$ 缩小, 将其划成 $(n+1)$ 个小区域块, 则式 (2.1.8) 可以写成

$$x (t) = \sum_ {i = 0} ^ {n} u (i \Delta T) \Delta T h _ {\Delta} (t - i \Delta T) \tag {2.1.9}$$

式(2.1.9)是卷积的离散表达形式。令 $\Delta T \rightarrow 0$ ，便可以得到卷积的连续表达形式。根据积分的定义，可得
