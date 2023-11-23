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

[参考記事](https://luciferous.notion.site/luciferous/Github-AWS-CI-CD-JAWS-FESTA-2023-b5198ec36520483ab44760764323e272)

- cloud9

git config --global user.name "<YOUR NAME>"
git config --global user.email "<YOUR EMAIL>"

### python環境構築

```bash
curl https://pyenv.run | bash
```

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
```

```bash
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
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

## streamlit Community Cloudへデプロイする
[Streamlit Community Cloud](https://streamlit.io/cloud)