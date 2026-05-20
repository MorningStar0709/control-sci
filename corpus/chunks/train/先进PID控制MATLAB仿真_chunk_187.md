式中， $k_{\mathrm{i}}(e_{\mathrm{p}}(t)) = a_{\mathrm{i}} \operatorname{sech}(c_{\mathrm{i}} e_{\mathrm{i}}(t))$ ，为正实常数； $k_{i}$ 的取值范围为 $(0, a_{i})$ ，当 $e_{p} = 0$ 时， $k_{i}$ 取最大值； $c_{i}$ 的取值决定了 $k_{i}$ 的变化快慢程度。

非线性 PID 调节器的控制输入为

$$u (t) = k _ {\mathrm{p}} \left(e _ {\mathrm{p}} (t)\right) e _ {\mathrm{p}} (t) + k _ {\mathrm{i}} \left(e _ {\mathrm{p}} (t)\right) \int_ {0} ^ {t} e _ {\mathrm{p}} (t) \mathrm{d} t + k _ {\mathrm{d}} \left(e _ {\mathrm{p}} (t), e _ {\mathrm{v}} (t)\right) \frac {\mathrm{d} e _ {\mathrm{p}} (t)}{\mathrm{d} t} \tag {2.31}$$

由上述分析可知，如果非线性函数中的各项参数选择适当的话，能够使控制系统既达到响应快，又无超调现象。另外，由于非线性PID调节器中的增益参数能够随控制误差而变化，因而其抗干扰能力也较常规线性PID控制强。 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 变化的示意图如图2-25所示。

![](image/67b8fdf97fb984a41bbf8d01d6ab9f393ebe62dcbafe6c723997b0738bc6a237.jpg)

<details>
<summary>text_image</summary>

kp
ap
O
ep
</details>

(a) $k_{p}$ 变化曲线

![](image/6062c03791e519e42e59fa7dfb1b4cca0dc899748646b28146fc42900c0414a8.jpg)

<details>
<summary>text_image</summary>

k_d
a_d + \frac{b_d}{1 + c_d}
O
e_p
</details>

(b) $k_{d}$ 变化曲线

![](image/9fd4a8a4b30dc92aff8ca07dc58636b7ab822f421b06bb7aaaccb32a5a592c8c.jpg)

<details>
<summary>line</summary>

| e_p | k_i |
| --- | --- |
| 0 | Peak value at ap |
| >0 | Decreasing trend from peak to baseline |
</details>

(c) $k_{i}$ 变化曲线  
图 2-25 非线性增益调节参数变化曲线

![](image/f165b4ab8d7cc9a1ea86cf4abf4956fbeb2b500c13e2da60781711f969bf6c8c.jpg)
