# 4.4 本章要点总结

\- 一阶系统的表达形式：

\- 微分方程： $\frac{\mathrm{d}x(t)}{\mathrm{d}t} + ax(t) = au(t)$ 。

\- 传递函数： $G(s)=\frac{X(s)}{U(s)}=\frac{a}{s+a}$ 。

\- 传递函数极点： $s_{p}=-a$ 。

\- 一阶系统的单位冲激响应：

○ 单位冲激函数： $\left\{\begin{aligned}\delta(t)&=0,t\neq0\\ \int_{-\infty}^{\infty}\delta(t)\mathrm{d}t&=1\end{aligned}\right.$

\- 系统输出的拉普拉斯变换： $X(s)=\frac{a}{s+a}$ 。

\- 冲激响应的时域表达： $x(t)=ae^{-at}$

当 $a > 0$ 时， $s_{\mathrm{p}} < 0$ ，系统收敛于0。当 $a < 0$ 时， $s_{\mathrm{p}} > 0$ ，系统趋于负无穷。

\- 系统对初始条件的响应即冲激响应。

\- 一阶系统的单位阶跃响应：

\- 单位阶跃函数： $u(t)=\left\{\begin{aligned}&1,&t\geqslant0\\ &0,&t<0\end{aligned}\right.$

- 系统输出的拉普拉斯变换： $X(s)=\frac{a}{s(s+a)}$ 。  
单位阶跃响应的时域表达： $x(t)=1-\mathrm{e}^{-at}$ 。  
当 $a > 0$ 时， $s_{\mathrm{p}} < 0$ ，系统收敛于1。当 $a < 0$ 时， $s_{\mathrm{p}} > 0$ ，系统趋于负无穷。  
- 时间常数 $\tau = \frac{1}{a}$ , 此时系统输出在终值状态的 $63\%$ 。  
- 调节时间 $T_{\mathrm{s}} = 4\tau = \frac{4}{a}$ ，此时系统输出达到了终值的 $98\%$ 。  
- 使用相轨迹法可以直观明了地分析系统对于不同初始条件的响应。
