# so we can plot the x-dot(t)
C = np.matrix([[1,0], [0,1]])
D = ColVector([0,0])
sys2 = ctl.ss(A,B,C,D)  # redo the system and step response
input_row = 0
output_row = 1
stepResponseData = ctl.step_response(sys2, t)  # note py.ctl generates its own input
t = stepResponseData.time
y2 = stepResponseData.outputs
print("Shape y2:",y2.shape)
plt.plot(t, y2[output_row][input_row])  # plot x-dot(t)

plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
ax = plt.gca()
