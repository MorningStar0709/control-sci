# (4) 选择操作

为了确定 $x_{i}(t)$ 是否成为下一代的成员，试验向量 $v_{i}(t + 1)$ 和目标向量 $x_{i}(t)$ 对评价函数进行比较：

$$
x _ {i} (t + 1) = \left\{ \begin{array}{l l} v _ {i} (t + 1), f (v _ {i 1} (t + 1), \dots , v _ {i n} (t + 1)) > f (x _ {i 1} (t), \dots , x _ {i n} (t)) \\ x _ {i j} (t), \quad f (v _ {i 1} (t + 1), \dots , v _ {i n} (t + 1)) \leqslant f (x _ {i 1} (t), \dots , x _ {i n} (t)) \end{array} \right. \tag {10.17}
$$

反复执行步骤(2)至步骤(4)操作,直至达到最大的进化代数G,差分进化基本运算流程如图10-11所示。

![](image/a085eb02bd9ade856221e167e0f01ff544bd55178a97195a2f9a48722d92c97a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["开始"] --> B["初始化种群, DE算法参数"]
    B --> C["计算群体中每个个体的适应度"]
    C --> D{是否满足终止条件?}
    D -->|是| E["最优结果"]
    D -->|否| F["变异操作"]
    F --> G["交叉操作"]
    G --> H["选择操作"]
    H --> I["G=G+1"]
    I --> C
```
</details>

图 10-11 差分进化基本运算流程
