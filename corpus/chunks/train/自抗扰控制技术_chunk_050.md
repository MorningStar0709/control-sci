$$
\left\{ \begin{array}{l l} \dot {e} _ {0} = e _ {1}, & e _ {0} (0) = 0 \\ \dot {e} _ {1} = e _ {2}, & e _ {1} (0) = v _ {0} \\ \dot {e} _ {2} = - a _ {1} \left(e _ {1} - v _ {0}\right) - a _ {2} e _ {2} - \left(k _ {0} e _ {0} + k _ {1} e _ {1} + k _ {2} e _ {2}\right), e _ {2} (0) = 0 \\ y = v _ {0} - e _ {1} & \end{array} \right. \tag {1.5.8}
$$

现在,假定时间尺度 $\rho = 1$ (即 $a_{1} = 1$ 的) 系统

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ x _ {2} = - (x _ {1} - u) - a _ {2} x _ {2} \end{array} \right. \tag {1.5.9}
$$

设定值为 $v_{0}$ 时，已调好了PID控制律

$$u ^ {*} = k _ {0} ^ {*} e _ {0} + k _ {1} ^ {*} e _ {1} + k _ {2} ^ {*} e _ {2} \tag {1.5.10}$$

这时所得的闭环系统误差方程为

$$
\left\{ \begin{array}{l l} e _ {0} ^ {*} = e _ {1} ^ {*}, & e _ {0} ^ {*} (0) = 0 \\ e _ {1} ^ {*} = e _ {2} ^ {*}, & e _ {1} ^ {*} (0) = v _ {0} \\ e _ {2} ^ {*} = - \left(e _ {1} ^ {*} - v _ {0}\right) - a _ {2} e _ {2} ^ {*} - \left(k _ {0} ^ {*} e _ {0} ^ {*} + k _ {1} ^ {*} e _ {1} ^ {*} + k _ {2} ^ {*} e _ {2} ^ {*}\right), e _ {2} ^ {*} (0) = 0 \\ y = v _ {0} - e _ {1} ^ {*} \end{array} \right. \tag {1.5.11}
$$

我们的问题是误差反馈律(1.5.7) $u=k_{0}e_{0}+k_{1}e_{1}+k_{2}e_{2}$ 和误差反馈律(1.5.10) $u^{*}=k_{0}^{*}e_{0}+k_{1}^{*}e_{1}+k_{2}^{*}e_{2}$ 之间有何关系?

对误差系统(1.5.8)施行如下时间尺度变换和误差尺度变换

$$
\left\{ \begin{array}{l} t = \frac {1}{\sqrt {a _ {1}}} \tau = \rho \tau \\ \varepsilon_ {0} = \frac {e _ {0}}{\rho}, \varepsilon_ {1} = e _ {1}, \varepsilon_ {2} = \rho e _ {2} \end{array} \quad \left(x ^ {\prime} = \frac {\mathrm{d} x}{\mathrm{d} \tau}, \frac {\mathrm{d} x}{\mathrm{d} \tau} = \rho \frac {\mathrm{d} x}{\mathrm{d} t}\right) \right. \tag {1.5.12}
$$

就得

$$
\left\{ \begin{array}{l l} \varepsilon_ {0} ^ {\prime} = \varepsilon_ {1}, & \varepsilon_ {0} (0) = 0 \\ \varepsilon_ {1} ^ {\prime} = \varepsilon_ {2}, & \varepsilon_ {1} (0) = v _ {0} \\ \varepsilon_ {2} ^ {\prime} = - \rho^ {2} a _ {1} (\varepsilon_ {1} - v _ {0}) - \rho a _ {2} \varepsilon_ {2} - (\rho^ {3} k _ {0} \varepsilon_ {0} + \rho^ {2} k _ {1} \varepsilon_ {1} + p k _ {2} \varepsilon_ {2}), \varepsilon_ {2} (0) = 0 \\ y = v _ {0} - \varepsilon_ {1} & \end{array} \right. \tag {1.5.13}
$$

显然，由于 $\rho^2 a_1 = 1$ ，这个系统变成时间尺度 $\rho = 1$ 的系统.于是由等式

$$u ^ {*} = k _ {0} ^ {*} e _ {0} + k _ {1} ^ {*} e _ {1} + k _ {2} ^ {*} e _ {2} = \rho^ {3} k _ {0} \varepsilon_ {0} + \rho^ {2} k _ {1} \varepsilon_ {1} + \rho k _ {2} \varepsilon_ {2}$$

可得控制系统(1.5.5)所需的PID控制律(1.5.7)的各增益

$$k _ {0} = \frac {k _ {0} ^ {*}}{\rho^ {3}}, k _ {1} = \frac {k _ {1} ^ {*}}{\rho^ {2}}, k _ {2} = \frac {k _ {2} ^ {*}}{\rho} \tag {1.5.14}$$
