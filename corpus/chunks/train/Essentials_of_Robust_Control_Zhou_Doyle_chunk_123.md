To focus our discussion, we shall consider the standard feedback configuration shown in Figure 5.1. It consists of the interconnected plant P and controller K forced by command $r ,$ sensor noise $n ,$ plant input disturbance $d _ { i } .$ , and plant output disturbance $d .$ In general, all signals are assumed to be multivariable, and all transfer matrices are assumed to have appropriate dimensions.

![](image/d38e23538b51fbc8633de9fdb2e313e47ed16d93529183e0b0571f66ae0206b0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |r| A["•"]
    A --> B["K"]
    B --> C["u"]
    C --> D["•"]
    D --> E["Up"]
    E --> F["P"]
    F --> G["•"]
    G --> y
    y --> H["n"]
    H --> A
    d_i --> D
    d --> G
```
</details>

Figure 5.1: Standard feedback configuration
