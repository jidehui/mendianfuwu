==========
门店服务平台
==========

请在Linux的mOrder项目中输入启动命令：
# export ops_config=local && python3 manager.py runserver


##flask-sqlacodegen

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables user --outfile "common/models/User.py"  --flask

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables app_access_log --outfile "common/models/log/AppAccessLog.py"  --flask

    flask-sqlacodegen 'mysql://root:A_a123456@127.0.0.1/shop_db' --tables app_error_log --outfile "common/models/log/AppErrorLog.py"  --flask

    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables member --outfile "common/models/member/Member.py"  --flask
    
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/shop_db' --tables oauth_member_bind --outfile "common/models/member/OauthMemberBind.py"  --flask


