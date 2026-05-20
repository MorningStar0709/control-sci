# Definition 2.4.1 — PID controller.

$$u (t) = K _ {p} e (t) + K _ {i} \int_ {0} ^ {t} e (\tau) d \tau + K _ {d} \frac {d e}{d t} \tag {2.4}$$

where $K _ { p }$ is the proportional gain, $K _ { i }$ is the integral gain, $K _ { d }$ is the derivative gain, e(t) is the error at the current time t, and τ is the integration variable.

Figure 2.8 shows a block diagram for a system controlled by a PID controller.   
![](image/465ae65738e503ccacc16f42b12020169dd4516aab232143904bc13eda5b0d53.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r_t["r(t)"] --> add1["+"]
    add1 --> e_t["e(t)"]
    e_t --> Kp_e_t["K_p e(t)"]
    e_t --> Ki_d_t["K_i ∫₀ᵗ e(τ) dτ"]
    Ki_d_t --> add2["+"]
    add2 --> Plant["u(t)"]
    Plant --> y_t["y(t)"]
    y_t --> plant
    plant --> Kd_de_t["K_d de(t)/dt"]
    Kd_de_t --> add1
    add1 --> Kp_e_t
```
</details>

Figure 2.8: PID controller block diagram
