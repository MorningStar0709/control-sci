```mermaid
graph TD
    A["Initialization"] --> B["Navigation"]
    B --> C["Air data"]
    C --> D["Air data computer"]
    D --> E["Pitot-static tube"]
    D --> F["Total temperature probe"]
    B --> G["Air vehicle free flight filter"]
    G --> H["Position error"]
    H --> I["Terrain correlation"]
    I --> J["Radar clearance, r"]
    J --> K["Steering"]
    K --> L["Profile mission data"]
    L --> M["Mission data storage (core memory element)"]
    L --> N["Map reference data"]
    N --> O["Radar altimeter element"]
    B --> P["Corrections"]
    P --> Q["h_PT"]
    Q --> R["Velocity pulses"]
    R --> S["Inertial reference unit"]
    B --> T["ρ, V"]
    T --> U["ADCU"]
    U --> V["r"]
    V --> W["V's D.C.'s, h_s"]
    W --> X["r"]
    X --> Y["v' s D.C.'s, h_s"]
    Y --> Z["r"]
```
</details>

DC’s = Direction cosines (i.e., $C _ { x x } , C _ { x y } , C _ { x z } , \mathrm { e t c } )$   
H = system altitude   
ADCU = Air data control unit

Fig. 7.7. Typical free flight navigation function.

channel during terrain following. The vertical channel thus accurately computes a reference altitude so that terrain correlation can be performed during any type of altitude changes over the maps. One additional feature of the system is the resetting of altitude h at each terrain correlation update. The system altitude $h _ { s }$ is reset so that no transients are introduced into the system. For more information on the vertical channel mechanization, the reader is referred to [8].
