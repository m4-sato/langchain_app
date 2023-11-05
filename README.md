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