$G2 = tf(10, [1, 20, 0])$ ; %负载传递函数

$\mathrm{Gp} = \mathrm{tf}(72.58,[1,72.58])$ ；%前置滤波的传递函数

$$\mathrm{G} 3 = \text { series } (\mathrm{Gc}, \mathrm{G} 1);\mathrm{G} = \text { series } (\mathrm{G3}, \mathrm{G2});$$

G4=feedback(G,1); %无前置滤波器时系统的闭环传递函数

G5=series(Gp,G4); %有前置滤波器时系统的闭环传递函数

G6=feedback(G2,G3); %系统的扰动闭环传递函数

figure(1); step(G4); grid

figure(2); step(G5); grid

figure(3); step(G6); grid

![](image/d713c8d314fc0b34ca5a92a0b67996f4f1ca6b8fc37700c7bb8bbd52e0c6baed.jpg)

<details>
<summary>line</summary>

| Time | Amplitude |
| --- | --- |
| 0.00 | 0.0 |
| 0.01 | 0.4 |
| 0.02 | 0.8 |
| 0.03 | 0.95 |
| 0.04 | 1.0 |
| 0.05 | 1.0 |
| 0.06 | 1.0 |
</details>

(a) 单位阶跃输入响应

![](image/27987c65140db5232ebfcb2fbd9d02f026d24943350373ae812a7c54816914e8.jpg)

<details>
<summary>line</summary>

| Time | Amplitude (×10⁻⁴) |
| --- | --- |
| 0.00 | 0.0 |
| 0.01 | 2.5 |
| 0.02 | 5.0 |
| 0.03 | 6.5 |
| 0.04 | 7.0 |
| 0.05 | 7.0 |
| 0.06 | 7.0 |
</details>

(b) 单位阶跃扰动响应  
图 6-46 有前置滤波器时系统的时间响应(MATLAB)
