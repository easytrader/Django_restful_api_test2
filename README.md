# Django_restful_api_test1

cmd:
curl -X GET http://127.0.0.1:8000/task<br/>

http://blog.kent-chiu.com/2013/08/14/testing-rest-with-curl-command.html<br/>

HTTP Parameter

http參數可以直接加在url的query string，也可以用-d帶入參數間用&串接，或使用多個-d

# 使用`&`串接多個參數
curl -X POST -d "param1=value1&param2=value2"
# 也可使用多個`-d`，效果同上
curl -X POST -d "param1=value1" -d "param2=value2"
curl -X POST -d "param1=a 0space"     
# "a space" url encode後空白字元會編碼成'%20'為"a%20space"，編碼後的參數可以直接使用
curl -X POST -d "param1=a%20space"     
