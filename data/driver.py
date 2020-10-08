#!/usr/bin/python
import sys, os
from optparse import *
from extractor import extract

if __name__ == "__main__":

    # Parse the command line arguments
    parser = OptionParser()
    parser.add_option("--rendezvous_file", type="string", dest="rendezvous_file",
                      help="the rendezvous file to load")
    parser.add_option("--estimator_id", type="int", dest="estimator_id",
                      help="the estimator id to use")
    parser.add_option("--entity_id", type="int", dest="entity_id",
                      help="the entity id to use")
    parser.add_option("--mcnp_file", type="string", dest="mcnp_file",
                      help="the mcnp output file to load")
    parser.add_option("--mcnp_file_start", type="int", dest="mcnp_file_start",
                      help="the mcnp output file start line")
    parser.add_option("--mcnp_file_end", type="int", dest="mcnp_file_end",
                      help="the mcnp output file start line")
    parser.add_option("--current", action="store_true", dest="is_a_current",
                      help="the data corresponds to a current")
    parser.add_option("--flux", action="store_false", dest="is_a_current",
                      help="the data corresponds to a flux")
    options,args = parser.parse_args()

    # extract the relevant data
    extract(  options.rendezvous_file,
              options.estimator_id,
              options.entity_id,
              options.mcnp_file,
              options.mcnp_file_start,
              options.mcnp_file_end,
              options.is_a_current)