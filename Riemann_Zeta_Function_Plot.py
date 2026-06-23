import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta

# ==========================
# Parameters
# ==========================

t = np.linspace(0, 50, 2000)
s = 0.5 + 1j * t

# ==========================
# Compute Zeta Function
# ==========================

zeta_vals = zeta(s)

real_part = np.real(zeta_vals)
imag_part = np.imag(zeta_vals)
magnitude = np.abs(zeta_vals)

# First few non-trivial zeros
zeros = [
    14.134725,
    21.022040,
    25.010858,
    30.424876,
    32.935061,
    37.586178,
    40.918719,
    43.327073,
    48.005150
]

# ==========================
# Plot Styling
# ==========================

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(14, 8))

# Real Part
ax.plot(
    t,
    real_part,
    linewidth=2,
    color='cyan',
    label='Re(ζ)'
)

# Imaginary Part
ax.plot(
    t,
    imag_part,
    linewidth=2,
    color='orange',
    label='Im(ζ)'
)

# Magnitude
ax.plot(
    t,
    magnitude,
    linewidth=2,
    linestyle='--',
    color='lime',
    label='|ζ|'
)

# Highlight Non-Trivial Zeros
for z in zeros:
    ax.axvline(
        z,
        color='red',
        linestyle=':',
        alpha=0.6
    )

    ax.scatter(
        z,
        0,
        color='red',
        s=50
    )

# Labels
ax.set_title(
    'Riemann Zeta Function on the Critical Line',
    fontsize=18,
    pad=20
)

ax.set_xlabel(
    'Imaginary Part (t)',
    fontsize=14
)

ax.set_ylabel(
    r'$\zeta(0.5+it)$',
    fontsize=14
)

# Formula Display
plt.figtext(
    0.5,
    0.02,
    r'$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}'
    r'\qquad'
    r'\zeta(s)=\prod_{p\,prime}\frac{1}{1-p^{-s}}$',
    ha='center',
    fontsize=12,
    color='white'
)

# Grid
ax.grid(
    True,
    linestyle='--',
    alpha=0.3
)

# Legend
ax.legend(fontsize=12)

plt.tight_layout()
plt.show()