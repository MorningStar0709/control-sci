$$T _ {\mathrm{m}} = i K _ {\mathrm{m}} \tag {11.17}J _ {\mathrm{m}} \ddot {\theta} _ {\mathrm{m}} = T _ {\mathrm{m}} - b _ {\mathrm{m}} \dot {\theta} _ {\mathrm{m}} - K _ {\mathrm{L}} (\theta_ {\mathrm{m}} - \theta_ {\mathrm{L}}) \tag {11.18}$$

负载 $J_{L}\ddot{\theta}_{L}=T_{mL}-b_{L}\dot{\theta}_{L}$ (11.19)

$$K _ {\mathrm{L}} (\theta_ {\mathrm{m}} - \theta_ {\mathrm{L}}) - T _ {\mathrm{mL}} = 0 \tag {11.20}$$

根据上述描述，得到二质量伺服系统部分结构图（其余部分与单质量伺服系统结构相同），如图 11-16 所示。

![](image/182fb41d5392d6ffabc172a756229f208addd3edd7be129b1d594b28f89c8306.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u_a"] --> B["+"]
    B --> C["电机电流环"]
    C --> D["+"]
    D --> E["1/(J_m s + b_m)"]
    E --> F["\dot{\theta}_m"]
    F --> G["1/s"]
    G --> H["θ_m"]
    H --> I["+"]
    I --> J["K_L"]
    J --> K["T_{mL}"]
    K --> L["1/(J_L s + b_L)"]
    L --> M["1/s"]
    M --> N["θ_L"]
    N --> O["C_e"]
    O --> B
```
</details>

图 11-16 二质量伺服系统部分结构框图

![](image/f961a61c0e2b41d4b08c25b3c04f110c487b191114d463c249530ea272015c95.jpg)
