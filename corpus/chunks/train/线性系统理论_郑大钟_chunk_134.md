$$
\bar {A} = P A P ^ {- 1} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & - 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{array} \right] \left[ \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 2 & 1 \\ \hline 0 & 0 & 0 \end{array} \right]

\ddot {B} = P B = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & - 1 \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ \hdashline 0 & 0 \end{array} \right]

\bar {C} = C P ^ {- 1} = \left[ \begin{array}{l l l} 1 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] = [ 0, 2; 1 ]
$$

这样, 就导出了系统按能控性分解的表达式为:

$$
\left[ \begin{array}{c} \dot {\bar {x}} _ {e} \\ \dot {\bar {x}} _ {i} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 2 & 1 \\ - & - & - \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \bar {x} _ {e} \\ \bar {x} _ {i} \end{array} \right] + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ - & - \\ 0 & 0 \end{array} \right] u

y = [ 0 2 \vdots 1 ] \left[ \begin{array}{l} \bar {x} _ {e} \\ \bar {x} _ {z} \end{array} \right]
$$

下面，我们对由（3.239）所给出的系统结构按能控性分解的规范表达式，进行几点讨论：

(1) (3.239) 表明, 在此分解规范表达式下, 系统被明显地分解为能控部分和不能控部分。其中, 能控部分为如下的 $k$ 维子系统

$$
\begin{array}{l} \dot {\vec {x}} _ {c} = \overline {{A}} _ {c} \vec {x} _ {c} + \overline {{A}} _ {1 2} \vec {x} _ {c} + \overline {{B}} _ {c} \boldsymbol {\alpha} \tag {3.248} \\ \mathbf {y} _ {1} = \bar {C} _ {c} \bar {\mathbf {x}} _ {c} \\ \end{array}
$$

不能控部分为如下的 $n - k$ 维子系统

$$
\begin{array}{l} \dot {\vec {x}} _ {2} = \overline {{{A}}} _ {2} \vec {x} _ {3} \\ \text {   } \quad \overline {{{\vec {a}}}} _ {1} = \overline {{{\vec {a}}}} _ {2} \end{array} \tag {3.249}
$$

而 $y = y_{1} + y_{2}$

(2) 考虑到

$$
\begin{array}{l} \det (s I - A) = \det (s I - \bar {A}) = \det \left[ \begin{array}{c c} s I - \bar {A} _ {e} & - \bar {A} _ {1 2} \\ 0 & s I - \bar {A} _ {2} \end{array} \right] \\ = \det (s I - \bar {A} _ {c}) \det (s I - \bar {A} _ {c}) \tag {3.250} \\ \end{array}
$$

表明不完全能控系统（3.236）的特征值由两部分组成。一部分为 $\overline{A}_{\varepsilon}$ 的特征值，称为系统的能控振型；另一部分为 $\overline{A}_{\varepsilon}$ 的特征值，称为系统的不能控振型。外输入 $\pmb{\alpha}$ 的引入，只能改变能控振型的位置，而不能改变不能控振型的位置。

（3）进一步，根据（3.239），可以画出系统在结构分解后的方块图，如图3.6所示。从图中可直观地看出，系统的不能控部分既不受输入 $\pmb{u}$ 的直接影响，也没有通过能控状态 $\pmb{x}_{i}$ 而受 $\pmb{u}$ 的间接影响。因此，不能控部分 $\Sigma_{z}$ 是“黑箱”内部的一个不能由外部作用所影响的部分。
