$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \left(\phi_ {- t} ^ {X}\right) _ {*} Y \left(\phi_ {t} ^ {X} (x)\right) = \lim _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \left[\left(\phi_ {- t - \Delta t} ^ {X}\right) _ {*} Y \left(\phi_ {t + \Delta t} ^ {X} (x)\right) - \left(\phi_ {t} ^ {X}\right) _ {*} Y (x) \right] \\ = \lim _ {\Delta t \rightarrow 0} \frac {1}{\Delta t} \left[\left(\phi_ {\Delta t} ^ {X}\right) _ {*} \left(\phi_ {t} ^ {X}\right) _ {*} Y \left(\phi_ {- \Delta t} ^ {X} (x)\right)\right] - \left(\phi_ {t} ^ {X}\right) * Y (x) ] \\ = \left(\phi_ {t} ^ {X}\right) _ {*} \lim _ {\Delta t \rightarrow 0} \left[\left(\phi_ {\Delta t} ^ {X}\right) _ {*} Y \left(\phi_ {- \Delta t} ^ {X} (x)\right) - Y (x) \right] \\ = \left(\phi_ {t} ^ {X}\right) _ {*} \mathrm{ad} _ {X} Y. \\ \end{array}
$$

于是可递归得到

$$
\begin{array}{l} \frac {\mathrm{d} ^ {k}}{\mathrm{d} t ^ {k}} \left(\phi_ {t} ^ {X}\right) _ {*} Y (x) | _ {t = 0} = \left(\phi_ {t} ^ {X}\right) _ {*} \mathrm{ad} _ {X} ^ {k - 1} Y (x) | _ {t = 0} \\ = \mathrm{ad} _ {X} ^ {k} Y (x), \quad k \geqslant 0. \tag {3.8.15} \\ \end{array}
$$

再由 Taylor 展式可得式 (3.8.12);

(4) 式 (3.8.13) 的证明本质上是一样的，先求导，得

$$\frac {\mathrm{d}}{\mathrm{d} t} \left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) = \left(\phi_ {t} ^ {X}\right) ^ {*} L _ {X} \omega \left(\phi_ {t} ^ {X} (x)\right),\frac {\mathrm{d} ^ {k}}{\mathrm{d} t ^ {k}} \left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) = \left(\phi_ {t} ^ {X}\right) ^ {*} L _ {X} ^ {k} \omega \left(\phi_ {t} ^ {X} (x)\right).$$

因此

$$\frac {\mathrm{d} ^ {k}}{\mathrm{d} t ^ {k}} \left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) \Big | _ {t = 0} = L _ {X} ^ {k} \omega (x).$$

再由 Taylor 展式即得式 (3.8.13).

推论3.8.1

$$\phi_ {t} ^ {X} (x) = x + t X (x) + \sum_ {k = 1} ^ {\infty} \frac {t ^ {k + 1}}{(k + 1) !} L _ {X} ^ {k} (X (x)). \tag {3.8.16}$$

证明 对坐标函数 $x_{i}$ 使用式(3.8.11)，即得

$$x _ {i} \left(\phi_ {t} ^ {X} (x)\right) = x _ {i} + t L _ {X} \left(x _ {i}\right) + \sum_ {k = 2} ^ {\infty} \frac {t ^ {k}}{k !} L _ {X} ^ {k} \left(x _ {i}\right).$$

注意 $L_{X}(x_{i}) = X_{i}$ 是 $X$ 的第 $i$ 个分量. 将 $L_{X}^{k}(x_{i}), k \geqslant 2$ 用 $L^{k-1}(X_{i})$ 代替, 并将 $n$ 个分量放在一起, 即得式 (3.8.16).

设 $H$ 为 $V(M)$ 的一组向量场在 $\mathbb{R}$ 上生成的子空间。一条曲线 $\sigma(t), 0 \leqslant t \leqslant 1$ ，称为 $H$ 的积分曲线，如果

$$\frac {\mathrm{d} \sigma (t)}{\mathrm{d} t} \in H _ {\sigma (t)}, \quad 0 \leqslant t \leqslant 1.$$
