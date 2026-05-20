# 11.10 CONCLUSIONS

Practical aspects on implementation of adaptive controllers have been discussed in this chapter. There are many things to consider, since adaptive controllers are quite complicated devices. The following are some of the important issues:

\- Analog anti-aliasing filters must be used. They are typically second- or fourth-order filters that effectively eliminate signal components with frequencies above the Nyquist frequency $\pi / h$ , where $h$ is the sampling period.

![](image/0f43ae31df28d9aa73436086211395be6a7d5fb69a8d990225ca3ebc95205993.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Design"] --> B["Controller"]
    B --> C["u"]
    C --> D["D-A"]
    D --> E["G_pf(s)"]
    E --> F["Process"]
    F --> G["G_aa(s)"]
    G --> H["A-D"]
    H --> I["Feedback Loop"]
    I --> A
    J["Controller parameters"] --> B
    K["Process parameters"] --> A
    L["Controller parameters"] --> B
    M["Hf"] --> N["Estimation"]
    O["Hf"] --> N
    N --> P["Output"]
    style A fill:#000,stroke:#000,color:#fff
    style B fill:#000,stroke:#000,color:#fff
    style C fill:#000,stroke:#000,color:#fff
    style D fill:#000,stroke:#000,color:#fff
    style E fill:#000,stroke:#000,color:#fff
    style F fill:#000,stroke:#000,color:#fff
    style G fill:#000,stroke:#000,color:#fff
    style H fill:#000,stroke:#000,color:#fff
    style I fill:#000,stroke:#000,color:#fff
    style J fill:#000,stroke:#000,color:#fff
    style K fill:#000,stroke:#000,color:#fff
    style L fill:#000,stroke:#000,color:#fff
    style M fill:#000,stroke:#000,color:#fff
```
</details>

Figure 11.17 Block diagram of an adaptive control system with added filters. $G_{an}$ is the anti-aliasing filter, $G_{pf}$ is the postsampling filter, and $H_{f}$ is the data filter for the estimation.

The dynamics of the filters should be taken into account in the control design.
