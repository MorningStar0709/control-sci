# 6.7 Conclusions

This chapter presents an overview of the design problems. There is a large step from the large and poorly defined problems of the real world to the small and well-defined problems that control theory can handle. Problems of structuring are discussed.

The notion of the control principle is introduced in order to apply the top-down approach. It is also shown how a bottom-up approach can be used to build complex systems from simple control structures such as feedback, feedforward, estimation, and optimization. Finally, specifications and approaches to the design of simple loops are discussed.

A chemical process consists of many unit operations, such as performed by reactors, mixers, and distillation columns. In a bottom-up approach to control-system design, control loops are first designed for the individual unit operations. Interconnections are then added to obtain a total system. In a top-down approach, control principles—such as composition control and material-balance control—are first postulated for the complete plant. In the decomposition, these principles are then applied to the individual units and loops.

In process control the majority of the loops for liquid level, flow, and pressure control are most frequently designed empirically and tuned on-line. However, control of composition and pH, as well as control of nonlinear distributed large systems with strong interaction, are often designed with care.

Control systems can be quite complicated because design is a compromise between many different factors. The following issues must typically be considered:

- Command signals   
- Load disturbances   
- Measurement noise   
- Model uncertainty   
- Actuator saturation   
• State constrainte   
- Controller complexity

There are few design methods that consider all these factors. The design methods discussed in this book will typically focus on a few of the issues. In a good design it is often necessary to grasp all factors. To do this it is often necessary to investigate many aspects by simulation. The relation between process design and controller design should also be considered.
