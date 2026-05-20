# 6.5.1 Disturbance Rejection in the Frequency Domain

Example 6.9   
![](image/699df1ab10a3c83d3d54645b56279f847f58c5835bf181c373f2e95e1cb54168.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X -->|+| O
    O --> A["1000/(s + 500)"]
    A --> B["+"]
    B --> Y
    H[" H = 1 "] --> O
    d[" d(+) "] --> B
```
</details>

Find

$$\frac {Y (s)}{D (s)} \quad \text { for } \quad X (s) = 0$$

and sketch the BAMP of $G H ( j \omega )$ and $\frac { Y ( j \omega ) } { D ( j \omega ) }$ .

$$\frac {Y (s)}{D (s)} = \frac {1}{1 + G H} = \frac {s + 5 0 0}{s + 5 0 0 + 1 0 0 0} = \frac {(s + 5 0 0)}{(s + 1 5 0 0)}$$

and

$$G H (s) = \frac {1 0 0 0}{(s + 5 0 0)}$$

![](image/8bbe6ccd0423bac23777b9cec357111089b7873035df426f7cce25f32bfc7f0a.jpg)

![](image/90264a390b9378091393cea57090f2f621e61fa8bd7739ad1254ff411c0a8775.jpg)

The disturbance rejection is -9.5dB for frequencies below about 100 rad/sec. There is little or no disturbance rejection above about 1000 (which is the point where loop gain magnitude is 1.0).

![](image/b85c53525aba3d48849a9aed710a92c77a0514de3ec675a50313be5ec25d82b1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X -->|+| Sum
    Sum -->|e| G
    G --> Y
    Y --> H
    H -->|-| Sum
    d(t) -->|d(t)| Sum
```
</details>

Figure 6.7: A closed loop negative feedback control system with a disturbance injected at the input.   
![](image/248e020460f8b849eea23dd1a2800277fc8df6c8f0fb3332e3708ec817df661d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X -->|+| e
    e --> G1
    G1 --> G2
    G2 --> Y
    y --> H
    H -->|-| e
    e --> G1
    G1 --> G2
    G2 -->|d(+)| e
    G2 -->|(Plant)| y
```
</details>

Figure 6.8: A closed loop negative feedback control system with a disturbance injected between the controller (G1) and the plant $G _ { 2 } )$ .
