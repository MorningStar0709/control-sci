若 $\Gamma_{G}$ 曲线和 $-\frac{1}{N(A)}$ 曲线有交点，表明式(8-84)有 $\omega$ 的正实数解，则系统存在着无外作用下的周期运动，对应于相平面分析中的极限环，这种情况下系统的稳定性和所具有的周期运动的稳定性必须另行分析。

(3) 非线性系统存在周期运动时的稳定性分析

当 $\Gamma_{G}$ 曲线和 $-\frac{1}{N(A)}$ 曲线有交点时，式(8-85)成立，即有

$$\mid G (\mathrm{j} \omega) \mid = \left| \frac {1}{N (A)} \right|, \quad \underline {{{/ G (\mathrm{j} \omega)}}} = - \pi - \underline {{{/ N (A)}}} \tag {8-86}$$

或

$$\operatorname{Re} [ G (\mathrm{j} \omega) N (A) ] = - 1, \quad \operatorname{Im} [ G (\mathrm{j} \omega) N (A) ] = 0 \tag {8-87}$$

![](image/74a0583eb7723cad705d82c947c87f73a21887b251f536098ff5f1d87b8a06cf.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -11 | -1.5 |
| -10 | -1.0 |
| -8 | 0.0 |
| -6 | 0.5 |
| -4 | 1.0 |
| -2 | 1.0 |
| 0 | 0.0 |
</details>

MATLAB 文本：

$$
\begin{array}{l} \mathrm{G} = \mathrm{zpk} ([ ], [ 0 - 1 - 0. 2 5 ], 2. 5); \\ \mathrm{A} = 0; 0. 0 1; \mathrm{le} 3; \mathrm{k} = 0. 5; \mathrm{M} = 1; \mathrm{NA} 1 = - 1. / (\mathrm{k} + (4. \\ * \mathrm{M} / (\mathrm{pi}. * \mathrm{A}))); \\ \mathrm{x} = \text { real } (\mathrm{NA1}); \mathrm{y} = \text { imag } (\mathrm{NA1}); \text { plot } (\mathrm{x}, \mathrm{y}); \text { hold   on }; \\ \mathrm{w} = 1 \mathrm{e} - 3: 0. 0 1: 1 0 0; \text { nyquist } (\mathrm{G}, \mathrm{w}); \text { axis } ([ - 1 2 0. 5 \\ - 1. 5 1. 5 ]) \\ \end{array}
$$

图 8-46 例 8-5 系统稳定性分析(MATLAB)

由上两式可解得交点处的频率 $\omega$ 和幅值 A。系统处于周期运动时，非线性环节的输入近似为等幅振荡

$$x (t) = A \sin \omega t$$

即每一个交点对应着一个周期运动。如果该周期运动能够维持，即在外界小扰动作用下使系统偏离该周期运动，而当该扰动消失后，系统的运动仍能恢复原周期运动，则称为稳定的周期运动。图8-47给出了非线性系统存在周期运动的四种形式。图中 $\Gamma_G$ 曲线和 $-\frac{1}{N(A)}$ 的交点为 $N_0 = -\frac{1}{N(A_0)}$ ，负倒描述函数上的一点 $N_i$ 对应的幅值为 $A_i$ 。

对于图 8-47(a) 所示系统, 设系统周期运动的幅值为 $A_0$ 。当外界扰动使非线性环节输入振幅减小为 $A_1$ 时, 由于 $\Gamma_G$ 曲线包围 $\left(-\frac{1}{N(A_1)}, j0\right)$ 点, 系统不稳定, 振幅将增大, 最终回到 $N_0$ 点;

当外界扰动使输入振幅增大为 $A_{2}$ ，由于 $\Gamma_{G}$ 曲线不包围 $\left(-\frac{1}{N(A_2)}, j0\right)$ 点，系统稳定，振幅将衰减，最终也将回到 $N_{0}$ 点。这说明 $N_{0}$ 点对应的周期运动是稳定的。

![](image/24648f78ced5f502bc343542ecf8c472c2748b97c86b05fc7f2d3f1ae6310e9b.jpg)

<details>
<summary>text_image</summary>

-\frac{1}{N(A)} G(j\omega)\nN_2\nN_0 N_1 0\n\omega
</details>

(a)

![](image/6b21dab0a1f91fde21a18019ca8e8d4374a57e13abefae14c492008e47d1121d.jpg)

<details>
<summary>text_image</summary>

-\frac{1}{N(A)} G(j\omega)\nN_1 N_0 N_2 0\n\omega
</details>

(b)
