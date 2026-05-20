The quantity $G H ( s )$ is called the loop gain. In more complex block diagrams, the loop gain is the product of all blocks around the loop. Expressed as a block diagram transformation, HS Black's equation (Eqn 6.2) is shown in Figure 6.5.

![](image/0743fc553cc0f04fd32a375ab1d1626898e2a1d54c4afea9c06bdaf045546d4c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> G
    X --> H
    G --> Y
    H --> Y
    Y --> X
    X --> G/(1+GH)
    G/(1+GH) --> Y
    Y --> H
    H --> Y
    subgraph Transformation
    direction TB
    X --> G
    G --> Y
    H --> Y
    end
    subgraph Output
    direction TB
    X --> H
    H --> Y
    end
    Note: The diagram shows a simple process flow with inputs X, G, H and outputs Y, and a transformation arrow labeled 'for |GH| >= 1'.
```
</details>

Figure 6.5: Equation 6.2 expressed as a block diagram transformation.
