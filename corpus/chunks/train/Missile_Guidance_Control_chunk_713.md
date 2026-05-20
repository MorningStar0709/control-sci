Figure 7.1 illustrates the primary mission functions, their time sequencing, and the role the missile and carrier aircraft computers play in each part of the mission. After ground testing of the aircraft and missile systems, the B-52 with missiles uploaded is placed on alert. Next, the mission planner selects a path for the ALCM, which is part of the mission data preparation system (MDPS), from launch to target that passes over the terrain maps. The planner has flexibility between maps, but must fly over the maps in the direction of map orientation. The distances between maps must be chosen so that there is a high probability of crossing the maps yet not so close as to unnecessarily constrain the missile flight path. The probability of map overflight is computed for each map of the mission by computing the ratio of the crosstrack and downtrack errors to one-half the map function. This function calculates the probability of overflight with negligible error. Also, the mission planner selects the vertical profile based on knowledge of the terrain on the missile flight path and other trajectory requirements.

![](image/052f21ecbd98b31057ab257793977201bc95df4b9bc73c78f23647ac14f2a26f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Prelaunch preparations"] --> B["Launch consent"]
    B --> C["Time of arrival"]
    C --> D["Launch point ranging"]
    D --> E["Fine align"]
    E --> F["Segment/element built-in tests and mission data transfer"]
    F --> G["Coarse alignment"]
    G --> H["Air vehicle: Power on Initialization Alignment"]
    H --> I["B-52 Carrier aircraft equipment"]
    I --> J["Takeoff"]
    J --> K["Mission data preparation and ground test"]
    K --> L["Upload weapons on B-52"]
    K --> M["Integrated system test"]
    K --> N["Mission data loading"]
    K --> O["Place on alert"]
    P["Launch sequence"] --> Q["Surface deployment"]
    P --> R["Engine ignition"]
    S["Free flight"] --> T["Navigation"]
    S --> U["Steering"]
    S --> V["Terrain following"]
    S --> W["Terrain correlation"]
    S --> X["Arming and fuzzing"]
    Y["ALCM"] --> Z["Master comp/missile computer"]
    Y --> AA["Missile computer only"]
    AB["Legend for ALCM software"] --> AC["Master computer only"]
    AD["Legend for ALCM software"] --> AE["Master comp/missile computer"]
    AF["Legend for ALCM software"] --> AG["Missile computer only"]
```
</details>

Fig. 7.1. Typical mission functions.
