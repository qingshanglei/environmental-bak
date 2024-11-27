<template>
    <div class="footer">
            <div class="yy">
                <h1>关于我们</h1>
                <p>平台简介</p>
                <p>发展历程</p>
                <p>支持机构</p>
                <p>项目案例</p>
                <p>加入我们</p>
                <p>联系我们</p>
            </div>
            <div class="yy">
                <h1>平台功能</h1>
                <p>平台优势</p>
                <p>网络广告</p>
                <p>网站会员</p>
                <p>新媒体</p>
                <p>专业服务</p>
            </div>
            <div class="yy">
                <h1>服务条款</h1>
                <p>会员条款</p>
                <p>法律声明</p>
                <p>下载中心</p>
                <p>帮助中心</p>
            </div>
            <div class="yy">
                <h1>友情链接</h1>
                <p>政府机关</p>
                <p>环保组织</p>
                <p>国际组织</p>
                <p>招标网站</p>
            </div>
</template>

<script>
export default {
    name : 'footer',
}
</script>

<style>
.header {
    height: 80px;
}

.nav {
    height: 60px;
}

.nav-back {
    position: relative;
    height: 60px;
    z-index: 0;
    display: none;
}

.banner {
    height: 1000px;
}

.content {
    height: 300px;
}


.footer {
    background: #e4fad8;
    width: 1200px;
    padding-top: 35px;
    height: 400px;
    padding-left: 10%;
}

.yy {
    padding-right: 100px;
    border-top: 1px solid #868686;
    margin-right: 50px;
    float: left;
}

h1{
    font-size: 20px;
}


p {
    font-size: 10px;
    color: #5a5858;
    font-weight: bold;
}

.header,
.banner,
.content,
.footer {
    margin-left: 150px;
    margin-right: 150px;
    text-align: center;
    border: solid;
    margin-top: 3px;
    font-size: 20px;
}

.nav,
.nav-back {
    text-align: center;
    border: solid;
    margin-top: 3px;
    font-size: 20px;
}
</style>