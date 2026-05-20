# Pairing of Inputs and Outputs

A large system will typically have a large number of inputs and outputs. Even if a control principle, which involves only a few variables, is found initially, many variables typically must be considered once the variables that can be manipulated and measured are introduced. With a top-down approach, a system should be broken down into small subsystems. It is then desirable to group different inputs and outputs together, so that a collection of smaller systems is obtained. If possible, the grouping should be done so that (1) there are only weak couplings between the subsystems; and (2) each subsystem is dynamically well behaved, that is, time constants are of the same magnitude and time delay, nonminimum phase, and severe variations in process dynamics are avoided.

![](image/22e27a47ffca32bdc5c608293aa70c19bfb962e8512d4f685d73c1f9e003eb8a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Purchasing"] --> B["Raw material"]
    B --> C["Intermediate storages"]
    C --> D["Production supervision"]
    D --> E["Final product"]
    E --> F["Output"]
```
</details>

![](image/19b4314766b10a51c418c587dc758077cf3ae86986112888efe52559e96b75dd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Purchasing"] --> B["Raw material"]
    B --> C["Intermediate storages"]
    C --> D["Final product"]
    D --> E["Output"]
```
</details>

Figure 6.2 Material-balance control (a) in the direction of the flow and (b) in the direction opposite to the flow.

There are no general rules for the grouping. Neither are there any good ways of deciding if it is possible to find a grouping with the desired properties. Trial and error, combined with analysis of models, is one possibility. The following example illustrates the pairing problem.
