```mermaid
graph LR
    A["E₁(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["Kₐ"]
    D --> E["Cₘ"]
    E --> F["1/(Cωs)"]
    F --> G["r"]
    G --> H["L(s)"]
    H --> I["K₁"]
    I --> J["E₂(s)"]
    J --> K["-"]
    K --> L["Summing Junction"]
    L --> M["Summing Junction"]
    M --> N["Summing Junction"]
    N --> O["Summing Junction"]
    O --> P["Summing Junction"]
    P --> Q["Summing Junction"]
    Q --> R["Summing Junction"]
    R --> S["Summing Junction"]
    S --> T["Summing Junction"]
    T --> U["Summing Junction"]
    U --> V["Summing Junction"]
    V --> W["Summing Junction"]
    W --> X["Summing Junction"]
    X --> Y["Summing Junction"]
    Y --> Z["Summing Junction"]
    Z --> AA["Summing Junction"]
    AA --> AB["Summing Junction"]
    AB --> AC["Summing Junction"]
    AC --> AD["Summing Junction"]
    AD --> AE["Summing Junction"]
    AE --> AF["Summing Junction"]
    AF --> AG["Summing Junction"]
    AG --> AH["Summing Junction"]
    AH --> AI["Summing Junction"]
    AI --> AJ["Summing Junction"]
    AJ --> AK["Summing Junction"]
    AK --> AL["Summing Junction"]
    AL --> AM["Summing Junction"]
    AM --> AN["Summing Junction"]
    AN --> AO["Summing Junction"]
    AO --> AP["Summing Junction"]
    AP --> AQ["Summing Junction"]
    AQ --> AR["Summing Junction"]
    AR --> AS["Summing Junction"]
    AS --> AT["Summing Junction"]
    AT --> AU["Summing Junction"]
    AU --> AV["Summing Junction"]
    AV --> AW["Summing Junction"]
    AW --> AX["Summing Junction"]
    AX --> AY["Summing Junction"]
    AY --> AZ["Summing Junction"]
    AZ --> BA["Summing Junction"]
    BA --> BB["Summing Junction"]
    BB --> BC["Summing Junction"]
    BC --> BD["Summing Junction"]
    BD --> BE["Summing Junction"]
    BE --> BF["Summing Junction"]
    BF --> BG["Summing Junction"]
    BG --> BH["Summing Junction"]
    BH --> BI["Summing Junction"]
    BI --> BJ["Summing Junction"]
    BJ --> BK["Summing Junction"]
    BK --> BL["Summing Junction"]
    BL --> BM["Summing Junction"]
    BM --> BN["Summing Junction"]
    BN --> BO["Summing Junction"]
    BO --> BP["Summing Junction"]
    BP --> BQ["Summing Junction"]
    BQ --> BR["Summing Junction"]
    BR --> BS["Summing Junction"]
    BS --> BT["Summing Junction"]
    BT --> BU["Summing Junction"]
    BU --> BV["Summing Junction"]
    BV --> BW["Summing Junction"]
    BW --> BX["Summing Junction"]
    BX --> BY["Summing Junction"]
    BY --> BZ["Summing Junction"]
```
</details>

(h)

![](image/3f4b3bbfe4f38f4dd1fed1d2e03383ad896872b5981d40feacfa5c22d200417a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["E₁(s)"] --> B["+"]
    B --> C["Kₐ"]
    C --> D["\frac{Kₘ}{s(Tₘs+1)}"]
    D --> E["r"]
    E --> F["L(s)"]
    F --> G["K₁"]
    G --> H["E₂(s)"]
    H --> I["-"]
    I --> B
    J["Uₐ(s)"] --> D
    K["Θₘ(s)"] --> E
```
</details>

(i)   
图 2-23 电压测量装置系统结构图

一个复杂的系统结构图,其方框间的连接必然是错综复杂的,但方框间的基本连接方式只有串联、并联和反馈连接三种。因此,结构图简化的一般方法是移动引出点或比较点,交换比较点,进行方框运算将串联、并联和反馈连接的方框合并。在简化过程中应遵循变换前后变量关系保持等效的原则,具体而言,就是变换前后前向通路中传递函数的乘积应保持不变,回路中传递函数的乘积应保持不变。
