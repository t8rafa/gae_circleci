# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-

import unittest
import webtest
import main

sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/')
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/lib/yaml/lib')

class MainTests(unittest.TestCase):
	def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()

    def tearDown(self):
        self.testbed.deactivate()
	
	def test_get(self):
	    app = webtest.TestApp(main.app)
	
	    response = app.get('/')
	
	    assert response.status_int == 200
	    assert response.body == 'Hello, World!'
	    
if __name__ == '__main__':
    unittest.main()