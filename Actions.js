const fs = require('fs'),
      sqlite3 = require('sqlite3').verbose(),
      db = new sqlite3.Database('test.db');

let matrix = "";

matrix = fs.readFileSync('./AAPL.csv', 'utf8');

matrix = matrix.split('\n').map(row => row.split(','));

db.serialize(() => {
    db.run('CREATE TABLE IF NOT EXISTS actions (date DATE, open NUM, high NUM, low NUM, close NUM, adj_close NUM, volume NUM)');

    let stmt = db.prepare('INSERT INTO actions VALUES (?, ?, ?, ?, ?, ?, ?)');
    matrix.slice(1).map((row, index) => {
        if (row.length > 1){
            stmt.run([...row]);
        }
    });
    stmt.finalize();
});
db.each('SELECT * FROM actions', (err, row) => console.log(row));
db.close();
