mongod --version

1. C:\Program Files\MongoDB\Server\6.0\bin
2. Use mongosh to do it.

use dbName;
db.dropDatabase();
exit

Example:

use UTA_Enrollment;
db.dropDatabase();
exit

mongoimport --jsonArray --db UTA_Enrollment --collection user --file users.json
mongoimport --jsonArray --db UTA_Enrollment --collection course --file courses.json