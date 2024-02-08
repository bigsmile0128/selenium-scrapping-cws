
import openai


# Set up your API key
openai.api_key = "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"

# Create a prompt for ChatGPT to respond to
message = "以下は「ラボ部」の提案書です。\
\
\"\
タイトル: 【フルリモート】【時給１５００円〜】プログラミングサロンの講師募集！！フロントエンドのスキルをお持ちの方！\
\
初心者を対象としてプログラミングスクールの講師をしてくださる方を募集します。\
ZOOMによる通話指導とチャット質問サポートが業務内容です。\
基本は時給1500円スタートで、受講生の担任人数によって月額制への移行も可能です。\
\
言語はフロントエンド周りのWEB制作をメインに指導する形となります。\
詳細は書きをご確認ください。\
\
【 依頼内容 】\
オンラインスクールのZOOMサポート講師\
\
HTML,CSS,Bootstrap,jQuery,JavaScript,PHP,MySQL,WordPress等を扱います。\
\
《ZOOMサポート》\
1週間（もしくは2週間）に1回、受講生に対して技術的な内容のレクチャーから、\
案件の獲得のアドバイスなどをZOOMを通じてチャットでは解決できない課題をサポートしていただきます。\
\
《チャットサポート》\
主な質問はフロントエンドの技術的な質問、学習の進め方に対する不明点です。\
\
・ここがわからない・・・\
・ここで躓いている・・・\
そういった内容に対してチャットでサポートをお願いします。\
\
\
働き方はフルリモート、フルフレックスです。\
PC・ネットがあれば全国どこからでも業務をしていただくことが可能です。\
在籍メンバーの中には月に20〜30万円を稼いでいるメンバーもいて\
安定的に稼働していただける方には長期的にお願いしたいと考えています。\
\
\
【必須】\
■プログラミングの知識\
■ご自身で案件獲得の経験、収益化したことがある方\
\
【尚可】\
■接客業などのユーザー対応経験\
▼少しでも当てはまったらお気軽にご連絡ください！▼\
\
・空いた時間を活用して収入を増やしたい！\
\
・プログラミング（フロントエンド）の経験を違う形で活かしてみたい！\
\
・これから伸びていく業界や市場でキャリアを積んでみたい！\
\
・フルリモートで働きたい！\
\
\
【 依頼期間 】\
半年以上〜\
\
【 契約金額(税込) 】\
生徒1人の場合の1ヶ月の報酬\
\
①通話指導：1時間1500円×4回＝6000円\
②チャットサポート：1回150円×回答数\
\
生徒さんは１０人、２０人、３０人とご紹介することが可能です。\
\
\
\
【 応募方法 】\
下記のフォーマットにてご応募をお願いいたします。\
\
１．お名前\
２．性別・年齢\
３．プログラミング歴\
４．扱える言語\
５．フリーランス歴\
６．プログラミング関連での月々の収入\
\
\
ご質問がありましたら、気軽にお問い合わせください。\
\
応募をお待ちしております！\
\"\
"

with open("me_system.txt", "r", encoding="utf-8") as f:
    intro_me = f.read()    

# Define the parameters for your query
model_engine = "gpt-3.5-turbo"


# Generate a response from ChatGPT
completion  = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message+intro_me}
    ]
)

print(completion.choices[0].message.content)
