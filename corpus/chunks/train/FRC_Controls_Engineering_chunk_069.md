# 1.2 Block diagrams

When designing or analyzing a control system, it is useful to model it graphically. Block diagrams are used for this purpose. They can be manipulated and simplified systematically (see appendix A). Figure 1.2 is an example of one.

![](image/69ecf9db434cc5f5c36747b9ac5f8df5d01e67883c1d61dbbc08c46187275e42.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["input"] --> B["+"]
    B --> C["open-loop"]
    C --> D["output"]
    D --> E["feedback"]
    E --> B
    F["+"] --> B
    G["∓"] --> B
```
</details>

Figure 1.2: Block diagram with nomenclature

The open-loop gain is the total gain from the sum node at the input (the circle) to the output branch. This would be the system’s gain if the feedback loop was disconnected. The feedback gain is the total gain from the output back to the input sum node. A sum node’s output is the sum of its inputs.

Figure 1.3 is a block diagram with more formal notation in a feedback configuration.

![](image/b86fb710dfe203a8c6f2b2d1975b8b16d4846f95c026ba2938fc989efef6f785.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> |+| Sum((+))
    Sum --> P1["P₁"]
    P1 --> Y
    Y --> P2["P₂"]
    P2 --> |feedback| Sum
    Sum --> |±| P2
```
</details>

Figure 1.3: Feedback block diagram

∓ means “minus or plus” where a minus represents negative feedback.
