var data = {a:1}

var vm = new Vue({
    data:data
})

vm.a == data.a

vm.a = 2
data.a

data.a =3
vm.a