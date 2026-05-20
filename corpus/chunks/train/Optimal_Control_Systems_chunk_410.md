for all $t \in [t_{0}, t_{f}]$ . In other words, if the fuel-optimal system is normal, the components of the fuel-optimal control are piecewise constant functions of time. The fuel-optimal control can switch between +1, 0 and -1 and hence is called the bang-off-bang control (or principle).

\- Step 6: Implementation: As before in time-optimal control system, the fuel-optimal control law can be implemented either in open-loop configuration as shown in Figure 7.27. Here, an iterative procedure is to be used to finally drive the state to origin. On the other hand, we can realize closed-loop configuration as

![](image/83403ca882fb581c5f4f9d9335c107a825398d79add5d61b4802673938200995.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["λ(t)=-A' λ(t)"] --> B["λ*(t)"]
    B --> C["-B'"]
    C --> D["-q*(t)"]
    D --> E["Dead Zone"]
    E --> F["u*(t)"]
    F --> G["ẋ(t)=Ax(t)+Bu(t)"]
    G --> H["x*(t)"]
    I["Start Iteration/Change λ(0)"] --> J{Is x(tf) = 0?}
    J -->|Yes| K["Stop Iteration"]
    J -->|No| L["End"]
    M["λ(0)"] --> N["Open-Loop Fuel-Optimal Controller"]
    N --> O["Plant"]
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#f9f,stroke:#333
    style F fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
    style I fill:#f9f,stroke:#333
    style J fill:#ccf,stroke:#333
    style K fill:#ccf,stroke:#333
    style L fill:#ccf,stroke:#333
```
</details>

Figure 7.27 Open-Loop Implementation of Fuel-Optimal Control System

shown in Figure 7.28, where the current initial state is used to realize the fuel-optimal control law (7.4.22).

![](image/7a1e57307632c578cbdfb7e677200d83e4ed96cef11ce5bdc18059cee7a02408.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["x*(t)"] --> B["Algorithm"]
    B --> C["h[x*(t)"]]
    C --> D["Dead Zone"]
    D --> E["u*(t)"]
    E --> F["\dot{x}(t)=Ax(t)+Bu(t)"]
    F --> G["x*(t)"]
    G --> H["Plant"]
    style A fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    subgraph Closed-Loop Fuel-Optimal Controller
        B
        C
        D
        E
        F
    end
    subgraph Plant
        G
    end
```
</details>

Figure 7.28 Closed-Loop Implementation of Fuel-Optimal Control System
