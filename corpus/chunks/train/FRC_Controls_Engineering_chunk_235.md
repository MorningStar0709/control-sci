# 8.6.3 Holonomic vs nonholonomic control

Drivetrains that are unable to exercise all possible degrees of freedom (e.g., moving sideways with respect to the chassis) are nonholonomic. An LQR on each degree of freedom is ideal for holonomic drivetrains, but not for nonholonomic. Section 8.7 will use the differential drive as a motivating example for various nonholonomic controllers.

![](image/d9f85719c47a08b28ef5a68e36a461ed79169f4a98db2381d5c4e73a4b67d933.jpg)

Nonholonomic controllers should not be used for holonomic drivetrains. They make different assumptions about the drivetrain dynamics that yield suboptimal results compared to holonomic controllers.
