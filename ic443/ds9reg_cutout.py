import numpy as np
import astropy.io.fits as pyfits
import pyregion
import pyregion._region_filter as filter


# User input: infile, outfile, region_name, binsize
def ds9reg_cutout(infile, outfile, region_name, binsize):

    hdu_orig = pyfits.open(infile)[0]
    data = hdu_orig.data
    new_header = hdu_orig.header.copy()

    hdu = pyfits.PrimaryHDU(data)
    hdu.header = new_header
    hdulist = pyfits.HDUList([hdu])

    r = pyregion.open(region_name)
    myfilter = r.get_filter()

    mask = myfilter.mask(data.shape)
    data[~mask] = 0
    hdulist[0].data = data
    norm = np.sum(hdulist[0].data)*(np.pi/180)**2*(binsize**2)
    hdulist[0].data = hdulist[0].data/norm
    hdulist[0].writeto(outfile)
