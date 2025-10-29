# Copyright 2025 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_array_divide]
display('2 / 0:', ee.Array(2).divide(0))  # 0
display('2 / 1:', ee.Array(2).divide(1))  # 2
display('2 / [1]:', ee.Array(2).divide([1]))  # [2]
display('[3,4] / 2:', ee.Array([3, 4]).divide(2))  # [1.5,2]
display('[3,4] / [2,4]:', ee.Array([3, 4]).divide([2,4]))  # [1.5,1]
display('[3,4] / ee.Array([2,4]):', ee.Array([3, 4]).divide(ee.Array([2,4])))  # [1.5,1]
# [END earthengine__apidocs__ee_array_divide]
