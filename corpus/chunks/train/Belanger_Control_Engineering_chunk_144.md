![](image/281d44048b5d6452b29ec78edff4d477e0d3b6af17599ea3d20c0b6ef534ba5f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["Controllable Unobservable"]
    A --> C["Controllable Observable"]
    A --> D["Uncontrollable Observable"]
    A --> E["Uncontrollable Unobservable"]
    B --> F["+"]
    C --> F
    D --> G["+"]
    E --> G
    F --> H["y"]
    G --> H
```
</details>

Figure 3.10 The canonical decomposition for the case of independent eigenvectors

![](image/61401295d8951ad31914268b0ad1f4e80f03dc0088b852836b7c0b5280211d89.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["Controllable"]
    B --> C["Uncontrollable"]
```
</details>

Figure 3.11 Decomposition into controllable and uncontrollable blocks

![](image/86f91cf3170cc5e3ec8c198eef9b45c61127a69239b84134cd2ba7a5dc1add31.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Unobservable"] --> B["Observable"]
    B --> C["y"]
```
</details>

Figure 3.12 Decomposition into observable and unobservable blocks

![](image/6fb3d7fa333e0ba698ac79e90a60b6c9fa21c4dd78d012179376250da266e939.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> A["Controllable Unobservable"]
    u --> B["Uncontrollable Unobservable"]
    A --> C["Controllable Observable"]
    B --> D["Uncontrollable Observable"]
    C --> E["+"]
    D --> F["+"]
    E --> G["y"]
    F --> G
    G --> y
```
</details>

Figure 3.13 The canonical decomposition for the general case
