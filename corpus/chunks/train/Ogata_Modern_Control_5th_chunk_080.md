# PROBLEMS

B–2–1. Simplify the block diagram shown in Figure 2–29 and obtain the closed-loop transfer function $C ( s ) / R ( s )$ .

B–2–2. Simplify the block diagram shown in Figure 2–30 and obtain the closed-loop transfer function $C ( s ) / R ( s )$ .

B–2–3. Simplify the block diagram shown in Figure 2–31 and obtain the closed-loop transfer function $C ( s ) / R ( s )$ .

![](image/bf0a8dfd1ec8ae0c0efee7d5aea845d168201db7fbc1e4d5e0d2703433810a0f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["s"] --> A["+"] --> G1["G₁"]
    R["s"] --> B["-"] --> G2["G₂"]
    R["s"] --> C["-"] --> G3["G₃"]
    R["s"] --> D["+"] --> G4["G₄"]
    G1 --> C
    G2 --> C
    G3 --> C
    G4 --> C
    C --> D
```
</details>

Figure 2–29   
Block diagram of a system.

![](image/36eae2fa188fea804bedd56057d085e0f9b7faa2bb473a42a9131fbed1e35f51.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["s"] --> G1["G₁"]
    R["s"] --> G2["G₂"]
    G1 --> Sum1["+"]
    G2 --> Sum2["+"]
    Sum1 --> Sum3["+"]
    Sum2 --> Sum4["+"]
    Sum3 --> H1["H₁"]
    Sum4 --> H2["H₂"]
    H1 --> Sum5["+"]
    H2 --> Sum5
    Sum5 --> C["s"]
```
</details>

Figure 2–30   
Block diagram of a system.

![](image/a1ca34115ccc5ba44617808e0ff7a37d90460cea9c8321b8ad4acf58137b8945.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> G1["G1"]
    G1 --> A2["+"] --> G2["G2"]
    G2 --> A3["+"] --> G3["G3"]
    G3 --> C["s"]
    C["s"] --> D["H3"]
    D --> E["H2"]
    E --> F["+"] --> G2
    G2 --> F
    F --> G1
    G1 --> A2
    A2 --> G1
    G1 --> A3
    A3 --> G3
```
</details>

Figure 2–31   
Block diagram of a system.

B–2–4. Consider industrial automatic controllers whose control actions are proportional, integral, proportional-plusintegral, proportional-plus-derivative, and proportional-plusintegral-plus-derivative. The transfer functions of these controllers can be given, respectively, by

$$\frac {U (s)}{E (s)} = K _ {p}\frac {U (s)}{E (s)} = \frac {K _ {i}}{s}\frac {U (s)}{E (s)} = K _ {p} \left(1 + \frac {1}{T _ {i} s}\right)\frac {U (s)}{E (s)} = K _ {p} \left(1 + T _ {d} s\right)\frac {U (s)}{E (s)} = K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right)$$

where $U ( s )$ is the Laplace transform of $u ( t )$ , the controller output, and $E ( s )$ the Laplace transform of $e ( t )$ , the actuating error signal. Sketch $u ( t )$ -versus-t curves for each of the five types of controllers when the actuating error signal is

(a) e(t)=unit-step function   
(b) e(t)=unit-ramp function
