| Time | Output pH (a) | Output pH (b) | Output pH (c) | Input u (a), (b) | Input u (c) | Concentration x (a), (b) | Concentration x (c) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 4 | 4 | 1.0 | 1.0 | -1.0e-4 | -1.0e-4 |
| 2 | ~6 | ~5 | ~5 | ~1.0 | ~1.0 | ~0 | ~0 |
| 4 | ~7 | ~7 | ~7 | ~1.0 | ~1.0 | ~0 | ~0 |
| 6 | ~7 | ~7 | ~7 | ~1.0 | ~1.0 | ~0 | ~0 |
| 8 | ~7 | ~7 | ~7 | ~1.0 | ~1.0 | ~0 | ~0 |
| 10 | ~7 | ~7 | ~7 | ~1.0 | ~1.0 | ~0 | ~0 |
</details>

Figure 9.12 The same experiment as in Fig. 9.10, but with the controller structure in Fig. 9.11. The gain of the controller is 1000, and the reset time is 1. (a) $pH_{ref} = 7$ ; (b) $pH_{ref} = 8$ ; (c) $pH_{ref} = 9$ .

measured pH by the formula

$$x = f ^ {- 1} (\mathrm{pH}) = 1 0 ^ {\mathrm{pH} - 1 4} - 1 0 ^ {- \mathrm{pH}} \tag {9.22}$$

The transfer function from $u$ to $x$ is

$$\frac {c _ {B}}{q (1 + s T _ {m}) (1 + s \bar {T}) ^ {2}}$$

which is independent of the operating point. Figure 9.12 shows the same experiments as in Fig. 9.10, but with the control modification shown in Fig. 9.11. It should be noted that the nonlinear compensation with Eq. (9.22) can be used, since a strong acid-base pair is controlled. The more general problem of mixtures of many weak acids and bases does not have an easy linearizing transformation. It is then necessary to measure the concentrations of the components or to make an on-line measurement of the titration curve. Some other form of adaptation can then be reasonable.
