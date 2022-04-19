//获取应用实例
var app = getApp();
Page({
    data: {
        addressList: []
    },
    selectTap: function (e) {
        //从商品详情下单选择地址之后返回
        wx.navigateBack({});
    },
    addessSet: function (e) {
        wx.navigateTo({
            url: "/pages/my/addressSet"
        })
    },
    onShow: function () {
        var that = this;
        that.setData({
            addressList: [
                {
                    id:1,
                    name: "ime",
                    mobile: "13800138000",
                    detail: "广东省广州市天河区381号",
                    isDefault: 1
                },
                {
                    id: 2,
                    name: "ime2",
                    mobile: "12345678910",
                    detail: "广东省广州市天河区382号"
                }
            ]
        });
    }
});
