あなたの仕事は、直近1週間（今日から7日前まで）の Python と Rust に関する最新情報を英語圏の一次情報を中心に収集し、日本語で要約したダイジェストを Gmail で {{RECIPIENT_EMAIL}} 宛てに送信することです。誰も見ていない自動実行なので、質問はせず最後まで完了させてください。

## 手順

### 1. 情報収集（WebSearch / WebFetch を使用）
Python と Rust それぞれについて、以下の3分野で複数回検索し、直近7日以内に公開されたものだけを集めてください。古い記事は除外します。検索クエリは英語で、年月を含めて「this week」「latest」「release」などを加えると精度が上がります。

**Python**
1. **言語・ランタイム**：CPython のリリース（安定版・プレリリース）、PEP の提案・採択・却下、Steering Council や PSF の発表、free-threading / JIT などのランタイム進展、PyPy・他実装の動き
2. **ライブラリ・ツール**：主要パッケージのメジャー/マイナーリリースと破壊的変更（uv, ruff, pip, pydantic, FastAPI, Django, Flask, NumPy, pandas, Polars, PyTorch など）、パッケージング・型システム・テスト周りの新ツール、PyPI のセキュリティ関連
3. **コミュニティ・記事**：注目された技術記事、カンファレンス（PyCon 各国、EuroPython など）の発表、Hacker News や Reddit r/Python で議論になった話題

**Rust**
1. **言語・コンパイラ**：Rust の安定版・ベータ版リリースと主要な安定化機能、RFC の提案・承認、Inside Rust / Rust Blog の公式発表、edition や async/const generics などの進展、rustc・cargo の変更
2. **クレート・ツール・エコシステム**：主要クレートのリリースと破壊的変更（tokio, axum, serde, clap, bevy, wgpu, tauri, polars など）、crates.io / cargo 周りの変更、WebAssembly・組み込み・Linux カーネルなど適用領域の動き
3. **コミュニティ・記事**：注目された技術記事、This Week in Rust で取り上げられた話題、RustConf・EuroRust などの発表、Hacker News や Reddit r/rust で議論になった話題

**両言語にまたがる話題**：PyO3 / maturin、Python ツールの Rust 実装（uv, ruff, Polars, pydantic-core など）、相互運用やパフォーマンス比較の記事があれば独立して拾ってください。

優先する情報源：
- Python: python.org の公式ブログ・リリースノート、PEP 一覧、discuss.python.org、PSF ブログ、Python Insider、各ライブラリの GitHub Releases、Real Python
- Rust: blog.rust-lang.org、Inside Rust、This Week in Rust、rust-lang/rfcs、各クレートの GitHub Releases、crates.io
- 共通: Hacker News、GitHub Trending、lobste.rs、各社の公式エンジニアリングブログ

SEO 目的のまとめサイトや根拠の薄い噂は避けてください。検索結果のスニペットだけで判断せず、重要な記事は WebFetch で本文を読んでから要約してください。

### 2. 選別
- Python・Rust それぞれ、各分野につき 2〜4 件、言語ごとに 7〜10 件程度に絞る
- 「今週最も重要なニュース」を全体から 3 件選ぶ（両言語から偏りなく）
- 同じ話題の重複記事は1つにまとめる
- リリース情報は「何が変わったか」「アップグレード時の注意点」を優先して書く

### 3. メール作成と送信
Gmail の送信ツール（mcp__Gmail__send_message）で、以下の形式で {{RECIPIENT_EMAIL}} に送信してください。本文は日本語、HTML形式で読みやすく整えてください。

- 件名：`【週刊Python/Rustダイジェスト】YYYY/MM/DD〜YYYY/MM/DD`（対象期間）
- 冒頭：**今週の注目トップ3** を各2〜3文で
- **Python セクション**：上記3分野の順。各記事について：
  - 見出し（日本語）
  - 2〜3文の要約：何が発表され、なぜ重要か。バージョン番号は必ず明記
  - 元記事へのリンク（必ず記載）
  - 公開日
- **Rust セクション**：同じ形式で上記3分野の順
- **両言語にまたがる話題**：該当があれば（なければセクションごと省略）
- 末尾：**今週の一言所感**（両言語のエコシステムを俯瞰して2〜3文）

要約は自分の言葉で書き、記事本文を長く引用しないでください。事実と推測は区別し、不確かな情報には「報道によれば」などを付けてください。

### 4. 完了報告
送信できたら、送信した件数と主なトピックを1〜2文で報告してください。Gmail送信が失敗した場合は、作成したダイジェスト本文をそのまま応答として出力し、失敗理由も添えてください。
