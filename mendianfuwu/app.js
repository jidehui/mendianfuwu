/* pages/app.js */
//app.js
App({
  onLaunch: function () {

  },
  globalData: {
    userInfo: null,
    version: "1.0",
    shopName: "智慧门店服务平台",
    domain: "http://192.168.220.137:8899/api"
    //domain: "http://192.168.220.137:8899/api"
  },
  tip: function (params) {
    var that = this;
    var title = params.hasOwnProperty('title') ? params['title'] : '手机门店提示您';
    var content = params.hasOwnProperty('content') ? params['content'] : '';
    wx.showModal({
      title: title,
      content: content,
      success: function (res) {
        if (res.confirm) { //点击确定
          if (params.hasOwnProperty('cb_confirm') && typeof (params.cb_confirm) == "function") {
            params.cb_confirm();
          }
        } else { //点击否
          if (params.hasOwnProperty('cb_cancel') && typeof (params.cb_cancel) == "function") {
            params.cb_cancel();
          }
        }
      }
    })
  },
  alert: function (params) {
    var title = params.hasOwnProperty('title') ? params['title'] : '手机门店提示您';
    var content = params.hasOwnProperty('content') ? params['content'] : '';
    wx.showModal({
      title: title,
      content: content,
      showCancel: false,
      success: function (res) {
        if (res.confirm) { //用户点击确定
          if (params.hasOwnProperty('cb_confirm') && typeof (params.cb_confirm) == "function") {
            params.cb_confirm();
          }
        } else {
          if (params.hasOwnProperty('cb_cancel') && typeof (params.cb_cancel) == "function") {
            params.cb_cancel();
          }
        }
      }
    })
  },
  console: function (msg) {
    console.log(msg);
  },
  getRequestHeader: function () {
    return {
      'content-type': 'application/x-www-form-urlencoded',
      'Authorization': this.getCache("token")
    }
  },
  buildUrl: function (path, params) {
    var url = this.globalData.domain + path;
    var _paramUrl = "";
    if (params) {
      _paramUrl = Object.keys(params).map(function (k) {
        return [encodeURIComponent(k), encodeURIComponent(params[k])].join("=");
      }).join("&");
      _paramUrl = "?" + _paramUrl;
    }
    return url + _paramUrl;
  },
  getCache: function (key) {
    var value = undefined;
    try {
      value = wx.getStorageSync(key);
    } catch (e) {}
    return value;
  },
  setCache: function (key, value) {
    wx.setStorage({
      key: key,
      data: value
    });
  }
});