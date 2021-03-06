# Lint as: python3
# Copyright 2020 DeepMind Technologies Limited. All Rights Reserved.
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
# ==============================================================================
"""Experimental features developed by the Haiku core team.

Features may be removed or modified at any time.
"""

from haiku._src.base import custom_creator
from haiku._src.base import custom_getter
from haiku._src.base import ParamContext
from haiku._src.dot import to_dot
from haiku._src.lift import lift
from haiku._src.module import profiler_name_scopes


__all__ = (
    "custom_creator",
    "custom_getter",
    "ParamContext",
    "lift",
    "to_dot",
    "profiler_name_scopes",
)
