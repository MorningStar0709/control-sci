In practice, the ports shown in Figure 4–17(a) are often made wider than the corresponding valves. In such a case, there is always leakage through the valves. Such leakage improves both the sensitivity and the linearity of the hydraulic servomotor. In the following analysis we shall make the assumption that the ports are made wider than the valves—that is, the valves are underlapped. [Note that sometimes a dither signal, a high-frequency signal of very small amplitude (with respect to the maximum displacement of the valve), is superimposed on the motion of the pilot valve. This also improves the sensitivity and linearity. In this case also there is leakage through the valve.]

![](image/5bfded43a14e92207b04bd81575ceb21786b25bf077d7b7c2de9de493a55c588.jpg)

<details>
<summary>text_image</summary>

p0 ps p0
x ④① ②③
q q
p1 p2
y
Load
m b
</details>

![](image/9b039abdc902dc021577fb713c8bd7fc3631e00d7e734a9599d757e37ae55939.jpg)

<details>
<summary>text_image</summary>

ps
x0/2 + x
x0/2 - x
①
②
x
</details>

(b)   
Figure 4–17 (a) Hydraulic servo system; (b) enlarged diagram of the valve orifice area.

We shall apply the linearization technique presented in Section 2–7 to obtain a linearized mathematical model of the hydraulic servomotor. We assume that the valve is underlapped and symmetrical and admits hydraulic fluid under high pressure into a power cylinder that contains a large piston, so that a large hydraulic force is established to move a load.

In Figure 4–17(b) we have an enlarged diagram of the valve orifice area. Let us define the valve orifice areas of ports 1, 2, 3, 4 as $A _ { 1 } , A _ { 2 } , A _ { 3 } , A _ { 4 }$ , respectively.Also, define the flow rates through ports 1, 2, 3, 4 as $q _ { 1 } , q _ { 2 } , q _ { 3 } , q _ { 4 }$ , respectively. Note that, since the valve is symmetrical, $A _ { 1 } = A _ { 3 }$ and $A _ { 2 } = A _ { 4 }$ . Assuming the displacement x to be small, we obtain

$$A _ {1} = A _ {3} = k \left(\frac {x _ {0}}{2} + x\right)A _ {2} = A _ {4} = k \left(\frac {x _ {0}}{2} - x\right)$$

where $k$ is a constant.

Furthermore, we shall assume that the return pressure $p _ { o }$ in the return line is small and thus can be neglected. Then, referring to Figure $4 \mathrm { - } 1 7 ( \mathrm { a } )$ , flow rates through valve orifices are
