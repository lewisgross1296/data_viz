import numpy
import math as m
import matplotlib.pyplot as plt
import os
import sys
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Collision as Collision
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager
from spectrum_plot_tools import plotSpectralDataWithErrors

def extract(  rendezvous_file,
              estimator_id,
              entity_id,
              mcnp_file,
              mcnp_file_start,
              mcnp_file_end,
              is_a_current):
    
    # Reload the simulation
    manager = Manager.ParticleSimulationManagerFactory( rendezvous_file ).getManager()
    
    # Extract the estimator of interest
    estimator = manager.getEventHandler().getEstimator( estimator_id )

    entity_bin_data = estimator.getEntityBinProcessedData( entity_id )
    entity_bin_data["e_bins"] = estimator.getEnergyDiscretization()
    
    # Extract the mcnp data from the output file
    mcnp_file = open( mcnp_file, "r" )
    mcnp_file_lines = mcnp_file.readlines()
    
    mcnp_bin_data = {"e_up": [], "mean": [], "re": []}
    
    for i in range(mcnp_file_start,mcnp_file_end+1):
        split_line = mcnp_file_lines[i-1].split()
        
        mcnp_bin_data["e_up"].append( float(split_line[0]) )
        mcnp_bin_data["mean"].append( float(split_line[1]) )
        mcnp_bin_data["re"].append( float(split_line[2]) )

    if(is_a_current):
        with open('current_comparison.txt', 'w') as f: 
            print(entity_bin_data) 
            print('\n')
            print(mcnp_bin_data, file=f)
    else
        with open('flux_comparison.txt', 'w') as f:  
            print(entity_bin_data) 
            print('\n')
            print(mcnp_bin_data, file=f)
            
    # ensure file is closed
    print('file is closed? ')
    print(f.close)