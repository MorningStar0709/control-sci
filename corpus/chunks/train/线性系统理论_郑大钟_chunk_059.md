```mermaid
graph TD
    A["u"] --> B["+"]
    B --> C["Σ1"]
    C --> D["y1"]
    D --> E["y"]
    E --> F["Σ2"]
    F --> G["y2"]
    G --> H["Σ3"]
    H --> I["u2"]
    I --> J["x1"]
    J --> K["Σ1"]
    K --> L["y1"]
    L --> M["y"]
    M --> N["Σ2"]
    N --> O["y2"]
    O --> P["Σ3"]
    P --> Q["y2"]
    Q --> R["Σ2"]
    R --> S["y2"]
    S --> T["Σ3"]
    T --> U["y2"]
    U --> V["Σ2"]
    V --> W["y2"]
    W --> X["Σ3"]
    X --> Y["y2"]
```
</details>

图1.8 子系统的反馈联接

子系统的反馈联接 考虑由两个子系统 $\Sigma_{1}$ 和 $\Sigma_{2}$ 按图 1.8 所示方式构成的反馈系统, 其中子系统的状态空间描述如 (1.128) 所示 $(D_{i}=0)$ 。

对于图示反馈系统,其构成条件为:

$$\dim \left(\boldsymbol {u} _ {1}\right) = \dim \left(\boldsymbol {y} _ {2}\right), \dim \left(\boldsymbol {u} _ {2}\right) = \dim \left(\boldsymbol {y} _ {1}\right) (1. 1 4 2)$$

而其在变量上的特点为：

$$u _ {1} = u - y _ {2}, \quad y _ {1} = y = u _ {2} \tag {1.143}$$

于是，由(1.128)(其中 $D_{i} = 0$ )和(1.143)，即可导出按图1.8所示方式构成的反馈系统的状态空间描述为：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = A _ {1} x _ {1} + B _ {1} u - B _ {1} C _ {2} x _ {2} \\ \dot {x} _ {2} = A _ {2} x _ {2} + B _ {2} C _ {1} x _ {1} \\ y = C _ {1} x _ {1} \end{array} \right. \tag {1.144}
$$

或将其表示为标准化的形式就为：

$$
\Sigma_ {P}: \left[ \begin{array}{l} \dot {\boldsymbol {x}} _ {1} \\ \dot {\boldsymbol {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} A _ {1} & - B _ {1} C _ {2} \\ B _ {2} C _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} _ {1} \\ \boldsymbol {x} _ {2} \end{array} \right] + \left[ \begin{array}{l} B _ {1} \\ 0 \end{array} \right] u \tag {1.145}

\boldsymbol {y} = \left[ \begin{array}{l l} C _ {1} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

再来推导反馈系统的传递函数矩阵的表达式。已知子系统的传递函数矩阵为：

$$G _ {i} (s) = C _ {i} \left(s I - A _ {i}\right) ^ {- 1} B _ {i} \quad i = 1, 2 \tag {1.146}$$

再据(1.143)，有

$$
\begin{array}{l} \hat {y} (s) = \hat {y} _ {1} (s) - G _ {1} (s) [ \hat {u} (s) - G _ {2} (s) \hat {y} (s) ] = G _ {1} (s) \hat {u} (s) \\ - G _ {1} (s) G _ {2} (s) \hat {\mathcal {Y}} (s) \tag {1.147} \\ \end{array}
$$

将上式化简之,得到

$$[ I + G _ {1} (s) G _ {2} (s) ] \hat {\mathbf {y}} (s) = G _ {1} (s) \hat {\mathbf {u}} (s) \tag {1.148}$$

进而，若 $\operatorname{det}(I + G(s)G_2(s)) \neq 0^{1)}$ ，那么即可得到反馈系统的传递函数矩阵为：

$$G (s) = [ I + G _ {1} (s) G _ {2} (s) ] ^ {- 1} G _ {1} (s) \tag {1.149}$$

类似地,根据(1.143)也可有
