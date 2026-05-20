```mermaid
graph LR
    Wr["Wr"] --> r["r"]
    r --> o1((o))
    o1 --> K["K"]
    K --> u["u"]
    u --> o2((o))
    o2 --> P["P"]
    P --> o3((o))
    o3 --> y["y"]
    y --> We["We"]
    We --> e["e"]
    e --> n["n"]
    n --> Wn["Wn"]
    Wn --> ñ[ñ]
    ñ --> o1
    Wd["Wd"] --> d["d"]
    d --> w_d["d̃"]
    w_d --> w_i["Wi"]
    w_i --> wi["wi"]
    w_u["w_u"] --> u_u["ũ"]
    w_u --> u["u"]
    w_i --> di["d̃i"]
    w_i --> di["d̃i"]
    w_u --> u_d["d̃"]
    w_u --> u_d
```
</details>

Figure 6.3: Standard feedback configuration with weights

In general, we shall modify the standard feedback diagram in Figure 6.1 into Figure 6.3. The weighting functions in Figure 6.3 are chosen to reflect the design objectives and knowledge of the disturbances and sensor noise. For example, $W _ { d }$ and $W _ { i }$ may be chosen to reflect the frequency contents of the disturbances $d$ and $d _ { i }$ or they may be used to model the disturbance power spectrum depending on the nature of signals involved in the practical systems. The weighting matrix $W _ { n }$ is used to model the frequency contents of the sensor noise while $W _ { e }$ may be used to reflect the requirements on the shape of certain closed-loop transfer functions (for example, the shape of the output sensitivity function). Similarly, $W _ { u }$ may be used to reflect some restrictions on the control or actuator signals, and the dashed precompensator $W _ { r }$ is an optional element used to achieve deliberate command shaping or to represent a nonunity feedback system in equivalent unity feedback form.

It is, in fact, essential that some appropriate weighting matrices be used in order to utilize the optimal control theory discussed in this book $( \mathrm { i . e . , \ } \mathcal { H } _ { 2 }$ and $\mathcal { H } _ { \infty }$ theory). So a very important step in the controller design process is to choose the appropriate weights, $W _ { e } , W _ { d } , W _ { u } .$ , and possibly $W _ { n } , W _ { i } , W _ { r }$ . The appropriate choice of weights for a particular practical problem is not trivial. In many occasions, as in the scalar case, the weights are chosen purely as a design parameter without any physical bases, so these weights may be treated as tuning parameters that are chosen by the designer to achieve the best compromise between the conflicting objectives. The selection of the weighting matrices should be guided by the expected system inputs and the relative importance of the outputs.
