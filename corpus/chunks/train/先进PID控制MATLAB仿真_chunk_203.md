# 2.12.1 基本原理

可通过扫频测试得到对象的传递函数，假设模型为 $G_{\mathrm{p}}(s)$ ，如图 2-40 所示。

设开环系统输入指令信号为

$$u (t) = A _ {m} \sin (\omega t) \tag {2.32}$$

式中， $A_{m}$ 、 $\omega$ 分别为输入信号的幅度和角速度。

假设开环系统是线性的，则其位置输出可表示为：

$$
\begin{array}{l} y (t) = A _ {\mathrm{f}} \sin (\omega t + \varphi) \\ = A _ {\mathrm{f}} \sin (\omega t) \cos (\varphi) + A _ {\mathrm{f}} \cos (\omega t) \sin \varphi \tag {2.33} \\ = \left[ \sin (\omega t) \quad \cos (\omega t) \right] \left[ \begin{array}{l} A _ {\mathrm{f}} \cos \varphi \\ A _ {\mathrm{f}} \sin \varphi \end{array} \right] \\ \end{array}
$$

![](image/f990b6530ac84d0abd84b20c7b5cc9d7f2584e505d2aa664bbe2ae1b2ed075db.jpg)  
图 2-40 开环传递函数测试框图

式中， $A_{f}$ 、 $\varphi$ 分别为开环系统输出的幅度和相位。

在时间域上取 $t=0, h, 2h, \cdots, nh$ ，并设

$$
\boldsymbol {Y} ^ {\mathrm{T}} = \left[ \begin{array}{c c c c} y (0) & y (h) & \dots & y (n h) \end{array} \right]

\boldsymbol {\Psi} ^ {\mathrm{T}} = \left[ \begin{array}{l l l l} \sin (w 0) & \sin (w h) & \dots & \sin (w n h) \\ \cos (w 0) & \cos (w h) & \dots & \cos (w n h) \end{array} \right] \tag {2.34}
c _ {1} = A _ {\mathrm{f}} \cos \varphi , c _ {2} = A _ {\mathrm{f}} \sin \varphi
$$

由式（2.32）和（2.33）得

$$
\boldsymbol {Y} = \boldsymbol {\Psi} \cdot \left[ \begin{array}{l} c _ {1} \\ c _ {2} \end{array} \right] \tag {2.35}
$$

由式（2.35），根据最小二乘原理，可求出 $c_{1}$ 、 $c_{2}$ 的最小二乘解为

$$
\left[ \begin{array}{l} \hat {c} _ {1} \\ \hat {c} _ {2} \end{array} \right] = \left(\boldsymbol {\Psi} ^ {\mathrm{T}} \boldsymbol {\Psi}\right) ^ {- 1} \boldsymbol {\Psi} ^ {\mathrm{T}} \boldsymbol {Y} \tag {2.36}
$$

根据测得的 $\hat{c}_{1}$ 和 $\hat{c}_{2}$ ，输出信号的振幅和相位估计值如下：

$$\hat {A} _ {\mathrm{f}} = \sqrt {\hat {c} _ {1} ^ {2} + \hat {c} _ {2} ^ {2}} \tag {2.37}\hat {\varphi} = \arctan \left(\frac {\hat {c} _ {2}}{\hat {c} _ {1}}\right) \tag {2.38}$$

相频为输出信号与输入信号相位之差，幅频为稳态输出振幅与输入振幅之比的分贝表示。由于输入信号 $u(t)=A_{\mathrm{m}}\sin(\omega t)$ 的相移为零，则开环传递函数的相频和幅频估计值为：

$$\hat {\varphi} _ {\mathrm{e}} = \varphi_ {\text {out}} - \varphi_ {\text {in}} = \hat {\varphi} - 0 = \arctan^ {- 1} \left(\frac {\hat {c} _ {2}}{\hat {c} _ {1}}\right) \tag {2.39}\hat {M} = 2 0 \lg \left(\frac {\hat {A} _ {\mathrm{f}}}{A _ {\mathrm{m}}}\right) = 2 0 \lg \left(\frac {\sqrt {\hat {c} _ {1} ^ {2} + \hat {c} _ {2} ^ {2}}}{A _ {\mathrm{m}}}\right) \tag {2.40}$$

在待测量的频率段取角频率序列 $\left\{\omega_{i}\right\}$ ， $i=0,1,\cdots,n$ ，对每个角频率点，用上面方法计算相频和幅频，就可得到开环传递函数的频率特性数据，从而得到模型的传递函数。

![](image/f2483e990398eeece53a077441efb05ab4dfd7a10a6abcca66114a69eab7885e.jpg)
