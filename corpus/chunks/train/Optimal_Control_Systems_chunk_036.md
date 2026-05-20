1. the input $\mathbf{u}(t)$ is determined by the controller (consisting of error detector and compensator) driven by system states $\mathbf{x}(t)$ and reference signal $\mathbf{r}(t)$ ,   
2. all or most of the state variables are available for control, and   
3. it depends on well-established matrix theory, which is amenable for large scale computer simulation.

![](image/76ba30e70d7e9245bec51dfad0af645087b40427cc311f773e4cec4b1ac2556f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Reference Input r(t)"] --> B["Controller"]
    B --> C["Control Input u(t)"]
    C --> D["Plant P"]
    D --> E["Output y(t)"]
    B --> F["State x(t)"]
    D --> F
```
</details>

Figure 1.2 Modern Control Configuration

The fact that the state variable representation uniquely specifies the transfer function while there are a number of state variable representations for a given transfer function, reveals the fact that state variable representation is a more complete description of a system.

Figure 1.3 shows components of a modern control system. It shows three components of modern control and their important contributors. The first stage of any control system theory is to obtain or formulate the dynamics or modeling in terms of dynamical equations such as differential or difference equations. The system dynamics is largely based on the Lagrangian function. Next, the system is analyzed for its performance to find out mainly stability of the system and the contributions of Lyapunov to stability theory are well known. Finally, if the system performance is not according to our specifications, we resort to design [25, 109]. In optimal control theory, the design is usually with respect to a performance index. We notice that although the concepts such as Lagrange function [85] and V function of Lyapunov [94] are old, the techniques using those concepts are modern. Again, as the phrase modern usually refers to time and what is modern today becomes ancient after a few years, a more appropriate thing is to label them as optimal control, nonlinear control, adaptive control, robust control and so on.

![](image/0563c4f5065b20af030178dea97d211acc9b28f44db81ebae732e7d87e29ce17.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Modern Control System"] --> B["System Dynamics (Modeling)"]
    A --> C["System Analysis (Performance)"]
    A --> D["System Synthesis (Design)"]
    B --> E["State Function of Lagrange (1788)"]
    C --> F["V Function of Lyapunov (1892)"]
    D --> G["H Function of Pontraygin (1956)"]
```
</details>

Figure 1.3 Components of a Modern Control System
