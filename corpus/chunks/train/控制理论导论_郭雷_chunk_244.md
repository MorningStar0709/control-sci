$$F _ {*} (X) (h) = X (h \circ F), \quad \forall h \in C ^ {r} (N);$$

(3) 设 $\phi \in V^{*r}(N)$ , 则 $F$ 的一个导出映射 $F^{*}: V^{*r}(N) \to V^{*r}(M)$ 定义为

$$\langle F ^ {*} (\phi), X \rangle = \langle \phi , F _ {*} (X) \rangle , \quad \forall X \in V ^ {r} (M).$$

如果 $F$ 是一个局部微分同胚，那么上述映射也是局部定义的.

定义3.7.4 设 $X \in V(M), f \in C^r(M)$ . 那么 $f$ 对 $X$ 的 Lie 导数，记作 $L_X(f)$ ，定义为

$$L _ {X} (f) = \lim _ {t \rightarrow 0} \frac {1}{t} [ (\phi_ {t} ^ {X}) ^ {*} f (x) - f (x) ]. \tag {3.7.2}$$

命题3.7.1 在局部坐标下Lie导数(3.7.2)可表示为

$$L _ {X} (f) = \langle \mathrm{d} f, X \rangle = \sum_ {i = 1} ^ {n} X _ {i} \frac {\partial f}{\partial x _ {i}}. \tag {3.7.3}$$

证明 由定义： $(\phi_t^X)^*\mathit{f}(\pmb {x}) = f(\phi_t^X (\pmb {x}))$ ，它对 $t$ 的Taylor展式为

$$f (\phi_ {t} ^ {X} (x)) = f (x) + t \mathrm{d} f \cdot X (x) + O (t ^ {2}).$$

将它代入式 (3.7.2) 即得式 (3.7.3).

定义3.7.5 设 $X, Y \in V(M)$ . $Y$ 对 $X$ 的 Lie 导数，记作 $\operatorname{ad}_X(Y)$ ，定义为

$$\operatorname{ad} _ {X} (Y) = \lim _ {t \rightarrow 0} \frac {1}{t} \left(\left(\phi_ {- t} ^ {X}\right) _ {*} Y \left(\phi_ {t} ^ {X} (x)\right) - Y (x)\right). \tag {3.7.4}$$

命题3.7.2 在局部坐标下Lie导数(3.7.4)可表示为

$$\operatorname{ad} _ {X} (Y) = J _ {Y} X - J _ {X} Y = [ X, Y ], \tag {3.7.5}$$

这里 $J_{Y}$ 是 $Y$ 的Jacobi矩阵.

证明 利用Taylor展式，我们有

$$\phi_ {t} ^ {X} (x) = x + (t X) + O \left(t ^ {2}\right), \tag {3.7.6}Y (\phi_ {t} ^ {X} (x)) = Y (x) + J _ {Y} (t X) + O (t ^ {2}). \tag {3.7.7}$$

利用 $\phi_{-t}^{X}$ 的Jacobi矩阵

$$\boldsymbol {J} _ {\phi_ {- t} ^ {X}} = \boldsymbol {I} - t \boldsymbol {J} _ {X} + O (t ^ {2}). \tag {3.7.8}$$

由式 (3.7.6)\~ 式 (3.7.8) 可得

$$\left(\phi_ {- t} ^ {X}\right) _ {*} Y \left(\phi_ {t} ^ {X} (x)\right) = \left(I - t J _ {X} + O \left(t ^ {2}\right)\right) \left(Y (x) + J _ {Y} (t X) + O \left(t ^ {2}\right)\right) \tag {3.7.9}= Y (x) + t \left(J _ {Y} X - J _ {X} Y\right) + O \left(t ^ {2}\right).$$

代入式 (3.7.4) 即得式 (3.7.5).

定义3.7.6 设 $X \in V(M)$ 及 $\omega \in V^{*}(M)$ . $\omega$ 关于 $X$ 的Lie导数, 记作 $L_{X}(\omega)$ , 定义为

$$L _ {X} (\omega) = \lim _ {t \rightarrow 0} \frac {1}{t} \left[\left(\phi_ {t} ^ {X}\right) ^ {*} \omega \left(\phi_ {t} ^ {X} (x)\right) - \omega (x) \right]. \tag {3.7.10}$$

命题3.7.3 在局部坐标下Lie导数(3.7.6)可以表示为

$$L _ {X} (Y) = \left(J _ {\omega} X\right) ^ {\mathrm{T}} + \omega J _ {X}. \tag {3.7.11}$$

证明 类似于命题 3.7.1, 3.7.2 的证明，利用 Taylor 展式可得
