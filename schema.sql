drop table if exists messages;
create table messages (
    id integer primary key autoincrement,
    category integer not null,
    title string not null,
    body string not null
);

drop table if exists categories;
create table categories (
    id integer primary key autoincrement,
    name string not null
);
