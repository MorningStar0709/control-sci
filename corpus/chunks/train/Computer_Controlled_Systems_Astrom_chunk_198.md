# Character of Disturbances

It is customary to distinguish among different types of disturbances, such as load disturbances, measurement errors, and parameter variations.

Load disturbances. Load disturbances influence the process variables. They may represent disturbance forces in a mechanical system—for example, wind gusts on a stabilized antenna, waves on a ship, load on a motor. In process control, load disturbances may be quality variations in a feed flow or variations in demanded flow. In thermal systems, the load disturbances may be variations in surrounding temperature. Load disturbances typically vary slowly. They may also be periodic—for example, waves in ship-control systems.

Measurement errors. Measurement errors enter in the sensors. There may be a steady-state error in some sensors due to errors in calibration. However, measurement errors typically have high-frequency components. There may also be dynamic errors because of sensor dynamics. There may also be complicated dynamic interaction between sensors and the process. Typical examples are gyroscopic measurement and measurement of liquid level in nuclear reactors. The character of the measurement errors often depends on the filtering in the instruments. It is often a good idea to look at the instrument and modify the filtering so that it fits the particular problem.

Parameter variations. Linear theory is used throughout this book. The load disturbance and the measurement noise then appear additively. Real systems are, however, often nonlinear. This means that disturbances can enter in a more complicated way. Because the linear models are obtained by linearizing the nonlinear models, some disturbances then also appear as variations in the parameters of the linear model.
