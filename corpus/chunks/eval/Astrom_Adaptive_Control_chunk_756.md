# 12.6 AUTOMOBILE CONTROL

Microprocessor-based engine control systems were introduced in the automotive industry in the 1970s to address the demands of increased fuel economy and reduced emissions. Early electronic control systems had modest application. Today, the powertrain computer accomplishes a multitude of control tasks, including vehicle speed or "cruise" control, idle speed regulation, automatic transmission shift actuation, control of various emission-related systems, fuel control, and ignition timing, as well as many diagnostic functions. These highly I/O intensive systems must be cost effective and function acceptably in many thousands of vehicles with attendant manufacturing variability over a wide range of operating conditions.

![](image/6dbe7e05b6c5c21606918f76321345367382a336c76b8e95bb1f5dfb1d4994f4.jpg)

<details>
<summary>natural_image</summary>

Side profile of a black sedan car on a road (no visible text or symbols)
</details>

Figure 12.14 This Ford Mustang has state-of-the-art adaptive power train controls. (With courtesy of Ford Motor Company.)

Many of the control functions in automobiles are open-loop look-up table oriented. Some automatic calibration methods have been developed to optimize table entries with respect to fuel economy, constrained by emissions. Typical closed-loop structures are comprised of individual operational loops, often PI or PID, and may contain several feedforward paths that are designed to reject measurable or predictable disturbances. Applications of adaptive control concepts can be found in many of those powertrain control functions where online self-tuning techniques are used to adjust controller parameters (in most cases, the feedforward parameters) to compensate for component and operating condition variability. One such adaptive control structure is the air-fuel ratio control method introduced by Ford in the mid-1980s to reduce sensitivity to component variability and calibration inaccuracy. Figure 12.14 shows a car with adaptive power train control.
