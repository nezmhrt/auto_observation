import auto_observation


def main():
    model = auto_observation.auto_observation(
        wait=3
    )
    model.watch_start("https://www.amazon.co.jp/Nintendo-Switch-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81-%E3%83%8D%E3%82%AA%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BC-%E3%83%90%E3%83%83%E3%83%86%E3%83%AA%E3%83%BC%E6%8C%81%E7%B6%9A%E6%99%82%E9%96%93%E3%81%8C%E9%95%B7%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%83%A2%E3%83%87%E3%83%AB/dp/B07WXL5YPW/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1LFHBJGPIC9H3&dchild=1&keywords=switch&qid=1598348555&sprefix=sw%2Caps%2C377&sr=8-1",
                      interval=10,
                      lim=50,)

    model.quit()


if __name__ == "__main__":
    main()
