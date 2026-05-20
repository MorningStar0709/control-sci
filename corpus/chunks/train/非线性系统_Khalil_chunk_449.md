$$u = - \left\{\frac {k \rho^ {\mathrm{T}}}{1 + \rho^ {\mathrm{T}} \rho} [ I _ {3} + S (\rho) + \rho \rho^ {\mathrm{T}} ] \right\} ^ {\mathrm{T}} + v = - k \rho + v$$

这里用到性质 $\rho^{T}S(\rho)=0$ 。此外，还需要检验无源系统

$$
\begin{array}{l} \dot {\rho} = \frac {1}{2} \left[ I _ {3} + S (\rho) + \rho \rho^ {T} \right] \omega \\ M \dot {\omega} = - S (\omega) M \omega - k \rho + v \\ y = \omega \\ \end{array}
$$

的零状态可观测性。当 $v = 0$ 时，有

$$y (t) \equiv 0 \Leftrightarrow \omega (t) \equiv 0 \Rightarrow \dot {\omega} (t) \equiv 0 \Rightarrow \rho (t) \equiv 0$$

因此,系统是零状态可观测的,且控制律

$$u = - k \rho - \phi (\omega)$$

可使系统实现全局稳定,其中任意局部利普希茨函数 $\phi$ 满足 $\phi(0)=0$ ,且对于所有 $y\neq0$ ,有 $y^{T}\phi(y)>0$ 。

如果把对 $W(z)$ 的假设加强为

$$\frac {\partial W}{\partial z} f _ {a} (z) < 0, \quad \forall z \neq 0, \quad \frac {\partial W}{\partial z} (0) = 0 \tag {14.83}$$

即 $\dot{z}=f_{a}(z)$ 的原点是全局渐近稳定的, 则可免去检验整个系统(14.80)\~(14.82)的零状态可观测性。取

$$u = - \left(\frac {\partial W}{\partial z} F (z, y)\right) ^ {T} - \phi (y) \tag {14.84}$$

其中 $\phi$ 是任意局部利普希茨函数，满足 $\phi(0) = 0$ ，且对于任意 $y \neq 0$ ，有 $y^{\mathrm{T}}\phi(y) > 0$ 。以 $U$ 作为闭环系统的备选李雅普诺夫函数，可得

$$\dot {U} \leqslant \frac {\partial W}{\partial z} f _ {a} (z) - y ^ {\mathrm{T}} \phi (y) \leqslant 0$$

此外， $\dot{U} = 0$ 表明 $z = 0, y = 0$ ，亦即 $u = 0$ 。如果驱动系统(14.78)～(14.79)是零状态可观测的，则条件 $u(t) \equiv 0$ 和 $y(t) \equiv 0$ 就意味着 $x(t) \equiv 0$ 。因此，由不变原理，原点 $(z = 0, x = 0)$ 是全局渐近稳定的。通过上面的讨论，可以总结出下一个定理。

定理 14.5 假设系统(14.78)\~(14.79)是零状态可观测的,且为无源系统,具有径向无界的正定存储函数。假设 $z=f_{a}(z)$ 的原点是全局渐近稳定的,且设 $W(z)$ 是满足式(14.83)的径向无界正定李雅普诺夫函数,则控制律(14.84)使原点 $(z=0,x=0)$ 全局稳定。

例14.18 考虑例13.16和例14.11讨论过的系统

$$
\begin{array}{l} \dot {\eta} = - \eta + \eta^ {2} \xi \\ \dot {\xi} = u \\ \end{array}
$$

以 $y = \xi$ 作为输出，则系统取(14.77)\~(14.79)的形式。系统 $\xi = u, y = \xi$ 是无源系统，其存储函数为 $V(\xi) = \xi^2 / 2$ 。由于 $y = \xi$ ，显然系统是零状态可观测的。当李雅普诺夫函数为 $W(\eta) = \eta^2 / 2$ 时， $\dot{\eta} = -\eta$ 的原点是全局指数稳定的，因此满足定理14.5的所有条件，且全局稳定状态反馈控制可取为 $u = -\eta^3 - k\xi, k > 0$ ，与用反步法推出的结果相同。
