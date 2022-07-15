/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.up = function(knex) {
  return knex.schema
      .createTable("analyses", tbl => {
          tbl.increments();
          tbl.text("piece").notNullable()
          tbl.text("analysis").notNullable()
          tbl.text("comments")
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
