$(function(){

	$("head").append("<link>");
		css = $("head").children(":last");
		css.attr({
		rel:  "stylesheet",
		type: "text/css",
		href: "/css/site-navbar.css"
	});



var sitenavbar = "<div id=\"site-navbar\" style=\"z-index: 10000;\">" +
			"<a href=\"/\" title=\"返回首页\">" +
				"<img src=\"/assets/ico/apple-touch-icon-72-precomposed.png\">"+
			"</a>"+
		"</div>";

	$("body").append(sitenavbar);


});


var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F3d8e7fc0de8a2a75f2ca3bfe128e6391' type='text/javascript'%3E%3C/script%3E"));

