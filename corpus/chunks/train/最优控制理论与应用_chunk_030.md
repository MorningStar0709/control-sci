$$
\boldsymbol {X} = \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \quad \Delta \boldsymbol {X} = \left[ \begin{array}{l} \Delta x _ {1} \\ \Delta x _ {2} \end{array} \right] \quad f _ {\boldsymbol {X} ^ {*}} ^ {\prime} = \left[ \begin{array}{l l} f _ {x _ {1}} ^ {\prime} & f _ {x _ {2}} ^ {\prime} \end{array} \right] _ {\boldsymbol {X} = \boldsymbol {X} ^ {*}} ^ {\mathrm{T}}

f _ {X} ^ {\prime \prime} = \left[ \begin{array}{l l} f _ {x _ {1} x _ {1}} ^ {\prime \prime} & f _ {x _ {1} x _ {2}} ^ {\prime \prime} \\ f _ {x _ {1} x _ {2}} ^ {\prime \prime} & f _ {x _ {2} x _ {2}} ^ {\prime \prime} \end{array} \right] _ {X = X}. \tag {2-6}
$$

由式(2-5)可知, $f(X^{*})=f(x_{1}^{*},x_{2}^{*})$ 取极值的必要条件为

$$f _ {x ^ {*}} ^ {\prime} = 0 \tag {2-7}$$

进一步,若

$$\Delta \boldsymbol {X} ^ {\mathrm{T}} f _ {\boldsymbol {X} ^ {*}} ^ {\prime \prime} \Delta \boldsymbol {X} > 0 \tag {2-8}$$

则这个极值为极小值。由于 $\Delta X$ 是任意的不为0的向量，要使式(2-8)成立，由矩阵理论可知，二阶导数矩阵（又称为Hessian阵） $f''_{X}$ 必须是正定的。正定阵形式上可表示为

$$f _ {x ^ {*}} ^ {\prime \prime} > 0 \tag {2-9}$$

式(2-7)和(2-9)一起构成了 $f(X)$ 在 $X^{*}=\left[x_{1}^{*},x_{2}^{*}\right]^{T}$ 处取极小值的充分条件。

上面的结果不难推广到多元函数的极值问题。设 n 个变量的多元函数为

$$f (\textbf {X}) = f (x _ {1}, x _ {2}, \dots , x _ {n})$$

式中

$$
\boldsymbol {X} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right].
$$

则 $f(X)$ 在 $X = X^{*} = [x_{1}^{*}, x_{2}^{*}, \cdots, x_{n}^{*}]^{T}$ 处有极小值的必要条件为一阶导数向量等于零向量，即

$$f _ {X} ^ {\prime} = \left[ f _ {x _ {1}} ^ {\prime}, f _ {x _ {2}} ^ {\prime}, \dots , f _ {x _ {n}} ^ {\prime} \right] _ {X = X ^ {*}} ^ {T} = 0 \tag {2-10}$$

进一步,若二阶导数矩阵是正定阵,即

$$
f _ {X ^ {*}} ^ {\prime \prime} = \left[ \begin{array}{c c c c} f _ {x _ {1} x _ {1}} ^ {\prime \prime} & f _ {x _ {1} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {1} x _ {n}} ^ {\prime \prime} \\ f _ {x _ {2} x _ {1}} ^ {\prime \prime} & f _ {x _ {2} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {2} x _ {n}} ^ {\prime \prime} \\ & \dots \dots & & \\ f _ {x _ {n} x _ {1}} ^ {\prime \prime} & f _ {x _ {n} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {n} x _ {n}} ^ {\prime \prime} \end{array} \right] _ {X = X ^ {*}} > 0 \tag {2-11}
$$

则这个极值是极小。式(2-10)和(2-11)一起构成了多元函数 $f(x_{1}, x_{2}, \cdots, x_{n})$ 在 $X^{*} = [x_{1}^{*}, x_{2}^{*}, \cdots, x_{n}^{*}]^{T}$ 处取极小值的充分条件。

由式(2-11)可知, $f''_{x}$ .是实对称矩阵。判别实对称矩阵是否为正定有两个常用的方法。一是检验 $f''_{x}$ .的特征值,若特征值全部为正,则 $f''_{x}$ 是正定的。另一是应用西尔维斯特(Sylvester)判据。根据此判据,若 $f''_{x}$ 的各阶顺序主子式均大于0,即
