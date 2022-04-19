/* pages/shop/info.js */
//获取应用实例
var app = getApp();
var WxParse = require('../../wxParse/wxParse.js');

Page({
  data: {
    autoplay: true,
    interval: 3000,
    duration: 1000,
    swiperCurrent: 0,
    hideShopPopup: true,
    buyNumber: 1,
    buyNumMin: 1,
    buyNumMax: 1,
    canSubmit: false, //  选中时候是否允许加入购物车
    shopCarInfo: {},
    shopType: "addShopCar", //购物类型，加入购物车或立即购买，默认为加入购物车,
    id: 0,
    shopCarNum: 4,
    commentCount: 2
  },
  onLoad: function () {
    var that = this;

    that.setData({
      "info": {
        "id": 1,
        "name": "蓝牙耳机",
        "summary": '<p>多色可选的马甲</p><p><img src="https://imgsc01.wooline.cn/EcommerceStoreImg/content/images/thumbs/0117237_-gm600r-tws_350.jpeg"/></p><p><br/>音质相当好</p>',
        "total_count": 2,
        "comment_count": 2,
        "stock": 2,
        "price": "85.00",
        "main_image": "/images/shop1.jpg",
        "pics": ['/images/shop1.jpg', '/images/shop1.jpg']
      },
      buyNumMax: 2,
      commentList: [{
          "score": "好评",
          "date": "2022-01-11 09:30:00",
          "content": "电量非常持久，一直在他们家购买",
          "user": {
            "avatar_url": "/images/more/logo.png",
            "nick": "angellee 🐰 🐒"
          }
        },
        {
          "score": "好评",
          "date": "2022-01-11 09:30:00",
          "content": "电量超级持久，一直在他们家购买",
          "user": {
            "avatar_url": "/images/more/logo.png",
            "nick": "angellee 🐰 🐒"
          }
        }
      ]
    });

    WxParse.wxParse('article', 'html', that.data.info.summary, that, 5);
  },
  goShopCar: function () {
    wx.reLaunch({
      url: "/pages/cart/index"
    });
  },
  toAddShopCar: function () {
    this.setData({
      shopType: "addShopCar"
    });
    this.bindGuiGeTap();
  },
  tobuy: function () {
    this.setData({
      shopType: "tobuy"
    });
    this.bindGuiGeTap();
  },
  addShopCar: function () {

  },
  buyNow: function () {
    wx.navigateTo({
      url: "/pages/order/index"
    });
  },
  /**
   * 规格选择弹出框
   */
  bindGuiGeTap: function () {
    this.setData({
      hideShopPopup: false
    })
  },
  /**
   * 规格选择弹出框隐藏
   */
  closePopupTap: function () {
    this.setData({
      hideShopPopup: true
    })
  },
  numJianTap: function () {
    if (this.data.buyNumber <= this.data.buyNumMin) {
      return;
    }
    var currentNum = this.data.buyNumber;
    currentNum--;
    this.setData({
      buyNumber: currentNum
    });
  },
  numJiaTap: function () {
    if (this.data.buyNumber >= this.data.buyNumMax) {
      return;
    }
    var currentNum = this.data.buyNumber;
    currentNum++;
    this.setData({
      buyNumber: currentNum
    });
  },
  //事件处理函数
  swiperchange: function (e) {
    this.setData({
      swiperCurrent: e.detail.current
    })
  }
});