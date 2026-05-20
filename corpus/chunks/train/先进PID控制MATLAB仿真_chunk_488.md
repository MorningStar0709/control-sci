# 11.3.2 仿真实例

被控对象为一个具有三环结构的伺服系统，如图 11-8，图 11-9 和图 11-10 所示。伺服系统参数和控制参数在程序中给予了描述，系统采样时间为 1ms。取 M=2，此时输入指令为正弦迭加信号： $y_{\mathrm{d}}(t)=A\sin(2\pi Ft)+0.5A\sin(1.0\pi Ft)+0.25A\sin(0.5\pi Ft)$ ，其中 A=0.50，F=0.50。

考虑到 $K_{i}$ 、 L 和 $C_{e}$ 的值很小，前馈补偿系数 $F_{c1}$ 和 $b_{c1}$ 等效到摩擦力矩端的系数可近似写为

$$\mathrm{Gain} \approx K _ {\mathrm{u}} \times K _ {\mathrm{d}} \times 1 / R \times K _ {\mathrm{m}} \times K _ {\mathrm{g}}$$

式中， $K_{\mathrm{g}}$ 为经验系数。则摩擦模型估计系数 $F_{\mathrm{cl}}$ 和 $b_{\mathrm{cl}}$ 为 $F_{\mathrm{cl}} \approx F_{\mathrm{c}} / \mathrm{Gain}$ ， $b_{\mathrm{cl}} \approx b_{\mathrm{c}} / \mathrm{Gain}$ 。

系统总的控制输出为

$$u (t) = u _ {\mathrm{p}} (t) + u _ {\mathrm{f}} (t)$$

式中， $u_{\mathrm{p}}(t)$ 为PID控制的输出，其三项系数为 $k_{\mathrm{pp}} = 15$ ， $k_{\mathrm{ii}} = 0.10$ ， $k_{\mathrm{dd}} = 1.5$ 。

根据是否加入前馈补偿分别进行仿真。无前馈补偿时正弦跟踪如图 11-11 所示，由于静摩擦的作用，在低速跟踪时，位置跟踪存在“平顶”现象，速度跟踪存在“死区”现象。有前馈补偿时的正弦跟踪如图 11-12 所示，采用 PID 控制+前馈控制可很大程度地克服摩擦的影响，基本消除了位置跟踪的“平顶”和速度跟踪的“死区”，实现了较高的位置跟踪和速度跟踪精度。

![](image/0d3e261cccf4d1b75bb0491001c738590d44e340cc1a67e7b41c66141d27fc02.jpg)  
图 11-11 无前馈补偿时位置和速度跟踪

![](image/c73129fb8f4d0c0442daa1b0ef36f7fb279cab507c1ce92dd323b8388bc05d64.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.5 | 0.5 |
| 1.0 | 0.8 | 0.8 |
| 1.5 | 0.9 | 0.9 |
| 2.0 | 0.8 | 0.8 |
| 2.5 | 0.6 | 0.6 |
| 3.0 | 0.3 | 0.3 |
| 3.5 | 0.0 | 0.0 |
| 4.0 | -0.5 | -0.5 |
| 4.5 | -1.0 | -1.0 |
| 5.0 | -1.0 | -1.0 |
</details>

![](image/4b760f2a8bafcb123b3ade788b0d01362c515d98299b09eb534d6577cebb3f90.jpg)

<details>
<summary>line</summary>

| time(s) | ideal speed signal | speed tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 1.0 |
| 0.5 | 0.8 | 0.8 |
| 1.0 | 0.5 | 0.5 |
| 1.5 | 0.2 | 0.2 |
| 2.0 | -0.1 | -0.1 |
| 2.5 | -0.4 | -0.4 |
| 3.0 | -0.7 | -0.7 |
| 3.5 | -0.9 | -0.9 |
| 4.0 | -0.6 | -0.6 |
| 4.5 | -0.2 | -0.2 |
| 5.0 | 0.3 | 0.3 |
</details>

图 11-12 有前馈补偿时位置和速度跟踪
