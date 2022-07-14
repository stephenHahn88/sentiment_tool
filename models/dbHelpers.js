// const knex = require('knex')
// const config = require('../knexfile')
// const db = knex(config.development)
const db = require("../dbConfig")

module.exports = {
    add,
    find
};

async function add(analysis) {
    const {id} = await db('analyses').insert(analysis)
}

function find() {
    return db("analyses")
}