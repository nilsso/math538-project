import numpy as np
from matplotlib import pyplot as plt

from melody import Melody, pitch_intervals, rhythmic_intervals
from bach_bwv816 import notes as bwv816 # Gavotte
from bach_bwv1009 import notes as bwv1009 # Bourree

#! Sequence-to-mask helper
def mask(indices):
    res = np.array([False] * (indices[-1]+1))
    for i in indices:
        res[i] = True
    return res

#! Covering count $p_i(r)$
def p_i(mask, i, r):
    a = max(i - r, 0)
    b = min(i + r, len(mask))
    return sum(mask[a:b])

#! Calculate scaling for fixed i
def scaling(mask, i=None):
    i = i or len(mask) // 2
    # "to avoid the boundary effect (since the sequence is finite in length),
    # the largest radius of the box is limited to 1/10 of the total length of
    # the sequence"
    rvals = np.arange(2, len(mask) // 10, dtype=int)
    pvals = np.array([p_i(mask, i, r) for r in rvals])

    log2_rvals = np.ma.log2(rvals)
    log2_pvals = np.ma.log2(pvals)

    # Get cutoff for linear regression
    j = len(log2_pvals)
    while j > 2 and (log2_pvals[j-2] == log2_pvals[1]):
        j -= 1

    # Slope and intercept where slope is alpha the scaling
    if j > 1:
        z = np.polyfit(log2_rvals[:j], log2_pvals[:j], 1)
    else:
        z = np.polyfit(log2_rvals, log2_pvals, 1)

    return z, i, log2_rvals, log2_pvals, j

#! Plot scaling for fixed i
def plot_scaling(mask, s, i=None):
    z, i, log2_rvals, log2_pvals, j = scaling(mask, i)
    a, _ = z

    # Linear regression
    tvals = np.linspace(log2_rvals[0], log2_rvals[-1])
    f = np.poly1d(z)
    plt.plot(tvals, f(tvals), '--r', label=fr'$\alpha={a:.5}$')

    # Points
    plt.scatter(log2_rvals[:j], log2_pvals[:j], s=2**3, c='b', zorder=3,
            label='included in regression')
    plt.scatter(log2_rvals[j:], log2_pvals[j:], s=2**3, c='k', zorder=3,
            label='excluded from regression')

    plt.title(fr'({s}) Scaling of $p_i(r)$ for box-size $r$ with $i={i}$')
    plt.xlabel(r'$\log_2(r)$')
    plt.ylabel(r'$\log_2(p_i(r))$')
    plt.legend(loc='best')

def plot_scaling2(mask, s):
    n = len(mask) // 10
    a, b = n, n*9
    ivals = np.arange(a, b)
    avals = [scaling(mask, i)[0][0] for i in ivals]

    plt.scatter(ivals, avals, s=2**3)

    plt.xlim(0, len(mask))
    plt.ylim(0, 2)
    plt.xlabel(r'position $i$')
    plt.ylabel(r'$\alpha$')

# ------------------------------------------------------------------------------

notes = bwv816
# notes = bwv1009
# notes = ['c8']*600
# notes = ['c8'] + \
        # ['d', 'e', 'f', 'g', 'a', 'b', 'c'] * 20
M = Melody(notes)

# for n in M.notes:
    # print(n)

I = pitch_intervals(M)
R = rhythmic_intervals(M)

# print(I)
# print(R)

I_mask = mask(I)
R_mask = mask(R)

# print(I_mask)
# print(R_mask)

# plot_scaling(I_mask, 'Melody')
# plot_scaling(R_mask, 'Rhythm')
plot_scaling2(I_mask, 'Melody')
plt.show()
