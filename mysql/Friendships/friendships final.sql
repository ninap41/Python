select * from users
LEFT JOIN friendships ON friendships.users_id =users.id
LEFT JOIN users as user2 ON friendships.friends_id =