The error signal is thus positive if the fuel-air ratio is low (lean mixture) and negative when the ratio is high (rich mixture). The error signal is sent to a PI controller whose gain and integration time are set from the scheduling table. The values are set on the basis of load (air flow) and engine speed. The gain schedule is implemented simply by adding entries for the gain and integration time to the table used for feedforward of the nominal control variable. Because of the relay characteristic, there will be an oscillation in the fuel-air ratio. This is beneficial, because the catalytic sensor needs a variation to operate properly. The amplitude and the frequency of the oscillation are determined by the parameters of the controller.

![](image/af64af645422204c10c0581bdb25e2addaa6d93b55b5c13fb340b4f822c5ab4a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Pitch stick"] --> B["Position"]
    B --> C["Filter"]
    C --> D["A/D"]
    D --> E["K_OSE"]
    E --> F["∫"]
    F --> G["Σ"]
    G --> H["D/A"]
    H --> I["Σ"]
    I --> J["To servos"]
    K["Acceleration"] --> L["Filter"]
    L --> M["A/D"]
    M --> N["∫"]
    N --> O["Σ"]
    O --> P["D/A"]
    P --> Q["Σ"]
    Q --> R["To servos"]
    S["Pitch rate"] --> T["Filter"]
    T --> U["A/D"]
    U --> V["1/(1+T₃s)"]
    V --> W["K_Q1"]
    W --> X["Σ"]
    X --> Y["K_NZ"]
    Y --> Z["∫"]
    Z --> AA["Σ"]
    AA --> AB["To servos"]
    AC["V_IAS H"] --> AD["Gear"]
    AE["H"] --> AF["T₁s/(1+T₁s)"]
    AF --> AG["∫"]
    AG --> AH["K_SG"]
    AH --> AI["Σ"]
    AI --> AJ["D/A"]
    AJ --> AK["Σ"]
    AL["M"] --> AM["K_Q1"]
    AM --> AN["Σ"]
    AO["M"] --> AP["K_NZ"]
    AP --> AQ["∫"]
    AQ --> AR["Σ"]
    AS["H"] --> AT["T₂s/(1+T₂s)"]
    AT --> AU["K_QD"]
    AU --> AV["H M V_IAS"]
```
</details>

Figure 9.16 Simplified block diagram of the pitch control of the autopilot for a supersonic aircraft. The highlighted blocks show the parts of the autopilot where gain scheduling is used.
