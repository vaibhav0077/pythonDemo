import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("demo1-aa391-firebase-adminsdk-dkotv-a2d80f2f90.json")
firebase_admin.initialize_app(cred)


db = firestore.client()  # this connects to our Firestore database
collection = db.collection('demo')  # opens 'places' collection
doc = collection.document('rome')  # specifies the 'rome' document

doc = collection.document('barcelona')
res = doc.get().to_dict()
print("res1 : ",res)


docs = collection.get()
print("Docs : ",docs)


res = collection.document('barcelona').set({
    'lat': 41.3851, 'long': 2.1734,
    'weather': 'great',
    'landmarks': [
        'guadí park',
        'gaudí church',
        'gaudí everything'
    ]
})
print("res2 : ",res)

res = collection.document('barcelona').update({
    'weather': 'sun'
})
print("res3 ",type(res))

# collection.document('rome').update({
#     'where_to_go': firestore.ArrayUnion(['colosseum'])
# })


# collection.document('rome').update({
#     'where_to_go': firestore.ArrayRemove(
#         ['vatican_city', 'trastevere']
# )})


# collection.document('rome').delete()


collection.document('barcelona').update({
    'weather': firestore.DELETE_FIELD})


# doc = collection.document('barcelona')
# res = collection.document('barcelona').get().to_dict()
print("res4 : ",collection.document('barcelona'))

# where(fieldPath, opStr, value):
# fieldPath — the field we are targeting, in this case 'long'
# opStr — comparison operation string, '==' checks equality
# value — the value we are comparing to

# a  = collection.where('long', '<', 9.4989).get().to_dict()
# print(a)
# print(collection.document(a).get().to_dict())
collection.where('lat', '>',11).get()
print('cond1 : ',type(collection.where('long', '<', 9.4989).get()))
print('cond2 : ',collection.where('long', '>', -9.4989) \
          .where('long', '<', 33.4299).get())



# for x in collection.where(u'long', u'<', 9.4989):
#   print(x.stream())



  # museums = db.collection_group(u'landmarks')\
  #       .where(u'type', u'==', u'museum')
  #   docs = museums.stream()
  #   for doc in docs:
  #       print(f'{doc.id} => {doc.to_dict()}')


aa = collection.where('long', '<', 9.4989).get()
# bb = aa.stream()
for x in aa:
    print(f'{x.id} => {x.to_dict()}')
