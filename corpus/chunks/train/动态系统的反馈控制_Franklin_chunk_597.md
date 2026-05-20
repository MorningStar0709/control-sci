# 例 9.12 具有滞环非线性的继电器的描述函数

考虑图 9.29a 所示的具有滞环非线性的继电器函数。求出此非线性的描述函数。

![](image/9aceff27fd4738e860d79d0ec6ce6fc97f0afa7be57b4dc1aacc58a87d57ce62.jpg)

<details>
<summary>text_image</summary>

u○→
N
y
-h O h u
-N
○ y
</details>

a）滞环非线性

![](image/94f36852ea6ec8c743ab9da76895f1e956d77d9690827b1352c366e6585d418b.jpg)

<details>
<summary>line</summary>

| t | u |
| --- | --- |
| 0 | -N |
| t₁ | u |
| t₂ | u |
</details>

b）非线性的输入与输出   
图 9.29

解答。具有滞环的系统倾向于停留在它当前的状态。若不知道输出的历史值，则只有等到符号函数的输入超过值 h 时，才能唯一地确定输出值。这意味着非线性是带记忆的。只要输入幅值 a 比滞后阈值 h 大，输出就是幅值 N 的方波。从图 9.29b 可以看出，方波在时间上滞后于输入。滞后的时间可以用下式计算：

$$a \sin (\omega t) = h \quad \text {或} \quad \omega t = \arcsin (\frac {h}{a}) \tag {9.31}$$

因为对于所有频率相角都是已知的，有

$$
\begin{array}{l} K _ {\mathrm{eq}} (a) = \frac {4 N}{\pi a} \angle - \arcsin (\frac {h}{a}) = \frac {4 N}{\pi a} \mathrm{e} ^ {- \mathrm{j} \arcsin (\frac {h}{a})} (9.32) \\ = \frac {4 N}{\pi a} \left(\sqrt {1 - (\frac {h}{a}) ^ {2}} - j \frac {h}{a}\right) (9.33) \\ \end{array}
$$

描述函数为

$$
K _ {\mathrm{eq}} (a) = \left\{ \begin{array}{l l} \frac {4 N}{\pi a} \left(\sqrt {1 - \left(\frac {h}{a}\right) ^ {2}} - \mathrm{j} \frac {h}{a}\right), & a \geqslant h \\ 0, & a <   h \end{array} \right. \tag {9.34}
$$

图 9.30 画出了描述函数。幅值和输入信号幅值的倒数成比例，相角在 $-90^{\circ}$ 到 $0^{\circ}$ 间变化。

![](image/b0dd3e1f46f0eac7bc9b96aa9020c276d2d2ab57dd74353bc8c63d55d29a8a8c.jpg)  
a）幅值

![](image/ab26e54f5c9dc6bcc455d4eb2f432c964be31f9cf6294e59196e78028e441882.jpg)

<details>
<summary>line</summary>

| a | ∠K_eq (°) |
| --- | --- |
| 0.1 | -80 |
| 0.2 | -40 |
| 0.3 | -20 |
| 0.4 | -10 |
| 0.5 | -5 |
| 0.6 | -2 |
| 0.7 | -1 |
| 0.8 | -0.5 |
| 0.9 | -0.2 |
| 1.0 | 0 |
</details>

b）相位  
图 9.30 h=0.1, N=1 时滞环非线性的描述函数
