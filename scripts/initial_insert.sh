sqlite3 skeleton.db "insert into categories (name) values ('Category One')"
sqlite3 skeleton.db "insert into categories (name) values ('Category Two')"
sqlite3 skeleton.db "insert into messages (category, title, body) values (1, 'First', 'Message goes here.')"
