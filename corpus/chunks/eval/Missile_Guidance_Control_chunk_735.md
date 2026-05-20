During free flight, the Kalman filter continues to align and calibrate the INS in addition to reducing the air vehicle position and velocity errors. The necessary information is provided by the terrain correlation (or GPS) position fixes. Velocities, angular rates, torques, and direction cosine derivatives are computed in double precision (32 bits). Moreover, the free flight Kalman filter operates radial residuals, which are defined as the difference between the missile’s position determined by the terrain correlation algorithm and the inertial navigation system. Consequently, the data will be statistically combined by the filter algorithm to correct position, velocity, tilt, and gyro bias. The magnitude of the residuals decreases as the mission progresses and as the map cell size decreases, which indicates good mechanization and filter performance.

The functional diagram of the inertial navigation computations is shown in Figure 7.8. This diagram shows a standard computational sequence for a locallevel wander azimuth system. The wander azimuth system gives the cruise missile worldwide navigation capability, and the local-level mechanization contributes to the simplicity of the filter design and interface with the terrain correlation system [8].

The vertical channel is mechanized by the navigation module. The vertical channel has been extensively studied and analyzed to maximize its performance for terraincorrelation usage, especially during terrain following. This altitude is used to damp a standard third-order loop whose gains are selected to minimize the errors in the vertical

![](image/5cc61b4969ac0962981db16a45cefb1da7eeb53858c02d925125f4bc6f9311cf.jpg)

<details>
<summary>flowchart</summary>
