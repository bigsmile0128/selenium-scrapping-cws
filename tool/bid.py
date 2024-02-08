import os
import datetime
from openai import OpenAI
import utils.log as log 
import time


def make_bid(job_title, employer_name, job_detail, job_link):
        
    dt_now = datetime.datetime.now()
    today = dt_now.strftime('%Y%m%d')
    timestamp = dt_now.strftime('%Y%m%d_%H%M%S')
    
    os.makedirs(os.path.join("bid", today), exist_ok=True)
    
    bid_template = f""""
    あなたはクラウドワークスでシステムエンジニアとして働く村山であり、あなたの目標は、以下の案件の内容をもとに、この案件に合格できる提案文を作成することです。


    案件に通過しやすい提案文の書き方:
    -自己紹介
    提案文をご覧いただきありがとうございます。はじめまして。現在、専業システムエンジニアとして活動している村山と申します。
    -志望動機
    志望動機を入れると「ちゃんと募集要項を見ているな」と、クライアントに伝わります。
    という形で、クライアントの要望に沿っていて、かつ自分の経験ともマッチすることを伝えられると、クライアント視点では非常に頼り甲斐のある人だという認識を持ってもらえます。
    -案件内容の確認
    次にどんな案件内容なのかを確認します。仕事の内容が、自分の認識にあっているかどうかすり合わせを行いましょう。
    このように募集要項を読んで、クライアントのゴールを見極めましょう。
    という風に確認しておかないと、案件に通過した後に「自分が思っていた仕事と違う」という状況になりかねません。
    クライアントも仕事内容を理解してくれている人に発注したいと考えているので、お互いのために応募の時にこのような文面を送っておくことをおすすめします。
    -自分ならではの提案と返信のお願い
    案件内容の確認を記載した後は、自分ならではの提案と返信のお願いをしましょう。たとえば以下のような提案＋返信を依頼する文面を送ると、クライアントから良い印象を持ってもらえます。
    提案をするだけでなく、希望に合わせた仕事ができることを文面に記載しておけば「この人は自社の色に合わせて仕事をしてくれる」と、思われるので、受注率がアップするでしょう。
    -スキルや実績の提示
    クライアントは基本的に、スキルや実績がある人に依頼したいと思っています。
    -納期の提示
    -仕事で意識している点
    仕事で意識している点を書いて、クライアントに熱意を伝えましょう。クライアントとしても、スピード感を持って仕事に取り組んでくれる人を優遇する傾向にあるので、納期のスピードや返信速度の速さを伝えるのが効果的です。
    -結びの言葉
    「お忙しいところ恐縮ですが、ご検討のほどよろしくお願いいたします。」や「即日稼働できますので、よろしくお願いいたします。」などを書いています。
    -ポートフォリオ
     https://akiramurayama-dev.vercel.app

    =========
    案件名: {job_title}
    お客様名： {employer_name}
    案件内容: {job_detail}
    =========
    
    提案内容のみ記入してください:
    """
                 
    # Set up your API key
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )
    # Generate a response from ChatGPT
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": bid_template,
            }
        ],
        model="gpt-3.5-turbo",
    )


    with open(os.path.join("bid", today, timestamp+".txt"), "w", encoding="utf-8") as f:
        f.write(f" 案件名: {job_title}\n")
        f.write(f"URL: {job_link}")
        f.write(f" お客様名： {employer_name}\n")
        f.write(f" 案件内容 : {job_detail}\n")
        f.write(f" 提案文 :\n")
        f.write(chat_completion.choices[0].message.content)


    return chat_completion.choices[0].message.content