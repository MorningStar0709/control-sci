几点讨论 对于上面所导出的能控规范形和能观测规范形，可进一步指出如下的两点讨论：

(1) 在能控规范形 $(A_{c}, b_{c})$ 和能观测规范形 $(A_{o}, c_{o})$ 中，以明显的形式和反映系统结构特性的特征多项式的系数 $\sigma_{i}(i=0,1,\cdots,n-1)$ 直接联系起来，无论对综合系统的状态反馈和状态观测器还是对系统进行仿真研究，这都将是很方便的。  
（2）代数等价的完全能控系统具有相同的能控规范形，代数等价的完全能观测系统具有相同的能观测规范形。

只需证明代数等价系统的 $\alpha(s)$ 和 $\beta_{i}(i=0,1,\cdots,n-1)$ 相同。为此，设有 $(A,b,c)$ 和 $(\bar{A},\bar{b},\bar{c})$ ，且两者之间成立关系式

$$\bar {A} = T A T ^ {- 1}, \quad \bar {\boldsymbol {b}} = T \boldsymbol {b}, \quad \bar {\boldsymbol {c}} = c T ^ {- 1} \tag {3.175}$$

其中 $T$ 为非奇异常阵。于是，分别有

$$
\begin{array}{l} \bar {a} (s) = \det (s I - \bar {A}) = \det T (s I - A) T ^ {- 1} = \det (s I - A) \\ = \alpha (s) \tag {3.176} \\ \end{array}
$$

和

$$
\begin{array}{l} \bar {\beta} _ {i - 1} = \bar {c} \bar {A} ^ {n - i} \bar {b} + a _ {n - 1} \bar {c} \bar {A} ^ {n - i - 1} \bar {b} + \dots + a _ {i} \bar {c} \bar {b} \\ = c T ^ {- 1} T A ^ {n - i} T ^ {- 1} T b + a _ {n - 1} c T ^ {- 1} T A ^ {n - i - 1} T ^ {- 1} T b + \dots \\ + \alpha_ {i} c T ^ {- 1} T b = c A ^ {n - i} b + \alpha_ {s - 1} c A ^ {n - i - 1} b + \dots \\ + \alpha_ {i} \mathbf {c b} = \beta_ {i - 1}, \quad i = 1, \dots , n \tag {3.177} \\ \end{array}
$$

从而，就完成了证明。
