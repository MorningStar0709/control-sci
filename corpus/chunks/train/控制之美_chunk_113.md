# 6.1.3 稳定性的研究对象

在分析系统的稳定性时,一定要明确分析的对象。在6.1.2节中,稳定性的定义是针对平衡点的。而一个动态系统的平衡点可能有很多个,例如一个单摆系统,如图6.1.3(a)所示。在没有外力的作用下,这个动态系统有两个平衡点,分别是直上(A点)和直下(B点)。其中,垂直向下的B点本身是一个渐近稳定的平衡点,当小球小范围偏离B点的时候,它会自己摆回来并最终停在B点。而A点则不同,小球可以稳定地停在A点(无速度),但是它一旦偏离A点,在没有外力的作用下,就将远离A点。因此,如果希望将A点也改变为渐近稳定点,就需要引入外力,例如在单摆的两边各加入一个吹风机。吹风机的风力强度由小球偏离A点的距离决定。这样就形成了一个反馈控制系统,其框图如图6.1.3(b)所示。控制器C(s)设计的目标就是将A点转化成为一个稳定的平衡点。除此之外,我们甚至可以设计出合适的控制器,使得小球稳定在C点这样一个倾斜的位置。此时的控制器设计需要达成两个目标:第一,使C点成为系统的平衡点;第二,使C点成为一个渐近稳定的平衡点。

![](image/2b7e30410c76e7d42a84aadbcb841cdf12a2a0ba84ddc1f7a5c4a262319e9179.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["吹风机1"] --> B["C"]
    B --> C["A"]
    C --> D["B"]
    D --> E["θ"]
    E --> F["单摆系统"]
    
    G["吹风机2"] --> H["参考角度 R(s)"]
    H --> I["+"]
    I --> J["E(s)"]
    J --> K["C(s) 控制器"]
    K --> L["U(s)"]
    L --> M["G(s)"]
    M --> N["角度 X(s)"]
    N --> O["反馈反馈"]
    
    style A fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#ccf,stroke:#333
    style I fill:#cff,stroke:#333
    style J fill:#ffc,stroke:#333
    style K fill:#cfc,stroke:#333
    style L fill:#fcc,stroke:#333
    style M fill:#fcc,stroke:#333
    style N fill:#fcc,stroke:#333
```
</details>

图6.1.3 单摆的平衡性与控制
