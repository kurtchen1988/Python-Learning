function initFeedback(){if(bds&&bds.qa&&bds.qa.ShortCut&&bds.qa.ShortCut.initRightBar){var e={needImage:!0,upload_file:!0,appid:215637,productLine:20174,wenjuanTitle:"",wenjuanURL:"",issuePlaceholder:"请输入问题描述",contactPlaceholder:"请输入邮件、手机号码或QQ号码任意一种联系方式",showPosition:"center",contactWayType:"contact_way",needContactWay:!0,needHotQuestion:!1,needQuestionnaire:!1,needFeedbackType:!1,needProductType:!1,needEvaluate:!0,typeArray:[],titleBgColor:"#F5F5F5",buttonColor:"#2C61BD",mainFontColor:"#222222",secondaryFontColor:"#999999",titleColor:"#222222",hotQuestionArray:[]};bds.qa.ShortCut.initRightBar(e);var t={};bds.qa.ShortCut._getProData(t)}}function loadScript(e,t,a){var n=document.createElement("script"),s=a||{};n.type="text/javascript",s.charset&&(n.charset=s.charset),s.id&&(n.id=s.id),n.readyState?n.onreadystatechange=function(){("loaded"===n.readyState||"complete"===n.readyState)&&(n.onreadystatechange=null,t())}:n.onload=function(){t()},n.src=e,document.body.appendChild(n)}function getChosenParams(e){var e=0,t=baiduIdHandle();return{mid:t,cuid:"",ln:18,wf:0,action:0===e?1:0,down:0===e?1:0,display_time:e,withtoppic:1,orientation:1,from:"news_webapp",pd:"webapp",os:"iphone",nids:""}}function getRefreshParams(e){return{mid:mid,ts:0,topic:e,type:"info",token:"info",ln:total,an:perPage,withtopic:0,wf:0,"internet-subscribe":0,ver:4,pd:"webapp",nids:""}}function getLoadMoreParams(e,t,a){return{mid:mid,nids:e,wf:0,ts:t,time:t,topic:a,pd:"webapp"}}function addPublicParams(e){var t=/pad/i.test(navigator.userAgent)?2:1,a=isIOS()?2:1;return e.remote_device_type=t,e.os_type=a,e.screen_size_width=screen.width,e.screen_size_height=screen.height,e}function baiduIdHandle(e){if(e)return e;var t=document.cookie.match(new RegExp("(^| )BAIDUID=([^;]*)(;|$)"));return t?t[2]:"7C35091F8552AFD19AA4A03D0828F99B:FG=1"}function isAndroid(){const e=window.navigator.userAgent;return/(Android);?[\s\/]+([\d.]+)?/.test(e)}function isIOS(){const e=window.navigator.userAgent;return e.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)}var login=require("jian:widget/login/login.js"),Share=require("jian:widget/mod_share/mod_share.js"),focus=require("jian:widget/focus/focus.js"),header=require("jian:widget/header/header.js"),BASE_URL="//news.baidu.com";BASE_URL+="8211"===location.port?":8251/":"/";var cache={},channel,home={init:function(){this.ie=!!window.ActiveXObject,this.ie6=!!window.ActiveXObject&&!window.XMLHttpRequest,serverData.isLogin?login.login.userinit():login.login.logininit(),clickMonitor.init("jian","m=51&pid=107"),this.ie?setTimeout(function(){header.header.init()},1e3):header.header.init(),this.share=new Share,this.sky=$("#sky"),this.body=$("#Body"),this.header=$("#Header"),this.main=$(".main"),this.feeds=this.main.find(".feeds"),this.menulist=window.menulist,this.flag=!0,this.hasmore=!0,this.pn=1,this.lastnid="",this.cd=900,this.initLayout(),this.render(),this.addEvent()},addEvent:function(){this.ie||($(window).scroll($.proxy(this.addHeaderShadow,this)),$(window).scroll($.proxy(this.removeFuture,this))),this.ie6?($("#land").scroll($.proxy(this.showGotopbtn,this)),$("#land").scroll($.proxy(this.showSkyuploading,this)),$("#land").scroll($.proxy(this.renderMore,this))):($(window).scroll($.proxy(this.showGotopbtn,this)),$(window).scroll($.proxy(this.showSkyuploading,this)),$(window).scroll($.proxy(this.renderMore,this))),$(".uploading").closest(".channelpage").length||(this.interval=setInterval($.proxy(this.renderNewdata,this),15e3),this.countdown(),this.sky.on("click",".addNewdata",$.proxy(this.addNewdata,this)),this.main.on("click",".addNewdata",$.proxy(this.addNewdata,this))),this.feeds.on("click",".feedb .agree",$.proxy(this.argeeFeed,this)),this.feeds.on("click",".feedb .unagree",$.proxy(this.unargeeFeed,this)),this.sky.on("click",".gotop",$.proxy(this.gotop,this)),this.sky.on("click",".feedback",$.proxy(this.loadRightBar,this)),this.sky.on("click",".feedbackmw .close",$.proxy(this.hidefbmw,this)),this.sky.on("click",".feedbackmw .sendbtn",$.proxy(this.sendFeedback,this)),this.sky.on("keyup",".feedbackmw .tarea textarea",$.proxy(this.showSendbtn,this)),this.body.on("click",".downloading .load a",$.proxy(this.renderMore,this))},initLayout:function(e,t){var a=window.innerHeight||document.documentElement.clientHeight;if(e)"推荐"===e?(this.topic="推荐",this.type="chosen",this.body.removeClass("channelpage"),this.sky.removeClass("channelpage"),this.sky.find(".float").height(a-55-52),focus.focus.init(),this.render()):(this.topic=e,this.type=t,this.flag=!0,this.hasmore=!0,this.pn=1,this.lastnid="",this.body.addClass("channelpage"),this.sky.addClass("channelpage"),this.header.css("boxShadow","0 0 6px rgba(0,0,0,.3)"),window.scrollTo(0,0),$(".downloading").addClass("nodis"),this.render(),this.sky.find(".float").height(a-55));else if(location.href.indexOf("#list")>0){var n=location.href.split("#list/")[1],s=this;$.each(this.menulist,function(e,t){t.index==n&&(s.topic=t.topic)}),this.type="info",this.header.css("boxShadow","0 0 6px rgba(0,0,0,.3)"),this.sky.find(".float").height(a-55)}else this.topic="推荐",this.type="chosen",this.body.removeClass("channelpage"),this.sky.removeClass("channelpage"),this.sky.find(".float").height(a-55-52),focus.focus.init();channel=this.topic,cache[channel]={}},render:function(){var e=this,t=[],a=[],n=this.share;if(this.main.find(".downloading").removeClass("showloading showNocontent"),"推荐"===this.topic){var s=0;$.ajax({url:BASE_URL+"news?tn=bdapibaiyue&t=newchosenlist",type:"post",data:addPublicParams(getChosenParams(s)),dataType:"json",success:function(a){0===a.errno&&(e.feeds.html(""),a.data.news.length&&(s=a.timestamp,cache["推荐"].ts=s,t=e.template(a.data.news),e.feeds.append(t),n.init(),$(".downloading").removeClass("nodis"),e.flag=!0,e.lastnid=a.data.lastnid,e.hasMore=!0))}})}else $.ajax({url:BASE_URL+"news?tn=bdapibaiyue&t=recommendlist",type:"post",data:addPublicParams(getRefreshParams(this.topic)),dataType:"json",success:function(s){0===s.errno&&(e.feeds.html(""),s.data.news.length&&(cache[channel].ts=s.timestamp,$.each(s.data.news,function(e,t){t.title||a.push(t.nid)}),cache[channel].nids=a,t=e.template(s.data.news),e.feeds.append(t),n.init(),$(".downloading").removeClass("nodis"),e.flag=!0,e.lastnid=s.data.lastnid,e.hasMore=!!cache[channel].nids.length))}})},renderMore:function(e){var t;t=this.ie6?document.getElementById("land").scrollHeight-$("#land").scrollTop()-$(window).height():$(document).height()-$(document).scrollTop()-$(window).height(),this.flag&&(this.pn%4!==0&&500>t?(this.flag=!1,this.main.find(".downloading").addClass("showloading").removeClass("showNocontent"),this.hasmore?this.getDataFromServer():this.main.find(".downloading").addClass("showNocontent").removeClass("showloading")):"A"==e.target.tagName&&this.pn%4===0&&(this.flag=!1,this.main.find(".downloading").addClass("showloading").removeClass("showNocontent"),this.hasmore?this.getDataFromServer():this.main.find(".downloading").addClass("showNocontent").removeClass("showloading")))},getDataFromServer:function(){var e,t=this,a="";if("推荐"===this.topic){var n=cache["推荐"].ts;$.ajax({url:BASE_URL+"news?tn=bdapibaiyue&t=newchosenlist",type:"post",data:addPublicParams(getChosenParams(n)),dataType:"json",success:function(a){0===a.errno&&(a.data.news.length?(cache["推荐"].ts=a.timestamp,e=t.template(a.data.news,!0),t.feeds.append(e),t.removeFuture(),t.main.find(".downloading").removeClass("showloading showNocontent"),t.flag=!0,t.lastnid=a.data.lastnid,t.hasMore=!0):(t.main.find(".downloading").addClass("showNocontent").removeClass("showloading"),t.hasmore=!1))}})}else{for(var s=0;perPage>s;s++)a+=cache[channel].nids.shift()+",";$.ajax({url:BASE_URL+"news?tn=bdapibaiyue&t=recommendinfo",type:"post",data:addPublicParams(getLoadMoreParams(a,cache[channel].ts,channel)),dataType:"json",success:function(a){0===a.errno&&(cache[channel].ts=a.timestamp,a.data.news.length?(e=t.template(a.data.news,!0),t.feeds.append(e),t.removeFuture(),t.main.find(".downloading").removeClass("showloading showNocontent"),t.flag=!0,t.lastnid=a.data.lastnid,t.hasMore=!!cache[channel].nids.length):(t.main.find(".downloading").addClass("showNocontent").removeClass("showloading"),t.hasmore=!1))}})}},template:function(e,t){var a=[];return $.each(e,function(e,n){if(n.imageurls&&n.imageurls.length?(a.push(t?n.title.length>21?'<div class="feed long future" data-nid="'+n.nid+'">':'<div class="feed future" data-nid="'+n.nid+'">':n.title.length>21?'<div class="feed long" data-nid="'+n.nid+'">':'<div class="feed" data-nid="'+n.nid+'">'),a.push('<p class="img">'),"recommend"==n.type?a.push('<i class="itype ityperecommend">荐</i>'):"hot"==n.type&&a.push('<i class="itype itypehot">热</i>'),a.push('<a href="'+n.display_url+'" target="_blank" '),a.push("recommend"==n.type?'mon="name=jiannews"':"hot"==n.type?'mon="name=hotnews"':'mon="name=othernews"'),a.push(">"),a.push('<span class="mark"></span><img src="'+n.imageurls[0].url+'" onload="window.checkimg(this)"></a></p>')):t?a.push("recommend"==n.type||"hot"==n.type?n.title.length>29?'<div class="feed noimglong future" data-nid="'+n.nid+'">':'<div class="feed noimg future" data-nid="'+n.nid+'">':n.title.length>31?'<div class="feed noimglong future" data-nid="'+n.nid+'">':'<div class="feed noimg future" data-nid="'+n.nid+'">'):n.title&&a.push("recommend"==n.type||"hot"==n.type?n.title.length>29?'<div class="feed noimglong" data-nid="'+n.nid+'">':'<div class="feed noimg" data-nid="'+n.nid+'">':n.title.length>31?'<div class="feed noimglong" data-nid="'+n.nid+'">':'<div class="feed noimg" data-nid="'+n.nid+'">'),a.push('<div class="info">'),n.imageurls&&(!n.imageurls.length&&"hot"==n.type||!n.imageurls.length&&"recommend"==n.type?(a.push('<p class="title hastype">'),"recommend"==n.type?a.push('<i class="itype ityperecommend">荐</i>'):"hot"==n.type&&a.push('<i class="itype itypehot">热</i>'),a.push('<a href="'+n.display_url+'" target="_blank" '),a.push("recommend"==n.type?'mon="name=jiannews"':"hot"==n.type?'mon="name=hotnews"':'mon="name=othernews"'),a.push(">"+n.title+"</a></p>")):(a.push('<p class="title">'),a.push('<a href="'+n.display_url+'" target="_blank" '),a.push("recommend"==n.type?'mon="name=jiannews"':"hot"==n.type?'mon="name=hotnews"':'mon="name=othernews"'),a.push(">"+n.title+"</a></p>"))),n.imageurls){var s=n.abs;(s.indexOf("span")>=0||s.indexOf("bjh-")>=0)&&(s=""),a.push(n.imageurls.length?n.title.length>21?s.length>24?'<p class="summary">'+s.substr(0,24)+"...</p>":'<p class="summary">'+s+"</p>":s.length>50?'<p class="summary">'+s.substr(0,50)+"...</p>":'<p class="summary">'+s+"</p>":"recommend"==n.type||"hot"==n.type?n.title.length>29?s.length>40?'<p class="summary">'+s.substr(0,40)+"...</p>":'<p class="summary">'+s+"</p>":s.length>86?'<p class="summary">'+s.substr(0,86)+"...</p>":'<p class="summary">'+s+"</p>":n.title.length>31?s.length>40?'<p class="summary">'+s.substr(0,40)+"...</p>":'<p class="summary">'+s+"</p>":s.length>86?'<p class="summary">'+s.substr(0,86)+"...</p>":'<p class="summary">'+s+"</p>")}a.push("</div></div>")}),a.join("")},addHeaderShadow:function(){var e=document.body.scrollTop||document.documentElement.scrollTop;"推荐"==this.topic?e>55?this.header.css("boxShadow","0 0 6px rgba(0,0,0,.3)"):this.header.css("boxShadow","none"):this.header.css("boxShadow","0 0 6px rgba(0,0,0,.3)")},argeeFeed:function(e){var t=$(e.currentTarget),a={nid:t.closest(".feed").data("nid"),type:"up",topic:this.topic},n=this;t.hasClass("dis")||t.hasClass("nooper")||$.ajax({url:"ajax/newssupport",type:"GET",data:a,dataType:"json",success:function(e){0==e.errno&&(n.flaping(t),t.find("b").text(parseInt(t.find("b").text())+1),t.addClass("dis"),t.closest(".feedb").find(".unagree").addClass("nooper"))}})},unargeeFeed:function(e){var t=$(e.currentTarget),a={nid:t.closest(".feed").data("nid"),type:"down",topic:this.topic},n=this;t.hasClass("dis")||t.hasClass("nooper")||$.ajax({url:"ajax/newssupport",type:"GET",data:a,dataType:"json",success:function(e){0==e.errno&&(n.flaping(t),t.find("b").text(parseInt(t.find("b").text())+1),t.addClass("dis"),t.closest(".feedb").find(".agree").addClass("nooper"))}})},flaping:function(e){var t=e[0].getBoundingClientRect().left,a=e[0].getBoundingClientRect().top+$(document).scrollTop()-60,n=$('<p class="flap"><em>+1</em></p>');n.css({left:t,top:a,width:e.width()}),this.main.append(n),this.ie?setTimeout(function(){n.remove()},800):(setTimeout(function(){n.find("em").css("top","-16px"),n.addClass("fadein")},200),setTimeout(function(){n.addClass("fadeout")},800))},renderNewdata:function(){$("body").find(".uploading").addClass("uploading_showload").removeClass("uploading_showloading");var e=this;e.showSkyuploading(),e.sky.find(".uploading .load").addClass("hasshadow"),e.interval&&clearInterval(e.interval)},addNewdata:function(e){var t,a=this,n=[],s=$("body").find(".uploading");$(e.currentTarget).data("reload")?location.reload():(s.addClass("uploading_showloading").removeClass("uploading_showload"),$.each(this.feeds.find(".feed"),function(e,t){n.push($(t).data("nid"))}),$.ajax({url:BASE_URL+"news?tn=bdapibaiyue&t=newchosenlist",type:"post",data:addPublicParams(getChosenParams(0)),dataType:"json",success:function(e){if(0===e.errno&&e.data.news.length){t=a.template(e.data.news),a.feeds.prepend(t),$.each(s,function(e,t){$(t).removeClass("uploading_showload uploading_showloading").addClass("novis")}),a.ie6?$("#land").animate({scrollTop:"404px"},"fast"):setTimeout(function(){$("html,body").stop(!0,!0).animate({scrollTop:"404px"},"fast")},300),a.interval=setInterval($.proxy(a.renderNewdata,a),15e3),a.cd=900}}}))},countdown:function(){var e=this;this.myinterval=setInterval(function(){e.cd>0?e.cd--:($(".addNewdata").attr("data-reload",!0),clearInterval(e.myinterval))},1e3)},showSkyuploading:function(){var e;e=this.ie6?document.getElementById("land").scrollTop:document.body.scrollTop||document.documentElement.scrollTop,e>404?(this.sky.find(".uploading").removeClass("novis"),this.main.find(".uploading").addClass("novis")):(this.sky.find(".uploading").addClass("novis"),this.main.find(".uploading").removeClass("novis"))},removeFuture:function(){$.each(this.feeds.find(".future"),function(e,t){var a=t.getBoundingClientRect().top-window.innerHeight;60>a&&$(t).removeClass("future")})},showGotopbtn:function(){var e=document.body.scrollTop||document.documentElement.scrollTop,t=window.innerHeight||document.documentElement.clientHeight;this.ie6&&(e=$("#land")[0].scrollTop),e>t?this.sky.find(".gotop").removeClass("nodis"):this.sky.find(".gotop").addClass("nodis")},gotop:function(e){$(e.currentTarget).hasClass("nodis")||(this.ie6?$("#land").animate({scrollTop:"0"},"fast"):window.scrollTo(0,0))},loadRightBar:function(){return window.bds&&window.bds.qa&&window.bds.qa.ShortCut?init_feedback():loadScript("https://ufosdk.baidu.com/Public/feedback/js/dist/feedback_plugin_2.0.js",function(){init_feedback()},{charset:"utf-8",id:"feedback_script"}),!1},showfbmw:function(){var e=navigator.userAgent;return e.indexOf("MSIE 6.0")>0||e.indexOf("MSIE 7.0")>0?void alert("暂时不支持IE6、IE7的反馈，请升级浏览器后再反馈"):void(window.bds&&window.bds.qa&&window.bds.qa.ShortCut?initFeedback():loadScript("http://f3.baidu.com/feedback/js/feedback/feedback0.0.2.js",function(){initFeedback()},{charset:"utf-8",id:"feedback_script"}))},hidefbmw:function(e){var t=$(e.currentTarget).closest(".mw");t.find("textarea").val(""),t.find("input").val(""),t.addClass("nodis"),this.sky.find(".mark").addClass("nodis")},showSendbtn:function(e){var t=$(e.currentTarget);$.trim(t.val()).length?t.closest(".mw").find(".sendbtn").removeClass("btndis"):t.closest(".mw").find(".sendbtn").addClass("btndis")},sendFeedback:function(e){var t,a=this;$(e.currentTarget).hasClass("btndis")||(t={msg:$.trim(this.sky.find(".feedbackmw .tarea textarea").val()),contact:$.trim(this.sky.find(".feedbackmw .info input").val())},$.ajax({url:"/ajax/feedback",data:t,type:"POST",dataType:"json",success:function(e){if(0==e.errno){var t,n=a.sky.find(".feedbackmw"),t=a.sky.find(".successmw"),s=window.innerHeight||document.documentElement.clientHeight,i=window.innerWidth||document.documentElement.clientWidth,o=[],d=a;t.removeClass("nodis"),n.find("textarea").val(""),n.find("input").val(""),n.find(".sendbtn").addClass("btndis"),n.addClass("nodis"),a.sky.append(o.join("")),t.css({top:(s-t.height())/2+"px",left:(i-t.width())/2+"px"}),setTimeout(function(){d.sky.find(".mark").addClass("nodis"),t.addClass("nodis")},1e3)}}}))}};home.init();var mid="03c7a16f2e8028127e42c5f7ca9e210b",total=200,perPage=10;