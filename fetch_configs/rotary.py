# Copyright (c) 2025 Owen Gaydosz. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# Purpose: This makes the command fetch --nohooks --no-history osmium possible, instead of rebranding Chromium in the terminal.

import ast
import sys
import config_util

class OsmiumBrowser(config_util.Config):
    """Basic Config class for the Rotary Engine."""
    @staticmethod
    def fetch_spec(props):
        url = 'https://github.com/owgydz/rotary.git'
      
        solution = {
            'name': 'src',
            'url': url,
            'managed': False,
            'custom_deps': {},
            'custom_vars': {},
        }

        spec = {
            'solutions': [solution],
        }

        return {
            'type': 'gclient_git',
            'gclient_git_spec': spec,
        }

    @staticmethod
    def expected_root(props):
        return 'src'

def main(argv=None):
    return RotaryEngine().handle_args(argv)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
