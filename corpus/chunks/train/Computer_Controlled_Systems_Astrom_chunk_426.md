An illustration of the aliasing effect is shown in Fig. 7.8. Two signals with the frequencies 0.1 Hz and 0.9 Hz are sampled with a sampling frequency of 1 Hz (h = 1 s). The figure shows that the signals have the same values at the sampling instants. Equation (7.10) gives that 0.9 has the alias frequency 0.1. The aliasing problem was also seen in Fig. 1.11.

![](image/c3a93737072295658af35f73f6cbc77f8c48d45f79866e2b4a6c6afaeb59bd48.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 0 |
| 3 | -1 |
| 4 | 0 |
| 5 | 1 |
| 6 | 0 |
| 7 | -1 |
| 8 | 0 |
| 9 | 1 |
| 10 | 0 |
</details>

Figure 7.8 Two signals with different frequencies, 0.1 Hz and 0.9 Hz, may have the same value at all sampling instants.

![](image/5dbcb498d3e00b32a7dec478e8aa5d577d22848dfb3b89dd0db302d22cfe2569.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Feed water"] --> B["Pump"]
    B --> C["Condensed water"]
    C --> D["Valve"]
    D --> E["To boiler"]
    F["Pressure"] --> C
    G["Steam"] --> C
    H["Temperature"] --> C
```
</details>

Figure 7.9 Process diagram for a feed-water heating system of a boiler.
