$$\operatorname{rank} \left[ D _ {2} (s), N _ {1} (s) \right] = p _ {2}, \forall s \in \mathcal {C} \tag {11.31}$$

也即在满足结论中给出的条件下，必有 $\{D_{i}(s), N_{1}(s)\}$ 为左互质；再据结论1知，此时串联系统 $S_{T}$ 为能控。从而，证明完成。

由于结论2中给出的只是充分条件，因此当 $G_{2}(s)$ 的极点中包含和 $G_{1}(s)$ 的传输零点等同的极点时，仍有可能使串联系统 $S_{T}$ 为能控。这要对具体问题进行具体的分析。但是，若令 $\lambda_{i} (i = 1, 2, \dots, \beta)$ 为和 $G_{1}(s)$ 的传输零点等同的 $G_{2}(s)$ 的极点，且表

$$\operatorname{rank} N _ {1} \left(\lambda_ {i}\right) = \alpha_ {i} < p _ {2}, \operatorname{rank} D _ {2} \left(\lambda_ {i}\right) = \gamma_ {i} < p _ {2} \tag {11.32}$$

其中 $i=1,2,\cdots,\beta$ ，并表

$$
\left\{ \begin{array}{l} \alpha = \min \left\{\alpha_ {1}, \dots , \alpha_ {\beta} \right\} \\ \gamma = \min \left\{\gamma_ {1}, \dots , \gamma_ {\beta} \right\} \end{array} \right. \tag {11.33}
$$

那么当同时满足条件：

① $G_{1}(s)$ 的传输零点和 $G_{2}(s)$ 的极点包含等同的 $s$ 值

② $\alpha +\gamma <  p_{2}$

时，串联系统 $S_{\mathbb{T}}$ 必定不是完全能控的。对于单输入-单输出的情况，如果 $G_{2}(s)$ 的至少一个极点等同于 $G_{1}(s)$ 的传输零点，那么此时必然成立 $\alpha + \gamma < p_{2}$ ，所以结论2中的充分条件同时也是必要条件。于是，我们进一步有如下的结论。

结论3 如果限于考虑单输入-单输出的情况，则对于图11.2所示的串联系统 $S_{T}$ 成立如下的论断：

(i) $S_{T}$ 为能控的充分必要条件是 $g_{2}(s)$ 没有一个极点为 $g_{1}(s)$ 的零点所对消；

(ii) $S_{\pmb{\tau}}$ 为能观测的充分必要条件是 $g_{1}(s)$ 没有一个极点为 $g_{2}(s)$ 的零点相对消；

(iii) $S_{T}$ 为联合能控和能观测，即可用 $g_{2}(s)g_{1}(s)$ 完全表征的充分必要条件，是 $g_{1}(s)$ 和 $g_{2}(s)$ 间没有零点极点对消现象。

还需指出，零点极点对消的概念，也可推广到多输入-多输出系统。若令

$\Delta (s) = G_{2}(s)G_{1}(s)$ 的特征多项式

$\Delta_1(s) = G_1(s)$ 的特征多项式

$\Delta_2(s) = G_2(s)$ 的特征多项式

那么 $G_{2}(s)$ 和 $G_{1}(s)$ 没有零点极点对消就等价于

$$\deg \Delta (s) = \deg \Delta_ {1} (s) + \deg \Delta_ {2} (s) \tag {11.34}$$

而当 $G_{2}(s)$ 和 $G_{1}(s)$ 间包含零点极点对消时则有

$$\deg \Delta (s) < \deg \Delta_ {1} (s) + \deg \Delta_ {2} (s) \tag {11.35}$$

并且被对消掉的极点就即为

$$\Delta_ {1} (s) \Delta_ {2} (s) / \Delta (s) = 0 \tag {11.36}$$

的根。进一步，如果 $G_{i}(s)$ 用MFD来表示，也即

$$G _ {i} (s) = N _ {i} (s) D _ {i} ^ {- 1} (s) = D _ {L i} ^ {- 1} (s) N _ {L i} (s), i = 1, 2 \tag {11.37}$$

且为不可简约, 那么当 $G_{2}(s)$ 和 $G_{1}(s)$ 间包含零点极点对消时, 所对消掉的极点就对应地为使 $[D_{2}(s), N_{1}(s)]$ , $[D_{L1}(s)D_{2}(s), N_{L1}(s)]$ , $[D_{L2}(s), N_{L2}(s)N_{1}(s)]$ 行降秩的 $s$ 值, 和对应地使

$$
\left[ \begin{array}{c} D _ {L 1} (s) \\ N _ {L 2} (s) \end{array} \right], \left[ \begin{array}{c} D _ {L 1} (s) D _ {2} (s) \\ N _ {2} (s) \end{array} \right], \left[ \begin{array}{c} D _ {2} (s) \\ N _ {L 2} (s) N _ {1} (s) \end{array} \right]
$$

列降秩的 s 值。
