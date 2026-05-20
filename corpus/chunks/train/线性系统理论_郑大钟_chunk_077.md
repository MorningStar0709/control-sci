脉冲响应矩阵和传递函数矩阵 进一步,我们来讨论线性定常系统的这两个输入-输出特性表达式间的关系。对此,可证明如下的结论。

结论 用 $G(t)$ 和 $\hat{G}(s)$ 分别表示给定的线性定常系统的脉冲响应矩阵和传递函数矩阵, 则两者之间成立如下的关系式:

$$\hat {G} (s) = \mathscr {L} [ G (t) ], \quad t \geqslant 0 \tag {2.92}$$

和

$$G (t) = \mathscr {L} ^ {- 1} [ \hat {G} (s) ], \quad t \geqslant 0 \tag {2.93}$$

证 考虑到

$$G (t) = C e ^ {A t} B + D \delta (t) \tag {2.94}$$

和

$$\mathcal {L} [ e ^ {A t} ] = (s I - A) ^ {- 1}, \quad \mathcal {L} [ \delta (t) ] = 1 \tag {2.95}$$

就可导出：

$$\mathscr {L} [ G (t) ] = C (s I - A) ^ {- 1} B + D = \hat {G} (s) \tag {2.96}$$

类似地，按相反的步骤则可导出(2.93)。于是，证明完成。

利用由(2.92)和(2.93)所给出的关系,我们还可进而有如下的推论。

推论 给定两个线性定常系统 $(A, B, C, D)$ 和 $(\overline{A}, \overline{B}, \overline{C}, \overline{D})$ ，设两者具有相同的输出和输入维数，但它们的状态维数可不一定相同，则此两系统具有相同脉冲响应矩阵（即相同传递函数矩阵）的充分必要条件是

$$D = \overline {{D}} \tag {2.97}$$

和

$$C A ^ {i} B = \overline {{C}} \overline {{A}} ^ {i} \overline {{B}}, \quad i = 0, 1, 2 \dots \tag {2.98}$$

证 $G(t) = \overline{G}(t)$ ，或 $\hat{G}(s) = \hat{G}(s)$ ，当且仅当

$$D + C (s I - A) ^ {- 1} B = \bar {D} + \bar {C} (s I - \bar {A}) ^ {- 1} \bar {B} \tag {2.99}$$

考虑到预解矩阵的关系式:

$$(s I - A) ^ {- 1} = I s ^ {- 1} + A s ^ {- 2} + A ^ {2} s ^ {- 3} + \dots \tag {2.100}$$

则上述条件(2.99)还可进而表为:

$$
\begin{array}{l} D + C B s ^ {- 1} + C A B s ^ {- 2} + C A ^ {2} B s ^ {- 3} + \dots \\ = \bar {D} + \bar {C} \bar {B} s ^ {- 1} + \bar {C} \bar {A} \bar {B} s ^ {- 2} + \bar {C} \bar {A} ^ {2} \bar {B} s ^ {- 3} + \dots \tag {2.101} \\ \end{array}
$$

显然，欲使上式对任意的 $s$ 均成立，当且仅当

$$D = \overline {{D}} \text {和} C A ^ {i} B = \overline {{C}} \overline {{A}} ^ {i} \overline {{B}}, i = 0, 1, 2, \dots \tag {2.102}$$

于是，就完成了证明。
