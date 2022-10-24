from mongita import MongitaClientDisk
client = MongitaClientDisk()

from bson.objectid import ObjectId

hello_world_db = client.hello_world_db
mongoose_collection =  hello_world_db.mongoose_collection
mongoose_collection.insert_many([{'name':'Meercate'},{'does_not_eat': 'snakes'},
                                 {'name': 'Yellow mongoose'}, {'eats': 'Termites' }])

mongoose_collection.count_documents({})

list(mongoose_collection.find({'name':'Meercate' }))

#mongoose_collection.update_one({'weight':})

