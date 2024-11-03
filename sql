

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    published BOOLEAN NOT NULL DEFAULT TRUE
);

-- Insert 5 random values into the posts table
INSERT INTO posts (title, content, published) VALUES
('Post 1 Title', 'Content for post 1', TRUE),
('Post 2 Title', 'Content for post 2', TRUE),
('Post 3 Title', 'Content for post 3', TRUE),
('Post 4 Title', 'Content for post 4', FALSE),
('Post 5 Title', 'Content for post 5', TRUE);