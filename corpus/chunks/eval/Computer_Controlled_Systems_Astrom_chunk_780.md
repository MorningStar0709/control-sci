# Example 13.1 Model hierarchies

To describe a drum boiler power unit, several different models may be needed. For production planning and frequency control, it may be sufficient to characterize the unit using two or three states describing the energy storage in the drum and the superheaters. To construct security systems and control systems, it may be necessary to have a model with 20 to 50 states. Finally, to model temperature and stresses in the turbine unit, several hundred states must be used.

In principle, there are two different ways in which models can be obtained: from prior knowledge—for example, in terms of physical laws or by experimentation on a process. When attempting to obtain a specific model, it is often beneficial to combine both approaches.

Mathematical model building based on physical laws is discussed briefly in Sec. 13.2. In most cases it is not possible to make a complete model only from physical knowledge. Some parameters must be determined from experiments. This approach is called system identification and is discussed in Sec. 13.3. There are many methods for analyzing data obtained from experiments. One basic approach is the principle of least squares (LS), discussed in Sec. 13.4. Recursive ways to make the computations are given in Sec. 13.5. Examples are given in Sec. 13.6.
