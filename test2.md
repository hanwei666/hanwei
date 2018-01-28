#### js正则表达式

- test

```
匹配到返回true
rep = /\d+/
/\d+/
rep.test("asdsdf")
false

rep.test("asd12")
true

^$ 精确匹配
rep = /^\d+$/;
/^\d+$/
rep.test("112sdf")
false
rep.test("11")
true


```



- exec

```
分组匹配和匹配所有(\W*) g
text = "JavaScript is more fun than \nJava or JavaBeans!"
var rep = /^Java(\W*)/g;
rep.exec(text)

匹配所有行m
text = "JavaScript is more fun than \nJava or JavaBeans!"
var rep = /^Java(\W*)/gm;
rep.exec(text)
```

#### 提交时间

```
-登录注册验证
	默认事件先执行
		checkbox
	自定义事件先执行
		a
		submit
		
		<form>
			<input type='type'/>
			<input type='password' />
			<input type='submit' />
		<form>
		
		$(':submit').click(function(){
          $(':text,:password').each(function(){
            retuen false;
          })
          return false;
		})

```



