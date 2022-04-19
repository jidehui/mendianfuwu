/* pages/order/index.js */
Page({

  /**
   * 页面的初始数据
   */
  data: {
    goods_list: [{
        id: 22,
        name: "蓝牙耳机",
        price: "85.00",
        pic_url: "/images/shop1.jpg",
        number: 1,
      },
      {
        id: 22,
        name: "手机支架",
        price: "5.00",
        pic_url: "/images/shop2.jpg",
        number: 1,
      }
    ],
    default_address: {
      name: "ime",
      mobile: "13800138000",
      detail: "广州市天河区XX",
    },
    yun_price: "1.00",
    pay_price: "85.00",
    total_price: "86.00",
    params: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    var that = this;
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    var that = this;
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  createOrder: function (e) {
    wx.showLoading();
    var that = this;
    wx.navigateTo({
      url: "/pages/my/order_list"
    });
  },
  addressSet: function () {
    wx.navigateTo({
      url: "/pages/my/addressSet"
    });
  },
  selectAddress: function () {
    wx.navigateTo({
      url: "/pages/my/addressList"
    });
  }

})