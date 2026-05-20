# Mathematical Models of Electrical Systems

Mathematical models of electrical systems can be derived using a systematic two-step process:

1. Write the corresponding first-order ODE for each energy-storage element (capacitor or inductor). The dynamic variables of the ODEs will be either voltage $e _ { C }$ (for a capacitor) or current $I _ { L }$ (for an inductor).   
2. Use Kirchhoff’s laws to express the unknown voltages and currents in terms of either the dynamic variables associated with the energy-storage elements $( e _ { C }$ or $I _ { L } )$ or the sources (input voltage $e _ { \mathrm { i n } }$ or input current $I _ { \mathrm { i n } } )$ .

![](image/39282069d95011606cb7ea2f29713a04b065065a2b26c4d3c9410d202d1da089.jpg)

<details>
<summary>text_image</summary>

I₁
I₂
I₃
I₄
</details>

Figure 3.6 Example of Kirchhoff’s current (node) law.

In general, we write a first-order ODE for each energy-storage element; that is, each capacitor and each inductor. For example, a circuit with two capacitors and one inductor will result in a third-order mathematical model (i.e., three first-order ODEs). It is important that the complete model of the electrical system be in terms of the dynamic variables associated with the energy-storage elements and the source input variable. The two-step modeling process is best illustrated by the following examples.
