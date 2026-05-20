$$a \dot {x} = - x + u, \qquad y = h (x)$$

表示。用 $V(x) = a\int_0^x h(\sigma)d\sigma$ 作为存储函数，有

$$\dot {V} = h (x) (- x + u) = y u - x h (x) \leqslant y u$$

因此系统是无源的。当对于所有 $x \neq 0, xh(x) > 0$ 时，系统是严格无源的。

![](image/462f594de4538367fff5dfb43aefd63043639aa4a57971fc8f5e757a94a8ac45.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u"] --> B["∫"]
    B --> C["x"]
    C --> D["h(·)"]
    D --> E["y"]
```
</details>

(a)

![](image/62fb1cc8783f09612baf907c709c110e04d8c5d07311d39b3669f933ee006d4f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u"] --> B["1/(as+1)"]
    B --> C["x"]
    C --> D["h(·)"]
    D --> E["y"]
```
</details>

(b)   
图6.10 例6.3
