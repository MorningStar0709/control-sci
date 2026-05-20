# Reduction at the Source

The most obvious way to reduce the effects of disturbances is to attempt to reduce the source of the disturbances. This approach is closely related to process design. The following are typical examples:

Reduce variations in composition by a tank with efficient mixing.

Reduce friction forces in a servo by using better bearings.

Move a sensor to a position where there are smaller disturbances.

Modify sensor electronics so that less noise is obtained.

Replace a sensor with another having less noise.

Change the sampling procedure by spacing the samples better in time or space to obtain a better representation of the characteristics of the process.

These are just a few examples, but it is very important to keep these possibilities in mind. Compare with the integrated process and control design discussed in Chapter 6.

![](image/e3e3b985ee590275f977e39ddd3828f9d5eb739fde31531b929c8959ecd6f346.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    u --> A
    A --> Σ
    Σ --> B
    B --> Σ
    Σ --> Disturbance
    Disturbance --> Process
    Local feedback --> A
    Local feedback --> B
    Process --> y
```
</details>

Figure 10.1 Reduction of disturbances by local feedback. The disturbance should enter the system between points A and B. The dynamics between A and B should be such that a high gain can be used in the loop.
