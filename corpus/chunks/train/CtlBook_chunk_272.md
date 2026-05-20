# Plot time response
plt.figure(1)
plt.plot(t, y1[0][0], t, y1[1][0])
plt.plot(t, y1[2][0], t, y1[3][0])

plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
ax = plt.gca()
ax.set_ylim([-2,10])
plt.legend(['Position X2', 'Velocity X2-dot', 'Position X3', 'Velocity X3-dot'])
plt.title('Step Response: 4x4 state space model')
