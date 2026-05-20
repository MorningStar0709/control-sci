# 7.3 习题

7.1 利用圆判据,判断下列各标量传递函数的绝对稳定性,并求出系统绝对稳定的扇形区域 $[\alpha,\beta]$ 。

(1) $G(s) = \frac{s}{s^2 - s + 1}$

(6) $G(s) = \frac{s + 1}{(s + 2)^{2}(s - 1)}$

(2) $G(s)=\frac{1}{(s+2)(s+3)}$

(7) $G(s) = \frac{1}{(s + 1)^4}$

(3) $G(s) = \frac{1}{s^2 + s + 1}$

(8) $G(s) = \frac{1}{(s + 1)^2(s + 2)^2}$

(4) $G(s) = \frac{s^2 - 1}{(s + 1)(s^2 + 1)}$

(5) $G(s) = \frac{1 - s}{(s + 1)^2}$

7.2 考虑图 7.1 所示的反馈连接, 其中 $G(s)=2s/(s^{2}+s+1)$ 。

(a) 证明系统对扇形区域[0,1]内的非线性是绝对稳定的。

(b) 证明当 $\psi(y)=\mathrm{sat}(y)$ 时, 系统没有极限环。

7.3 考虑系统 $\dot{x}_1 = -x_1 - h(x_1 + x_2),\quad \dot{x}_2 = x_1 - x_2 - 2h(x_1 + x_2)$

其中 h 是光滑函数, 满足

$$
y h (y) \geqslant 0, \forall y \in R, \quad h (y) = \left\{ \begin{array}{c c c c} c, & & y & \geqslant & a _ {2} \\ 0, & & | y | & \leqslant & a _ {1} \\ - c, & & y & \leqslant & - a _ {2} \end{array} \right.
| h (y) | \leqslant c, \quad \text {当} a _ {1} < y < a _ {2} \quad \text {且} \quad - a _ {2} < y < - a _ {1}
$$

(a) 证明原点是唯一的平衡点。

(b) 根据圆判据证明原点是全局渐近稳定的。

7.4 (见文献[201])考虑系统

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - (\mu^ {2} + a ^ {2} - q \cos \omega t) x _ {1} - 2 \mu x _ {2}$$

其中 $\mu, a, q$ 和 $\omega$ 是正常数。试用图 7.1 的形式表示该系统，其中 $\psi(t, y) = qy \cos \omega t$ ，并用圆判据推导保证系统在原点为指数稳定的 $\mu, a, q$ 和 $\omega$ 值。

7.5 考虑线性时变系统 $\dot{x} = [A + BE(t)C]x$ ，其中 $A$ 是赫尔维茨的， $\|E(t)\|_2 \leqslant 1, \forall t \geqslant 0$ ，且 $\sup_{\omega \in R} \sigma_{\max}[C(j\omega I - A)^{-1}B] < 1$ 。证明原点是一致渐近稳定的。

7.6 考虑系统 $\dot{x}=Ax+Bu$ ，并设 u=-Fx 是稳定的状态反馈控制，即矩阵 $(A-BF)$ 是赫尔维茨的。假设由于物理上的限制，必须用一个限幅器将 $u_{i}$ 的值限定为 $|u_{i}(t)|\leqslant L$ 。闭环系统可用 $\dot{x}=Ax-BL\operatorname{sat}(Fx/L)$ 表示，其中 $\operatorname{sat}(v)$ 是一个向量，其第 i 个分量是饱和函数。

(a) 证明系统可由图7.1的形式表示, 其中 $G(s)=F(sI-A+BF)^{-1}B,\psi(y)=L\ \text{sat}(y/L)-y$ 。  
(b) 用多变量圆判据推导原点渐近稳定的条件。  
(c) 将以上结果应用到下面的情况:

$$
A = \left[ \begin{array}{c c} {0} & {1} \\ {0. 5} & {1} \end{array} \right], \quad B = \left[ \begin{array}{c} {0} \\ {1} \end{array} \right], \quad F = \left[ \begin{array}{c c} {1} & {2} \end{array} \right], \quad L = 1
$$

并估计吸引区。

7.7 用 Popov 判据重解习题 7.1。

7.8 本题针对标量转移函数 $G(s)$ 除一个留数为正的单极点在虚轴上外, 其余所有极点都在左半开平面的情况, 推导 Popov 判据的另一种形式。系统可以表示为

$$\dot {z} = A z - B \psi (y), \quad \dot {v} = - \psi (y), \quad y = C z + d v$$

其中 $d > 0, A$ 是赫尔维茨的， $(A, B)$ 可控， $(A, C)$ 可观测，并且 $\psi$ 属于扇形区域 $(0, k]$ 。设 $V(z, v) = z^{\mathrm{T}} Pz + a(y - Cz)^{2} + b \int_{0}^{y} \psi(\sigma) d\sigma$ ，其中 $P = P^{\mathrm{T}} > 0, a > 0, b \geqslant 0$ 。

(a) 证明 V 是正定的,且径向无界。

(b) 证明 $\dot{V}$ 满足不等式
