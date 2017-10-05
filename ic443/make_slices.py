import numpy as np
import astropy.io.fits as pyfits
import math as m


def _distance(x0,y0,x,y):
    return m.sqrt((x-x0)**2 + (y-y0)**2)

def make_slices(path, infile, sample_file, min_slice, max_slice, clean, threshold, radius):

    hdu_orig = pyfits.open(infile)[0]
    header = hdu_orig.header
    data = hdu_orig.data

    hdu_sample = pyfits.open(sample_file)[0]
    sample_header = hdu_sample.header

    new_header = sample_header.copy()
    new_header['NAXIS1'] = header['NAXIS1']
    new_header['NAXIS2'] = header['NAXIS2']
    new_header['CTYPE1'] = header['CTYPE1']
    new_header['CRPIX1'] = header['CRPIX1']
    new_header['CRVAL1'] = header['CRVAL1']
    new_header['CDELT1'] = header['CDELT1']
    new_header['CTYPE2'] = header['CTYPE2']
    new_header['CRPIX2'] = header['CRPIX2']
    new_header['CRVAL2'] = header['CRVAL2']
    new_header['CDELT2'] = header['CDELT2']
    new_header['DATE'] = header['DATE-OBS']
    del new_header['TELESCOP']
    del new_header['INSTRUME']
    del new_header['CREATOR']
    del new_header['CHECKSUM']
    del new_header['FILENAME']
    del new_header['DSTYP1']
    del new_header['DSUNI1']
    del new_header['DSVAL1']
    del new_header['DSTYP2']
    del new_header['DSUNI2']
    del new_header['DSVAL2']
    del new_header['DSREF2']
    del new_header['DSTYP3']
    del new_header['DSUNI3']
    del new_header['DSVAL3']
    del new_header['DSTYP4']
    del new_header['DSUNI4']
    del new_header['DSVAL4']
    del new_header['DSTYP5']
    del new_header['DSUNI5']
    del new_header['DSVAL5']
    del new_header['DSTYP6']
    del new_header['DSUNI6']
    del new_header['DSVAL6']
    del new_header['DSTYP7']
    del new_header['DSUNI7']
    del new_header['DSVAL7']
    del new_header['DSTYP8']
    del new_header['DSUNI8']
    del new_header['DSVAL8']

    data_sum = data[min_slice-1]
    this_range = np.arange(min_slice,max_slice,1)
    for i in this_range:
        data_sum += data[i]
    hdu = pyfits.PrimaryHDU(data_sum)
    hdu.header = new_header
    hdulist = pyfits.HDUList([hdu])

    hdulist.writeto('%s%i-%i.fits' % (path,int(min_slice),int(max_slice)), overwrite=True)

    if clean:
        wmap_image = pyfits.open('%s%i-%i.fits' % (path,int(min_slice),int(max_slice)))
        for x,row in enumerate(wmap_image[0].data):
            for y in enumerate(row):
                if (y[1] < threshold) or (_distance(np.ceil(float(wmap_image[0].header['NAXIS2'])/2)-10,np.ceil(float(wmap_image[0].header['NAXIS1']/2)), x, y[0]) > radius):
                        #or (_distance(np.ceil(float(wmap_image[0].header['NAXIS2'])/2)-10,np.ceil(float(wmap_image[0].header['NAXIS1']/2)-5), x, y[0]) < 15)\
                        #or (_distance(np.ceil(float(wmap_image[0].header['NAXIS2'])/2)-25,np.ceil(float(wmap_image[0].header['NAXIS1']/2)-15), x, y[0]) < 12)\
                        #or (_distance(np.ceil(float(wmap_image[0].header['NAXIS2'])/2)-15,np.ceil(float(wmap_image[0].header['NAXIS1']/2)+20), x, y[0]) < 12)
                    wmap_image[0].data[x,y[0]]=0

        wmap_image[0].writeto('%s%i-%i_clean.fits' % (path, int(min_slice), int(max_slice)), overwrite=True)

