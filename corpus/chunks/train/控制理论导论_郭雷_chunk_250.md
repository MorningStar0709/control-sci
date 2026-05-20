$$\frac {\partial \Phi}{\partial y _ {1}} = Y _ {1} (\phi_ {y _ {1}} ^ {Y _ {1}} \dots \phi_ {y _ {n}} ^ {Y _ {n}} (p)), \tag {3.8.8}$$

考虑到 $\phi_{y_i}^{Y_i}$ 和 $\phi_{y_j}^{Y_j}$ 的可交换性，交换(3.8.7)右式的 $\phi_{y_1}^{Y_1}$ 与 $\phi_{u_i}^{Y_i}$ 可得

$$\frac {\partial \Phi}{\partial y _ {i}} = Y _ {i} (\phi_ {y _ {1}} ^ {Y _ {1}} \dots \phi_ {y _ {n}} ^ {Y _ {n}} (p)), \quad i = 1, \dots , k. \tag {3.8.9}$$

因此

$$S = \{y \in V \mid y _ {k + 1} = 0, \dots , y _ {n} = 0 \}$$

是 $D$ 的一个积分流形.

注3.8.1 (1) Frobenius定理还说明如果分布是对合且有定常维数，则通过每一点 $x \in M$ 存在最大的积分子流形[2]；

(2) 如果流形与分布均是解析的，那么无需定常维数的假定，微分流形也存在 [22].

在本节的余下部分中，函数，向量场和余向量场均假定为解析的.

命题3.8.1 设 $X, Y \in V^{\omega}(M), h \in C^{\omega}(M), \omega \in V^{*}(M)$ . 那么：

(1)

$$\frac {\mathrm{d}}{\mathrm{d} t} h \left(\phi_ {t} ^ {X} (x)\right) = L _ {X} h \left(\phi_ {t} ^ {X} (x)\right); \tag {3.8.10}$$

(2) (解析函数的 Lie 展式)

$$h \left(\phi_ {t} ^ {X} (x)\right) = \sum_ {k = 0} ^ {\infty} \frac {t ^ {k}}{k !} L _ {X} ^ {k} h (x); \tag {3.8.11}$$

(3) (向量场的 Lie 展式)

$$\left(\phi_ {- t} ^ {X}\right) _ {*} Y \left(\phi_ {t} ^ {X} (x)\right) = \sum_ {k = 0} ^ {\infty} \frac {t ^ {k}}{k !} \mathrm{ad} _ {X} ^ {k} Y (x); \tag {3.8.12}$$

(4) (1-形式的 Lie 展式)

$$\left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) = \sum_ {k = 0} ^ {\infty} \frac {t ^ {k}}{k !} L _ {X} ^ {k} \omega (x). \tag {3.8.13}$$

Lie 展式 (3.8.11)\~(3.8.13) 也称为 Campbell-Baker-Hausdorff 公式.

证明 (1) 利用链式法则，我们有

$$\mathrm{LHS} = \mathrm{d} h \frac {\mathrm{d}}{\mathrm{d} t} (\phi_ {t} ^ {X} (x)) = \mathrm{d} h X (\phi_ {t} ^ {X} (x)) = L _ {X} h (\phi_ {t} ^ {X} (x));$$

(2) 反复应用 (3.8.10), 可以得到

$$\frac {\mathrm{d} ^ {k}}{\mathrm{d} t ^ {k}} h \left(\phi_ {t} ^ {X} (x)\right) | _ {t = 0} = L _ {X} ^ {k} h \left(\phi_ {t} ^ {X} (x)\right), \quad k \geqslant 0. \tag {3.8.14}$$

现在式 (3.8.11) 通过对 $t$ 的 Taylor 展式即可得到;

(3) 首先求其对 $t$ 的导数，得到
