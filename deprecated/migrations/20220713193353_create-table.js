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
          tbl.text("custom_id")

          tbl.dateTime('created_at').notNullable().defaultTo(knex.raw('CURRENT_TIMESTAMP'))
      })
};

/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.down = function(knex) {
    return knex.schema.dropTableIfExists("analyses")
};
