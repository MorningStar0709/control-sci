$$
\begin{array}{l} C (s) = D (s) N ^ {- 1} (s) P (s) \\ = D (s) \cdot N ^ {- 1} (s) \left[ \begin{array}{c c c} \beta_ {1} (s) & & \\ & \ddots & \\ & & \beta_ {p} (s) \end{array} \right] \cdot \left[ \begin{array}{c c c} \alpha_ {1} (s) & & \\ & \ddots & \\ & & \alpha_ {p} (s) \end{array} \right] ^ {- 1} \\ = D (s) \widetilde {N} ^ {- 1} (s). \left[ \begin{array}{c c c} \alpha_ {1} (s) & & \\ & \ddots & \\ & & \alpha_ {p} (s) \end{array} \right] ^ {- 1} \tag {11.214} \\ \end{array}
$$

当选取 $\alpha_{i}(s)$ ( $j=1,2,\cdots,p$ ) 为稳定多项式时是稳定的有理分式矩阵，这就为保证 $C(s)$ 的物理可实现性提供了必要的前提。进一步，考虑到在此种情况下， $C(s)$ 和 $G_{p}(s)$ 的表达式分别具有如下的形式：

$$
C (s) = \left[ \begin{array}{c c} \frac {\beta_ {1} (s) n _ {1 1} (s)}{\alpha_ {1} (s) d _ {1 1} (s)} & \dots \frac {\beta_ {p} (s) n _ {1 p} (s)}{\alpha_ {p} (s) d _ {1 p} (s)} \\ \vdots & \vdots \\ \frac {\beta_ {1} (s) n _ {p 1} (s)}{\alpha_ {1} (s) d _ {p 1} (s)} & \dots \frac {\beta_ {p} (s) n _ {p p} (s)}{\alpha_ {p} (s) d _ {p p} (s)} \end{array} \right] \tag {11.215}
$$

和

$$
G _ {P} (s) = \left[ \begin{array}{c c c} \frac {\beta_ {1} (s)}{\alpha_ {1} (s) + \beta_ {1} (s)} & & \\ & \ddots & \\ & & \frac {\beta_ {p} (s)}{\alpha_ {p} (s) + \beta_ {p} (s)} \end{array} \right] \tag {11.216}
$$

所以只要选取 $\alpha_{j}(s)$ 满足关系式：

$$\deg \alpha_ {j} (s) \geqslant \deg \beta_ {j} (s) + \max _ {i} [ \deg n _ {i j} (s) - \deg d _ {i j} (s) ] j = 1, 2, \dots , p \tag {11.217}$$

时，就可确保 $C(s)$ 和 $G_{F}(s)$ 是真的或严格真的有理分式矩阵，从而满足物理可实现性的要求。而 $\alpha_{j}(s) (j=1,2,\cdots,p)$ 的系数，则可根据对解耦后单输入一单输出系统

$$g _ {i} (s) = \frac {\beta_ {i} (s)}{\alpha_ {i} (s) + \beta_ {i} (s)}, j = 1, 2, \dots , p \tag {11.218}$$

的期望性能指标来加以确定,其中最常用的期望性能指标即为期望的闭环极点组。但是,需要指出,此种情况下得到的 $g_{i}(s)$ 是非最小相的,这不能不说是一个重要的缺点。

几点讨论 下面,我们就解耦控制问题的上述输出反馈方案,作如下的几点讨论。

（1）实现解耦控制的上述方案的实质是采用直接的零点一极点对消。用补偿器 $C(s)$ 的一部分极点即 $\det N(s) = 0$ 的根去对消掉受控系统 $G_{\bullet}(s)$ 的零点即 $\det N(s) = 0$ 的根，而用补偿器 $C(s)$ 的一部分零点即 $\det D(s) = 0$ 的根去对消掉受控系统 $G_{\bullet}(s)$ 的极点即 $\det D(s) = 0$ 的根。从物理的观点而言，通常不允许对 $G_{\bullet}(s)$ 的不稳定极点进行对消，因为任意小的摄动都会破坏绝对的对消，而导致所得到的反馈系统不稳定。基于这个理由，在上述解耦控制方案中，引入了 $D(s)$ 为稳定多项式矩阵的假定。

(2) 如果所考虑的受控系统 $G_{\bullet}(s) = N(s)D^{-1}(s)$ 中， $D(s)$ 为不稳定多项式矩阵，即 $\det D(s) = 0$ 的根中包含实部为正的根，则就不能直接采用上述解耦控制方案，但在引入适当的附加补偿后仍可利用上述方案来实现解耦控制。为此，如图11.20所示那样，

![](image/0230e9f924c37ff4474fa14f81afc3ad4e23e90101b1b97dd5c948a5ab3c7433.jpg)

<details>
<summary>flowchart</summary>
