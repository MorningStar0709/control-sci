# Accessing the solution

You can obtain the solution by querying the values of the variables like so.

```ini
position = X.value[0, 0]
velocity = X.value[1, 0]
acceleration = U.value(0) 
```

![](image/01b96e08833e8b75c594dec8a1cebf2d4acb191a2136182d429b9a351fec8d52.jpg)

<details>
<summary>line</summary>

| Time (s) | Position (m) |
| -------- | ------------ |
| 0.0      | 0.0          |
| 0.5      | 0.2          |
| 1.0      | 0.6          |
| 1.5      | 1.0          |
| 2.0      | 1.5          |
| 2.5      | 1.8          |
| 3.0      | 2.0          |
| 3.5      | 2.0          |
</details>

Figure 17.1: Double integrator position

![](image/c0819f7c106146ec4b4f470513af95b47ce83ae6de089e5f1fe01584d0d2f91d.jpg)

<details>
<summary>line</summary>

| Time (s) | Velocity (m/s) |
| -------- | -------------- |
| 0.0      | 0.0            |
| 1.0      | 1.0            |
| 2.0      | 1.0            |
| 3.2      | -0.2           |
| 3.5      | 0.0            |
</details>

Figure 17.2: Double integrator velocity   
![](image/035b2c5ebde3090ec664bafafe478cee273127825697743b63cf4d5414c26db0.jpg)

<details>
<summary>line</summary>

| Time (s) | Acceleration (m/s²) |
| -------- | ------------------- |
| 0.0      | 1.00                |
| 1.0      | 1.00                |
| 2.0      | 0.00                |
| 2.0      | -1.00               |
| 3.5      | 1.00                |
</details>

Figure 17.3: Double integrator acceleration
