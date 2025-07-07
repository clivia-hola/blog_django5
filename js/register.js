console.log("register.js loaded!");
$(function (){
   function boundemail() {
       $("#email-code").click(function (event) {
           let $this = $(this);
           let email = $("input[name='email']").val();
           if (!email) {
               alert("请输入邮箱");
               return;
           }
           $this.off('click');
           
           $.ajax({
                url: '/authory/emailcode',
                data: { email: '1982525429@qq.com' },
                success: function(res) {
                    console.log('验证码已发送');
                },
                error: function(xhr) {
                    alert(xhr.status === 500 ? '服务器开小差了，请稍后重试' : '网络异常');
                }
            });
           //倒计时
           let countdown = 40;
           let timer = setInterval(function () {
               if (countdown <= 0) {
                   $this.text('获取验证码');
                   //清理定时器
                   clearInterval(timer);
                   //重新绑定事件
                   boundemail();
               } else {
                   countdown--;
                   $this.text(countdown + "秒后重试");
               }

           }, 1000);
       })
   }
   boundemail();
   });



