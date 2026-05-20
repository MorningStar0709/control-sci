# PROBLEMS

B–6–1. Plot the root loci for the closed-loop control system with

$$G (s) = \frac {K (s + 1)}{s ^ {2}}, \quad H (s) = 1$$

B–6–2. Plot the root loci for the closed-loop control system with

$$G (s) = \frac {K}{s (s + 1) (s ^ {2} + 4 s + 5)}, \quad H (s) = 1$$

B–6–3. Plot the root loci for the system with

$$G (s) = \frac {K}{s (s + 0 . 5) \left(s ^ {2} + 0 . 6 s + 1 0\right)}, \quad H (s) = 1$$

B–6–4. Show that the root loci for a control system with

$$G (s) = \frac {K \left(s ^ {2} + 6 s + 1 0\right)}{s ^ {2} + 2 s + 1 0}, \quad H (s) = 1$$

are arcs of the circle centered at the origin with radius equal to 110 .

B–6–5. Plot the root loci for a closed-loop control system with

$$G (s) = \frac {K (s + 0 . 2)}{s ^ {2} (s + 3 . 6)}, \quad H (s) = 1$$

B–6–6. Plot the root loci for a closed-loop control system with

$$G (s) = \frac {K (s + 9)}{s \left(s ^ {2} + 4 s + 1 1\right)}, \quad H (s) = 1$$

Locate the closed-loop poles on the root loci such that the dominant closed-loop poles have a damping ratio equal to 0.5. Determine the corresponding value of gain K.

B–6–7. Plot the root loci for the system shown in Figure 6–100. Determine the range of gain K for stability.

![](image/a744575059a1eaa27f8882ffcbc56e1dec7548361a6484feeb0bc479ddfc84ab.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum
    Sum --> K["K (s + 1)/(s + 5)"]
    K --> |2/(s²(s + 2))| C["s"]
    C --> |feedback| Sum
```
</details>

Figure 6–100   
Control system.

B–6–8. Consider a unity-feedback control system with the following feedforward transfer function:

$$G (s) = \frac {K}{s \left(s ^ {2} + 4 s + 8\right)}$$

Plot the root loci for the system. If the value of gain K is set equal to 2, where are the closed-loop poles located?

B–6–9. Consider the system whose open-loop transfer function is given by

$$G (s) H (s) = \frac {K (s - 0 . 6 6 6 7)}{s ^ {4} + 3 . 3 4 0 1 s ^ {3} + 7 . 0 3 2 5 s ^ {2}}$$

Show that the equation for the asymptotes is given by

$$G _ {a} (s) H _ {a} (s) = \frac {K}{s ^ {3} + 4 . 0 0 6 8 s ^ {2} + 5 . 3 5 1 5 s + 2 . 3 8 2 5}$$

Using MATLAB, plot the root loci and asymptotes for the system.

B–6–10. Consider the unity-feedback system whose feedforward transfer function is

$$G (s) = \frac {K}{s (s + 1)}$$

The constant-gain locus for the system for a given value of K is defined by the following equation:

$$\left| \frac {K}{s (s + 1)} \right| = 1$$

Show that the constant-gain loci for 0 - K - q may be given by

$$\left[ \sigma (\sigma + 1) + \omega^ {2} \right] ^ {2} + \omega^ {2} = K ^ {2}$$
