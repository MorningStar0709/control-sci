# 2. 结构图的等效变换和简化

由控制系统的结构图通过等效变换(或简化)可以方便地求取闭环系统的传递函数或系统输出量的响应。实际上, 这个过程对应于由元部件运动方程消去中间变量求取系统传递函数的过程。例如, 在例 2-10 中, 由两相伺服电动机三个方程式消去中间变量 $M_{m}$ 及 $M_{s}$ 得到传递函数 $\Theta_{m}(s)/U_{a}(s)$ 的过程, 对应于将图 2-23(h) 虚线内的四个方框简化为图 2-23(i) 中一个方框的过程。

![](image/2bdcab6bef73e7c29e416e1e649e497b7e3b236426f2c8de6800c0a74a501212.jpg)  
(a)

![](image/d2f5c30203dca4ed4e608ee9a4cbad72dcc1da3d6875fbc93c18ae78155d7f17.jpg)  
(b)

![](image/fc923df66c80913af388329e2516b743f69f983504177a8409ed98138c0ef15f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["M_s"] --> B((+))
    C["M_m"] --> B
    B --> D["1/(Cωs)"]
    D --> E["Θ_m(s)"]
```
</details>

(c)

![](image/50c10ed1a6373b169589f6618155d48ce87df120188033adfa41590f5710a180.jpg)  
(d)

![](image/69f5a8a68594a6f1040b65a6a86669e0a1c5ab43fe8de55241e2e30c8f883fa7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Θm(s)"] --> B["Jm s²"]
    A --> C["f_m s"]
    B --> D((+))
    C --> D
    D --> E["M_m"]
    E --> D
```
</details>

(e)

![](image/86822635dff1983630ff02b3067a34042cef1f4fe62d8ad0fa037954d67c4efb.jpg)  
(f)

![](image/704698968b0021f3b5acf129394b798b7b509451e107d1d6f920edf997b43b10.jpg)

(g)   
![](image/8b8ef93a08d18f9431a109980bba9d002cd3650bcaa90f73526df7ebb39d057c.jpg)

<details>
<summary>flowchart</summary>
