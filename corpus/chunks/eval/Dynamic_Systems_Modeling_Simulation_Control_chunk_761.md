# Creating Subsystem Blocks

Although the system defined by Eqs. (C.10) and (C.11) is only third order, the resulting Simulink model shown in Fig. C.11 requires four feedback paths and two summing junctions, which creates a somewhat cluttered block diagram. Therefore, higher-order nonlinear systems will result in a cluttered Simulink model with a web of signal paths. One way to create “clean” Simulink models is to condense parts of the overall block diagram into subsystems. Simulink has two methods for constructing subsystem blocks: (1) dragging and dropping the Subsystem block from the Ports & Subsystems library and (2) grouping an existing Simulink diagram into a subsystem. The second method involves constructing the subsystem model first and enclosing the entire model with a bounding box (click and hold outside of diagram, drag cursor across the diagram so that a dotted box encloses the diagram, release the mouse button). Figure C.13 shows the complete Simulink model from Example C.4 (i.e., Fig. C.11) with a “bounding box” around the block diagram section that represents Eq. (C.12). When the desired block diagram is selected, the user chooses Diagram > Subsystem & Model Reference > Create Subsystem from Selection and a subsystem is constructed. A subsystem for Eq. (C.13) can be created in a similar manner. Figure C.14 shows the complete Simulink model for Example C.4 using two subsystems. Note that the only external input to the ẏ (or top) subsystem is dynamic variable z. The ẏ subsystem, Eq. (C.12), also depends on dynamic variable y but this signal resides “inside” the subsystem. The z̈ (or bottom) subsystem, Eq. (C.13), has u(t) as its sole input function. Some subsystems may have multiple inputs and multiple outputs. The user can double click the subsystem block to see and edit

![](image/8de0ab29878d4139cf5eea9661684ced1f39743bfd2b6eafca9aecbfe926b60b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph "Bounding box"
        A["+"] --> B["1/0.5 Gain, 1/0.5"]
        B --> C["1/s Integrator"]
        C --> D["y"]
        D --> E["To Workspace1"]
        F["0.6 Gain, 0.6"] --> G["Sign"]
        G --> H["1.4 Gain, 1.4"]
        H --> I["z"]
    end
