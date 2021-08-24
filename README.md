# Mowen Project
## API
### 首页 - 轮播图配置
    GET '/api/lecake/index/shuffling-figure'
Params:
* `None`

Returns:
* `data` (Array of Object)
    * `_id` (String) - id
    * `figure_url` (String) - 图片url
    * `title` (Array) - 主题
    * `sub_title` (Array) - 副主题


### 首页 - 热门商品
    GET '/api/lecake/index/hot-goods'
Params:
* `None`

Returns:
* `data` (Array of Object)
    * `_id` (String) - id
    * `goods_url` (String) - 商品详细url
    * `img_url` (String) - 商品图片url
    * `label` (String) - 标签字符
    * `price` (String) - 价格
    * `recommend_reason_info` (String) - 推荐原因
    * `tag` (String) - 标签


### 首页 - 热门评论
    GET '/apilecake/index/hot-comments'
Params:
* `start` (int) 起始 **optional** 默认为0
* `end` (int) 终止 **optional** 默认为12

Returns:
* `data` (Array of Object)
    * `_id` (String) - id
    * `date` (String) - 时间
    * `img_url` (String) - 商品图片url
    * `nick_phone` (String) - 电话号码(脱敏)
    * `text` (String) - 内容