from pymongo import ReadPreference
from pymongo.collection import Collection

from backend.model import (
    CollectionName,
    db
)

class Goods(object):
    """
    * `_id` (str) - id
    * `img_url` (str) - 主图片url
    * `label` (str) - 左上角标签
    * `tag` (str) - 优惠标签
    * `title` (str) - 名称
    * `recommend_reason_info` (str) - 推荐原因
    * `price` (int) - 价格
    """

    class Field(object):
        _id = "_id"
        name = "name"
        market_price = "market_price"
        main_pic_url = "main_pic_url"
        spec = "spec"
        aboutOrder = "aboutOrder"
        aboutShipping = "aboutShipping"
        brief = "brief"
        dessertShopRecommendReason = "dessertShopRecommendReason"
        midCategoryName = "midCategoryName"
        tasteLabel = "tasteLabel"
        warmHint = "warmHint"
        postId = "postId"
        details = "details"
        remind = "remind"

    COL_NAME = CollectionName.Goods

    p_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.PRIMARY_PREFERRED
    )

    s_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.SECONDARY_PREFERRED
    )