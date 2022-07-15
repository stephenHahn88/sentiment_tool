const server = require('./api/server')
const sqlite = require('sqlite3');
const { Client } = require('pg');

const PORT = process.env.PORT || 8080
server.listen(PORT, () => console.log(`listening at ${PORT}`))


