import astropy.io.fits as pyfits
import aplpy

from scipy import ndimage
from astropy.convolution import convolve as con,Gaussian2DKernel as gaus

def convolve(fits, sigma, mode, outfile):

    hdu = pyfits.open(fits)[0]
    header = hdu.header
    data = hdu.data

    smoothed = con(data, gaus(stddev=sigma))

    #smoothed_figure = aplpy.FITSFigure(fits.PrimaryHDU(data=smoothed,header=header))

    #img_gaus = ndimage.filters.gaussian_filter(data, sigma, mode)

    hdu = pyfits.PrimaryHDU(smoothed)
    hdu.header = header
    hdulist = pyfits.HDUList([hdu])

    hdulist.writeto('%s.fits' % (outfile), overwrite=True)