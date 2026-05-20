# 1.3 Open-loop and closed-loop systems

The system or collection of actuators being controlled by a control system is called the plant. A controller is used to drive the plant from its current state to some desired state (the reference). We’ll be using the following notation for relevant quantities in block diagrams.

r(t) reference u(t) control input

e(t) error y(t) output

Controllers which don’t include information measured from the plant’s output are called open-loop or feedforward controllers. Figure 1.4 shows a plant with a feedforward controller.

![](image/f34e5d77a846068dfcda360b8643ba9eadb3b9266417c5f944f5a43cb30d5e57.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B["Feedforward controller"]
    B --> C["u(t)"]
    C --> D["y(t)"]
```
</details>

Figure 1.4: Open-loop control system

Controllers which incorporate information fed back from the plant’s output are called closed-loop or feedback controllers. Figure 1.5 shows a plant with a feedback controller.

![](image/1ef61037e6c7d32bbc4391a397964819b1afec441882598fe001cc8998830376.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r_t["r(t)"] --> adder["+"]
    adder --> e_t["e(t)"]
    e_t --> Feedback["Feedback controller"]
    Feedback --> u_t["u(t)"]
    u_t --> plant["pot"]
    plant --> y_t["y(t)"]
    y_t -->|feedback| adder
```
</details>

Figure 1.5: Closed-loop control system

Note that the input and output of a system are defined from the plant’s point of view. The negative feedback controller shown is driving the difference between the reference and output, also known as the error, to zero.

Figure 1.6 shows a plant with feedforward and feedback controllers.

![](image/1372348b81770dae25ffe0e645d359664377a58ba42ea904026fcc1a7274b28a.jpg)

<details>
<summary>flowchart</summary>
