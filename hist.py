# Randomizing data, generating statistics and histogram

import numpy as np
import matplotlib.pyplot at plt
mu = 80
sigma =  10
x = np.random.normal(mu, sigma, 100)

print("Random Normal Array Mean Centered",x[:10])

print("mean", np.mean(x))
print("std dev", np.std(x))

plt.hist(x)
plt.show()

#did it!
 

