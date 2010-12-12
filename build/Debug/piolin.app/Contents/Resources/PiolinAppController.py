#
#   PiolinAppController.py
#
#   Created by Jair Gaxiola on 12/12/10.
#   Copyright 2010 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class PiolinAppController(NSObject):
    webView = objc.IBOutlet()
	
    def awakeFromNib(self):
		self.webView.setMainFrameURL_("https://mobile.twitter.com/session/new")




