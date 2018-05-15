import numpy as np

def extract_results(npy_file,sources_elements):

    # Read the npy file created by the analysis script
    o = np.load(npy_file).flat[0]
    for i in range(2,len(o['sources'].keys())):
        for j in range(0,len(sources_elements)):
            source = o['sources'].keys()[i]
            print(sources_elements[j])
            print(o['sources'][source][sources_elements[j]])
            print
        print('************************************************')
        print