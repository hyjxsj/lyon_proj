#-*- coding:utf-8 -*-
_Auth_ = "yangyang.huang"

import re
html = '''
<a class="logo" data-act="icon-click" href="//maoyan.com"></a>
<a class="js-geo-city" data-ci="55">南京</a>
<a data-act="home-click" href="/">首页</a>
<a data-act="movies-click" href="/films">电影</a>
<a data-act="cinemas-click" href="/cinemas">影院</a>
<a href="http://www.gewara.com">演出</a>
<a class="active" data-act="board-click" href="/board">榜单</a>
<a data-act="hotNews-click" href="/news">热点</a>
<a href="/edimall">商城</a>
<a href="javascript:void 0">登录</a>
<a href="/app" target="_blank">
<span class="iphone-icon"></span>
<span class="apptext">APP下载</span>
<span class="caret"></span>
<div class="download-icon">
<p class="down-title">扫码下载APP</p>
<p class="down-content">选座更优惠</p>
</div>
</a>
<a data-act="subnav-click" data-val="{subnavClick:7}" href="/board/7">热映口碑榜</a>
<a data-act="subnav-click" data-val="{subnavClick:6}" href="/board/6">最受期待榜</a>
<a data-act="subnav-click" data-val="{subnavClick:1}" href="/board/1">国内票房榜</a>
<a data-act="subnav-click" data-val="{subnavClick:2}" href="/board/2">北美票房榜</a>
<a class="active" data-act="subnav-click" data-state-val="{subnavId:4}" data-val="{subnavClick:4}" href="javascript:void(0);">TOP100榜</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:1203}" href="/films/1203" title="霸王别姬">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="霸王别姬" class="board-img" data-src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:1203}" href="/films/1203" title="霸王别姬">霸王别姬</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:1297}" href="/films/1297" title="肖申克的救赎">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="肖申克的救赎" class="board-img" data-src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:1297}" href="/films/1297" title="肖申克的救赎">肖申克的救赎</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:4055}" href="/films/4055" title="这个杀手不太冷">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="这个杀手不太冷" class="board-img" data-src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:4055}" href="/films/4055" title="这个杀手不太冷">这个杀手不太冷</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:2641}" href="/films/2641" title="罗马假日">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="罗马假日" class="board-img" data-src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:2641}" href="/films/2641" title="罗马假日">罗马假日</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:267}" href="/films/267" title="泰坦尼克号">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="泰坦尼克号" class="board-img" data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:267}" href="/films/267" title="泰坦尼克号">泰坦尼克号</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:7431}" href="/films/7431" title="乱世佳人">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="乱世佳人" class="board-img" data-src="https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:7431}" href="/films/7431" title="乱世佳人">乱世佳人</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:837}" href="/films/837" title="唐伯虎点秋香">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="唐伯虎点秋香" class="board-img" data-src="https://p0.meituan.net/movie/851fa4bfb2c4095986bb8527d4787335191063.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:837}" href="/films/837" title="唐伯虎点秋香">唐伯虎点秋香</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:2760}" href="/films/2760" title="魂断蓝桥">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="魂断蓝桥" class="board-img" data-src="https://p0.meituan.net/movie/58782fa5439c25d764713f711ebecd1e201941.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:2760}" href="/films/2760" title="魂断蓝桥">魂断蓝桥</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:3667}" href="/films/3667" title="辛德勒的名单">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="辛德勒的名单" class="board-img" data-src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:3667}" href="/films/3667" title="辛德勒的名单">辛德勒的名单</a>
<a class="image-link" data-act="boarditem-click" data-val="{movieId:9025}" href="/films/9025" title="喜剧之王">
<img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
<img alt="喜剧之王" class="board-img" data-src="https://p0.meituan.net/movie/1f0d671f6a37f9d7b015e4682b8b113e174332.jpg@160w_220h_1e_1c"/>
</a>
<a data-act="boarditem-click" data-val="{movieId:9025}" href="/films/9025" title="喜剧之王">喜剧之王</a>
<a class="page_1" href="javascript:void(0);" style="cursor: default">1</a>
<a class="page_2" href="?offset=10">2</a>
<a class="page_3" href="?offset=20">3</a>
<a class="page_4" href="?offset=30">4</a>
<a class="page_5" href="?offset=40">5</a>
<a class="page_10" href="?offset=90">10</a>
<a class="page_2" href="?offset=10">下一页</a>
<a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
<a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
<a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
<a data-query="utm_source=wwwmaoyan" href="http://www.meituan.com" target="_blank">美团网</a>
<a data-query="utm_source=wwwmaoyan" href="http://www.gewara.com">格瓦拉</a>
<a data-query="utm_source=wwwmaoyan" href="http://i.meituan.com/client" target="_blank">美团下载</a>
<a data-query="utm_source=maoyan_pc" href="https://www.huanxi.com" target="_blank">欢喜首映</a>
<a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
<a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
<a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
<a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2019）3837-369号 </a>
<a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
<a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
<a href="/rules/privacy" target="_blank">隐私政策 </a>
<a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备
      11010102003232号</a>
<a href="http://www.beian.miit.gov.cn/" target="_blank">京ICP备16022489号</a>
<a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E" target="_blank">
<img src="http://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png"/>
</a>
<a href="/about/licence/5" target="_blank">
<img src="http://p1.meituan.net/moviemachine/805f605d5cf1b1a02a4e3a5e29df003b8376.png"/>
</a>
'''

pattern = re.compile('<a.*?title="(.*?)">.*?</a>',re.S)
results = re.findall(pattern,html)

for index,result in enumerate(results):
    print(index,result)