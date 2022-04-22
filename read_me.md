==========
门店服务平台
==========

请在Linux的mOrder项目中输入启动命令：
# export ops_config=local && python3 manager.py runserver


## flask-sqlacodegen已实现:

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables user --outfile "common/models/User.py"  --flask

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables app_access_log --outfile "common/models/log/AppAccessLog.py"  --flask

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables app_error_log --outfile "common/models/log/AppErrorLog.py"  --flask

    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables member --outfile "common/models/member/Member.py"  --flask
    
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables oauth_member_bind --outfile "common/models/member/OauthMemberBind.py"  --flask

    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables shop --outfile "common/models/shop/Shop.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables shop_cat --outfile "common/models/shop/ShopCat.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables shop_sale_change_log --outfile "common/models/shop/ShopSaleChangeLog.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables shop_stock_change_log --outfile "common/models/shop/ShopStockChangeLog.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables wx_share_history --outfile "common/models/shop/WxShareHistory.py"  --flask
    
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables member_cart --outfile "common/models/member/MemberCart.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables member_comments --outfile "common/models/member/MemberComments.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables member_address --outfile "common/models/member/MemberAddress.py"  --flask
    
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables pay_order --outfile "common/models/pay/PayOrder.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables images --outfile "common/models/Image.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables pay_order_item --outfile "common/models/pay/PayOrderItem.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables pay_order_callback_data --outfile "common/models/pay/PayOrderCallbackData.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables queue_list --outfile "common/models/queue/QueueList.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables oauth_access_token --outfile "common/models/pay/OauthAccessToken.py"  --flask

### 待实现:
### stat_daily_shop、stat_daily_member、stat_daily_site
