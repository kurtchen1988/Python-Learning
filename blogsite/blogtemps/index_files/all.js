// Copyright (c) 2009, Baidu Inc. All rights reserved.
// 
// Licensed under the BSD License
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//      http:// tangram.baidu.com/license.html
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * 声明baidu包
 * @author: allstar, erik, meizz, berg
var T,
    baidu = T = baidu || {version: "1.3.8"}; 

//提出guid，防止在与老版本Tangram混用时
//在下一行错误的修改window[undefined]
baidu.phoenix.guid = "$BAIDU$";

//Tangram可能被放在闭包中
//一些页面级别唯一的属性，需要挂载在window[baidu.guid]上
window[baidu.guid] = window[baidu.guid] || {};
 */
 
 
 /**
 * 声明baidu.phoenix包
 * @author: renlei@baidu.com
 */
 
var baidu = baidu || {version: "1.3.8",author:"phoenix"};
baidu.phoenix = baidu.phoenix || {};

/**
 * @namespace baidu.phoenix.array 操作数组的方法。
 */

baidu.phoenix.array = baidu.phoenix.array || {};


/**
 * 遍历数组中所有元素
 * @name baidu.phoenix.array.each
 * @function
 * @grammar baidu.phoenix.array.each(source, iterator[, thisObject])
 * @param {Array} source 需要遍历的数组
 * @param {Function} iterator 对每个数组元素进行调用的函数，该函数有两个参数，第一个为数组元素，第二个为数组索引值，function (item, index)。
 * @param {Object} [thisObject] 函数调用时的this指针，如果没有此参数，默认是当前遍历的数组
 * @remark
 * each方法不支持对Object的遍历,对Object的遍历使用baidu.phoenix.object.each 。
 * @shortcut each
 * @meta standard
 *             
 * @returns {Array} 遍历的数组
 */
 
baidu.phoenix.each = baidu.phoenix.array.forEach = baidu.phoenix.array.each = function (source, iterator, thisObject) {
    var returnValue, item, i, len = source.length;
    
    if ('function' == typeof iterator) {
        for (i = 0; i < len; i++) {
            item = source[i];
            //TODO
            //此处实现和标准不符合，标准中是这样说的：
            //If a thisObject parameter is provided to forEach, it will be used as the this for each invocation of the callback. If it is not provided, or is null, the global object associated with callback is used instead.
            returnValue = iterator.call(thisObject || source, item, i);
    
            if (returnValue === false) {
                break;
            }
        }
    }
    return source;
};

/**
 * 从数组中寻找符合条件的第一个元素
 * @name baidu.phoenix.array.find
 * @function
 * @grammar baidu.phoenix.array.find(source, iterator)
 * @param {Array} source 需要查找的数组
 * @param {Function} iterator 对每个数组元素进行查找的函数，该函数有两个参数，第一个为数组元素，第二个为数组索引值，function (item, index)，函数需要返回true或false
 * @see baidu.phoenix.array.filter,baidu.phoenix.array.indexOf
 *             
 * @returns {Any|null} 符合条件的第一个元素，找不到时返回null
 */
baidu.phoenix.array.find = function (source, iterator) {
    var item, i, len = source.length;
    
    if ('function' == typeof iterator) {
        for (i = 0; i < len; i++) {
            item = source[i];
            if (true === iterator.call(source, item, i)) {
                return item;
            }
        }
    }
    
    return null;
};

/**
 * 查询数组中指定元素的索引位置
 * @name baidu.phoenix.array.indexOf
 * @function
 * @grammar baidu.phoenix.array.indexOf(source, match[, fromIndex])
 * @param {Array} source 需要查询的数组
 * @param {Any|Function} match 查询项
 * @param {number} [fromIndex] 查询的起始位索引位置，如果为负数，则从source.length+fromIndex往后开始查找
 * @see baidu.phoenix.array.find,baidu.phoenix.array.lastIndexOf
 *             
 * @returns {number} 指定元素的索引位置，查询不到时返回-1
 */
baidu.phoenix.array.indexOf = function (source, match, fromIndex) {
    var len = source.length,
        iterator = match;
        
    fromIndex = fromIndex | 0;
    if(fromIndex < 0){//小于0
        fromIndex = Math.max(0, len + fromIndex)
    }
    for ( ; fromIndex < len; fromIndex++) {
        if(fromIndex in source && source[fromIndex] === match) {
            return fromIndex;
        }
    }
    
    return -1;
};

/**
 * 移除数组中的项
 * @name baidu.phoenix.array.remove
 * @function
 * @grammar baidu.phoenix.array.remove(source, match)
 * @param {Array} source 需要移除项的数组
 * @param {Any|Function} match 要移除的项
 * @meta standard
 * @see baidu.phoenix.array.removeAt
 *             
 * @returns {Array} 移除后的数组
 */
baidu.phoenix.array.remove = function (source, match) {
    var len = source.length;
        
    while (len--) {
        if (len in source && source[len] === match) {
            source.splice(len, 1);
        }
    }
    return source;
};

/**
 * @namespace baidu.phoenix.dom 操作dom的方法。
 */
baidu.phoenix.dom = baidu.phoenix.dom || {};


/**
 * 从文档中获取指定的DOM元素
 * @name baidu.phoenix.dom.g
 * @function
 * @grammar baidu.phoenix.dom.g(id)
 * @param {string|HTMLElement} id 元素的id或DOM元素
 * @shortcut g,T.G
 * @meta standard
 * @see baidu.phoenix.dom.q
 *             
 * @returns {HTMLElement|null} 获取的元素，查找不到时返回null,如果参数不合法，直接返回参数
 */
baidu.phoenix.dom.g = function (id) {
    if ('string' == typeof id || id instanceof String) {
        return document.getElementById(id);
    } else if (id && id.nodeName && (id.nodeType == 1 || id.nodeType == 9)) {
        return id;
    }
    return null;
};

// 声明快捷方法
baidu.phoenix.g = baidu.phoenix.G = baidu.phoenix.dom.g;

/**
 * 获取目标元素指定标签的最近的祖先元素
 * @name baidu.phoenix.dom.getAncestorByTag
 * @function
 * @grammar baidu.phoenix.dom.getAncestorByTag(element, tagName)
 * @param {HTMLElement|string} element 目标元素或目标元素的id
 * @param {string} tagName 祖先元素的标签名
 * @see baidu.phoenix.dom.getAncestorBy,baidu.phoenix.dom.getAncestorByClass
 *             
 * @returns {HTMLElement|null} 指定标签的最近的祖先元素，查找不到时返回null
 */
baidu.phoenix.dom.getAncestorByTag = function (element, tagName) {
    element = baidu.phoenix.dom.g(element);
    tagName = tagName.toUpperCase();

    while ((element = element.parentNode) && element.nodeType == 1) {
        if (element.tagName == tagName) {
            return element;
        }
    }

    return null;
};

/**
 * @namespace baidu.phoenix.event 屏蔽浏览器差异性的事件封装。
 * @property target 	事件的触发元素
 * @property pageX 		鼠标事件的鼠标x坐标
 * @property pageY 		鼠标事件的鼠标y坐标
 * @property keyCode 	键盘事件的键值
 */
baidu.phoenix.event = baidu.phoenix.event || {};


/**
 * 获取事件的触发元素
 * @name baidu.phoenix.event.getTarget
 * @function
 * @grammar baidu.phoenix.event.getTarget(event)
 * @param {Event} event 事件对象
 * @meta standard
 * @returns {HTMLElement} 事件的触发元素
 */
 
baidu.phoenix.event.getTarget = function (event) {
    return event.target || event.srcElement;
};

/**
 * 事件监听器的存储表
 * @private
 * @meta standard
 */
baidu.phoenix.event._listeners = baidu.phoenix.event._listeners || [];

/**
 * @namespace baidu.phoenix.lang 对语言层面的封装，包括类型判断、模块扩展、继承基类以及对象自定义事件的支持。
*/
baidu.phoenix.lang = baidu.phoenix.lang || {};


/**
 * 判断目标参数是否string类型或String对象
 * @name baidu.phoenix.lang.isString
 * @function
 * @grammar baidu.phoenix.lang.isString(source)
 * @param {Any} source 目标参数
 * @shortcut isString
 * @meta standard
 * @see baidu.phoenix.lang.isObject,baidu.phoenix.lang.isNumber,baidu.phoenix.lang.isArray,baidu.phoenix.lang.isElement,baidu.phoenix.lang.isBoolean,baidu.phoenix.lang.isDate
 *             
 * @returns {boolean} 类型判断结果
 */
baidu.phoenix.lang.isString = function (source) {
    return '[object String]' == Object.prototype.toString.call(source);
};

// 声明快捷方法
baidu.phoenix.isString = baidu.phoenix.lang.isString;


/**
 * 从文档中获取指定的DOM元素
 * **内部方法**
 * 
 * @param {string|HTMLElement} id 元素的id或DOM元素
 * @meta standard
 * @return {HTMLElement} DOM元素，如果不存在，返回null，如果参数不合法，直接返回参数
 */
baidu.phoenix.dom._g = function (id) {
    if (baidu.phoenix.lang.isString(id)) {
        return document.getElementById(id);
    }
    return id;
};

// 声明快捷方法
baidu.phoenix._g = baidu.phoenix.dom._g;


/**
 * 为目标元素添加事件监听器
 * @name baidu.phoenix.event.on
 * @function
 * @grammar baidu.phoenix.event.on(element, type, listener)
 * @param {HTMLElement|string|window} element 目标元素或目标元素id
 * @param {string} type 事件类型
 * @param {Function} listener 需要添加的监听器
 * @remark
 * 
1. 不支持跨浏览器的鼠标滚轮事件监听器添加<br>
2. 改方法不为监听器灌入事件对象，以防止跨iframe事件挂载的事件对象获取失败
    
 * @shortcut on
 * @meta standard
 * @see baidu.phoenix.event.un
 *             
 * @returns {HTMLElement|window} 目标元素
 */
baidu.phoenix.event.on = function (element, type, listener) {
    type = type.replace(/^on/i, '');
    element = baidu.phoenix.dom._g(element);

    var realListener = function (ev) {
            // 1. 这里不支持EventArgument,  原因是跨frame的事件挂载
            // 2. element是为了修正this
            listener.call(element, ev);
        },
        lis = baidu.phoenix.event._listeners,
        filter = baidu.phoenix.event._eventFilter,
        afterFilter,
        realType = type;
    type = type.toLowerCase();
    // filter过滤
    if(filter && filter[type]){
        afterFilter = filter[type](element, type, realListener);
        realType = afterFilter.type;
        realListener = afterFilter.listener;
    }
    
    // 事件监听器挂载
    if (element.addEventListener) {
        element.addEventListener(realType, realListener, false);
    } else if (element.attachEvent) {
        element.attachEvent('on' + realType, realListener);
    }
  
    // 将监听器存储到数组中
    lis[lis.length] = [element, type, listener, realListener, realType];
    return element;
};

// 声明快捷方法
baidu.phoenix.on = baidu.phoenix.event.on;

/**
 * 增加自定义模块扩展,默认创建在当前作用域
 * @author erik, berg
 * @name baidu.phoenix.lang.module
 * @function
 * @grammar baidu.phoenix.lang.module(name, module[, owner])
 * @param {string} name 需要创建的模块名.
 * @param {Any} module 需要创建的模块对象.
 * @param {Object} [owner] 模块创建的目标环境，默认为window.
 * @remark
 *
            从1.1.1开始，module方法会优先在当前作用域下寻找模块，如果无法找到，则寻找window下的模块

 * @meta standard
 */
baidu.phoenix.lang.module = function(name, module, owner) {
    var packages = name.split('.'),
        len = packages.length - 1,
        packageName,
        i = 0;

    // 如果没有owner，找当前作用域，如果当前作用域没有此变量，在window创建
    if (!owner) {
        try {
            if (!(new RegExp('^[a-zA-Z_\x24][a-zA-Z0-9_\x24]*\x24')).test(packages[0])) {
                throw '';
            }
            owner = eval(packages[0]);
            i = 1;
        }catch (e) {
            owner = window;
        }
    }

    for (; i < len; i++) {
        packageName = packages[i];
        if (!owner[packageName]) {
            owner[packageName] = {};
        }
        owner = owner[packageName];
    }

    if (!owner[packages[len]]) {
        owner[packages[len]] = module;
    }
};

/**
 * @namespace baidu.phoenix.object 操作原生对象的方法。
 */
baidu.phoenix.object = baidu.phoenix.object || {};


/**
 * 将源对象的所有属性拷贝到目标对象中
 * @author erik
 * @name baidu.phoenix.object.extend
 * @function
 * @grammar baidu.phoenix.object.extend(target, source)
 * @param {Object} target 目标对象
 * @param {Object} source 源对象
 * @see baidu.phoenix.array.merge
 * @remark
 * 
1.目标对象中，与源对象key相同的成员将会被覆盖。<br>
2.源对象的prototype成员不会拷贝。
		
 * @shortcut extend
 * @meta standard
 *             
 * @returns {Object} 目标对象
 */
baidu.phoenix.extend =
baidu.phoenix.object.extend = function (target, source) {
    for (var p in source) {
        if (source.hasOwnProperty(p)) {
            target[p] = source[p];
        }
    }
    
    return target;
};

/**
 * @namespace baidu.phoenix.string 操作字符串的方法。
 */
baidu.phoenix.string = baidu.phoenix.string || {};


/**
 * 对目标字符串进行html解码
 * @name baidu.phoenix.string.decodeHTML
 * @function
 * @grammar baidu.phoenix.string.decodeHTML(source)
 * @param {string} source 目标字符串
 * @shortcut decodeHTML
 * @meta standard
 * @see baidu.phoenix.string.encodeHTML
 *             
 * @returns {string} html解码后的字符串
 */
baidu.phoenix.string.decodeHTML = function (source) {
    var str = String(source)
                .replace(/&quot;/g,'"')
                .replace(/&lt;/g,'<')
                .replace(/&gt;/g,'>')
                .replace(/&amp;/g, "&");
    //处理转义的中文和实体字符
    return str.replace(/&#([\d]+);/g, function(_0, _1){
        return String.fromCharCode(parseInt(_1, 10));
    });
};

baidu.phoenix.decodeHTML = baidu.phoenix.string.decodeHTML;

/*
 * 初始化，核心函数
 * @author zhengxin@baidu.com
 * @version 1.0.0
 */

/**
 * @namespace baidu
 */
var baidu = baidu ||{};

/**
 * @namespace baidu.phoenix
 */
baidu.phoenix = baidu.phoenix || {};


(function(){

    var phn = baidu.phoenix;
    
    /**
     * log
     */
    phn.log = function(){
        if( window.console && window.console.log ){
            console.log(arguments);
        }
    };
    

    phn.config = {
        target: document.body,
        onAfterRender: function(){},
        onBindSuccess: function(){return true;},
        onBindFailure: function(){return true;},
        onAfterAuth: function(){return true;},
        tpl: 'passport',
        u: document.location.href,
        html:[],
        jumpUrl: null,
        display: 'page',
        act:'login',
        openInSameWin:0
    };
    
    if( phn._public_config.target && typeof phn._public_config.target == 'string' ){
        phn._public_config.target = baidu.phoenix.g(phn._public_config.target);
    }
    baidu.phoenix.extend(phn.config , phn._public_config);
    
})();


/*
 * ui展现
 * @author zhengxin@baidu.com
 */

baidu.phoenix.lang.module('baidu.phoenix.ui' , {
    /**
     * 弹出窗口
     * @param {string} url 弹出窗口的url地址
     * @param {string} id 弹出窗口的id后缀
     * @param {boolean} is_dialog 弹出窗口or弹出页面，true为弹窗口
     */
    popup: function( url , id , is_dialog , config){
        var features = '';
        if( +is_dialog ){
            var
            screenX    = typeof window.screenX      != 'undefined'
                ? window.screenX
                : window.screenLeft,
            screenY    = typeof window.screenY      != 'undefined'
                ? window.screenY
                : window.screenTop,
            outerWidth = typeof window.outerWidth   != 'undefined'
                ? window.outerWidth
                : document.documentElement.clientWidth,
            outerHeight = typeof window.outerHeight != 'undefined'
                ? window.outerHeight
                : (document.documentElement.clientHeight - 22), // 22= IE toolbar height
            width    = config && +config.width || 400,
            height   = config && +config.height || 300,
            left     = parseInt(screenX + ((outerWidth - width) / 2), 10),
            top      = parseInt(screenY + ((outerHeight - height) / 2.5), 10);
            if( config.display == 'popup' ){
                top = 100;
            }
            features = (
                'width=' + width +
                    ',height=' + height +
                    ',left=' + left +
                    ',top=' + top
            );

            
        }
        return window.open(url , ('bd_phoenix_'+ id) , features );
    },
    /**
     * 渲染icons
     * @name baidu.phoenix.ui.render
     * @type function
     * @param {array} accs 需要渲染的icons
     */
    render: function(accs){
        var icons_config = baidu.phoenix.acc.getConfig();
        
        var ul = document.createElement('ul');
        ul.className = 'bd-acc-list';
        
        var html = '';
        baidu.phoenix.each( accs , function(acc){
            var user_html = baidu.phoenix.config.html[acc];
            
            var current_icon = baidu.phoenix.array.find(icons_config , function(item){
                return item.type == acc;
            });

            html += '<li class="bd-acc-'+ acc +'" data-dialog="'+ +current_icon['is_dialog'] +'" data-acc="'+ baidu.phoenix.acc.getStatusIdWithName(acc) +'" data-height="'+ (current_icon['height']||0) +'" data-width="'+ (current_icon['width']||0) +'">';
            if( !user_html ){
                html += '<img src="'+ current_icon['url'] +'" />';
            }else{
                html += user_html;
            }
            
            html += '</li>';
        } );
        
        ul.innerHTML = html;
        
        baidu.phoenix.config.target.appendChild(ul);
        
        baidu.phoenix.on( ul , 'click' , baidu.phoenix.ui.click );
        
        
        
        baidu.phoenix.config.onAfterRender();
    },
    click: function(e){
        var target = baidu.phoenix.event.getTarget(e);

        if( target.tagName.toLowerCase() != 'li' ){
            target = baidu.phoenix.dom.getAncestorByTag(target , 'li');
        }
        if(target){
            var is_dialog = target.getAttribute('data-dialog'),
            acc = target.getAttribute('data-acc'),
            height = target.getAttribute('data-height'),
            width = target.getAttribute('data-width');
            
            var phn = baidu.phoenix;
            
            var url = phn._SERVER_CONFIG['login'] + 'type=' + acc + '&tpl=' + phn.config.tpl + '&u=' + encodeURIComponent(phn.config.u) 
                + '&display=' + phn.config.display + '&act=' + phn.config.act;
            
            if( phn.config.jumpUrl ){
                var jumpUrl = phn.config.jumpUrl + '#display=popup';
                url = url + '&xd=' + encodeURIComponent(jumpUrl);
                if( phn.config.onBindFailure && typeof phn.config.onBindFailure == "function"){
                    url = url + '&fire_failure=1';
                }
            }
            if(phn.config.subpro){
                url += '&subpro=' + encodeURIComponent(phn.config.subpro);
            }
            var targetWin = phn.config.openInSameWin ? 'phoenix':acc;

            baidu.phoenix.ui._active = baidu.phoenix.ui.popup(url , targetWin , is_dialog , {
                width:width,
                height:height,
                display: phn.config.display
            });
        }
    },
    _active:null,
    close: function(){
        baidu.phoenix.ui._active && baidu.phoenix.ui._active.close();
        baidu.phoenix.ui._active = null;
    }
});
/**
 * 兼容connect xd.html
 */
 



var BD = BD || {};
BD.XD = BD.XD || {};

BD.XD.postMessage = BD.XD.postMessage || function(obj){
    baidu.phoenix.ui.close();
    if( obj.success == 1 ){
        var next = decodeURIComponent(obj.next);
        if( baidu.phoenix.config.onAfterAuth(next) ){
            obj.isFirstBind = !!+obj.isFirstBind;
            obj.osType = obj.os_type;
            if( !baidu.phoenix.config.onBindSuccess(next , obj) ){
                return;
            }
            window.top.document.location.href = next;
        }
    }else{
        baidu.phoenix.config.onBindFailure && baidu.phoenix.config.onBindFailure(obj);
    }
};/*
 * 负责acc icons管理
 * @author zhengxin@baidu.com
 */

(function(){

    baidu.phoenix.lang.module('baidu.phoenix.acc' , {
        need_all: false,
        _ACC_MAP:{
            "1" :"renren",
            "2" :"tsina",
            "3" :"baidu",
            "4" :"tqq",
            "7" :"kaixin001",
            "13":"hiapk",
            "14":"qunar",
            "15":"qzone",
            "16":"fetion",
            "19":"91zs",
            "42": "weixin",
            "53": "tianyi",
            "46": "feifan"
        },
        _ICONS_CONFIG: [
            {
                type: "tsina",
                url : "https://passport.baidu.com/phoenix/static/images/ico_sina.png?t=04021515",
                is_dialog: true,
                width:800,
                height:669
            },
            {
                type: 'renren',
                url: "https://passport.baidu.com/phoenix/static/images/ico_renren.png?t=04021515",
                is_dialog: true,
                width:600,
                height:356
            },
            {
                type: 'baidu',
                url: "https://passport.baidu.com/phoenix/static/images/ico_baidu.png?t=04021515",
                is_dialog: false
            },
            {
                type: 'tqq',
                url: "https://passport.baidu.com/phoenix/static/images/ico_tqq.png?t=04021515",
                is_dialog: true,
                width:610,
                height:410
            },
            {
                type: 'kaixin001',
                url: "https://passport.baidu.com/phoenix/static/images/ico_kaixin001.png?t=04021515",
                is_dialog: true,
                width:560,
                height:376
            },
            {
                type: 'qzone',
                url: "https://passport.baidu.com/phoenix/static/images/ico_qzone.png?t=04021515",
                is_dialog: true,
                width:750,
                height:450
            },
            {
                type: 'fetion',
                url: "https://passport.baidu.com/phoenix/static/images/ico_fetion.png?t=04021515",
                is_dialog: true,
                width:560,
                height:351
            },
            {
                type: '91zs',
                url: "https://passport.baidu.com/phoenix/static/images/ico_91zs.png?t=04021515",
                is_dialog: true,
                width:980,
                height:500
            },
            {
                type: 'hiapk',
                url: "https://passport.baidu.com/phoenix/static/images/ico_hiapk.png?t=04021515",
                is_dialog: true,
                width:980,
                height:640
            },
            {
                type: 'qunar',
                url: "https://passport.baidu.com/phoenix/static/images/ico_qunar.png?t=04021515",
                is_dialog: true,
                width:850,
                height:450
            },
            {
                type: 'weixin',
                url: "https://passport.baidu.com/phoenix/static/images/icon_weixin.png?t=04021515",
                is_dialog: true,
                width:850,
                height:450
            },
            {
                type: 'tianyi',
                url: "https://passport.baidu.com/phoenix/static/images/icon_tiany.png?t=04021515",
                is_dialog: true,
                width:850,
                height:450
            },
            {
            type: "feifan",
            url: "https://passport.baidu.com/phoenix/static/images/icon_wanda.png?t=04021515",
            is_dialog: true,
            width: 850,
            height: 450
        }
        ],
        getConfig: function(){
            return this._ICONS_CONFIG;
        },
        _getAcc: function(){
            var icons = baidu.phoenix._icons,
            icons_status = baidu.phoenix._icons_status;
            
            if( baidu.phoenix.array.indexOf( icons , '*' ) != -1 ){
                this.need_all = true;
                baidu.phoenix.array.remove( icons , '*' );
            }

            var target_icons = [];

            baidu.phoenix.each(icons , function(icon){
                if( +icons_status[icon]  == 1 ){
                    target_icons.push(icon);
                }
            });

            if( this.need_all ){//需要展现其他所有的
                baidu.phoenix.each( this._ICONS_CONFIG , function(icon){
                    icon = icon.type;
                    if( baidu.phoenix.array.indexOf( icons , icon ) == -1 ){ //在指定icon没有包含的情况下出现
                        if( icons_status[icon]  == 1 ){
                            target_icons.push(icon);
                        }
                    }
                } );
            }
            return target_icons;
        },
        _mapStatus: function(){
            var status = baidu.phoenix._icons_status;

            if( +status.err_no ) {
                return false;
            }
            
            status = status.os;
            var new_status = {};
            for( var i in status ){
                var transferType = baidu.phoenix.acc._ACC_MAP[i];
                new_status[transferType] = status[i];
            }
            baidu.phoenix._icons_status = new_status;
            return true;
        },
        getStatusIdWithName: function(acc){
            for( var i in this._ACC_MAP ){
                if( this._ACC_MAP[i] == acc ){
                    return i;
                }
            }
        },
        init: function(){
            if( baidu.phoenix.acc._mapStatus() ){
                var accs = baidu.phoenix.acc._getAcc();
                
                baidu.phoenix.ui.render(accs);
            }
        }
    });
    
    
    
})();
