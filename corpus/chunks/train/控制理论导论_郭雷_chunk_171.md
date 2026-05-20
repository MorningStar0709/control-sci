$$a | x | ^ {b} \leqslant V (t, x). \quad \forall x \in \mathbb {R} ^ {n}.$$

且 $V(t, x)$ 还具有无穷小上界，则方程 (2.4.27) 的零解指数稳定蕴含方程 (2.4.26) 的零解指数稳定；

(6) 如果存在函数 $\varphi(r), \psi(r) \in KR$ , 使得

$$\varphi (| x |) \leqslant V (t, x) \leqslant \psi (| x |),$$

则方程 (2.4.27) 的零解全局一致渐近稳定蕴含方程 (2.4.26) 的零解全局一致渐近稳定.

定理 2.4.14 $^{[10]}$ 设 $f(\cdot,\cdot)\in C(\Omega_{n+1}^{a},\mathbb{R}^{n})$ . $h(\cdot,\cdot)\in C(J\times J_{a},\mathbb{R}_{+})$ . 其中 $\Omega_{n+1}^{a}\stackrel{\mathrm{def}}{=} \{(t,x)\mid t\geqslant0,|x|<a\}$ , $J_{a}\stackrel{\mathrm{def}}{=} [0,a].a>0$ . 如果在 $\Omega_{n+1}^{a}$ 上存在具有无穷小上界的正定连续函数 $V(t,x)$ 满足

$$\left. D _ {+} V \right| _ {(2. 3. 1)} \geqslant h (t, V),$$

则标量微分方程 (2.4.27) 的零解不稳定蕴含向量微分方程 (2.4.26) 的零解不稳定.

基于2.2中的比较定理，根据定理条件及稳定性、不稳定性等的定义，不难得到定理2.4.13和定理2.4.14的结论．详细证明参见文献[10].

例2.4.4 考察宇宙飞船的姿态运动。在工程上，常用飞行器绕惯量主轴运动的欧拉方程来表征其姿态运动，即

$$
\left\{ \begin{array}{l} A _ {1} \dot {\omega} _ {x} - (B _ {1} - C _ {1}) \omega_ {y} \omega_ {z} = T _ {x}, \\ B _ {1} \dot {\omega} _ {y} - (C _ {1} - A _ {1}) \omega_ {z} \omega_ {x} = T _ {y}, \\ C _ {1} \dot {\omega} _ {z} - (A _ {1} - B _ {1}) \omega_ {x} \omega_ {y} = T _ {z}, \end{array} \right. \tag {2.4.28}
$$

其中 $A_{1} > 0, B_{1} > 0, C_{1} > 0$ 表示围绕飞行器三个惯量主轴的惯量矩， $\omega_{x}, \omega_{y}, \omega_{z}$ 表示围绕三个惯量主轴的角速度， $T_{x}, T_{y}, T_{z}$ 表示控制飞行器姿态运动的力矩，简称为控制力矩.

假设飞行器在某轨道上飞行时受干扰的作用，偏离了某个正确的姿态。因此，需要施加控制力矩使飞行器回到正确的姿态上来。当然这个过程应该尽可能快地完成。要做到这点，需要采用非线性控制力矩 $^{[9]}$ 。为了便于工程上实现，取如下形式的线性控制力矩：

$$T _ {x} = k _ {1} A _ {1} \omega_ {x}, \quad T _ {y} = k _ {2} B _ {1} \omega_ {y}, \quad T _ {z} = k _ {3} C _ {1} \omega_ {z}, \tag {2.4.29}$$

其中 $k_{1}, k_{2}, k_{3}$ 为待定常数.

下面选择 $k_{1}, k_{2}, k_{3}$ 使飞行器达到某一指定姿态。为了使处理过程规范化，我们记

$$x _ {1} = \omega_ {x}, \quad x _ {2} = \omega_ {y}, \quad x _ {3} = \omega_ {z},$$

并且 $\omega_{x} = \omega_{y} = \omega_{z} = 0$ 取为某指定的姿态（当指定姿态 $[\omega_{x0},\omega_{y0},\omega_{z0}] \neq 0$ 时，作一平移变换总能化为 $[\omega_{x0},\omega_{y0},\omega_{z0}] = 0$ 的情况）.

这时欧拉方程 (2.4.28) 变为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} - \left(\frac {B _ {1}}{A _ {1}} - \frac {C _ {1}}{A _ {1}}\right) x _ {2} x _ {3} = k _ {1} x _ {1}, \\ \dot {x} _ {2} - \left(\frac {C _ {1}}{B _ {1}} - \frac {A _ {1}}{B _ {1}}\right) x _ {3} x _ {1} = k _ {2} x _ {2}, \\ \dot {x} _ {3} - \left(\frac {A _ {1}}{C _ {1}} - \frac {B _ {1}}{C _ {1}}\right) x _ {1} x _ {2} = k _ {3} x _ {3}. \end{array} \right. \tag {2.4.30}
$$
