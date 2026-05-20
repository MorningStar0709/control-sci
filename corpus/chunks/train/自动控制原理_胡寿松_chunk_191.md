| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.05 |
| 1.0 | 1.02 |
| 1.5 | 1.01 |
| 2.0 | 1.00 |
| 2.5 | 1.00 |
| 3.0 | 1.00 |
</details>

图 3-45 K=20 时系统的单位阶跃响应(实线)及单位阶跃扰动响应(虚线)(MATLAB)

MATLAB 文本如下：

$$\mathbf {K} = [ 1 0 0 2 0 ];\text { for } i = 1: 1: 2\mathrm{sys} = \mathrm{tf} ([ 1 1 \mathrm{K(i)} ], [ 1 1 2 \mathrm{K(i)} ]); \quad \% \text {输入作用下系统闭环传递函数}\mathrm{sysn} = \mathrm{tf} ([ - 1 ], [ 1 1 2 \mathrm{K(i)} ]); \quad \% \text {扰动作用下系统闭环传递函数}\text { figure } (i); t = 0: 0. 0 0 2: 3;\text {step} (\text {sys}, t); \text {hold on}; \quad \% \text {单位阶跃输入响应}\text {step} (\text {sysn}, t); \text {grid} \quad \% \text {单位阶跃扰动响应}$$

end

从图 3-45 可以看出： $t_{p}=0.476s,\sigma\%=3.86\%,t_{s}=0.913s$ 。

钻机控制系统在两种增益情况下的响应性能如表 3-6 所示。由表 3-6 可见，应取 K=20。

表 3-6 钻机控制系统在两种增益情况下的响应性能

<table><tr><td>增益K</td><td>单位阶跃输入下超调量</td><td>单位阶跃输入下调节时间(Δ=2%)</td><td>单位阶跃输入下状态误差</td><td>单位阶跃扰动稳态误差</td></tr><tr><td>100</td><td>22%</td><td>0.666s</td><td>0</td><td>-0.01</td></tr><tr><td>20</td><td>3.86%</td><td>0.913s</td><td>0</td><td>-0.05</td></tr></table>
