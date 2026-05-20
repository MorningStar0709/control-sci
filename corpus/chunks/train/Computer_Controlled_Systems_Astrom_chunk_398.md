# Feedforward

Feedforward is another control method. It is used to eliminate disturbances that can be measured. The basic idea is to use the measured disturbance to anticipate the influence of the disturbance on the process variables and to introduce suitable compensating control actions. See Fig. 6.3. The advantage compared to feedback is that corrective actions may be taken before the disturbance has influenced the variables. If the transfer functions relating the output y to the disturbance w and the control u are $H_{w}$ and $H_{p}$ , the transfer function $H_{ff}$ of the feedforward compensator should ideally be

$$H _ {f f} = - H _ {p} ^ {- 1} H _ {w}$$

If this transfer function is unstable or nonrealizable, a suitable approximation is chosen instead. The design of the feedforward compensator is often based on a simple static model. The transfer function $H_{ff}$ is then simply a static gain.

Because feedforward is an open-loop compensation, it requires a good process model. With digital control, it is easy to incorporate a process model. Thus it can be anticipated that use of feedforward will increase with digital control. The design of a feedforward compensator is in essence a calculation of the inverse of a dynamic system.
