#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017-2018 Matt Martz
# Copyright 2023 Dmitry Titov
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import shutil
import ansible_collections

def remove_path(path: str) -> None:
    """Remove a directory or file."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.unlink(path)

def clean_collection_namespace(root: str) -> None:
    """Clean up unnecessary files and directories in ansible collections."""
    for namespace in os.listdir(root):
        namespace_path = os.path.join(root, namespace)
        if not os.path.isdir(namespace_path):
            continue
        for collection in os.listdir(namespace_path):
            collection_path = os.path.join(namespace_path, collection)
            if not os.path.isdir(collection_path):
                continue
            for path in os.listdir(collection_path):
                full_path = os.path.join(collection_path, path)
                if os.path.basename(full_path) != 'plugins':
                    remove_path(full_path)
                else:
                    modules_path = os.path.join(full_path, 'modules')
                    if os.path.isdir(modules_path):
                        remove_path(modules_path)

if __name__ == "__main__":
    root = ansible_collections.__path__[0]
    clean_collection_namespace(root)