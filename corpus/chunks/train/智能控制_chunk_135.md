# (1) 交运算算子

设 $C = A \cap B$ ，有 3 种模糊算子。

① 模糊交算子

$$\mu_ {C} (x) = \min \{\mu_ {A} (x), \mu_ {B} (x) \} \tag {3.13}$$

② 代数积算子

$$\mu_ {C} (x) = \mu_ {A} (x) \cdot \mu_ {B} (x) \tag {3.14}$$

③有界积算子

$$\mu_ {C} (x) = \max \{0, \mu_ {A} (x) + \mu_ {B} (x) - 1 \} \tag {3.15}$$

(2) 并运算算子

设 $C = A \cup B$ ，有 3 种模糊算子。

① 模糊并算子

$$\mu_ {C} (x) = \max \left\{\mu_ {A} (x), \mu_ {B} (x) \right\} \tag {3.16}$$

② 代数和算子

$$\mu_ {C} (x) = \mu_ {A} (x) + \mu_ {B} (x) - \mu_ {A} (x) \cdot \mu_ {B} (x) \tag {3.17}$$

③有界和算子

$$\mu_ {C} (x) = \min \left\{1, \mu_ {A} (x) + \mu_ {B} (x) \right\} \tag {3.18}$$

(3) 平衡算子

当隶属函数取大、取小运算时，不可避免地要丢失部分信息，采用一种平衡算子，即“ $\gamma$ 算子”，可起到补偿作用。

设 A 和 B 经过平衡运算后得 C，则

$$\mu_ {C} (x) = \left[ \mu_ {A} (x) \cdot \mu_ {B} (x) \right] ^ {1 - \gamma} \cdot \left[ 1 - \left(1 - \mu_ {A} (x)\right) \cdot \left(1 - \mu_ {B} (x)\right) \right] ^ {\gamma} \tag {3.19}$$

式中， $\gamma$ 取值为 $[0,1]$ 。当 $\gamma = 0$ 时， $\mu_{C}(x) = \mu_{A}(x) \cdot \mu_{B}(x)$ ，相当于 $A \cap B$ 时的代数积算子；当 $\gamma = 1$ 时， $\mu_{C}(x) = \mu_{A}(x) + \mu_{B}(x) - \mu_{A}(x) \cdot \mu_{B}(x)$ ，相当于 $A \cup B$ 时的代数和算子。

平衡算子目前已经应用于德国 Inform 公司研制的著名模糊控制软件 Fuzzy-Tech 中。
