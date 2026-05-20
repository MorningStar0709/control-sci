# 例 9.18 饱和非线性扇形区

考虑如图 9.52 所示的饱和非线性函数，确定此函数的扇形区。

解答。此函数上方由一条斜率为1的直线界定，所以 $k_{2}=1$ ；且由x轴界定下方，则 $k_{1}=0$ ，如图所示。因此，函数的扇形区为 $[0,1]$ 。

![](image/77facc1001e67e465e96d41682d908646618fb6a2a553118d2bebca865a0427d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["r ≡ 0"] --> B["+"]
    B --> C["Σ"]
    C --> D["G(s)"]
    D --> E["O y"]
    F["f(t, y)y"] --> C
    G["时变非线性系统"] --> H["y"]
    H --> E
    I["-"] --> C
```
</details>

图 9.50 非线性系统框图

![](image/df29727a99029797d5c6adf72ce335df80ba036a868892f7d9165dc38d5b6a08.jpg)

<details>
<summary>text_image</summary>

f(t,y)y
斜率为k₂
斜率为k₁
O
y
</details>

图9.51 限制在一定扇形区的非线性的输出

![](image/d9adb6cf7439270cfa1f83ca63621282aea367d5a4a953ec82814ae029b354f3.jpg)

<details>
<summary>line</summary>

| 输入 | 输出 |
| --- | --- |
| 0 | 0 |
| 0.1 | 0.1 |
</details>

图 9.52 饱和扇形区
