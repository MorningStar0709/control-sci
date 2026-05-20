# 9.5.3 RBF 网络自校正控制算法

分别采用两个 RBF 网络分别实现未知项 $g[\cdot]$ , $\varphi[\cdot]$ 的逼近。RBF 网络逼近器的结构如图 9-18 所示，W 和 V 分别为两个神经网络的权值向量。

![](image/3e187eba552c73cd39a0fdd06537276965778e48eb2b0930159d8fa2795b4e18.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u(k)"] --> B(( ))
    B --> C["ŷ(k)"]
    D["V"] --> E["H"]
    D --> F["H"]
    D --> G["H"]
    E --> H["ŷ(k)"]
    F --> H
    G --> H
    H --> I["y(k)"]
    J["Nφ[·"]] --> K["ŷ(k)"]
    L["Ng[·"]] --> M["ŷ(k)"]
    N["y(k)"] --> O["ŷ(k)"]
    P["ŷ(k)"] --> Q["ŷ(k)"]
    R["W"] --> S["H"]
    R --> T["H"]
    R --> U["H"]
    S --> V["ŷ(k)"]
    T --> V
    U --> V
    V --> W["ŷ(k)"]
```
</details>

图 9-18 神经网络逼近器

在 RBF 网络结构中, 取网络的输入为 $y(k)$ , 网络的径向基向量为 $H = [h_{1}, \cdots, h_{m}]^{T}$ , $h_{j}$ 为高斯基函数, 即

$$h _ {j} = \exp \left(- \frac {\| y (k) - \mathbf {C} _ {j} \| ^ {2}}{2 b _ {j} ^ {2}}\right) \tag {9.11}$$

式中， $j=1,\cdots,m$ 。 $b_{j}$ 为节点 j 的基宽参数， $b_{j}>0,C_{j}$ 为网络第 j 个节点的中心向量， $C_{j}=\left[c_{11},\cdots,c_{1m}\right]^{T},B=\left[b_{1},\cdots,b_{m}\right]^{T}$ 。

网络的权向量为

$$\boldsymbol {W} = \left[ w _ {1}, \dots , w _ {m} \right] ^ {\mathrm{T}} \tag {9.12}\boldsymbol {V} = \left[ v _ {1}, \dots , v _ {m} \right] ^ {\mathrm{T}} \tag {9.13}$$

两个 RBF 网络的输出分别为

$$N g (k) = h _ {1} w _ {1} + \dots + h _ {j} w _ {j} + \dots + h _ {m} w _ {m} \tag {9.14}N \varphi (k) = h _ {1} v _ {1} + \dots + h _ {j} v _ {j} + \dots + h _ {m} v _ {m} \tag {9.15}$$

式中，m 为 RBF 网络隐层神经元的个数。

采用逼近值,对象的输出估计值为

$$y _ {m} (k) = N g [ y (k - 1); W (k) ] + N \varphi [ y (k - 1); V (k) ] u (k - 1) \tag {9.16}$$

神经网络调整的性能指标为

$$E (k) = \frac {1}{2} (y (k) - y _ {m} (k)) ^ {2} \tag {9.17}$$

采用梯度下降法调整网络的权值为

$$\Delta w _ {j} (k) = - \eta_ {w} \frac {\partial E (k)}{\partial w _ {j} (k)} = \eta_ {w} (y (k) - y _ {m} (k)) h _ {j} (k)\Delta v _ {j} (k) = - \eta_ {v} \frac {\partial E (k)}{\partial v _ {j} (k)} = \eta_ {v} (y (k) - y _ {m} (k)) h _ {j} (k)$$

神经网络权值的调整过程为

$$\boldsymbol {W} (k) = \boldsymbol {W} (k - 1) + \Delta \boldsymbol {W} (k) + \alpha (\boldsymbol {W} (k - 1) - \boldsymbol {W} (k - 2)) \tag {9.18}\mathbf {V} (k) = \mathbf {V} (k - 1) + \Delta \mathbf {V} (k) + \alpha (\mathbf {V} (k - 1) - \mathbf {V} (k - 2)) \tag {9.19}$$

式中， $\eta_{w}$ 和 $\eta_{v}$ 为学习速率， $\alpha$ 为动量因子。

综上所述,神经网络自校正控制系统的结构如图 9-19 所示。

![](image/4f13c5e6b53c902c920d4cf6d773db449f0b7e072ac3625af474b7cc2396daad.jpg)

<details>
<summary>flowchart</summary>
