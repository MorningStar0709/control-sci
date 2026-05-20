# Example 1.13 Internal-combustion engines

An internal-combustion engine is a sampled system. The ignition can be viewed as a clock that synchronizes the operation of the engine. A torque pulse is generated at each ignition.

![](image/c063266191103c73a4cab730054d4e67ba72c23bfb00cbead57416893ceb93d0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Injector"] --> B["Kicker"]
    B --> C["D-A"]
    C --> D["Processing"]
    D --> E["A-D"]
    E --> F["f = 10 MHz"]
    F --> G["Ideal orbit"]
    G --> H["Detector"]
    H --> I["D-A"]
    I --> J["Processing"]
    J --> K["A-D"]
    K --> L["f = 10 MHz"]
```
</details>

Figure 1.14 Particle accelerator with stochastic cooling.
