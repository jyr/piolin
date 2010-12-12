#
#  main.py
#  piolin
#
#  Created by Jair Gaxiola on 12/12/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

import PiolinAppController

# import modules containing classes required to start application and load MainMenu.nib
import piolinAppDelegate
# pass control to AppKit
AppHelper.runEventLoop()
