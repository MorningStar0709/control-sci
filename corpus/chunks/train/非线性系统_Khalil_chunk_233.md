7.12 应用描述函数法研究 1.2.4 节中负阻振荡器周期解的存在性, 其中 $h(v) = -v + v^{3} - v^{5}/5, \varepsilon = 1$ 。对于每个可能的周期解估计其振荡频率及振荡幅度, 并用计算机仿真确定描述函数结果的准确性。

7.13 考虑图 7.1 所示的反馈连接, 其中 $G(s) = 2bs/(s^{2} - bs + 1)$ , $\psi(y) = \text{sat}(y)$ 。应用描述函数法证明对于足够小的 b > 0, 系统有周期解。应用定理 7.4 验证该结论, 并估计振荡频率及振荡幅度。

![](image/c21381e05a8364a36182a0130bad2c1aafa213324fb724a2833e5716643a3efc.jpg)

<details>
<summary>text_image</summary>

ψ(y)
斜率为k
A
y
(a)
</details>

![](image/511c99b549afa83e96fe447d1aad6af89ec7cc9c110f27a7243a826483774283.jpg)

<details>
<summary>text_image</summary>

ψ(y)
B
A
y
(b)
</details>

![](image/5f9b0d3f6ab55370619bbe98b1a52cdb5e4eb2dbe3391da3e61ccb4522cfcdc9.jpg)

<details>
<summary>text_image</summary>

ψ(y)
斜率为k
A B y
(c)
</details>

图7.24 习题7.10

7.14 考虑图 7.1 所示的反馈连接, 其中

$$
G (s) = \frac {1}{(s + 1) ^ {2} (s + 2) ^ {2}}, \qquad \psi (y) = \left\{ \begin{array}{c c} b y & - 1 \leqslant b y \leqslant 1 \\ \operatorname{sgn} (y) & b | y | > 1 \end{array} \right.
$$

$b > 0$

(a) 应用圆判据, 在保证闭环系统原点全局渐近稳定的前提下, 求出 b 的最大值。  
(b) 应用 Popov 判据, 在保证闭环系统原点全局渐近稳定的前提下, 求出 b 的最大值。  
(c) 应用描述函数法求出 b 的最小值, 使系统可能振荡, 并估计振荡频率。  
(d) 当 b=10 时, 应用定理 7.4 研究周期解的存在性, 对可能存在的振荡

i. 求出频率区间 $\left[\omega_{1},\omega_{2}\right]$ 及幅度区间 $\left[a_{1},a_{2}\right]$ 。

ii. 应用引理 7.1 求高次谐波能量值的上界, 并表示为与一次谐波能量的百分比。  
iii. 对系统进行仿真,并将仿真结果与前面的分析结果进行比较。

(e) 当 b=30 时, 重复(d)。

7.15 当 $G(s)=10/(s+1)^{2}(s+2)$ 时, 重复上一个习题中的 (a) 和 (c)。  
7.16 考虑图 7.1 所示的反馈连接, 这里 $G(s)=1/(s+1)^{3}$ , $\psi(y)$ 是图 7.15 中的分段线性函数, 其中 $\delta=1/k, s_{1}=k, s_{2}=0$ 。

(a) 应用描述函数法研究周期解的存在性, 并求当 k = 10 时可能的振荡频率及振荡幅度。  
(b) 当 k=10 时, 应用定理 7.4, 对于可能存在的振荡, 求出频率区间 $\left[\omega_{1}, \omega_{2}\right]$ 和幅度区间 $\left[a_{1}, a_{2}\right]$ 。  
(c) 可以保证系统无振荡的最大斜率 k > 0 是多少?

7.17 对于下列情况以图 7.1 所示的反馈连接形式,应用定理 7.4 研究其周期解的存在性,并对可能存在的振荡求出频率区间 $\left[\omega_{1},\omega_{2}\right]$ 及幅度区间 $\left[a_{1},a_{2}\right]$ 。

(1) $G(s)=2(s-1)/s^{3}(s+1),\psi(y)=\mathrm{sat}(y)$   
(2) $G(s) = -s/(s^{2} + 0.8s + 8)$ , $\psi(y) = (1/2)\sin y$ .   
(3) $G(s) = -s/(s^{2} + 0.8s + 8)$ , $\psi(y)$ 是习题 7.13 中的非线性特性。  
(4) $G(s) = -24/s^{2}(s + 1)^{3}, \psi(y)$ 是奇对称的,由下式给出:

$$
\psi (y) = \left\{ \begin{array}{l l} y ^ {3} + y / 2, & 0 \leqslant y \leqslant 1 \\ 2 y - 1 / 2, & y \geqslant 1 \end{array} \right.
$$
