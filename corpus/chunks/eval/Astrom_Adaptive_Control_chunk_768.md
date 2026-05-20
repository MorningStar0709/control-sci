# 12.8 ULTRAFILTRATION

Patients with little or no renal function need some form of artificial blood purification to stay alive. In dialysis the blood is cleansed of waste products and excess water, and the electrolytes in the blood are normalized. More than 350,000 patients all over the world undergo this treatment a couple of times a week. In its most common form, hemodialysis, the blood flows past a semipermeable membrane with a suitably composed dialysis fluid on the other side. Because of the large number of different dialyzers that are on the market, the control algorithm in the dialysis machine must be able to handle a wide span in process gain and other process characteristics.

An adaptive pole placement controller has been used in the fluid control monitor (FCM) developed by Gambro AB in Lund, Sweden. The system has been in use for many years and it has performed very well. This is probably one of the most widely used adaptive controllers in the world today. In this section we describe the system.

![](image/9dd8f31dfa17b98c676aa6a52802c764c3adde785913564c9aed52c76a47d69a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    Salt --> A["Water"]
    A --> B["DFM"]
    B --> C["P1"]
    C --> D["Bubble chamber"]
    D --> E["Dialyzer"]
    E --> F["Blood"]
    F --> G["FCM"]
    G --> H["Water"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#cfc,stroke:#333
    style H fill:#fcc,stroke:#333
```
</details>

Figure 12.17 Schematic diagram of a dialysis system.
