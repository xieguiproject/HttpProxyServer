#coding:utf-8

import re
#测试re
if __name__ == '__main__':
    string = '<ul class="l2">\
		    	<span><li>178.128.91.23</li></span> \
		        <span style="width: 100px;"><li class="port GEGEA">8110</li></span>\
				<span style="width: 100px; "><li><a class="href" href="http://www.data5u.com/free/anoy/匿名/index.html">匿名</a></li></span>\
					<span style="width: 100px;"><li><a class="href" href="http://www.data5u.com/free/type/http/index.html">http</a></li></span>\
		        <span><li><a class="href" href="http://www.data5u.com/free/country/新加坡/index.html">新加坡</a></li></span>\
		        <span style="width: 200px;"><li><a class="href" href="http://www.data5u.com/free/area/XX/index.html">XX</a><a class="href" href="http://www.data5u.com/free/area/XX/index.html">XX</a></li></span>\
		        <span style="width: 100px;"><li><a class="href" href="http://www.data5u.com/free/isp/XX/index.html">XX</a></li></span>\
		        <span style="width: 100px;"><li>2.664 秒</li></span>\
		        <span style="border:none; width: 190px;"><li>6分钟前</li></span>\
		        <div class="clearfix"></div></ul>'
    res = re.findall(r'<li>(.*?)</li>',string,re.S)
    renw = list()
    
    #print(renw)
    res2 = res[2]
    #print(res2)
    res3 = re.findall(r'<a class=.*?>(.*?)</a>',res2)[0]
    
    renw.append(res[0])
    renw.append(res3)
    renw.append(res[6])
    renw.append(res[7])
    print(renw)