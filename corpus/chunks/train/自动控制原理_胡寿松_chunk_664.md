$$
\boldsymbol {P} \boldsymbol {b} = \left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {1} \boldsymbol {A} \\ \vdots \\ \boldsymbol {p} _ {1} \boldsymbol {A} ^ {n - 1} \end{array} \right] \boldsymbol {b} = \boldsymbol {p} _ {1} \left[ \begin{array}{c} \boldsymbol {b} \\ \boldsymbol {A b} \\ \vdots \\ \boldsymbol {A} ^ {n - 1} \boldsymbol {b} \end{array} \right] = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \tag {9-183}
$$

即 $p_{1}[b\quad Ab\quad \cdots\quad A^{n-1}b]=[0\quad \cdots\quad 0\quad 1]$ (9-184)

故 $p_{1}=\left[\begin{matrix}0&\cdots&0&1\end{matrix}\right]\left[\begin{matrix}b&Ab&\cdots&A^{n-1}b\end{matrix}\right]^{-1}$ (9-185)

该式表明 $p_{1}$ 是可控性矩阵的逆阵的最后一行，于是可得出变换矩阵 $P^{-1}$ 的求法如下：

① 计算可控性矩阵 $S = [b \quad Ab \quad \cdots \quad A^{n-1}b]$ ;   
② 计算可控性矩阵的逆阵 $S^{-1}$ ，设一般形式为

$$
\boldsymbol {S} ^ {- 1} = \left[ \begin{array}{c c c c} S _ {1 1} & S _ {1 2} & \dots & S _ {1 n} \\ S _ {2 1} & S _ {2 2} & \dots & S _ {2 n} \\ \vdots & \vdots & & \vdots \\ S _ {n 1} & S _ {n 2} & \dots & S _ {m n} \end{array} \right]
$$

③ 取出 $S^{-1}$ 的最后一行(即第 $n$ 行)构成 $\pmb{p}_{1}$ 行向量

$$
\boldsymbol {p} _ {1} = \left[ \begin{array}{l l l l} S _ {n 1} & S _ {n 2} & \dots & S _ {m} \end{array} \right]
$$

④ 构造 P 阵

$$
\boldsymbol {P} = \left[ \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {1} \boldsymbol {A} \\ \vdots \\ \boldsymbol {p} _ {1} \boldsymbol {A} ^ {n - 1} \end{array} \right]
$$

⑤ $P^{-1}$ 便是将非标准型可控系统化为可控标准型的变换矩阵。
