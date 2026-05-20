# Abuses of Adaptive Control

An adaptive controller, being inherently nonlinear, is more complicated than a fixed-gain controller. Before attempting to use adaptive control, it is therefore important to investigate whether the control problem might be solved by constant-gain feedback. In the literature on adaptive control there are many cases in which constant-gain feedback can do as well as an adaptive controller. This is one reason why we are discussing alternatives to adaptive control in this book. One way to proceed in deciding whether adaptive control should be used is sketched in Fig. 1.22.

![](image/5489ec3fe7acae7c938ed23f9a20b4eec31ffaff1bc8adcd0dc3fc40480191dd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Process dynamics"] --> B["Varying"]
    A --> C["Constant"]
    B --> D["Use a controller with varying parameters"]
    C --> E["Use a controller with constant parameters"]
    D --> F["Unpredictable variations"]
    E --> G["Predictable variations"]
    F --> H["Use an adaptive controller"]
    G --> I["Use gain scheduling"]
```
</details>

Figure 1.22 Procedure to decide what type of controller to use.
