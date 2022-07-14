// Update with your config settings.

/**
 * @type { Object.<string, import("knex").Knex.Config> }
 */
module.exports = {

  development: {
    client: 'sqlite3',
    ssl: {
      rejectUnauthorized: false
    },
    connection: {
      filename: './data/test.db3'
    },
    useNullAsDefault: true,
  },

  production: {
    client: 'pg',
    connection: process.env.DATABASE_URL,
    dialect: 'postgres',
    native: true,
    ssl: {
      rejectUnauthorized: false
    },
    dialectOptions: {
      ssl: true
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      tableName: 'knex_migrations',
      directory: './migrations'
    }
  }

};
