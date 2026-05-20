仿照“1)”讨论，在给定参数值下，线性区间奇点 $\left(\frac{V_{0}}{K},0\right)$ 为稳定焦点；负饱和区内特殊的等倾线为 $\dot{e}=KM_{0}+V_{0}(k=\alpha=0)$ ；正饱和区内特殊的等倾线为 $\dot{e}=-KM_{0}+V_{0}(k=\alpha=0)$ 。综上知 $r(t)=V_{0}t$ 对系统运动的影响，与 $r(t)=R\cdot1(t)$ 的情况相比较，奇点将沿横轴向右平移 $\frac{V_{0}}{K}$ ，两条特殊的等倾线将沿纵轴向上平移 $V_{0}$ 。对于初始条件 $c(0)=c_{0},\dot{c}(0)=\dot{c}_{0}$ ，由于 $\dot{r}(0)=V_{0},r(0)=0$ ，故 $e(0)=-c_{0},\dot{e}(0)=V_{0}-\dot{c}_{0}$ 。而正因为奇点和特殊的等倾线的平移使奇点的虚实发生变化，特别是系统相轨迹的运动变得复杂，所以需根据参数K及输入系数 $V_{0}$ ，分别加以研究，下面仅讨论其中的三种情况。

当 $V_{0} = 1.2 > KM_{0}$ 时，线性区内，相轨迹奇点(0.3,0)为稳定焦点，且为虚奇点，饱和区的两条特殊的等倾线均位于相平面的上半平面。系统的相平面图如图8-32(a)所示，起始于任何初始点的相轨迹将沿正饱和区的特殊相轨迹发散至无穷。

![](image/173f497627dcb259da54e0019ad975ba8cc3ed79efb8a9f69a37dd6c61a969ca.jpg)

<details>
<summary>text_image</summary>

a=0 \u03b1=KM₀
e<-e₀
|e|≤e₀
a=0 \u03b1=-KM₀
e>e₀
</details>

(a) 等倾线法  
![](image/ffe4c54d6986a49fb09e6c1515954fd5117f2811b2d45de4a9e7f3237b106b26.jpg)

<details>
<summary>line</summary>

| e | ω |
| --- | --- |
| 0.0 | 0.3 |
| 0.1 | 0.2 |
| 0.2 | 0.1 |
| 0.3 | 0.0 |
| 0.4 | -0.1 |
| 0.5 | -0.2 |
| 0.6 | -0.3 |
| 0.7 | -0.4 |
| 0.8 | -0.5 |
| 0.9 | -0.6 |
| 1.0 | -0.7 |
| 1.1 | -0.8 |
| 1.2 | -0.9 |
| 1.3 | -1.0 |
| 1.4 | -1.1 |
| 1.5 | -1.2 |
| 1.6 | -1.3 |
| 1.7 | -1.4 |
| 1.8 | -1.5 |
| 1.9 | -1.6 |
| 2.0 | -1.7 |
</details>

(b) MATLAB法

![](image/3e26c2877d450aaf5236b3315924997368b385fa4edfb83363bcae05d4ba3a87.jpg)

<details>
<summary>line</summary>

| t | c(t) | e(t) |
| --- | --- | --- |
| 0 | 0.0 | 2.0 |
| 2 | 1.0 | 1.0 |
| 4 | 2.3 | -0.5 |
| 6 | 2.0 | 0.0 |
| 8 | 2.0 | -0.1 |
| 10 | 2.0 | -0.1 |
| 12 | 2.0 | -0.1 |
| 14 | 2.0 | -0.1 |
| 16 | 2.0 | -0.1 |
</details>

(c) 时间响应(MATLAB)  
图 8-31 $r(t)=2\cdot1(t)$ 具有饱和特性的非线性系统相轨迹

MATLAB 文本：

$$t = 0: 0. 0 1: 1 6; e 0 = [ 2 0 ]; [ t, e ] = \text { ode45 } (\text { fun0 }, t, e 0);$$

figure(1);

$$\operatorname{plot} (\mathrm{e} (:, 1), \mathrm{e} (:, 2)); \text { grid }$$

figure(2);

$$\text { subplot } (2, 1, 1); \text { plot } (t, 2 - e (:, 1)); \text { grid };\text { subplot } (2, 1, 2); \text { plot } (t, e (:, 1)); \text { grid }$$

调用函数：

$$\text { function de } = \text { fun0(t,e) }\mathrm{del} = \mathrm{e} (2);\text { if } (e (1) < - 0, 2)\mathrm{de} 2 = 0. 2 * 4 - \mathrm{e} (2);\text { elseif } (\mathrm{abs} (e (1)) < 0. 2)\mathrm{de} 2 = - 4 * \mathrm{e} (1) - \mathrm{e} (2);\text { else } \mathrm{de} 2 = - 0. 2 * 4 - \mathrm{e} (2);$$

end

$$\mathrm{de} = [ \text { de1 de2 } ];$$
