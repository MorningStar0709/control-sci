$$
\begin{array}{l} f (\lambda) = | \lambda I - A | \\ = \lambda^ {n} + a _ {n - 1} \lambda^ {n - 1} + \dots + a _ {1} \lambda + a _ {0} \tag {9-93} \\ \end{array}
$$

则 A 满足其特征方程, 即

$$f (\mathbf {A}) = \mathbf {A} ^ {n} + a _ {n - 1} \mathbf {A} ^ {n - 1} + \dots + a _ {1} \mathbf {A} + a _ {0} \mathbf {I} = \mathbf {0} \tag {9-94}$$

证明 由于

$$(\lambda I - A) ^ {- 1} = \frac {B (\lambda)}{| \lambda I - A |} = \frac {B (\lambda)}{f (\lambda)} \tag {9-95}$$

式中， $B(\lambda)$ 为 $(\lambda I - A)$ 的伴随矩阵，其一般展开式为

$$
\mathbf {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m n} \end{array} \right], \quad \lambda \mathbf {I} - \mathbf {A} = \left[ \begin{array}{c c c c} \lambda - a _ {1 1} & - a _ {1 2} & \dots & - a _ {1 n} \\ - a _ {2 1} & \lambda - a _ {2 2} & \dots & - a _ {2 n} \\ \vdots & \vdots & & \vdots \\ - a _ {n 1} & - a _ {n 2} & \dots & \lambda - a _ {m n} \end{array} \right]

\boldsymbol {B} (\lambda) = \left[ \begin{array}{c c c c c c c c} (- 1) ^ {1 + 1} & \lambda - a _ {2 2} & \dots & - a _ {2 n} \\ & \vdots & & \vdots \\ & - a _ {n 2} & \dots & \lambda - a _ {m n} \\ & & \vdots & & & & & \vdots \\ (- 1) ^ {1 + n} & - a _ {2 1} & \dots & - a _ {2, n - 1} \\ & \vdots & & \vdots \\ & - a _ {n 1} & \dots & - a _ {n, n - 1} \end{array} \right] \quad \dots \quad (- 1) ^ {n + 1} \left| \begin{array}{c c c} - a _ {1 2} & \dots & - a _ {1 n} \\ \vdots & & \vdots \\ - a _ {n - 1, 2} & \dots & - a _ {n - 1, n} \end{array} \right|
$$

显见 $\pmb{B}(\lambda)$ 的元素均为 $n - 1$ 阶多项式，由矩阵加法规则可将其分解为 $n$ 个矩阵之和，即

$$\boldsymbol {B} (\lambda) = \lambda^ {n - 1} \boldsymbol {B} _ {n - 1} + \lambda^ {n - 2} \boldsymbol {B} _ {n - 2} + \dots + \lambda \boldsymbol {B} _ {1} + \boldsymbol {B} _ {0} \tag {9-96}$$

式中 $B_{n-1}, B_{n-2}, \cdots, B_{0}$ 均为 n 阶矩阵。将式(9-95)两端右乘 $(\lambda I - A)$ ，得

$$\boldsymbol {B} (\lambda) (\lambda \boldsymbol {I} - \boldsymbol {A}) = f (\lambda) \boldsymbol {I} \tag {9-97}$$

将式 $(9-96)$ 代入式 $(9-97)$ 并展开，有

$$
\begin{array}{l} \lambda^ {n} \boldsymbol {B} _ {n - 1} + \lambda^ {n - 1} (\boldsymbol {B} _ {n - 2} - \boldsymbol {B} _ {n - 1} \boldsymbol {A}) + \lambda^ {n - 2} (\boldsymbol {B} _ {n - 3} - \boldsymbol {B} _ {n - 2} \boldsymbol {A}) + \dots + \lambda (\boldsymbol {B} _ {0} - \boldsymbol {B} _ {1} \boldsymbol {A}) - \boldsymbol {B} _ {0} \boldsymbol {A} \\ = \lambda^ {n} I + a _ {n - 1} \lambda^ {n - 1} I + \dots + a _ {1} \lambda I - a _ {0} I \tag {9-98} \\ \end{array}
$$

令式(9-98)等号两边 $\lambda$ 同次项的系数相等, 可得
