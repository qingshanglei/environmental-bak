new Vue({
    el : "#app",
    delimiters: ['[[', ']]'],
    data : {
        // v-model
        url:'http://127.0.0.1:8000',
        urls: 'http://127.0.0.1:8000/register',
        name: '',
        usertel: '',
        userm: '',
        password: '',
        password2: '',
        userto: false,
        // v-show
        namekey: false,
        usertelkey: false,
        usermkey: false,
        passwordkey: false ,
        password2key: false,
        usertokey: false, // 用户协议
        // [[]] 显示信息
        error_name: '',
        error_tel: ''

    },
    methods: {
       
        check_name(){
            let re = /^\w{3,10}$/;
            if (re.test(this.name)) {
                this.namekey = false;
            } else {
                this.error_name = '请输入3到10个字符'
                this.namekey = true;
            }
            if (this.namekey == false) { // 只有当用户输入的用户名满足条件时才回去判断
                let url = this.url + '/usernames/'+ this.name + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count == 1) {
                            // 用户名已存在
                            this.error_name = '用户名已存在';
                            this.namekey = true;
                        } else {
                            // 用户名不存在
                            this.namekey = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
                }
        },

         // 检查手机号
        check_usertel(){
            let re = /^[0-9]{11}$/;
            if (re.test(this.usertel)) {
                this.usertelkey = false;
            } else {
                this.error_tel = '请输入正确的手机号码'
                this.usertelkey = true;
            }
            if (this.usertelkey == false) { // 只有当用户输入的用户名满足条件时才回去判断
                let url =  this.url +  '/usertels/'+ this.usertel + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count == 1) {
                            // 时间和名已存在
                            this.error_tel = '手机号名已注册';
                            this.usertelkey = true;
                        } else {
                            // 时间和不存在
                            this.usertelkey = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
                }
        },
        // 校验邮箱
        check_userm(){
            let re = /^[0-9a-zA-Z]{5,11}\@(qq|163|192)\.com$/;
            if (re.test(this.userm)) {
                this.usermkey = false;
            } else {
                this.usermkey = true;
            }
        },
        // 检查密码
        check_password(){
            let re = /^[0-9A-Za-z]{8,20}$/;
            if (re.test(this.password)) {
                this.passwordkey = false;
            } else {
                this.passwordkey = true;
            }
        },
        check_password2(){
            if(this.password == this.password2){
                this.password2key = false
            } else{
                this.password2key = true
            }
        },
        // 用户协议
        check_userto(){
         if(!this.userto){
             usertokey = false
         } else{
             usertokey = true
         }
        },

        

        // 表单提交
        on_submit(){
            this.check_name();
            this.check_usertel();
            this.check_userm();
            this.check_password();
            this.check_password2();
            this.check_userto()

            if (this.namekey== true || this.usertelkey== true || this.usermkey== true || this.passwordkey== true || this.password2key== true || this.usertokey== true) {
                // 不满足登录条件：禁用表单
                window.event.returnValue = false
            }
        },
    }
    
})