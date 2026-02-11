# https://github.com/lmassaron/datasets/blob/master/air_passengers.feather

import pyarrow.feather as feather

read_df = feather.read_feather('air_passengers.feather')
print(read_df)