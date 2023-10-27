from pymongo import MongoClient

client = MongoClient()
client = MongoClient("localhost", 27017)

db = client.mdb_test
coll = db.graphlookup


def recursive_search():
    row = 1
    parents_children = []

    def children(docs):
        nonlocal row
        for doc in docs:
            parents_children.append('{} {} {}'.format(row, doc['name'], doc['name_child']))
            row += 1
            children(coll.find({'name': doc['name_child']}))

    children(coll.find({'name': 'BXHzrbVjlJ'}))
    return parents_children


def graphlookup_search():
    parents_children = []
    row = 1
    for doc in coll.aggregate([
        {
            '$match':
                {
                    'name': "BXHzrbVjlJ",
                },
        },
        {
            '$graphLookup':
                {
                    'from': "graphlookup",
                    'startWith': "$name_child",
                    'connectFromField': "name_child",
                    'connectToField': "name",
                    'as': "children",
                    'depthField': "level",
                    'restrictSearchWithMatch': {
                        'name_finished_good': "TL6100NCB",
                    },
                },
        },
    ]):
        parents_children.append('{} {} {}'.format(row, doc['name'], doc['name_child']))
        row += 1
        for p in doc['children']:
            parents_children.append('{} {} {}'.format(row, p['name'], p['name_child']))
            row += 1
    return parents_children


res1 = recursive_search()
res2 = graphlookup_search()

print('output from recursive find()')
for x in res1:
    print(x)
print()
print()
print('output from graphlookup')
for x in res2:
    print(x)
