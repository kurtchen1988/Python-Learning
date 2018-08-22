var vm = new Vue({
    el:'#example',
    data:{
        message:'Hello'
    },
    computed:{
        reversedMessage:function () {
            return this.message.split('').reverse().join('')
        }
    }
})
/**
methods:{
    reversedMessage: function () {
        return this.message.split('').reverse().join('')
    }
}**/

/** 不带计算属性的方法
var vm = new Vue({
    el:'#demo',
    data:{
        firstName:'Foo',
        lastName:'Bar',
        fullName:'Foo Bar'
    },
    watch:{
        firstName:function(val){
            this.fullName = val + ' ' + this.lastName
        },
        lastName:function (val) {
            this.fullName = this.firstName + ' ' + val
        }
    }
})**/

// 带计算属性的方法
var vm = new Vue({
    el:'#demo',
    data:{
        firstName:'Foo',
        lastName:'Bar'
    },
    computed:{
        fullName:function(){
            return this.firstName + ' ' + this.lastName
        }
    }
})

// 计算属性的setter
// 计算属性默认只有 getter ，不过在需要时你也可以提供一个 setter

computed:{
    fullName:{
        get:function () {
            return this.firstName + ' ' + this.lastName
        }

        set:function(newValue) {
            var names = newValue.split(' ')
            this.firstName = names[0]
            this.lastName = names[names.length - 1]
        }
    }
}