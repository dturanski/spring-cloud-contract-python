__copyright__ = '''
Copyright 2020 the original author or authors.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import functools
import os
import logging
from flask import current_app as app

FORMAT = '%(asctime)s - %(name)s - %(levelname)s : %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

"""
Generate flask endpoints for Spring Cloud Contract testing.
"""
class Stub:
    def __init__(self, app):
        self.app = app
        
    def create_stub(self, func, *args, **kwargs):
        '''Create a test endpoint at /springcloudcontract/" + func.__name__'''
        if 'CONTRACT_TEST' in os.environ:    
            def stub_for_func():
                return func(*args, **kwargs)
            logging.info("Adding contract test url: /springcloudcontract/" + func.__name__)
            self.app.add_url_rule('/springcloudcontract/'+func.__name__, methods=[
                                  'POST'], view_func=stub_for_func, endpoint=func.__name__)
