/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.up = function(knex) {
  return knex.schema
      .createTable("analyses", tbl => {
          tbl.increments();
          tbl.text("piece")
          tbl.json("analysis")
          tbl.timestamp(true, true)
      })
};

/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.down = function(knex) {
    return knex.schema.dropTableIfExists("analyses")
};
