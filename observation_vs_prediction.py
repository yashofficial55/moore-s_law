import pylab

# The data - lists of years:
year = [1972, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 1999, 2000, 2003,
        2004, 2007, 2008, 2012]
# and number of transistors (ntrans) on CPUs in millions:
ntrans = [0.0025, 0.005, 0.029, 0.12, 0.275, 1.18, 3.1, 7.5, 24.0, 42.0,
          220.0, 592.0, 1720.0, 2046.0, 3100.0]
# turn the ntrans list into a pylab array and multiply by 1 million
ntrans = pylab.array(ntrans) * 1.e6

y0, n0 = year[0], ntrans[0]
# A linear array of years spanning the data's years
y = pylab.linspace(y0, year[-1], year[-1] - y0 + 1)
# Time taken in years for the number of transistors to double
T2 = 2.
moore = pylab.log10(n0) + (y - y0) / T2 * pylab.log10(2)

pylab.plot(year, pylab.log10(ntrans), '*', markersize=12, color='r',
           markeredgecolor='r', label='observed')
pylab.plot(y, moore, linewidth=2, color='k', linestyle='--', label='predicted')
pylab.legend(fontsize=16, loc='upper left')
pylab.xlabel('Year', fontsize=16)
pylab.ylabel('log(ntrans)', fontsize=16)
pylab.title("Moore's Law")
pylab.show()
