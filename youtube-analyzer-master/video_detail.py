import json
import requests
import MySQLdb


# # url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
# url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id=r6sGWTCMz2k&key=AIzaSyCssZW-n55tZ_3GPwXbvmAn921aW5bbE34"
# json_url = requests.get(url)
# data = json.loads(json_url.text)
# print(json.dumps(data, indent=4))

# try:
#     data = data['items'][0][part]
# except KeyError as e:
#     # print(f'Error! Could not get {part} part of data: \n{data}')
#     print(f'Error! ')
#     data = dict()



# def _get_single_video_data(self, video_id, part):
def _get_single_video_data(video_id):
    """
    Extract further information for a single video
    parts can be: 'snippet', 'statistics', 'contentDetails', 'topicDetails'
    """

    # url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key=AIzaSyCssZW-n55tZ_3GPwXbvmAn921aW5bbE34"
    url = f"https://www.googleapis.com/youtube/v3/videos?fields=items(id,snippet(channelId,title,publishedAt,thumbnails),statistics)&part=snippet,statistics&id={video_id}&key=AIzaSyCssZW-n55tZ_3GPwXbvmAn921aW5bbE34"
    # convert to json
 
    json_url = requests.get(url)
    data = json.loads(json_url.text)
    return data

def _store_video_data(data):
    db = MySQLdb.connect("localhost","root","n21902", "midnight_special")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    id_valid = True
    try:
        data["items"][0]["id"] 
    except KeyError:
        id_valid = False
    if id_valid:
        id = data["items"][0]["id"]
    else:
        id = None
    publishedAt_valid = True
    try:
        data["items"][0]["snippet"]["publishedAt"] 
    except KeyError:
        publishedAt_valid = False
    if publishedAt_valid:
        publishedAt = data["items"][0]["snippet"]["publishedAt"]
    else:
        publishedAt = None
    channelId_valid = True
    try:
        data["items"][0]["snippet"]["channelId"] 
    except KeyError:
        channelId_valid = False
    if channelId_valid:
        channelId = data["items"][0]["snippet"]["channelId"]
    else:
        channelId = None
    title_valid = True
    try:
        data["items"][0]["snippet"]["title"] 
    except KeyError:
        title_valid = False
    if title_valid:
        title = data["items"][0]["snippet"]["title"]
    else:
        title = None
    default_url_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["default"]["url"] 
    except KeyError:
        default_url_valid = False
    if default_url_valid:
        default_url = data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    else:
        default_url = None
    default_width_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["default"]["width"] 
    except KeyError:
        default_width_valid = False
    if default_width_valid:
        default_width = data["items"][0]["snippet"]["thumbnails"]["default"]["width"]
    else:
        default_width = -1
    default_height_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["default"]["height"]
    except KeyError:
        default_height_valid = False
    if default_height_valid:
        default_height = data["items"][0]["snippet"]["thumbnails"]["default"]["height"]
    else:
        default_height = -1
    medium_url_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["medium"]["url"] 
    except KeyError:
        medium_url_valid = False
    if medium_url_valid:
        medium_url = data["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    else:
        medium_url = None
    medium_width_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["medium"]["width"] 
    except KeyError:
        medium_width_valid = False
    if medium_width_valid:
        medium_width = data["items"][0]["snippet"]["thumbnails"]["medium"]["width"]
    else:
        medium_width = -1
    medium_height_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["medium"]["height"]
    except KeyError:
        medium_height_valid = False
    if medium_height_valid:
        medium_height = data["items"][0]["snippet"]["thumbnails"]["medium"]["height"]
    else:
        medium_height = -1
    high_url_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["high"]["url"] 
    except KeyError:
        high_url_valid = False
    if high_url_valid:
        high_url = data["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    else:
        high_url = None
    high_width_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["high"]["width"] 
    except KeyError:
        high_width_valid = False
    if high_width_valid:
        high_width = data["items"][0]["snippet"]["thumbnails"]["high"]["width"]
    else:
        high_width = -1
    high_height_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["high"]["height"]
    except KeyError:
        high_height_valid = False
    if high_height_valid:
        high_height = data["items"][0]["snippet"]["thumbnails"]["high"]["height"]
    else:
        high_height = -1
    standard_url_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["standard"]["url"] 
    except KeyError:
        standard_url_valid = False
    if standard_url_valid:
        standard_url = data["items"][0]["snippet"]["thumbnails"]["standard"]["url"]
    else:
        standard_url = None
    standard_width_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["standard"]["width"] 
    except KeyError:
        standard_width_valid = False
    if standard_width_valid:
        standard_width = data["items"][0]["snippet"]["thumbnails"]["standard"]["width"]
    else:
        standard_width = -1
    standard_height_valid = True
    try:
        data["items"][0]["snippet"]["thumbnails"]["standard"]["height"]
    except KeyError:
        standard_height_valid = False
    if standard_height_valid:
        standard_height = data["items"][0]["snippet"]["thumbnails"]["standard"]["height"]
    else:
        standard_height = -1
    viewCount_valid = True
    try:
        data["items"][0]["statistics"]["viewCount"]
    except KeyError:
        viewCount_valid = False
    if viewCount_valid:
        viewCount = data["items"][0]["statistics"]["viewCount"]
    else:
        viewCount = -1
    likeCount_valid = True
    try:
        data["items"][0]["statistics"]["likeCount"]
    except KeyError:
        likeCount_valid = False
    if likeCount_valid:
        likeCount = data["items"][0]["statistics"]["likeCount"]
    else:
        likeCount = -1
    dislikeCount_valid = True
    try:
        data["items"][0]["statistics"]["dislikeCount"]
    except KeyError:
        dislikeCount_valid = False
    if dislikeCount_valid:
        dislikeCount = data["items"][0]["statistics"]["dislikeCount"]
    else:
        dislikeCount = -1
    favoriteCount_valid = True
    try:
        data["items"][0]["statistics"]["favoriteCount"]
    except KeyError:
        favoriteCount_valid = False
    if favoriteCount_valid:
        favoriteCount = data["items"][0]["statistics"]["favoriteCount"]
    else:
        favoriteCount = -1
    commentCount_valid = True
    try:
        data["items"][0]["statistics"]["commentCount"]
    except KeyError:
        commentCount_valid = False
        print ("commentCount has KeyError")
    if commentCount_valid:
        commentCount = data["items"][0]["statistics"]["commentCount"]
        print ("commentCount = True")
    else:
        commentCount = -1
        print ("commentCount = False")



    # build query for all Youtube video parameters
    sql = "INSERT INTO video (videoId, publishedAt, channelId, title, default_url, default_width, default_height, medium_url, medium_width, medium_height, high_url, high_width, high_height, standard_url, standard_width, standard_height, viewCount, likeCount, dislikeCount, favoriteCount, commentCount ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    # get the variables
    # val = (data["items"][0]["id"], 
    #         data["items"][0]["snippet"]["publishedAt"], 
    #         data["items"][0]["snippet"]["channelId"], 
    #         data["items"][0]["snippet"]["title"], 
    #         data["items"][0]["snippet"]["thumbnails"]["default"]["url"], 
    #         data["items"][0]["snippet"]["thumbnails"]["default"]["width"], 
    #         data["items"][0]["snippet"]["thumbnails"]["default"]["height"] ,
    #         data["items"][0]["snippet"]["thumbnails"]["medium"]["url"], 
    #         data["items"][0]["snippet"]["thumbnails"]["medium"]["width"], 
    #         data["items"][0]["snippet"]["thumbnails"]["medium"]["height"] ,
    #         data["items"][0]["snippet"]["thumbnails"]["high"]["url"], 
    #         data["items"][0]["snippet"]["thumbnails"]["high"]["width"], 
    #         data["items"][0]["snippet"]["thumbnails"]["high"]["height"] ,
    #         data["items"][0]["snippet"]["thumbnails"]["standard"]["url"], 
    #         data["items"][0]["snippet"]["thumbnails"]["standard"]["width"], 
    #         data["items"][0]["snippet"]["thumbnails"]["standard"]["height"],
    #         data["items"][0]["statistics"]["viewCount"],
    #         data["items"][0]["statistics"]["likeCount"],
    #         data["items"][0]["statistics"]["dislikeCount"],
    #         data["items"][0]["statistics"]["favoriteCount"],
    #         data["items"][0]["statistics"]["commentCount"]
    #     )
    val = (id, 
        publishedAt, 
        channelId, 
        title, 
        default_url, 
        default_width, 
        default_height,
        medium_url, 
        medium_width, 
        medium_height,
        high_url, 
        high_width, 
        high_height,
        standard_url, 
        standard_width, 
        standard_height,
        viewCount,
        likeCount,
        dislikeCount,
        favoriteCount,
        commentCount )


    # execute SQL query using execute() method.
    cursor.execute(sql, val)

    # commit the record
    db.commit()

    # disconnect from server
    db.close()


if __name__ == "__main__":
    # data = _get_single_video_data ( "r6sGWTCMz2k")
    # data = _get_single_video_data ( "Ig7yLiOVpy0")
    data = _get_single_video_data ( "lri67")
    # save video details to database 
    print ("data=", data["items"])
    if len (data["items"]) > 0:
        _store_video_data(data)
    else:
        print("data is []")




    # if data["items"][0]["id"]:
    #     _store_video_data(data)
    # else:
    #     print("videoId does not exist")
    
    # print(json.dumps(data, indent=4))
    if len (data["items"]) > 0:
        print("id:", data["items"][0]["id"])
        print("publishedAt:", data["items"][0]["snippet"]["publishedAt"])
        print("channelId:", data["items"][0]["snippet"]["channelId"])
        print("title:", data["items"][0]["snippet"]["title"])

        # get thumbnails
        print("default_url:", data["items"][0]["snippet"]["thumbnails"]["default"]["url"])
        print("default_width:", data["items"][0]["snippet"]["thumbnails"]["default"]["width"])
        print("default_height:", data["items"][0]["snippet"]["thumbnails"]["default"]["height"])


        print("medium_url:", data["items"][0]["snippet"]["thumbnails"]["medium"]["url"])
        print("medium_width:", data["items"][0]["snippet"]["thumbnails"]["medium"]["width"])
        print("medium_height:", data["items"][0]["snippet"]["thumbnails"]["medium"]["height"])

        print("high_url:", data["items"][0]["snippet"]["thumbnails"]["high"]["url"])
        print("high_width:", data["items"][0]["snippet"]["thumbnails"]["high"]["width"])
        print("high_height:", data["items"][0]["snippet"]["thumbnails"]["high"]["height"])

        print("standard_url:", data["items"][0]["snippet"]["thumbnails"]["standard"]["url"])
        print("standard_width:", data["items"][0]["snippet"]["thumbnails"]["standard"]["width"])
        print("standard_height:", data["items"][0]["snippet"]["thumbnails"]["standard"]["height"])

        print("viewCount:", data["items"][0]["statistics"]["viewCount"])
        print("likeCount:", data["items"][0]["statistics"]["likeCount"])
        print("dislikeCount:", data["items"][0]["statistics"]["dislikeCount"])
        print("favoriteCount:", data["items"][0]["statistics"]["favoriteCount"])
        # print("commentCount:", data["items"][0]["statistics"]["commentCount"])


        commentCount = False
        try:
            data["items"][0]["statistics"]["commentCount"]
        except KeyError:
            commentCount = False

            if commentCount:
                print ("commentCount = True")
            else:
                print ("commentCount = False")

