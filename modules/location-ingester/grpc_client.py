
import faker
import location_pb2
import location_pb2_grpc
import grpc


print("sending payload sample to pod ... ... ...")

channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

preloaded_person_ids = [1, 2, 7, 8, 9]
non_existing_person_ids = [859, 45]

fake = faker.Faker()

def randomFloatingStr():
    return str(fake.pyfloat(1))

# Send the desired payload to existing and non-existing people
payloads_list = [
    location_pb2.LocationMessage(person_id=y, latitude=randomFloatingStr(), longitude=randomFloatingStr()) for x in [preloaded_person_ids, non_existing_person_ids] for y in x
    ]

for location in payloads_list:
    response = stub.Create(location)
    print(f"gRPC Server Response: {response}")