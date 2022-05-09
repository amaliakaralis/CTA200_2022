import numpy as np
def complex_iter(z0, Npts, Nit):
    """
    For each of Npts points in the complex plane c=x+iy, iterate z_i+1 = z_i**2 + c.
    
    Parameters:
    -----------
    z0: float
        initial value of z for iteration
    Npts: int
        Npts the the gridsize
        (Npts**2 is the number of points in the complex plane)
    Nit: int
        number of iterations of z
        
    Returns:
    --------
    X: numpy array
        1d array of length Npts**2, xgrid
    Y: numpy array
        1d array of length Npts**2, ygrid
    Z: numpy array
        size Npts**2 x Nit, each of the Nit z values for each of the Npts**2 points in the plane
    div_iter: numpy array
        1d array of length Npts**2
        the iteration at which each point in the plane diverges
        if the point does not diverge within Nit, its value of div_iter is NaN
    """
    x = np.linspace(-2, 2, Npts)
    y = np.linspace(-2, 2, Npts)
    X, Y = np.meshgrid(x, y) # NxN grid of points in the complex plane
    X = X.flatten() # flatten to 1d arrays
    Y = Y.flatten()
    Z = np.zeros((Npts**2, Nit), dtype=np.complex_) # grid of length Npts**2 for each point in the plane to store the Nit values of zi
    div_iter = np.empty(Npts**2)
    div_iter[:] = np.NaN # initialize an arrays of NaNs for the iteration at which a point diverges
    for i in range(Npts**2):
        # iterate over each point in the complex plane
        zi = complex(z0, 0)
        c = complex(X[i], Y[i]) # the complex number c
        for k in range(Nit):
            # for each iteration of z 
            if np.isnan(zi) == True and np.isnan(div_iter[i]) == True:
                # the iteration at which this diverges
                div_iter[i] = k
            Z[i, k] = zi
            zip1 = zi**2 + c
            zi = zip1
    return X, Y, Z, div_iter
