$$t _ {r} = \frac {\pi - \beta}{\omega_ {d}} = \frac {\pi - \arccos \zeta}{\omega_ {n} \sqrt {1 - \zeta^ {2}}} = 0. 1 6 2 \mathrm{s}t _ {p} = \frac {\pi}{\omega_ {d}} = 0.314 \mathrm{s}, \quad t _ {s} = \frac {4 . 4}{\zeta \omega_ {n}} = 8.8 \mathrm{s} (\Delta = 2 \%)$$

PD 控制时: $\zeta_{d} = 0.6, z = \frac{K}{11} = 9.09$

$$r = \frac {\sqrt {z ^ {2} - 2 \zeta_ {d} \omega_ {n} z + \omega_ {n} ^ {2}}}{z \sqrt {1 - \zeta_ {d} ^ {2}}} = 1. 1 8, \quad \beta_ {d} = \arctan \left(\frac {\sqrt {1 - \zeta_ {d} ^ {2}}}{\zeta_ {d}}\right) = 5 3. 1 3 ^ {\circ}\varphi = - \pi + \arctan \left[ \frac {\omega_ {n} \sqrt {1 - \zeta_ {d} ^ {2}}}{z - \zeta_ {d} \omega_ {n}} \right] + \arctan \left[ \frac {\sqrt {1 - \zeta_ {d} ^ {2}}}{\zeta_ {d}} \right] = - 5 8 ^ {\circ}$$

动态性能 $t_r = \frac{0.9}{\omega_n} = 0.09\mathrm{s},\quad t_p = \frac{\beta_d - \varphi}{\omega_n\sqrt{1 - \zeta_d^2}} = 0.24\mathrm{s}$

$$t _ {s} = \frac {4 . 0 + \ln r}{\zeta_ {d} \omega_ {n}} = 0. 5 2 \mathrm{s} (\Delta = 2 \%)\sigma \% = r \sqrt {1 - \zeta_ {d} ^ {2}} \mathrm{e} ^ {- \zeta_ {d} \omega_ {n} t _ {p}} \times 100 \% = 22.4 \%$$

应用 MATLAB 仿真, 可得 $\sigma\% = 22\%, t_s = 0.66s$ , 系统时间响应曲线如图 3-44 所示。

![](image/8dc2d72de4b8879b736de9f1f5473d6588e6185b53bc40ab956d0a1e5f787b16.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.25 | 1.2 |
| 0.5 | 1.0 |
| 1.0 | 1.0 |
| 3.0 | 1.0 |
</details>

图 3-44 K = 100 时系统的单位阶跃响应(实线)及单位阶跃扰动响应(虚线)(MATLAB)

2) 取 K=20，则 $\omega_{n}=4.47, e_{\mathrm{sm}}(\infty)=-0.05$ 。

P 控制时： $\zeta = \frac{1}{2\omega_n} = 0.11$

动态性能 $\sigma\%=70.6\%$ , $t_{r}=0.38s$

$$t _ {p} = 0.71 \mathrm{s}, \quad t _ {s} = 8.95 \mathrm{s} (\Delta = 2 \%)$$

动态性能仍然很差。

PD 控制时: $\zeta_{d} = 1.34$

且有 $z = 1.82$ ，闭环传递函数

$$\Phi (s) = \frac {1 1 (s + 1 . 8 2)}{(s + 2) (s + 1 0)}$$

系统此时为有零点的过阻尼二阶系统。令 $R(s) = \frac{1}{s}$ ，则系统输出为

$$C (s) = \Phi (s) R (s) = \frac {1 1 (s + 1 . 8 2)}{s (s + 2) (s + 1 0)} = \frac {1}{s} + \frac {0 . 1 2 5}{s + 2} - \frac {1 . 1 2 5}{s + 1 0}$$

系统的单位阶跃响应

$$c (t) = 1 + 0. 1 2 5 \mathrm{e} ^ {- 2 t} - 1. 1 2 5 \mathrm{e} ^ {- 1 0 t}$$

可以求得： $t_{p}=0.5s,\sigma\%=3.8\%,t_{s}=1.0s(\Delta=2\%)$ ，其中超调量是由闭环零点引起的。

应用 MATLAB 软件包, 可得 K=20 时系统对单位阶跃输入和单位阶跃扰动的响应曲线, 如图 3-45 所示。此时, 系统响应的超调量较小, 扰动影响不大, 其动态性能可以满足工程要求。

![](image/ce21a7c8a8b43fa82279b5314f6aca322f32805449bbcd14b69cade04acf2eac.jpg)

<details>
<summary>line</summary>
