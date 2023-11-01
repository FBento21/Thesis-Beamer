import numpy as np
import matplotlib.pyplot as plt
import scienceplots
plt.style.use('science')

theta = np.linspace(0, 2*np.pi, 300)

def omega_boundary(t):
    return 1 + np.sin(4*t)/10 + np.cos(3*t)/10

def omega_source(t):
    return 1.1*(1 + np.sin(4*t)/10 + np.cos(3*t)/10)

def omega_hole(t):
    return 0.3*(1 + np.cos(3*t)/10)

def omega_hole_source(t):
    return 0.2*(1 + np.cos(3*t)/10)



x_boundary = omega_boundary(theta)*np.cos(theta)
y_boundary = omega_boundary(theta)*np.sin(theta)

x_source = omega_source(theta)*np.cos(theta)
y_source = omega_source(theta)*np.sin(theta)

x_hole = omega_hole(theta)*np.cos(theta)
y_hole = omega_hole(theta)*np.sin(theta)

boundary = np.column_stack([x_boundary, y_boundary])
source = np.column_stack([x_source, y_source])

plt.figure(figsize=(8, 6))
plt.plot(boundary[:, 0], boundary[:, 1])
plt.plot(source[:, 0], source[:, 1])
plt.text(0, 0, r'$\Omega$', fontsize=20)
plt.text(0.4, 0.85, r'$\hat{\Gamma}$', fontsize=20)

plt.fill(boundary[:, 0], boundary[:, 1], 'b', alpha=0.5)

plt.axis('off')


plt.show()
