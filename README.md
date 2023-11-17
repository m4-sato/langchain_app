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

[GitHub fingerprint](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)

