# Search 1

Using the command line or your Jupyter Notebook, run setup10p6.py. The script will call controlDesign447.py to perform the search of $1 3 ^ { 3 } \overset { \cdot } { = } 2 1 9 7$ controllers with the dierent values of the three gains, and nds the combination of gains that gives the best step response for each weight scheme.

At the end of the search the ve best step responses (according to your 5 weight schemes) are plotted automatically and the gains are reported on the console.

Our rst results are somewhat promising (Figure 10.3). A 6th weight vector was added (W\_BH) which weights settling time and percent overshoot equally and ignores the others.

Checking Search Boundaries ( Wbal )

Search boundary reached: Kd min

Search Time: 3.63 minutes. N sims = 9261 (2804129.0 ticks/min)

Do you want to see results printout? <CR>

Goals:

tsd : 0.55 pod : 20.0 ssed : 0.0 cu\_max: 100000 gm\_db : 10.0

<table><tr><td colspan="9">Reporting: WTS[Ts = 0.550 Kp: 7.270 Ki: 29.907 Kd: 0.559Settling Time: 0.550 Overshoot: 15.539 % SSE: 0.001 Ctl Effort: 22.361 Gain Marg: 80.0 dB ]</td></tr><tr><td colspan="9">Reporting: WOS[Overshoot = 20.00 Kp: 6.708 Ki: 17.027 Kd: 0.294Settling Time: 0.668 Overshoot: 19.994 % SSE: 0.000 Ctl Effort: 11.746 Gain Marg: 80.0 dB ]</td></tr><tr><td colspan="9">Reporting: WSSE[SSE = 0.00 Kp: 7.880 Ki: 20.000 Kd: 0.439Settling Time: 0.412 Overshoot: 16.004 % SSE: 0.000 Ctl Effort: 17.565 Gain Marg: 80.0 dB ]</td></tr><tr><td colspan="9">Reporting: WU[Control Effort Max = 100000.00 Kp: 6.708 Ki: 8.944 Kd: 0.112Settling Time: 1.099 Overshoot: 28.884 % SSE: 0.028 Ctl Effort: 5.997 Gain Marg: 26.5 dB ]</td></tr><tr><td colspan="9">Reporting: WM[Gain Margin = 10dB Kp: 13.840 Ki: 12.341 Kd: 0.131Settling Time: 1.099 Overshoot: 58.156 % SSE: 0.048 Ctl Effort: 11.266 Gain Marg: 10.0 dB ]</td></tr><tr><td colspan="9">Reporting: Wbal[Balanced Kp: 11.783 Ki: 9.694 Kd: 0.112Settling Time: 0.944 Overshoot: 44.784 % SSE: 0.003 Ctl Effort: 9.746 Gain Marg: 11.5 dB ]</td></tr><tr><td colspan="9">Reporting: W_BH[BH_bal Kp: 9.256 Ki: 20.000 Kd: 0.439Settling Time: 0.547 Overshoot: 19.753 % SSE: 0.001 Ctl Effort: 17.565 Gain Marg: 80.0 dB ]</td></tr></table>
