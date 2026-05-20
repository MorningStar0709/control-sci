# 1. 系统模型的建立

系统的状态方程为

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} \\ \boldsymbol {y} = \boldsymbol {C} \boldsymbol {x} + \boldsymbol {D} \boldsymbol {u} \end{array} \right.
$$

在 MATLAB 中只需要将各个系数按照常规矩阵的方式输入到工作空间即可：

$$, \mathrm{A} = \left[ \mathrm{a} _ {1 1}, \mathrm{a} _ {1 2}, \dots , \mathrm{a} _ {1 n}; \mathrm{a} _ {2 1}, \mathrm{a} _ {2 2}, \dots , \mathrm{a} _ {2 n}; \dots ; \mathrm{a} _ {n 1}, \mathrm{a} _ {n 2}, \dots , \mathrm{a} _ {n n} \right];\mathrm{B} = \left[ \mathrm{b} _ {1 1}, \mathrm{b} _ {1 2}, \dots , \mathrm{b} _ {1 p}; \mathrm{b} _ {2 1}, \mathrm{b} _ {2 2}, \dots , \mathrm{b} _ {2 p}; \dots ; \mathrm{b} _ {\mathrm{n} 1}, \mathrm{b} _ {\mathrm{n} 2}, \dots , \mathrm{b} _ {\mathrm{np}} \right];C = \left[ c _ {1 1}, c _ {1 2}, \dots , c _ {1 n}; c _ {2 1}, c _ {2 2}, \dots , c _ {2 n}; \dots ; c _ {q 1}, c _ {q 2}, \dots , c _ {q n} \right];D = \left[ d _ {1 1}, d _ {1 2}, \dots , d _ {1 p}; d _ {2 1}, d _ {2 2}, \dots , d _ {2 p}; \dots ; d _ {q 1}, d _ {q 2}, \dots , a _ {q p} \right]\mathbf {s s} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D})$$

传递函数的零极点模型为

$$\boldsymbol {G} (s) = K \frac {\left(s + z _ {1}\right) \left(s + z _ {2}\right) \cdots \left(s + z _ {m}\right)}{\left(s + p _ {1}\right) \left(s + p _ {2}\right) \cdots \left(s + p _ {n}\right)}$$

在 MATLAB 中可以采用如下语句将零极点模型输入到工作空间：

$$
\begin{array}{l} \mathrm{KGain} = \mathrm{K}; \\ Z = \left[ z _ {1}; z _ {2}; \dots ; z _ {m} \right]; \\ \mathrm{P} = \left[ \mathrm{p} _ {1}; \mathrm{p} _ {2}; \dots ; \mathrm{p} _ {n} \right]; \\ \mathbf {z p k} (\mathbf {Z}, \mathbf {P}, \mathbf {K G a i n}) \\ \end{array}
$$

传递函数模型在更一般的情况下,可以表示为复数变量 s 的有理函数形式:

$$\boldsymbol {G} (s) = \frac {b _ {1} s ^ {m} + b _ {2} s ^ {m - 1} + \cdots + b _ {m} s + b _ {m + 1}}{s ^ {n} + a _ {1} s ^ {n - 1} + a _ {2} s ^ {n - 2} + \cdots + a _ {n - 1} s + a _ {n}}$$

在 MATLAB 中可以采用如下语句将以上的传递函数模型输入到工作空间：

$$
\begin{array}{l} \mathrm{num} = \left[ \mathrm{b} _ {1}, \mathrm{b} _ {2}, \dots , \mathrm{b} _ {\mathrm{m}}, \mathrm{b} _ {\mathrm{m+1}} \right]; \\ \mathrm{den} = \left[ 1, \mathbf {a} _ {1}, \mathbf {a} _ {2}, \dots , \mathbf {a} _ {n - 1}, \mathbf {a} _ {n} \right]; \\ \mathrm{G} = \operatorname{tf} (\text { num }, \text { den }); \\ \end{array}
$$
