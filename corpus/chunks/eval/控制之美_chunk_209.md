$$
\boldsymbol {L} = \left[ \begin{array}{l} l _ {1} \\ l _ {2} \end{array} \right] \tag {10.4.10}
$$

此时

$$
\mathbf {A} - \mathbf {L C} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 0. 5 \end{array} \right] - \left[ \begin{array}{l} l _ {1} \\ l _ {2} \end{array} \right] [ 1 \quad 0 ] = \left[ \begin{array}{c c} - l _ {1} & 1 \\ - 1 - l _ {2} & - 0. 5 \end{array} \right] \tag {10.4.11}
$$

令 $|A-\lambda I|=0$ ，可以求 $(A-LC)$ 的特征值，得到

$$
\left| \begin{array}{c c} - l _ {1} - \lambda & 1 \\ - 1 - l _ {2} & - 0. 5 - \lambda \end{array} \right| = 0 \tag {10.4.12a}
$$

即

$$
(- l _ {1} - \lambda) (- 0. 5 - \lambda) - (1) \times (- 1 - l _ {2}) = 0
$$

$$
\Rightarrow \lambda^ {2} + (0. 5 + l _ {1}) \lambda + 0. 5 l _ {1} + 1 + l _ {2} = 0 \tag {10.4.12b}
$$

若希望观测器准确估计系统状态变量,则需要令 $(A-LC)$ 的特征值实部为负数。可以令 $\lambda_{1,2}=-1$ ,其对应的特征方程为

$$
(\lambda + 1) (\lambda + 1) = 0
$$

$$
\Rightarrow \lambda^ {2} + 2 \lambda + 1 = 0 \tag {10.4.13}
$$

对比式(10.4.12b)和式(10.4.13)，可得

$$
\left\{ \begin{array}{l} 0. 5 + l _ {1} = 2 \\ 0. 5 l _ {1} + 1 + l _ {2} = 1 \end{array} \right.
$$

$$
\Rightarrow \left\{ \begin{array}{l} l _ {1} = 1. 5 \\ l _ {2} = - 0. 7 5 \end{array} \right. \tag {10.4.14}
$$

将式(10.4.14)代入式(10.4.5)，可以得到观测器的表达式，即

$$
\frac {\mathrm{d} \hat {z} (t)}{\mathrm{d} t} = (\mathbf {A} - \mathbf {L C}) \hat {z} (t) + (\mathbf {B} - \mathbf {L D}) \mathbf {u} (t) + \mathbf {L y} (t)
$$

$$
= \left[ \begin{array}{c c} - 1. 5 & 1 \\ - 0. 2 5 & - 0. 5 \end{array} \right] \hat {\boldsymbol {z}} (t) + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u} (t) + \left[ \begin{array}{c} 1. 5 \\ - 0. 7 5 \end{array} \right] \boldsymbol {y} (t) \tag {10.4.15}
$$

为验证观测器的效果,设计如下测试:令系统的初始状态 $z(0)=\begin{bmatrix}z_{1}(0)\\z_{2}(0)\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix}$ ,它的物理意义是在初始状态时质量块的位置为 $z_{1}(0)=1m$ ,同时初速度 $z_{2}(0)=1m/s$ 。同时考虑无输入条件,即 $u(t)=0$ 。在此情况下,由于没有外力,质量块最终会停止下来。观测器的初始估计值可以设定为 $\hat{z}(0)=\begin{bmatrix}\hat{z}_{1}(0)\\\hat{z}_{2}(0)\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}$ 。测试结果如图 10.4.3 所示,其中,图 10.4.3(a)表示 $z_{1}(t)$ 与 $\hat{z}_{1}(t)$ 的对比,图 10.4.3(b)表示 $z_{2}(t)$ 与 $\hat{z}_{2}(t)$ 的对比。可见观测器可以准确地估计出实际的状态值。

![](image/78ebb602930c60c7466670cb31b87eb1bb55f9e814e1db9adb5565c41f7f4e25.jpg)  
(a) $z_{1}(t)$ 与 $\hat{z}_1(t)$ 的对比

![](image/c82649cc2e579ba5d99c9a086acdd9fd293b89f2dbeb804bccf4e51e270ce508.jpg)  
(b) $z_{2}(t)$ 与 $\hat{z}_{2}(t)$ 的对比  
图 10.4.3 估计值与实际值对比

线性观测器内容请扫描此二维码观看。

![](image/2172cf97d806389637974269cfb391cbaf3305df7e231498dc433c5bd6164aaf.jpg)
