# 习题 10.1

10.1.1 设 $A$ 生成Banach空间 $X$ 上指数稳定的 $C_0$ 半群 $T(t), f \in C[0, \infty)$ 满足

$\lim_{t \to \infty} f(t) = f_0$ . 设 $y(t)$ 是非齐次方程

$$
\left\{ \begin{array}{l l} \frac {\mathrm{d} y (t)}{\mathrm{d} t} = A y (t) + f (t), & t > 0 \\ y (0) = y _ {0} \end{array} \right.
$$

的温和解. 试证

$$\lim _ {t \rightarrow \infty} y (t) = - A ^ {- 1} f _ {0}.$$

10.1.2 试研究 Timoshenko 梁边界反馈控制系统的稳定性

$$
\left\{ \begin{array}{l l} \rho \ddot {w} + (K (\varphi - w ^ {\prime}) ^ {\prime}) = 0, & 0 <   x <   \ell , t > 0, \\ I _ {\rho} \ddot {\varphi} - (E I \varphi^ {\prime}) ^ {\prime} + K (\varphi - w ^ {\prime}) = 0, & 0 <   x <   \ell , t > 0, \\ w (0, t) = \varphi (0, t) - 0, & t > 0, \\ K (\ell) (\varphi (\ell , t) - w ^ {\prime} (\ell , t)) = u _ {1} (t), & t > 0, \\ - E I (\ell) \varphi^ {\prime} (\ell , t) = u _ {2} (t), & t > 0, \end{array} \right.
$$

其中 $\rho, I_{\rho}, K, EI \in C^{1}[0, \ell]$ , 并且存在常数 $c_{0} > 0$ 使得

$$\rho , I _ {\rho}, K, E I \geqslant c _ {0}.$$

假定 $u_{1}(t), u_{2}(t)$ 取如下边界反馈控制形式：

$$
\left\{ \begin{array}{l} u _ {1} (t) = \alpha \dot {w} (\ell , t) + d _ {1} \dot {\varphi} (\ell , t), \\ u _ {1} (t) = d _ {2} \dot {w} (\ell , t) + \gamma \dot {\varphi} (\ell , t), \end{array} \right.
$$

其中 $\alpha, \gamma, d_1, d_2$ 为适当的反馈增益常数。试研究上述反馈控制系统的稳定性，并证明当矩阵

$$
\boldsymbol {B} = \left[ \begin{array}{c c} \alpha & \frac {d _ {1} + d _ {2}}{2} \\ \frac {d _ {1} + d _ {2}}{2} & \gamma \end{array} \right]
$$

正定时，闭环系统是指数稳定的.
