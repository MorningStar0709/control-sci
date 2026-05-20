# 2.4节习题

2.23 精密桌的平面简图如图 2.55 所示，它依靠两角下方执行机构的热膨胀提升或降低各自拐角而使桌面保持水平。各个参数为： $T_{act}$ 为执行机构的温度； $T_{amb}$ 为环境的空气温度； $R_{f}$ 为执行机构和空气之间的热流量系数；C 为执行机构的热容；R 为加热丝电阻。

假定：①执行机构为纯电阻器件，②流入执行机构的热流量与输入电能成正比，③由热膨胀得到的移动量 d 与 $T_{act}$ 和 $T_{amb}$ 之间的差成正比。列写执行机构移动量的大小 d 与外加电压 $v_{i}$ 之间的微分方程。

2.24 如图 2.56a 所示，空调为高层建筑四楼的每个房间以相同的温度提供冷空气。第四层平面图如图 2.56b 所示，冷空气流入每个房间时，等量的热流量 q 流出房间。列写一组控制每个房间温度的微分方程，其中： $T_{0}$ 为建筑物外温度； $R_{0}$ 为热流量穿过外部墙壁的阻力； $R_{1}$ 为热流量穿过内部墙壁的阻力。

假定：①所有房间都是方形的，②无热流量穿过地面和天花板，③每个房间温度是均匀的。利用对称性简化成三个微分方程。

2.25 两水箱液体流量系统如图 2.57 所示，列写流入第一个水箱的流量与流出第二个水箱的流量间的微分方程。

![](image/89b6f3433cd529f65b4b3fcfee92e485d4d005367978fae4580aba547242ce75.jpg)

<details>
<summary>text_image</summary>

Diagram illustrating a mechanical system with a block and a transformer, showing input voltage vi and output voltage di.
</details>

a）由执行机构保持精密桌水平  
b）执行机构侧视图   
图 2.55

![](image/f738fb1496baa4598d056c1f817d1bf4c4196887972ccedc7ddfd2e3cf5e93a0.jpg)

<details>
<summary>text_image</summary>

第四层
b) 第四层平面图
</details>

a）高层建筑

图 2.56 空调建筑  
![](image/0c461d882d60e1cfa0e83f974dd8e2909d6b4b584b918db42fd7e42e04cc0dd5.jpg)

<details>
<summary>text_image</summary>

w_in
w_out
</details>

图 2.57 习题 2.25 的两水箱液体流量系统

2.26 某实验室通过两水箱做水流量的实验如图 2.58 所示。假定方程(2.93)描述了通过 A、B 或 C 处大小相同的孔的流量。

![](image/0f2c5e35f76710c9becbe10b74ef8c10ec0f3b0e796f2e8d5356ef19486ca931.jpg)

<details>
<summary>text_image</summary>

水泵
h₁
A
h₃
B
h₂
C
</details>

图 2.58 习题 2.26 的两水箱液体流量系统

(a) 当孔 B、C 存在但孔 A 不存在时，列写此系统关于 $h_{1}$ 和 $h_{2}$ 的运动方程，假定当 $h_{2}=10cm$ 时，流出量为 200g/min。

(b) 当 $h_{1}=30cm$ 且 $h_{2}=10cm$ 时，求解线性化模型和从水泵流量( $cm^{3}/min$ )到 $h_{2}$ 的传递函数。

(c) 假定孔 B 关闭，孔 A 打开，重新分析 (a) 问和 (b) 问。假设 $h_{3}=20cm$ ， $h_{1}>20cm$ 且 $h_{2}<20cm$ 。

2.27 式(2.81)和式(2.82)为给房屋加热的方程，特殊情况下，用小时表示时间可写为

$$C \frac {\mathrm{d} T _ {\mathrm{h}}}{\mathrm{d} t} = K u - \frac {T _ {\mathrm{h}} - T _ {\mathrm{o}}}{R}$$

其中：

(a) C 为房屋的热容，单位为 Btu/°F $^{-}$ ;  
(b) $T_{h}$ 为屋内温度，单位为 $^{\circ}F$ ;  
(c) $T_{0}$ 为屋外温度，单位为 $^{\circ}F$ ;  
(d) K 为壁炉的额定热流量，K=90 000Btu/h;   
(e) R 为热阻，单位为 $\mathrm{F}/(\mathrm{Btu}/\mathrm{h})$ ;  
(f) u 为壁炉开关，其中，壁炉打开为 1，壁炉关闭为 0。

经测定，外界温度为 $32^{\circ}F$ ，房屋温度为 $60^{\circ}F$ ，当打开壁炉时，温度在 $6\min(0.1h)$ 内上升 $2^{\circ}F$ 。关闭壁炉时，房屋温度在 40min 内下降 $2^{\circ}F$ 。该房屋的 C 和 R 的值为多少？
