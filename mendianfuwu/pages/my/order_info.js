var app = getApp();
Page({
    data: {},
    onLoad: function (e) {
        var that = this;
    },
    onShow: function () {
        var that = this;
        that.setData({
            info: {
                order_sn:"123123",
                status: -8,
                status_desc: "待支付",
                deadline:"2022-03-01 12:00",
                pay_price: "85.00",
                yun_price: 0.00,
                total_price: "85.00",
                address: {
                    name: "ime",
                    mobile: "13800138000",
                    address: "广东省广州市天河区华南理工大学381号"
                },
                goods: [
                    {
                        name: "蓝牙耳机",
                        price: "85.00",
                        unit: 1,
                        pic_url: "/images/shop1.jpg"
                    },
                    {
                        name: "小蓝牙耳机",
                        price: "85.00",
                        unit: 1,
                        pic_url: "/images/shop1.jpg"
                    }
                ]
            }
        });
    }
});