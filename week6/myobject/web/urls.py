from django.conf.urls import url

from web.views import index, cart

urlpatterns = [
    # 前台首页
    url(r'^$', index.index, name="index"),	#商城首页
    url(r'^list$', index.lists, name="list"),# 商品列表
    url(r'^list/(?P<pIndex>[0-9]+)$', index.lists, name="list"),# 商品列表
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="detail"),#商品详情

    # 会员及个人中心等路由配置
    url(r'^login$', index.login, name="login"),
    url(r'^dologin$', index.dologin, name="dologin"),
    url(r'^logout$', index.logout, name="logout"),

    # 购物车信息管理路由配置
    url(r'^cart$', cart.index, name="cart_index"),
    url(r'^cart/add/(?P<gid>[0-9]+)$', cart.add, name="cart_add"),
    url(r'^cart/del/(?P<gid>[0-9]+)$', cart.delete, name="cart_del"),
    url(r'^cart/clear$', cart.clear, name="cart_clear"),
    url(r'^cart/change$', cart.change, name="cart_change"),

]
