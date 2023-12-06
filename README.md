# langchain_app

## OpenAI 記事

https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api

[Functon calling](https://platform.openai.com/docs/guides/gpt/function-calling)

## Prompt Engineering

### Zero-shot プロンプティング

- 事前に例を与えずタスクを処理される方法

```
以下のテキストをポジティブ・ネガティブ・中立のいずれかに分類してください。

テキスト:ChatGPTはプログラミングの悩みをたくさん解決してくれる。

分類:
```

### Few-shot プロンプティング

- 事前に例を与えてタスクを処理される方法

```
色を回答してください。
Q：リンゴ
A：赤
Q：バナナ
A：黄色
Q：メロン
A：
```

### Zero-shot Chain of Thoughtプロンプティング（Zero shot CoT）

- 「ステップバイステップ」という文言を追加することで正確な応答を得やすくなる手法

```
私は市場へ行って10個にリンゴを買いました。隣人に２つ、修理工に２つ渡しました。それから5つのリンゴを買って一つ食べました。残りは何個ですか？
回答だけ教えてください。
```

```
私は市場へ行って10個にリンゴを買いました。隣人に２つ、修理工に２つ渡しました。それから5つのリンゴを買って一つ食べました。残りは何個ですか？
ステップバイステップで考えてみてみましょう。
```

## Langchain資料

[Langchainドキュメント](https://python.langchain.com/docs/modules/)

## 論文

### RAG(Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks)

[RAG](https://arxiv.org/abs/2005.11401)

### ReAct: Synerging Reasoning and Acting in Langage Models

[ReAct](https://react-lm.github.io/)

### Chain of Thought:

[CoT](https://www.promptingguide.ai/jp/techniques/cot)

### DocumentLoader

[DocumentLoader](https://integrations.langchain.com/)

### vector store

[Faiss](https://faiss.ai/index.html)
[Elasticsearch](https://www.elastic.co/jp/elasticsearch/)
[Redis](https://redis.io/)


[langchainGitHubエコシステム集](https://github.com/kyrolabs/awesome-langchain)
[Patterns for Building LLM-based Systems & Prodcts](https://eugeneyan.com/writing/llm-patterns/)

### Cloud9とGitHubの連携

[SSHキーの生成](https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

```bash
ssh-keygen -t ed25519 -C "mssst1116@gmail.com"
```

```bash
Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
```

```bash
Enter new passphrase (empty for no passphrase): [Type new passphrase]
```

```bash
Enter same passphrase again: [Repeat the new passphrase]
```

```github_Key(id_ed25519.pub)
four_file inner all copy
```

```bash
cat ~/.ssh/~id_ed25519.pub
```

[GitHub fingerprint](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)

## cloud9とGitHubの連携・streamlitの立ち上げ

[ChatGPTでの調査](https://chat.openai.com/c/0602ca1c-1a38-407b-a093-6296de63f083)

```bash
ssh -T git@github.com
```

## step1 cloud9の環境構築

- テキストを参照

## step2 SSHキー生成とGitHubへの追加

- cloud9のターミナル（デフォルトのディレクトリにて）
- GitHub アカウントに関連付けられたメールアドレスに置き換える

- 公開さえたキーの内容をコピー
- GitHub のアカウント設定に移動し、「SSH and GPG keys」セクションで「New SSH key」をクリックします。
- キーのタイトルを入力し、先ほどコピーした公開キーを貼り付けて、「Add SSH key」をクリックします。

```bash
ec2-user:~/environment $ git config --global user.email mssst1116@gmail.com
ec2-user:~/environment $ git config --global user.name masashisato
```

## step3 GitHub リポジトリのクローン

```bash
git clone git@github.com:m4-sato/slackapp-chatgpt_v2.git
```

## step4 Python と Streamlit のインストール

- cloud9のデフオルトpythonは2がインストールされているのでpip3を使用する。

```bash
pip3 install streamlit
```

## step5 streamlitの実行

- cloud9のEC2のセキュリティグループの設定を行う。
    - セキュリティグループの設定:

AWS EC2 インスタンス（Cloud9 が実行されている場所）のセキュリティグループ設定を確認し、Streamlit が使用するポート（この場合は 8501）がインターネットからアクセス可能になっているか確認してください。インバウンドルールで適切な設定がなされている必要があります。
    - Streamlit の設定で、アプリケーションが全てのネットワークインターフェイスをリッスンするように設定されていることを確認してください。つまり、config.toml ファイル（または Streamlit の起動コマンド）で server.address を 0.0.0.0 に設定してください。
    - ```mkdir -p ~/.streamlit```

```bash
echo "[server]
address = '0.0.0.0'
port = 8501
enableCORS = false" > ~/.streamlit/config.toml
```

```bash
streamlit run app.py --server.port 8080
```

### python環境構築

```bash
curl https://pyenv.run | bash
```

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
```

```bash
echo 'command -v pyenv >/dev/null || export PATH="PYENVROOT/bin:PYENV_ROOT/bin:PATH"' >> ~/.bashrc
```

```bash
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

```bash
exec "$SHELL"
```

```bash
pyenv --version
```

```bash
sudo yum remove -y openssl-devel
sudo yum install -y openssl11-devel bzip2-devel xz-devel
```

```bash
pyenv install 3.10
```

```bash
cd your_project
```

```bash
pyenv local 3.10
```

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

## pipにインストールされているパッケージをrequirements.txtに出力する

```bash
pip freeze > requirements.txt
```

## streamlit Community Cloudに対してデプロイする

[Streamlit Community Cloud](https://streamlit.io/cloud)