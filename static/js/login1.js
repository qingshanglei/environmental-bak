 new Vue({
        el : '#app',
        delimiters: ['[[',']]'],
        data : {
            url:'http://127.0.0.1:8000/login',
            username : '',
            password: '',
            usernamekey: false,
            passwordkey: false,
        },
        methods: {
            // 检查账号
            check_username(){
                let re = /^[0-9]{11}$/;
                let res = /^[0-9a-zA-Z]{5,11}\@(qq|163|192)\.com$/;
                if (re.test(this.username) || res.test(this.username)) {
                    this.usernamekey = false;
                } else {
                    this.usernamekey = true;
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
            // 表单提交
            on_submit(){
                this.check_username();
                this.check_password();
                if (this.username == true || this.passwordkey == true) {
                    // 不满足登录条件：禁用表单
                    window.event.returnValue = false
                }
            },
        }
       
    })