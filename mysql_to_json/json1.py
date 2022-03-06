import json
import collections
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3307,
        database="midnight_special"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
print ("geting cursor")
cur = conn.cursor()

cur.execute("SELECT * FROM `video`") 

# for (title) in cur:
#     print( cur.title)

rows = cur.fetchall()

for row in rows:
    t = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23])
    # print (t[0], t[5], t[6], t[23])

# with open("student_rowarrays.js", "w") as f:
#     f.write(j)

# # Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict() 
    
    d ["id"] = row[0] 
    d ["videoId"] = row[1] 
    d ["publishedAt"] = row[2] 
    d ["channelId"] = row[3] 
    d ["video_url"] = row[4] 
    d ["artist"] = row[5] 
    d ["title"] = row[6] 
    d ["default_url"] = row[7] 
    d ["default_width"] = row[8] 
    d ["default_height"] = row[9] 
    d ["medium_url"] = row[10] 
    d ["medium_width"] = row[11] 
    d ["medium_height"] = row[12] 
    d ["high_url"] = row[13] 
    d ["high_width"] = row[14] 
    d ["high_height"] = row[15] 
    d ["standard_url"] = row[16] 
    d ["standard_width"] = row[17] 
    d ["standard_height"] = row[18] 
    d ["viewCount"] = row[19] 
    d ["likeCount"] = row[20] 
    d ["dislikeCount"] = row[21] 
    d ["favoriteCount"] = row[22] 
    d ["commentCount"] = row[23] 
    objects_list.append(d)

j = json.dumps(objects_list)


with open("video_json.js", "w") as f:
    f.write(j)

conn.close()