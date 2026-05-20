$$
\begin{array}{l} \hat {\boldsymbol {u}} _ {1} (s) = \hat {\boldsymbol {u}} (s) - \hat {\boldsymbol {y}} _ {2} (s) = \hat {\boldsymbol {u}} (s) - G _ {2} (s) \hat {\boldsymbol {u}} _ {2} (s) = \hat {\boldsymbol {u}} (s) - G _ {2} (s) \hat {\boldsymbol {y}} _ {1} (s) \\ = \hat {\boldsymbol {u}} (s) - G _ {2} (s) G _ {1} (s) \hat {\boldsymbol {u}} _ {1} (s) \tag {1.150} \\ \end{array}
$$

和

$$\hat {\mathbf {y}} (s) = \hat {\mathbf {y}} _ {1} (s) = G _ {1} (s) \hat {\mathbf {u}} _ {1} (s) \tag {1.151}$$

从而，由(1.150)和(1.151)，且假定 $\operatorname{det}(I + G_2(s)G_1(s)) \neq 0^2$ ，又可导出反馈系统的传递函数矩阵的另一表达式为：

$$G (s) = G _ {1} (s) [ I + G _ {2} (s) G _ {1} (s) ] ^ {- 1} \tag {1.152}$$

还需指出，在子系统的反馈联接的讨论中，所以引入假定 $D_{i} = 0 (i = 1,2)$ ，只是为了使（1.145）给出的状态空间描述的形式不致于过份复杂，而且这也是符合大多数实际问题的。
