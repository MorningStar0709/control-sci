# 6.10.6 Voltage compensation

To improve controller tracking, one may want to use the voltage renormalized to the power rail voltage to compensate for voltage drop when current spikes occur. This can be done as follows.

$$V = V _ {c m d} \frac {V _ {\text { nominal }}}{V _ {\text { rail }}} \tag {6.23}$$

where V is the controller’s new input voltage, $V _ { c m d }$ is the old input voltage, $V _ { n o m i n a l }$ is the rail voltage when effects like voltage drop due to current draw are ignored, and $V _ { r a i l }$ is the real rail voltage.

To drive the model with a more accurate voltage that includes voltage drop, the reciprocal can be used.

$$V = V _ {c m d} \frac {V _ {\text { rail }}}{V _ {\text { nominal }}} \tag {6.24}$$

where V is the model’s new input voltage. Note that if both the controller compensation and model compensation equations are applied, the original voltage is obtained. The model input only drops from ideal if the compensated controller voltage saturates.
