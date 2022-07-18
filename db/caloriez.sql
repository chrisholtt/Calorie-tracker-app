DROP TABLE IF EXISTS reminders;
DROP TABLE IF EXISTS foods;
DROP TABLE IF EXISTS days;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE days (
    id SERIAL PRIMARY KEY,
    day VARCHAR(255),
    target_calories INT,
    calories_eaten INT,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE foods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  calories INT,
  food_type VARCHAR(255),
  eaten VARCHAR(255),
  day_id INT REFERENCES days(id) ON DELETE CASCADE,
  user_id INT REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE reminders (
  id SERIAL PRIMARY KEY,
  reminder VARCHAR(255),
  day_id INT REFERENCES days(id) ON DELETE CASCADE,
  user_id INT REFERENCES users(id) ON DELETE CASCADE
)
