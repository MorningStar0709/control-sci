$$\Delta Q _ {1} - \Delta Q _ {2} = C _ {2} \frac {\mathrm{d} \Delta h _ {2}}{\mathrm{d} t} \tag {2-62}\Delta Q _ {1} = \frac {\Delta h _ {1}}{R _ {1}}, \quad \Delta Q _ {2} = \frac {\Delta h _ {2}}{R _ {2}} \tag {2-63}\Delta Q _ {i} - \Delta Q _ {1} = C _ {1} \frac {\mathrm{d} \Delta h _ {1}}{\mathrm{d} t} \tag {2-64}\Delta Q _ {i} = K _ {u} \Delta u \tag {2-65}$$

式中， $C_{1}$ 和 $C_{2}$ 为两液槽的容量系数； $R_{1}$ 和 $R_{2}$ 为两液槽的液阻。将式(2-63)代入式(2-62)，得

$$\frac {\Delta h _ {1}}{R _ {1}} - \frac {\Delta h _ {2}}{R _ {2}} = C _ {2} \frac {\mathrm{d} \Delta h _ {2}}{\mathrm{d} t}$$

故有 $\Delta h_{1} = R_{1}\left(C_{2}\frac{\mathrm{d}\Delta h_{2}}{\mathrm{d}t} +\frac{\Delta h_{2}}{R_{2}}\right)$ (2-66)

$$\frac {\mathrm{d} \Delta h _ {1}}{\mathrm{d} t} = R _ {1} C _ {2} \frac {\mathrm{d} ^ {2} \Delta h _ {2}}{\mathrm{d} t ^ {2}} + \frac {R _ {1}}{R _ {2}} \frac {\mathrm{d} \Delta h _ {2}}{\mathrm{d} t} \tag {2-67}$$

将式(2-65)及式(2-63)代入式(2-64)，得

$$C _ {1} \frac {\mathrm{d} \Delta h _ {1}}{\mathrm{d} t} + \frac {\Delta h _ {1}}{R _ {1}} = K _ {u} \Delta u$$

分别将式(2-66)和式(2-67)代入上式,整理后可得双容水槽的微分方程

$$T _ {1} T _ {2} \frac {\mathrm{d} ^ {2} \Delta h _ {2}}{\mathrm{d} t ^ {2}} + (T _ {1} + T _ {2}) \frac {\mathrm{d} \Delta h _ {2}}{\mathrm{d} t} + \Delta h _ {2} = K \Delta u \tag {2-68}$$

式中， $T_{1}=R_{1}C_{1}$ 为第一个水槽的时间常数； $T_{2}=R_{2}C_{2}$ 为第二个水槽的时间常数；K 为双容水槽的传递系数。

在零初始条件下，对式(2-68)进行拉氏变换，得双容水槽的传递函数

$$G (s) = \frac {\Delta H _ {2} (s)}{\Delta U (s)} = \frac {K}{T _ {1} T _ {2} s ^ {2} + (T _ {1} + T _ {2}) s + 1} \tag {2-69}$$

若双容水槽调节阀1开度变化所引起的流入水量变化还存在纯延迟，则其传递函数不难导出为

$$G (s) = \frac {K}{T _ {1} T _ {2} s ^ {2} + (T _ {1} + T _ {2}) s + 1} \mathrm{e} ^ {- \sigma} \tag {2-70}$$
