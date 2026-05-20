```mermaid
graph TD
    A["+ Bump rate (rise)"] --> C["+"]
    B["-2*Bump rate"] --> C
    D["+ Bump rate (descend)"] --> C
    E["+ Bump rate (flat)"] --> C
    C --> F["u2 = z0dot"]
    F --> G["1/s"]
    G --> H["u1 = z0"]
    H --> I["u"]
    I --> J["x' = Ax + Bu\ny = Cx + Du"]
    J --> K["y"]
    K --> L["To Workspace"]
    M["Clock"] --> N["t"]
    O["t"] --> N
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#f9f,stroke:#333
    style F fill:#ccf,stroke:#333
    style G fill:#ccf,stroke:#333
    style H fill:#ccf,stroke:#333
    style I fill:#ccf,stroke:#333
    style J fill:#ccf,stroke:#333
    style K fill:#ccf,stroke:#333
    style L fill:#ccf,stroke:#333
    style M fill:#ccf,stroke:#333
    style N fill:#ccf,stroke:#333
```
</details>

Figure 11.2 Simulink diagram for the seat-suspension system: triangular pulse input.

![](image/36aec20dd74d329224e88bfda4e5aa337ef15988a68cc2657e1e076423ac1701.jpg)

<details>
<summary>line</summary>

| Time, s | Velocity input, u₂(t), m/s |
| --- | --- |
| 0.4 | 0 |
| 0.5 | 5 |
| 0.52 | -5 |
| 0.6 | 0 |
</details>

(a)

![](image/f1418f9b52dcfa43d87bfe5ce6af78df92619b01b4bd151466e7ee48af8023a5.jpg)

<details>
<summary>line</summary>

| Time, s | Floor input, u₁(t), m |
| --- | --- |
| 0.4 | 0.0 |
| 0.5 | 0.03 |
| 0.6 | 0.0 |
</details>

(b)

Figure 11.3 Seat-suspension system inputs: (a) velocity-pulse input $u _ { 2 } ( t )$ and (b) triangular-pulse input $u _ { 1 } ( t )$ .   
![](image/49f2e1bccb15e15ca1f73e8e60a37cfaad765aef9baab33cb2808fbf1f9abe04.jpg)

<details>
<summary>line</summary>

| Time, s | Driver-mass displacement, z₂(t), mm |
| --- | --- |
| 0.5 | 0.0 |
| 0.6 | 1.5 |
| 0.8 | -0.7 |
| 1.0 | 0.2 |
| 1.5 | -0.1 |
| 2.0 | 0.0 |
| 3.0 | 0.0 |
</details>

(a)

![](image/56a36e455c770499f5f56ca75541f0ba022891a596b61f1da490eb46ea75fbf7.jpg)

<details>
<summary>line</summary>

| Time, s | Driver acceleration, m/s² |
| --- | --- |
| 0.5 | 6.2 |
| 1.0 | 0.0 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
</details>

Figure 11.4 Impulse response of the seat-suspension system: (a) driver displacement and (b) driver acceleration.

damping ratio of the seat-suspension system. The first peak is 1.52 mm $( \mathrm { a t } t = 0 . 1 1 \mathrm { s }$ after the impulse), and the second peak value is 0.19 mm $( \mathrm { a t } t = 0 . 7 0 \mathrm { s }$ after the impulse). Therefore, the log decrement is

$$\delta = \ln {\frac {1 . 5 2}{0 . 1 9}} = 2. 0 6 9 4$$

The approximate damping ratio is
