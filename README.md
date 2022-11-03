# Games Info

```haskell
data InfoCard = InfoCard {
    title :: String
    createdAt :: String
    coverUrl :: String
    description :: String
}
```

## 概要

This module exports some information of music and books to html.

## テンプレート

```html
<div class="info-card">
    <div class="container">
        <div class="box" style="display: flex">
            <img src="https://www.oreilly.co.jp/books/images/picture_large978-4-8144-0006-5.jpeg">
        </div>
        <div class="box">
            <p>Title: ソフトウェアアーキテクチャ・ハードパーツ</p>
            <p>Author: Neal Ford、Mark Richards、Pramod Sadalage、Zhamak Dehghani</p>
            <p>Translation: 島田 浩二</p>
        </div>
    </div>
</div>
```

createdAt: 2022-10-16
