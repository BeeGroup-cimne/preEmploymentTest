const { Pool } = require('pg');

const pool = new Pool({
    user: 'beegroup',
    host: 'p4-db-1',
    password: '1234',
    database: 'mydb',
    port: '5432'
});

const getData = async (request, res) => {
  try {
      const response = await pool.query('SELECT * FROM time_series');
      res.send(response.rows);
  } catch (error) {
      console.error('Error fetching data:', error);
      res.status(500).json({ error: 'Internal Server Error' });
  }
}

module.exports = {getData}