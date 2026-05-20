$$\boldsymbol {K} \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K}\right) + \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K}\right) ^ {\mathrm{T}} \boldsymbol {K} + \left(\boldsymbol {Q} + \boldsymbol {K B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K}\right) = \boldsymbol {0}$$

迭代格式为

$$
\begin{array}{l} \boldsymbol {K} _ {i + 1} \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} _ {i}\right) + \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} _ {i}\right) ^ {\mathrm{T}} \boldsymbol {K} _ {i + 1} \\ = - \left(\boldsymbol {Q} + \boldsymbol {K} _ {i} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {K} _ {i}\right) \tag {5-110} \\ \end{array}
$$

上式是关于 $K_{i+1}$ 的线性方程，当已求得第 $i$ 步的 $K_i$ 后，很容易求得下一次迭代值 $K_{i+1}$ 。一般来说迭代不一定收敛，但已证明，若选择初始估计 $K_0$ 使得闭环系统方程 $(A - BR^{-1}B^{\mathrm{T}}K_0)$ 稳定，则迭代将收敛到黎卡提代数方程的唯一正定解。收敛标准可用

$$\sum_ {l, j} ^ {n} \left[ \boldsymbol {K} _ {i + 1} (l, j) - \boldsymbol {K} _ {i} (l, j) \right] ^ {2} \leqslant \varepsilon \tag {5-111}$$

其中， $K(l,j)$ 表示 K 矩阵的第 l 行第 j 列元素， $\varepsilon$ 是指定的小数。
