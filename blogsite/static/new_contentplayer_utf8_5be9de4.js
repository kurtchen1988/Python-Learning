function implement(t,e){for(var n in t)e[n]=t[n]}if("undefined"==typeof ContentPlayer)var ContentPlayer={};var Observable=function(){function t(t){t&&"object"==typeof t&&t.handleMessage&&this.observers.push(t)}function e(t){for(var e=this.observers,n=0;n<e.length;n++)e[n].handleMessage(t)}return{addObserver:t,notify:e}}();ContentPlayer.View=function(t){this.container=t.container,this.data=t.data||null,this.tpl=t.tpl||"",this.curIndex=t.curIndex||0,this.needFadeIn=t.needFadeIn||!1,this.observers=[],this.fadeInTimer=0,this.initOpacity=.1,this.curOpacity=.1,this.opacityDiff=.1},ContentPlayer.View.prototype.init=function(){this.registerEvent(),this.render()},ContentPlayer.View.prototype.registerEvent=function(){var t=this;baidu.event.on(this.container,"mouseover",function(){t.notify({type:"STOP"})}),baidu.event.on(this.container,"mouseout",function(){t.notify({type:"PLAY",param:{step:1}})})},ContentPlayer.View.prototype.render=function(){this.container.innerHTML=baidu.format(this.tpl,this.data[this.curIndex])},ContentPlayer.View.prototype.fadeIn=function(){var t=this;window.clearInterval(this.fadeInTimer),this.curOpacity=this.initOpacity,this.fadeInTimer=window.setInterval(function(){var e;e=t.opacityDiff,Fe.Browser.isIE?t.curOpacity<1?(t.curOpacity+=e,t.container.style.filter="alpha(opacity="+100*t.curOpacity+")"):(t.curOpacity=1,t.container.style.filter="alpha(opacity="+100*t.curOpacity+")",window.clearInterval(this.fadeInTimer)):t.curOpacity<1?(t.curOpacity+=e,t.container.style.opacity=t.curOpacity):(t.curOpacity=1,t.container.style.opacity=t.curOpacity,window.clearInterval(this.fadeInTimer))},50)},ContentPlayer.View.prototype.handleMessage=function(t){var e,n,i,o,r,a;switch(e=this.data,n=this.tpl,i=this.curIndex,o=e.length,t.type){case"NEXT":r=t.param.step,i=(i+r)%o;break;case"PREV":r=t.param.step,i=(o+i-r)%o;break;case"GOTO":a=t.param.index,i=a%o;break;default:return}this.curIndex=i,this.render(),this.needFadeIn&&this.fadeIn()},implement(Observable,ContentPlayer.View.prototype),ContentPlayer.ControlPanel=function(t){this.getBtns=t.getBtns||function(){return[]},this.data=t.data||[],this.curIndex=t.curIndex||0,this.style=t.style||null,this.observers=[],this.imgCache=window[Math.random()]=[],this.prevBtn=t.prevBtn,this.nextBtn=t.nextBtn,this.changeAction=t.changeAction||"mousedown"},ContentPlayer.ControlPanel.prototype.init=function(){this.registerEvent(),this.setStyle(),this.imgPreload()},ContentPlayer.ControlPanel.prototype.next=function(t){var e,n;e=this.data.length,n=this.curIndex,this.curIndex=(e+n+t)%e,this.setStyle(),this.notify({type:"NEXT",param:{step:t}})},ContentPlayer.ControlPanel.prototype.prev=function(t){var e,n;e=this.data.length,n=this.curIndex,this.curIndex=(e+n-t)%e,this.setStyle(),this.notify({type:"PREV",param:{step:t}})},ContentPlayer.ControlPanel.prototype.go=function(){this.setStyle(),this.notify({type:"GOTO",param:{index:this.curIndex}})},ContentPlayer.ControlPanel.prototype.registerEvent=function(){var t,e;e=this,t=this.getBtns();for(var n=0;n<t.length;n++)!function(){var i=t[n],o=n;baidu.event.on(i,e.changeAction,function(){e.curIndex=o,e.setStyle(),e.go()}),baidu.event.on(i,"mouseover",function(){e.notify({type:"STOP"})}),baidu.event.on(i,"mouseout",function(){e.notify({type:"PLAY",param:{step:1}})})}();this.prevBtn&&(baidu.event.on(this.prevBtn,"click",function(){this.blur(),e.prev(1)}),baidu.event.on(this.prevBtn,"mouseover",function(){e.notify({type:"STOP"})}),baidu.event.on(this.prevBtn,"mouseout",function(){e.notify({type:"PLAY",param:{step:1}})})),this.nextBtn&&(baidu.event.on(this.nextBtn,"click",function(){this.blur(),e.next(1)}),baidu.event.on(this.nextBtn,"mouseover",function(){e.notify({type:"STOP"})}),baidu.event.on(this.nextBtn,"mouseout",function(){e.notify({type:"PLAY",param:{step:1}})}))},ContentPlayer.ControlPanel.prototype.setStyle=function(){var t;t=this.getBtns();for(var e=0,n=t.length;n>e;e++)t[e].className=e!=this.curIndex?this.style.off:this.style.on},ContentPlayer.ControlPanel.prototype.handleMessage=function(){},ContentPlayer.ControlPanel.prototype.imgPreload=function(){var t,e;t=this.data;for(var n=0;n<t.length;n++)t[n].imgUrl&&(e=new Image,e.src=t[n].imgUrl,this.imgCache.push(e))},implement(Observable,ContentPlayer.ControlPanel.prototype),ContentPlayer.Model=function(t){this.interval=t.interval||4e3,t.container=t.mainViewContainer,t.tpl=t.mainViewTpl,t.needFadeIn=!1,this.mv=new ContentPlayer.View(t),t.container=t.subViewContainer,t.tpl=t.subViewTpl,t.needFadeIn=!1,this.sv=new ContentPlayer.View(t),this.cp=new ContentPlayer.ControlPanel(t),this.timerId=0,this.observers=[],this.init()},ContentPlayer.Model.prototype.init=function(){this.mv.init(),this.sv.init(),this.cp.init(),this.cp.addObserver(this.mv),this.cp.addObserver(this.sv),this.cp.addObserver(this),this.mv.addObserver(this),this.sv.addObserver(this)},ContentPlayer.Model.prototype.play=function(t){var e=this;this.stop(),this.timerId=window.setInterval(function(){e.cp.next(t)},this.interval)},ContentPlayer.Model.prototype.stop=function(){window.clearInterval(this.timerId)},ContentPlayer.Model.prototype.handleMessage=function(t){switch(t.type){case"STOP":this.stop();break;case"PLAY":this.play(t.param.step)}};