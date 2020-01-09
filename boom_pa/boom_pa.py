#!/bin/env python3

import argparse
import numpy as np
from pathlib import Path

#P = 103.1 + 20 * log10((S/1013)^0.556 * ((w2/2.2)/110)^0.444 * (25/(rm/1000))^1.333)
#P = Peak overpressure (dB)
#S = Atmospheric pressure (mbar)
#w2 = TNTe (lbs; multiply yield by 2 if on surface or above)
#rm = Measurement distance (m)

#Convert to Pa:
#0.00002*10^(P/20))

here = Path(__file__).resolve().parent
exec(open(here / "version.py").read())

def main():
    parser = argparse.ArgumentParser(
    	formatter_class=argparse.RawDescriptionHelpFormatter,
    	description=
    	'Compute peak overpressure using BOOM model. Outputs Pa')
    
    parser.add_argument("-a","--atmo", type=float, default=1013.25,
        required=False, help="atmosphere pressure in mbar (1013.25)")
    
    parser.add_argument("-w","--w", type=float, 
        required=True, help="Yield in TNTe kt")
    
    parser.add_argument("-d","--dist", type=float, 
        required=True, help="Distance in meters")
    
    parser.add_argument("-s","--s", action='store_true', 
        default=False, required=False, 
        help="if set, assumes surface explosion")
    
    parser.add_argument("-v", "--verbose", action="count",
        default=0, help="increase spewage")
    
    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))
    
    args = parser.parse_args()
    atmo=args.atmo
    
    w2=args.w * 2204620 # convert kt to lbs
    
    if args.s == True:
        w2=w2*2
    
    m=args.dist
    
    P = 103.1 + 20 * np.log10((atmo/1013)**0.556 * ((w2/2.2)/110)**0.444 * (25/(m/1000))**1.333)
    Pa=0.00002*10**(P/20)

    print(f"W: {args.w} kt Distance: {m} m Pressure: {Pa:0.2f} Pa")

if __name__ == '__main__':
    main()

