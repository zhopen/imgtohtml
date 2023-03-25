# 百度方案：
采用百度文档OCR技术+chatgpt
## 图像识别
通用文字识别 高精度文档识别 https://ai.baidu.com/tech/ocr/general
可以识别对象（文字内容和对象位置）
## chatgpt
prompt
```
根据下面对象内容和位置生成html文档，对象为北京也绿色：
1 使用场景
宽度： 173 高度： 47
左间距： 792 上间距： 95
2 UGC产生内容
宽度： 154 高度： 27
左间距： 954 上间距： 214
3 智能客服
宽度： 93 高度： 27
左间距： 141 上间距： 310
4 论坛评论
宽度： 81 高度： 22
左间距： 559 上间距： 332
5 论坛图片
宽度： 81 高度： 23
左间距： 846 上间距： 332
6 视频点播
宽度： 80 高度： 23
左间距： 1131 上间距： 332
```
response
```
<!DOCTYPE html>
<html>
<head>
	<title>对象文档</title>
	<style>
		.obj {
			position: absolute;
			background-color: green;
			color: white;
			text-align: center;
			font-size: 12px;
			line-height: 27px;
			border-radius: 5px;
		}
	</style>
</head>
<body>
	<div class="obj" style="width: 173px; height: 47px; left: 792px; top: 95px;">北京</div>
	<div class="obj" style="width: 154px; height: 27px; left: 954px; top: 214px;">UGC产生内容</div>
	<div class="obj" style="width: 93px; height: 27px; left: 141px; top: 310px;">智能客服</div>
	<div class="obj" style="width: 81px; height: 22px; left: 559px; top: 332px;">论坛评论</div>
	<div class="obj" style="width: 81px; height: 23px; left: 846px; top: 332px;">论坛图片</div>
	<div class="obj" style="width: 80px; height: 23px; left: 1131px; top: 332px;">视频点播</div>
	<div class="obj" style="width: 81px; height: 22px; left: 1418px; top: 332px;">视频直播</div>
	<div class="obj" style="width: 93px; height: 27px; left: 141px; top: 406px;">智能推荐</div>
	<div class="obj" style="width: 61px; height: 27px; left: 859px; top: 466px;">OCR</div>
	<div class="obj" style="width: 102px; height: 27px; left: 1266px; top: 463px;">图片截图</div>
</body>
</html>

```