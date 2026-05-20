# 10–7 DESIGN OF CONTROL SYSTEMS WITH OBSERVERS

In Section 10–6 we discussed the design of regulator systems with observers. (The systems did not have reference or command inputs.) In this section we consider the design of control systems with observers when the systems have reference inputs or command inputs. The output of the control system must follow the input that is time varying. In following the command input, the system must exhibit satisfactory performance (a reasonable rise time, overshoot, settling time, and so on).

In this section we consider control systems that are designed by use of the poleplacement-with-observer approach. Specifically, we consider control systems using observer controllers. In Section 10–6 we discussed regulator systems, whose block diagram is shown in Figure 10–25. This system has no reference input, or r=0. When the system has a reference input, several different block diagram configurations are conceivable, each having an observer controller.Two of these configurations are shown in Figures 10–26 (a) and (b); we shall consider them in this section.

Figure 10–25 Regulator system.   
![](image/a199bbf4572b3dbb7245d3dbeea7cfd5b50dac593398422174d45376da034c81.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r = 0"] --> B["+"]
    B --> C["-y"]
    C --> D["Observer controller"]
    D --> E["u"]
    E --> F["Plant"]
    F --> G["y"]
    G --> H["Feedback"]
    H --> B
```
</details>

![](image/990ed53aef25a5b0b67c81e23dfdc59125cbc8b781a317aadde0d04a064de0d4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |+| sum((+))
    sum --> r-y
    r-y --> Observer["Observer controller"]
    Observer --> u
    u --> Plant
    Plant --> y
    y --> |feedback| sum
```
</details>

Figure 10–26   
(a) Control system with observer controller in the feedforward path; (b) Control system with observer controller in the feedback path.

![](image/3037f774caf9873e3d3479335dd6354102e143c4b057dcfd6b7cf2dfad5fc318.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> sum((+))
    sum --> r + u
    r + u --> Plant
    Plant --> y
    y --> ObserverController
    ObserverController -->|-u
    -u --> sum
```
</details>
