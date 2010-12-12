#
#   TwitterController.py
#
#   Created by Jair Gaxiola on 12/12/10.
#   Copyright 2010 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

class TwitterController(WebView):

	def init(self):
		#print dir(self)
		#print "aca init twit"
		self.setMainFrameURL_("http://m.twitter.com")
		return self




