from datetime import datetime

import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='Tim',
    passenger_ids=['p1', 'p2','p3'],
    type=pb.POOL,
    location=pb.Location(
        lat=32.5270941,
        lng=34.9404309,
    ),
)

time = datetime(2023, 3, 25, 19, 15, 00)
request.time.FromDatetime(time)
print(request)

# region json
from google.protobuf.json_format import MessageToJson
data = MessageToJson(request)
print(data)
# endregion

# region size
print('encode size')
print('- json : ', len(data))
print('- protobuf : ', len(request.SerializeToString()))
# endregion