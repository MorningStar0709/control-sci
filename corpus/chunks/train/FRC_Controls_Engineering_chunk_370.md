# 12.1.3 Current limiting

Current limiting of a DC motor reduces the maximum input voltage to avoid exceeding a current threshold. Predictive current limiting uses a projected estimate of the current, so the voltage is reduced before the current threshold is exceeded. Reactive current limiting uses an actual current measurement, so the voltage is reduced after the current threshold is exceeded.

The following pseudocode demonstrates each type of current limiting.

```txt
