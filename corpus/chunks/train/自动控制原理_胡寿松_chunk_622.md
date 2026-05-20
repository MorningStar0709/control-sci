# (2) 开环与闭环传递矩阵

设多输入 - 多输出系统结构图如图 9-14 所示。图中 U, Y, Z, E 分别为输入、输出、反馈、偏差向量；G, H 分别为前向通路和反馈通路的传递矩阵。由图可知

$$\mathbf {Z} (s) = \mathbf {H} (s) \mathbf {Y} (s) = \mathbf {H} (s) \mathbf {G} (s) \mathbf {E} (s) \tag {9-50}$$

图 9-14 多输入-多输出系统结构图

定义偏差向量至反馈向量之间的传递矩阵 $H(s)G(s)$ 为开环传递矩阵，它描述了 $E(s)$ 至 $Z(s)$ 之间的传递关系。开环传递矩阵等于向量传递过程中所有部件传递矩阵的乘积，其相乘顺序与传递过程相反，而且由于是矩阵相乘，顺序不能任意交换。

由于

$$\mathbf {Y} (s) = \mathbf {G} (s) \mathbf {E} (s) = \mathbf {G} (s) [ \mathbf {U} (s) - \mathbf {Z} (s) ]= \mathbf {G} (s) [ \mathbf {U} (s) - \mathbf {H} (s) \mathbf {Y} (s) ]$$

则 $\mathbf{Y}(s)=[\mathbf{I}+\mathbf{G}(s)\mathbf{H}(s)]^{-1}\mathbf{G}(s)\mathbf{U}(s)$ (9-51)

定义输入向量至输出向量之间的传递矩阵为闭环传递矩阵，记为 $\Phi(s)$ ，则

$$\boldsymbol {\Phi} (s) = [ \boldsymbol {I} + \boldsymbol {G} (s) \boldsymbol {H} (s) ] ^ {- 1} \boldsymbol {G} (s) \tag {9-52}$$

它描述了 $U(s)$ 至 $Y(s)$ 之间的传递关系。

由于

$$\boldsymbol {E} (s) = \boldsymbol {U} (s) - \boldsymbol {Z} (s) = \boldsymbol {U} (s) - \boldsymbol {H} (s) \boldsymbol {G} (s) \boldsymbol {E} (s)$$

则 $\boldsymbol{E}(s)=[\boldsymbol{I}+\boldsymbol{H}(s)\boldsymbol{G}(s)]^{-1}\boldsymbol{U}(s)$ (9-53)

定义输入向量至偏差向量之间的传递矩阵为偏差传递矩阵，记为 $\Phi_{e}(s)$ ，则

$$\boldsymbol {\Phi} _ {e} (s) = [ \boldsymbol {I} + \boldsymbol {H} (s) \boldsymbol {G} (s) ] ^ {- 1} \tag {9-54}$$

它描述了 $U(s)$ 至 $E(s)$ 之间的传递关系。
