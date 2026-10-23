-- 建立相親會員資料表
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    occupation VARCHAR(50),
    bio TEXT
);

-- 新增示範相親會員資料
INSERT INTO profiles (name, gender, age, occupation, bio) VALUES
('陳小美', '女', 25, 'UI/UX 設計師', '喜歡看展覽、喝咖啡，尋找有幽默感的另一半。'),
('林大衛', '男', 28, '軟體工程師', '熱愛戶外運動與 Vibe Coding，希望能找到一起旅行的夥伴。'),
('張雅婷', '女', 27, '鋼琴教師', '平時喜歡彈琴與貓咪，性格溫和好相處。');
