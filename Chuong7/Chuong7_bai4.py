import json
jsonString = '{"ma":"nv1","age":50,"ten":"Ngô Sở Uý"}'
dataObject = json.loads(jsonString)
print(dataObject)
print("Mã: ",dataObject["ma"])
print("Tuổi: ",dataObject["age"])
print("Tên: ",dataObject["ten"])
