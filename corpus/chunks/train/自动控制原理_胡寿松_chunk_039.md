# 6. 磁盘驱动读取系统

磁盘驱动器广泛用于各类计算机中, 是控制工程的一个重要应用实例。考察图 1-16 所示的磁盘驱动器结构示意图可知, 磁盘驱动器读取装置的目标是将磁头准确定位, 以便正确读取磁盘上磁道的信息, 因此需要进行精确控制的变量是安装在滑动簧片上的磁头位置。磁盘旋转速度在 $1800 \sim 7200 \mathrm{r} / \mathrm{min}$ , 磁头位置精度要求为 $1 \mu \mathrm{m}$ , 且磁头由磁道 $a$ 移动到磁道 $b$ 的时间小于 $50 \mathrm{~ms}$ 。

图 1-17 给出了该系统的初步方案, 其闭环系统利用电机驱动磁头臂到达预期的位置。

![](image/0140d59ebfc8ce7ebd7ef5c005ccf400c20bf1735413d8d764010f5458e62eca.jpg)

<details>
<summary>text_image</summary>

转轴
磁头滑片
臂的转动
支持臂
磁盘
磁道a
磁道b
执行电机
</details>

图 1-16 磁盘驱动器结构示意图

![](image/9caccdcbc28dc55ceddc9165891c6f1acb0a30aff1e0f721ba35e05494464746.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["预期磁头位置"] --> B["+"]
    B --> C["偏差"]
    C --> D["控制装置"]
    D --> E["执行电机和臂"]
    E --> F["实际磁头位置"]
    F --> G["传感器"]
    G --> B
```
</details>

图 1-17 磁盘驱动读取系统初步方案
