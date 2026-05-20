# (2) 离散化的几种差分方法

采用 $v(i,j)$ 来描述 $v(x,t)$ ，i 描述 x，j 描述 t，中心点取 $(i,j)$ 的离散点示意图如图 13-13 所示。

![](image/35573838a8df7afeb559c640ceeafa2d10b33bd06ca56cc71d366b283a6535c1.jpg)

<details>
<summary>text_image</summary>

j-1
中心点j
j+1
t
</details>

图 13-13 离散点示意图

取时间间隔为 $\Delta t$ ，采用差分求 $v(x,t)$ 的离散值方法有三种，描述如下：

① 向后差分： $\left.\frac{\partial v}{\partial t}\right|_{t=i}=\frac{v(i,j)-v(i,j-1)}{\Delta t}$ 。

② 向前差分： $\left.\frac{\partial v}{\partial t}\right|_{t=i}=\frac{v(i,j+1)-v(i,j)}{\Delta t}$ 。

③ 中心差分为向前差分与向后差分之和的平均值： $\left.\frac{\partial v}{\partial t}\right|_{t=i}=\frac{v(i,j+1)-v(i,j-1)}{2\Delta t}$ 。

在离散化的程序设计中，可根据需要采用上述 3 种方法之一。
