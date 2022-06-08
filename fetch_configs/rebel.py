# Copyright (c) 2022 Viasat Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import ast
import sys

import config_util


class Rebel(config_util.Config):
    @staticmethod
    def fetch_spec(props):
        url = 'https://github.com/RebelBrowser/rebel.git'

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
    return Rebel().handle_args(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
