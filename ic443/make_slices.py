import numpy as np
import astropy.io.fits as pyfits

#from astropy.wcs import WCS
#from reproject import reproject_interp

def make_slices(infile, min_slice, max_slice):

    with pyfits.open(infile) as f:
        #header = f[0].header
        data = f[0].data

    # x_length = header['NAXIS1']
    # y_length = header['NAXIS2']
    # z_length = header['NAXIS3']
    #
    # delta = header['CDELT3']
    # init_vel = header['CRVAL3']
    data_sum = data[min_slice-1]
    this_range = np.arange(min_slice,max_slice,1)
    for i in this_range:
        data_sum += data[i]
    hdu = pyfits.PrimaryHDU(data_sum)

    hdulist = pyfits.HDUList([hdu])
    hdulist.writeto('%s%i-%i.fits' % ('slices',int(min_slice),int(max_slice)))