drop table if exists messages;
create table messages (
    id integer primary key autoincrement,
    title string not null,
    body string not null
);