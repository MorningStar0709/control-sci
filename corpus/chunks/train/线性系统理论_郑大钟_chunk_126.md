$$
A ^ {v _ {1}} \boldsymbol {b} _ {1} = \sum_ {j = 1} ^ {v _ {1}} \alpha_ {1 j} A ^ {j - 1} \boldsymbol {b} _ {1} \tag {3.183}
\left\{ \begin{array}{l} e _ {1 1} \triangleq A ^ {\nu_ {1} - 1} b _ {1} - \sum_ {j = 2} ^ {\nu_ {1}} \alpha_ {1 j} A ^ {j - 3} b _ {1} \\ e _ {1 2} \triangleq A ^ {\nu_ {1} - 2} b _ {1} - \sum_ {j = 3} ^ {\nu_ {1}} \alpha_ {1 j} A ^ {j - 3} b _ {1} \\ \dots \dots \\ e _ {1 \nu_ {1}} \triangleq b _ {1} \end{array} \right. \tag {3.184}
A ^ {v _ {1}} b _ {2} = \sum_ {j = 1} ^ {v _ {2}} \alpha_ {2 j} A ^ {j - 1} b _ {2} + \sum_ {j = 1} ^ {v _ {1}} \gamma_ {2 j 1} e _ {i j} \tag {3.185}
\left\{ \begin{array}{l} e _ {2 1} \triangleq A ^ {\nu_ {2} - 1} b _ {2} - \sum_ {j = 3} ^ {\nu_ {1}} a _ {2 j} A ^ {i - 2} b _ {2} \\ e _ {2 2} \triangleq A ^ {\nu_ {2} - 2} b _ {2} - \sum_ {j = 3} ^ {\nu_ {1}} a _ {2 j} A ^ {i - 3} b _ {2} \\ \dots \dots \\ e _ {2 \nu_ {2}} \triangleq b _ {2} \end{array} \right. \tag {3.186}
A ^ {v _ {1}} b _ {3} = \sum_ {j = 1} ^ {v _ {2}} \alpha_ {3 j} A ^ {j - 1} b _ {3} + \sum_ {k = 1} ^ {2} \sum_ {j = 1} ^ {v _ {k}} \gamma_ {3 j k} e _ {k l} \tag {3.187}
\left\{ \begin{array}{l} e _ {3 1} \triangleq A ^ {p _ {3} - 1} b _ {3} - \sum_ {j = 2} ^ {v _ {3}} \alpha_ {3 j} A ^ {i - 2} b _ {3} \\ e _ {3 2} \triangleq A ^ {p _ {3} - 2} b _ {3} - \sum_ {j = 3} ^ {v _ {3}} \alpha_ {3 j} A ^ {i - 3} b _ {3} \\ \dots \dots \\ c _ {3 n _ {3}} \triangleq b _ {3} \end{array} \right. \tag {3.188}
$$

● ● ● ● ●

$$
A ^ {v _ {l}} \boldsymbol {b} _ {l} = \sum_ {j = 1} ^ {v _ {l}} \alpha_ {i j} A ^ {j - 1} \boldsymbol {b} _ {l} + \sum_ {k = 1} ^ {l - 1} \sum_ {j = 1} ^ {v _ {k}} r _ {i j k} \boldsymbol {e} _ {k j} \tag {3.189}
\left\{ \begin{array}{l} \boldsymbol {e} _ {l 1} \triangleq A ^ {v _ {l} - 1} b _ {l} - \sum_ {j = 1} ^ {v _ {l}} \alpha_ {l j} A ^ {j - 2} \boldsymbol {b} _ {l} \\ \boldsymbol {e} _ {l 2} \triangleq A ^ {v _ {l} - 2} b _ {l} - \sum_ {j = 3} ^ {v _ {l}} \alpha_ {l j} A ^ {j - 3} \boldsymbol {b} _ {l} \\ \dots \dots \\ \boldsymbol {e} _ {l v _ {l}} \triangleq \boldsymbol {b} _ {l} \end{array} \right. \tag {3.190}
$$

在此基础上，组成如下的变换矩阵

$$T = \left[ e _ {1 1}, e _ {1 2}, \dots , e _ {j v _ {1}}; \dots ; e _ {l 1}, e _ {l 2}, \dots , e _ {l v _ {l}} \right] \tag {3.191}$$

并得到如下的结论：

结论1 对完全能控的多输入-多输出线性定常系统（3.178），引入线性非奇异变换 $\pmb{x} = T^{-1}\pmb{x}$ ，即可导出其旺纳姆能控规范形为：

$$
\begin{array}{l} \Sigma_ {c W}: \quad \dot {\bar {x}} = \bar {A} _ {c} \bar {x} + \bar {B} _ {c} u \\ y = \bar {C} _ {c} \bar {x} \end{array} \tag {3.192}
$$

其中
