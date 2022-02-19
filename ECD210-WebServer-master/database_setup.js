const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('test_database2');

/*

This function sets up the table in the database to hold user info

For testing purposing - a user is inserted. In reality this would all be created through the website

*/
function setup(){
    db.run('CREATE TABLE [IF NOT EXISTS] users(
		user_name TEXT NOT NULL, 
		password TEXT NOT NULL,
		first_name TEXT NOT NULL,
		last_name TEXT NOT NULL,
		)
	');

    db.run("INSERT INTO users(user_name, password, first_name, last_name) VALUES('jthakka1', 'abc123', 'jennifer', 'thakkar'	)");
	}
setup();

db.run(`INSERT INTO langs(name) VALUES(?)`, ['C'], function(err) {
    if (err) {
      return console.log(err.message);
    }
    // get the last insert id
    console.log(`A row has been inserted with rowid ${this.lastID}`);
});

