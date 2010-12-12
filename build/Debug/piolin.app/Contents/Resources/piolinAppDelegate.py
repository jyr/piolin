#
#  piolinAppDelegate.py
#  piolin
#
#  Created by Jair Gaxiola on 12/12/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

from Foundation import *
from AppKit import *

class piolinAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
