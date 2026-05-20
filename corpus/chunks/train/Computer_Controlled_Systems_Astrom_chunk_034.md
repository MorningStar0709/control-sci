# 1.1 Introduction

Practically all control systems that are implemented today are based on computer control. It is therefore important to understand computer-controlled systems well. Such systems can be viewed as approximations of analog-control systems, but this is a poor approach because the full potential of computer control is not used. At best the results are only as good as those obtained with analog control. It is much better to master computer-controlled systems, so that the full potential of computer control can be used. There are also phenomena that occur in computer-controlled systems that have no correspondence in analog systems. It is important for an engineer to understand this. The main goal of this book is to provide a solid background for understanding, analyzing, and designing computer-controlled systems.

A computer-controlled system can be described schematically as in Fig. 1.1. The output from the process $y(t)$ is a continuous-time signal. The output is converted into digital form by the analog-to-digital (A-D) converter. The A-D converter can be included in the computer or regarded as a separate unit, according to one's preference. The conversion is done at the sampling times, $t_k$ . The computer interprets the converted signal, $\{y(t_k)\}$ , as a sequence of numbers, processes the measurements using an algorithm, and gives a new sequence of numbers, $\{u(t_k)\}$ . This sequence is converted to an analog signal by a digital-to-analog (D-A) converter. The events are synchronized by the real-time clock in the computer. The digital computer operates sequentially in time and each operation takes some time. The D-A converter must, however, produce a continuous-time signal. This is normally done by keeping the control signal constant between the conversions. In this case the system runs open loop in the time interval between the sampling instants because the control signal is constant irrespective of the value of the output.

The computer-controlled system contains both continuous-time signals and sampled, or discrete-time, signals. Such systems have traditionally been called sampled-data systems, and this term will be used here as a synonym for computer-controlled systems.

![](image/ceb8e4729e93424b586e5bdbeadcb08ca856dae8b1d0dd3eaff5af7d4a234ccc.jpg)

<details>
<summary>flowchart</summary>
