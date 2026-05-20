# State-Space Descriptions

Consider a system composed of two subsystems that are continuous constant-coefficient dynamic systems. Assume that there are two periodic samplers with periods $h_{1}$ , and $h_{2}$ . Let the ratio of the periods be a rational number $h_{1}/h_{2} = m_{1}/m_{2}$ , where $m_{1}$ and $m_{2}$ have no common factor. Then there exists a smallest integer m and a real number h such that

$$m = m _ {1} m _ {2} \quad h _ {1} = \frac {h m _ {1}}{m} \quad h _ {2} = \frac {h m _ {2}}{m}$$

If the samplers are synchronized, it follows that the control signals will be constant over sampling periods of length h/m. Sampling with that period gives a discrete-time system that is periodic with period h. The system can then be described as a constant discrete-time system if the values of the system variables are considered only at integer multiples of h. The ordinary discrete-time theory can then be applied. An example illustrates the idea.
