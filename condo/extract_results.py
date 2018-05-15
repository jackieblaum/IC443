import numpy as np

# Print out results of analysis from npy file
def extract_results(npy_file,sources_elements):

    # Read the npy file created by the analysis script
    o = np.load(npy_file).flat[0]

    # Loop through the sources (not including first two which are background sources)
    for i in range(2,len(o['sources'].keys())):

        # Loop through the user-selected elements of the source to be printed
        for j in range(0,len(sources_elements)):

            source = o['sources'].keys()[i]
            print(sources_elements[j])
            print(o['sources'][source][sources_elements[j]])
            print

        print('************************************************')
        print