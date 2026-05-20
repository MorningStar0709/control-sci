A simple range-tracking loop is illustrated in Figure 3.31. This range-tracking loop has two major components: (1) the range discriminator, and (2) the servo that repositions the range gate. In Figure 3.31, Rt is the true range to the target, and $R _ { g }$ is the measured range to the target.

![](image/91f61134245ffb2a338f01fe8dda5469bf729c7d0200b43800a56b07e65b0158.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input Signal"] --> B((+))
    B --> C["Actual error"]
    C --> D["Range discriminator"]
    D --> E["Measured error"]
    E --> F["Range servo"]
    F --> G["Rg"]
    G --> H["Feedback Loop"]
    H --> B
```
</details>

Fig. 3.31. Range-track loop.

We conclude this section by noting that in aircraft survivability design and/or analysis, one commonly distinguishes between onboard and standoff (or offboard) active electronic equipment to degrade the effectiveness of the various nonterminal threat elements. Onboard radiation emission equipment for defensive electronic countermeasures is usually referred to as a self-screening or self-protection jammer, such as the Navy’s airborne self-protection jammer. Offboard equipment can be carried either by a drone (e.g., an unmanned aerial vehicle (UAV)) or by a specialpurpose ECM support aircraft, such as the Navy’s EA-6 and the Air Force’s EF-111 aircraft.
