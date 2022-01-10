import requests
import json


def send_single_sms(apikey, code, mobile):
    # 发送单条短信
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = f"【郭家桢】您的验证码是{code}。如非本人操作，请忽略本短信"

    res = requests.post(url, data={
        "apikey": apikey,
        "mobile": mobile,
        "text": text
    })
    re_json = json.loads(res.text)
    return re_json


if __name__ == "__main__":
    res = send_single_sms("65600f6616e6dc848a5217a0677ce126", "123456", "18782902568")

    code = res["code"]
    msg = res["msg"]
    if code == 0:
        print("发送成功")
    else:
        print(f"发送失败: {msg}")
    print(res)
