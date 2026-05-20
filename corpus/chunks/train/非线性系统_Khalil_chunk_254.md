\- $h$ 在 $R^n$ 上是连续正定的。

\- 对于 $x \in G, V(x)$ 满足偏微分方程

$$\frac {\partial V}{\partial x} f (x) = - h (x) [ 1 - V (x) ] \tag {8.17}$$

证明 x=0 是渐近稳定的, 且 G 是吸引区。

8.11 (见文献[72])考虑一个二阶系统

$$\dot {x} _ {1} = - h _ {1} (x _ {1}) + g _ {2} (x _ {2}), \quad \dot {x} _ {2} = - g _ {1} (x _ {1})$$

其中,对于某些正常数 $a_{i}$ 和 $b_{i}$ (允许 $a_{i} = \infty$ 或 $b_{i} = \infty$ )

$$h _ {1} (0) = 0, \quad z h _ {1} (z) > 0 \forall - a _ {1} < z < b _ {1}g _ {i} (0) = 0, \quad z g _ {i} (z) > 0 \forall - a _ {i} < z < b _ {i}\int_ {0} ^ {z} g _ {i} (\sigma) d \sigma \to \infty \text {当} z \to - a _ {i} \text {或} z \to b _ {i}$$

应用 Zubov 定理证明吸引区是 $\left\{x \in R_{2} \mid -a_{i} < x_{i} < b_{i}\right\}$ 。

提示: 取 $h(x)=g_{1}(x)h_{1}(x)$ ，并求偏微分方程(8.17)的解，其中 $V(x)=1-W_{1}(x_{1})W_{2}(x_{2})$ 。

注意,如此选择 $h,\dot{V}(x)$ 只是半负定的,可应用 LaSalle 不变原理。

8.12 求系统 $\dot{x}_1 = -x_1 + x_2$ ， $\dot{x}_2 = -\tan (x_1)$ 的吸引区。

提示:利用前一习题。

8.13 设 $\Omega$ 是包含原点的正不变开集。假设 $\Omega$ 内的每条轨线当 $t$ 趋于无穷时都趋于原点，证明 $\Omega$ 是连通的。

8.14 考虑二阶系统 $\dot{x}=f(x)$ ，其原点是渐近稳定的。设 $V(x)=x_{1}^{2}+x_{2}^{2}, D=\{x\in R^{2}\mid|x_{2}|<1, |x_{1}-x_{2}|<1\}$ 。假设 $[\partial V/\partial x]f(x)$ 在 D 上是负定的，估计吸引区。

8.15 考虑系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = -x_1 - x_2 - (2x_2 + x_1)(1 - x_2^2)$

(a) 应用 $V(x)=5x_{1}^{2}+2x_{1}x_{2}+2x_{2}^{2}$ ，证明原点是渐近稳定的。

(b) 设 $S = \{x \in R^2 \mid V(x) \leqslant 5\} \cap \{x \in R^2 \mid |x_2| \leqslant 1\}$

证明 S 是吸引区的估计值。

8.16 证明系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = -x_2 - x_1 + x_1^3$

的原点是渐近稳定的,并估计其吸引区。

8.17 考虑二阶系统 $\dot{x} = f(x)$ , 其李雅普诺夫函数为 $V(x)$ 。假设对所有 $x_{1}^{2} + x_{2}^{2} \geqslant a^{2}$ , $\dot{V}(x) < 0$ 。图8.6所示为圆 $x_{1}^{2} + x_{2}^{2} = a^{2}$ 上某点的向量场的4个方向。试问这四个方向中哪些是可能的, 哪些是不可能的? 验证你的答案。

8.18 考虑系统

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - x _ {2} - \sin x _ {1} - 2 \operatorname{sat} (x _ {1} + x _ {2})$$

(a) 证明原点是唯一的平衡点。

(b) 应用线性化方法证明原点是渐近稳定的。

(c) 设 $\sigma = x_{1} + x_{2}$ , 证明对于 $|\sigma| \geqslant 1, \dot{\sigma} \leqslant -|\sigma|$

(d) 设 $V(x)=x_{1}^{2}+0.5x_{2}^{2}+1-\cos x_{1}$ ，证明

$$M _ {c} = \{x \in R ^ {2} \mid V (x) \leqslant c \} \cap \{x \in R ^ {2} \mid | \sigma | \leqslant 1 \}, \quad c > 0$$

![](image/9f8a1f84eaeb746c7d6903f0e2fb9560c809fe4d9e355e415fa2685de658b2b6.jpg)

<details>
<summary>text_image</summary>

x₂
2
1
3
4
x₁
x₁² + x₂² = a²
v(x) = x
</details>

图8.6 习题8.17

是正不变集,且当 t 趋于无穷时, $M_{c}$ 内的轨线都趋于原点。

(e) 证明原点是全局渐近稳定的。

8.19 考虑习题 1.8 中的同步发电机模型, 状态变量和参数与习题 1.8 中的 (a) 和 (b) 相同。此外, 取 $\tau = 6.6 \, s, M = 0.0147$ (每单位功率) $\times \, s^{2}/rad, D/M = 4 \, s^{-1}$ 。
