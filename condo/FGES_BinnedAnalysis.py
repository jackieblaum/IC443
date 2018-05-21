import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

#Import the GAnalysis module from fermipy
from fermipy.gtanalysis import GTAnalysis

def FGES_BinnedAnalysis(prefix,ANALYSISDIR,numsources,xmlsources,spectrum,spectrumpoints,spectrumpointsUL,spectrum_mev_or_erg,spectrum_mev_or_tev,configfile):

    ANALYSISDIR = ANALYSISDIR + prefix + '/'
    i = numsources #number of sources
    sources_names = ''
    for x in range(0,i):
        sources_names += str(xmlsources[x])

    #Run the likelihood analysis up to doing the fit
    gta = GTAnalysis(ANALYSISDIR + configfile,logging={'verbosity': 3})
    gta.setup()

    #Print the pre likelihood fit parameters
    gta.print_roi()
    for x in range(0,i):
        print(gta.roi[xmlsources[x]])

    #Do an initial optimization of parameters
    gta.optimize()

    gta.print_roi()

    #Prepare to get the likelihood
    #Free the normalizations of sources within 7 degrees of the center of the field of view
    gta.free_sources(distance=7.0,pars='norm')
    gta.free_source('galdiff')
    gta.free_source('isodiff')
    for x in range(0,i):
       gta.free_source(xmlsources[x])

    #LIKELIHOOD ANALYSIS
    fit_results = gta.fit()

    #print out and return the results
    print('Fit Quality: ',fit_results['fit_quality'])
    for x in range(0,i):
        print(gta.roi[xmlsources[x]])
    gta.write_roi(sources_names + 'fit')

    #RESIDUAL MAP
    model = {'Index' : 2.0, 'SpatialModel' : 'PointSource'}
    maps = gta.residmap('residual',model=model,make_plots=True)

    # Generate residual map with source of interest removed from the model
    model_nosource = {'Index' : 2.0, 'SpatialModel' : 'PointSource'}
    maps_nosource = gta.residmap('residual_wsource',model=model_nosource,exclude=xmlsources,make_plots=True)

    #TS Map
    tsmap = gta.tsmap('tsmap',model={'SpatialModel' : 'PointSource', 'Index' : 2.0},exclude=xmlsources,make_plots=True)
    tsmap_wSNR  = gta.tsmap('tsmap_wSNR',model={'SpatialModel' : 'PointSource', 'Index' : 2.0},make_plots=True)

    #PLOT SEDs
    for x in range(0,i):
        c = np.load('10to500gev/' + sources_names + 'fit.npy').flat[0]
        sorted(c['sources'].keys())
        c['sources'][xmlsources[x]]['flux']
        print(c['sources'][xmlsources[x]]['param_names'][:4])
        print(c['sources'][xmlsources[x]]['param_values'][:4])
        c['sources'][xmlsources[x]]['ts']

        E = np.array(c['sources'][xmlsources[x]]['model_flux']['energies'])
        dnde = np.array(c['sources'][xmlsources[x]]['model_flux']['dnde'])
        dnde_hi = np.array(c['sources'][xmlsources[x]]['model_flux']['dnde_hi'])
        dnde_lo = np.array(c['sources'][xmlsources[x]]['model_flux']['dnde_lo'])

        if spectrum_mev_or_erg == "erg":
            suffix = 'erg'
            mult = 0.00000160218
        elif spectrum_mev_or_erg == "mev":
            suffix = 'MeV'
            mult = 1

        if spectrum_mev_or_tev == "mev":
            xaxis = 'MeV'
            denominator = 1
        elif spectrum_mev_or_tev == "tev":
            xaxis = 'TeV'
            denominator = 1000000

        if spectrum:
            plt.loglog(E, (E**2)*dnde, 'k--')
            plt.loglog(E, (E**2)*dnde_hi, 'k')
            plt.loglog(E, (E**2)*dnde_lo, 'k')
            plt.xlabel('E [MeV]')
            plt.ylabel(r'E$^2$ dN/dE [MeV cm$^{-2}$ s$^{-1}$]')
            plt.savefig('spectrum_'+xmlsources[x]+'.png')

        #GET SED POINTS
        if spectrumpoints:
            sed = gta.sed(xmlsources[x],make_plots=True)
            #sed = gta.sed(xmlsource,prefix=xmlsource + 'spectrum',loge_bins=)
            src = gta.roi[xmlsources[x]]
            #Plot without upper limits
            plt.loglog(E, (E**2)*dnde, 'k--')
            plt.loglog(E, (E**2)*dnde_hi, 'k')
            plt.loglog(E, (E**2)*dnde_lo, 'k')
            plt.errorbar(np.array(sed['e_ctr']),
                     sed['e2dnde'],
                     yerr=sed['e2dnde_err'], fmt ='o')
            plt.xlabel('E [MeV]')
            plt.ylabel(r'E$^{2}$ dN/dE [MeV cm$^{-2}$ s$^{-1}$]')
            #plt.show()
            plt.savefig('spectrumpoints_'+xmlsources[x]+'.png')
            #Plot with upper limits, last 5 points
            plt.loglog(E, (E**2)*dnde, 'k--')
            plt.loglog(E, (E**2)*dnde_hi, 'k')
            plt.loglog(E, (E**2)*dnde_lo, 'k')
            plt.errorbar(sed['e_ctr'][:-5],
                     sed['e2dnde'][:-5],
                     yerr=sed['e2dnde_err'][:-5], fmt ='o')
            plt.errorbar(np.array(sed['e_ctr'][-5:]),
                 sed['e2dnde_ul95'][-5:], yerr=0.2*sed['e2dnde_ul95'][-5:],
                     fmt='o', uplims=True)
            plt.xlabel('E [MeV]')
            plt.ylabel(r'E$^{2}$ dN/dE [MeV cm$^{-2}$ s$^{-1}$]')
            plt.savefig('spectrumpointsUL_'+xmlsources[x]+'.png')
        plt.clf()

