import rides_pb2 as pb

print(pb.POOL)
print(pb.RideType.Name(pb.POOL))
print(pb.RideType.Value('REGULAR'))

request = pb.StartRequest(
    car_id=95,
    driver_id='Jimmy',
    passenger_ids=['p1','p2','p3'],
)
print(request)

# region Marshal
data = request.SerializeToString()
print('type:', type(data))
print('size:', len(data))
# endregion

# region Unmarshal
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)
# endregion
