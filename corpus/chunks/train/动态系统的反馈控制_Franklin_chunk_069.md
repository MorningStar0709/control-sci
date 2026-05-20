# 2.1.5 分布参数系统

在前面所提出的例子中，尽管有些是通过弹簧彼此相连，但都含有一个或多个刚体。像卫星的太阳能面板、飞机的机翼或机器臂，这些实际的结构通常是弯曲的。如图2.23a所示的柔性梁就是这种情况。描述其运动的方程是一个四阶偏微分方程，这是因为质量是沿着这个梁连续分布的，每一部分之间都有微量变化，这类系统称为分布参数系统。本节提出的动态分析方法还不足以分析这种情况，而在更深入的文献（Thomson and Dahleh，1998）中证明了：

$$E I \frac {\partial^ {4} w}{\partial x ^ {4}} + \rho \frac {\partial^ {2} w}{\partial t ^ {2}} = 0 \tag {2.32}$$

![](image/887e92317193043a5ce362cb79e5de4a18266ebfd5e286864bdd753b7bbbe2a9.jpg)

<details>
<summary>natural_image</summary>

Person using a 5G motor in an urban park with palm trees and a distant building (no visible text or symbols)
</details>

图 2.22 Segway(同倒立摆相似，通过反馈控制系统保持直立)
(图片来源：David Powell)

其中：E 为弹性模量；I 为转动惯量； $\rho$ 为密度；w 为沿梁长度 x 处的挠度。

![](image/90527d1e897185823ff44950fdc01f0dfb99fcc2833e373795f319e687dcba31.jpg)

<details>
<summary>natural_image</summary>

Mechanical device with articulated arms and wiring, no visible text or symbols
</details>

a）斯坦福大学研究使用的柔性机器臂

![](image/306a3436e025cdd8ef4d5033e1ad9490f9849daec4c11861705803834316ad4f.jpg)

<details>
<summary>text_image</summary>

w
</details>

b）连续柔性梁模型

![](image/ea9871b9b224f65b374ee2afd6fe365164ed41024bd5084f40f5cb4891249df9.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a mechanical lever with a spiral base (no text or symbols)
</details>

c）起始弯曲部分的简化模型

![](image/33965f4abbd43c992f84d850ce8f3cfa80e6362f2fb288b12e6d588fc5d2cc86.jpg)

<details>
<summary>natural_image</summary>

Diagram of a mechanical linkage with three spiral components (no text or symbols)
</details>

d）前两个弯曲部分模型  
图2.23  
(图片来源：E. Schmitz)

在设计控制系统时，对式(2.32)精确求解是相当麻烦的，但在控制系统设计时描述总的弯曲效果通常很重要。

图 2.23b 所示的连续梁有无数振动模块，都具有不同的频率。通常，频率最低的模块振幅最大，且要求尽可能地精确近似。图 2.23c 的简化模型表示梁起始弯曲部分和频率，通常对控制器设计已足够了。如果在控制系统运行中，预期有比起始弯曲部分频率更高的模块，则必须建立如图2.23d所示的模型，这个模型用来近似前两个弯曲模块和频率。同样，如果认为更高的精确性和复杂性是必要的，那么可以应用更高阶模型（Schmitz，1985；Thomson and Dahleh，1998）。当一个连续弯曲物体近似为两个或更多通过弹簧连接的刚体时，该模型有时称为集中参数模型。
