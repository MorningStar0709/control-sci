图 3-73 垂直起飞高度控制系统  
![](image/085f56b07a000ed548b1d8ccfc47aae14888928a2f14afa2f2dac30c1b5b3046.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s) 转向指令"] --> B["+"]
    B --> C["10/(s+10)"]
    C --> D["1/s²"]
    D --> E["C(s) 漫游方向"]
    E --> F["H(s)"]
    F --> B
    G["-"] --> B
```
</details>

图 3-74 火星漫游车导向控制系统  
![](image/ec0122a93844204a2bd2f026ca82a74d5dc1a5995b9e35b3e7808829c06cc30e.jpg)

<details>
<summary>text_image</summary>

车体
电磁铁
导向
磁铁
吸引区域
气隙
T形
导轨
</details>

(a) 磁悬浮列车

![](image/b7b9daa067b47fdfb50e75a790aeac09db81a1b2998e22c781226a1b5d7be7a8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s) 预期间隙"] --> B["+"]
    B --> C["Gc(s)"]
    C --> D["控制器"]
    D --> E["车体与悬浮线圈G0(s)"]
    E --> F["(s) 气隙"]
    F --> G["-"]
    G --> B
```
</details>

(b) 间隙控制系统  
图 3-75 磁悬浮列车控制系统

(2) 可否确定 $K_{a}$ 的合适取值, 使系统对单位阶跃输入的稳态跟踪误差为零;  
(3) 取控制器增益 $K_{a}=2$ ，确定系统的单位阶跃响应。
