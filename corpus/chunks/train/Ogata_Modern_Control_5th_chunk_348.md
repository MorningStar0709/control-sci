```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["G(s)"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O
    O --> P
    P --> Q
    Q --> R
    R --> S
    S --> T
    T --> U
    U --> V
    V --> W
    W --> X
    X --> Y
    Y --> Z
```
</details>

Figure 6–54   
Control system.

is approximately unity, where $s = s _ { 1 }$ is one of the dominant closed-loop poles, choose the values of $T _ { 1 }$ and $\gamma$ from the requirement that

$$\left\lfloor \frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\gamma}{T _ {1}}} = \phi \right.$$

The choice of $T _ { 1 }$ and $\gamma$ is not unique. (Infinitely many sets of $T _ { 1 }$ and $\gamma$ are possible.) Then determine the value of $K _ { c }$ from the magnitude condition:

$$\left| K _ {c} \frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\gamma}{T _ {1}}} G (s _ {1}) \right| = 1$$

4. If the static velocity error constant $K _ { v }$ is specified, determine the value of $\beta$ to satisfy the requirement for $K _ { v }$ . The static velocity error constant $K _ { v }$ is given by

$$
\begin{array}{l} K _ {v} = \lim _ {s \to 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s K _ {c} \left(\frac {s + \frac {1}{T _ {1}}}{s + \frac {\gamma}{T _ {1}}}\right)\left(\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}}\right) G (s) \\ = \lim _ {s \rightarrow 0} s K _ {c} \frac {\beta}{\gamma} G (s) \\ \end{array}
$$

where $K _ { c }$ and $\gamma$ are already determined in step 3. Hence, given the value of $K _ { v }$ , the value of $\beta$ can be determined from this last equation. Then, using the value of $\beta$ thus determined, choose the value of $T _ { 2 }$ such that

$$\left| \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} \right| \div 1- 5 ^ {\circ} < \left\lfloor \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} < 0 ^ {\circ} \right.$$

(The preceding design procedure is illustrated in Example 6–8.)

Case 2. $\gamma = \beta$ If . $\gamma = \beta$ is required in Equation (6–23), then the preceeding design procedure for the lag–lead compensator may be modified as follows:

1. From the given performance specifications, determine the desired location for the dominant closed-loop poles.

2. The lag–lead compensator given by Equation (6–23) is modified to
