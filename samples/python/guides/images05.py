# Copyright 2020 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

"""Google Earth Engine Developer's Guide examples for 'Images - Mathematical operations'."""

# [START earthengine__images05__ndvi]
# Load a VIIRS 8-day surface reflectance composite for May 2024.
viirs202405 = (
    ee.ImageCollection('NASA/VIIRS/002/VNP09H1')
    .filter(ee.Filter.date('2024-05-01', '2024-05-16'))
    .first()
)

# Compute NDVI.
ndvi202405 = (
    viirs202405.select('SurfReflect_I2')
    .subtract(viirs202405.select('SurfReflect_I1'))
    .divide(
        viirs202405.select('SurfReflect_I2').add(
            viirs202405.select('SurfReflect_I1')
        )
    )
)
# [END earthengine__images05__ndvi]

# [START earthengine__images05__per_band]
# Load a VIIRS 8-day surface reflectance composite for September 2024.
viirs202409 = (
    ee.ImageCollection('NASA/VIIRS/002/VNP09H1')
    .filter(ee.Filter.date('2024-09-01', '2024-09-16'))
    .first()
)

# Compute multi-band difference between the September composite and the
# previously loaded May composite.
diff = viirs202409.subtract(ndvi202405)

m = geemap.Map()
m.add_layer(
    diff,
    {
        'bands': ['SurfReflect_I1', 'SurfReflect_I2', 'SurfReflect_I3'],
        'min': -1,
        'max': 1,
    },
    'difference',
)

# Compute the squared difference in each band.
squared_difference = diff.pow(2)

m.add_layer(
    squared_difference,
    {
        'bands': ['SurfReflect_I1', 'SurfReflect_I2', 'SurfReflect_I3'],
        'min': 0,
        'max': 0.7,
    },
    'squared diff.',
)
display(m)
# [END earthengine__images05__per_band]
